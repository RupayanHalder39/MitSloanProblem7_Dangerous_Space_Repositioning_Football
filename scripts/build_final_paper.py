#!/usr/bin/env python3
"""Build the two-page public manuscript from the reviewed scientific text."""
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "paper/Closing_the_Gap_MIT_Sloan_Public_Final.docx"


def set_font(run, size=10, bold=False, italic=False):
    run.font.name = "Times New Roman"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic


def body(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.0
    set_font(p.add_run(text), 10)
    return p


def caption(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(5)
    set_font(p.add_run(text), 9, italic=True)


def add_page_number(section):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    set_font(run, 9)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run._r.addnext(fld)


def main():
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Inches(8.5), Inches(11)
    section.top_margin = section.bottom_margin = Inches(0.52)
    section.left_margin = section.right_margin = Inches(0.58)
    add_page_number(section)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.space_after = Pt(7)
    set_font(title.add_run("Closing the Gap: Attack-Gated Space Control and Bounded Counterfactual Repositioning in Soccer"), 16, bold=True)
    for text, size, bold in [("Soccer", 11, True), ("Paper ID: [To be assigned]", 10, False)]:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(3)
        set_font(p.add_run(text), size, bold=bold)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(4); set_font(p.add_run("Abstract."), 12, bold=True)

    body(doc, "A coach watching a defensive shape break rarely asks only where the open space is; the real question is who should move into it before the opponent can exploit it, and whether that movement creates a second problem somewhere else. Existing pitch-control and Voronoi approaches are strong at describing geometry, but dangerous space is not useful if the current attack cannot actually reach it. We therefore ask whether tracking data can identify attack-relevant dangerous space and whether a bounded counterfactual search can recommend a realistic corrective movement without opening a new structural gap.")
    body(doc, "Using broadcast-video tracking at 30 fps over a 120-second match segment (3,600 frames), we compute a Voronoi tessellation in every frame and score opponent-owned cells from goal proximity (0.20), centrality (0.10), ball proximity (0.15), receiver support (0.20), and coverage gap (0.35). A causal tiered majority-vote estimator infers the attacking team from the current frame and 4 s/12 s/30 s trailing windows. A hard eligibility gate then keeps only regions aligned with the live attack - near the ball's longitudinal progress, reachable within 30 m, or supported above a 0.15 receiver threshold - while excluding cells behind the attack or generated when the defending team has possession. Up to three distinct regions survive centroid/radius de-duplication, and candidate fixers are scored on proximity, feasibility, abandonment cost, and local support before a bounded <=3 m local search evaluates danger removed against new-gap risk, structural damage, and movement cost.")
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(1)
    p.add_run().add_picture(str(ROOT / "results/figures/tracking_voronoi_assigned_fixer_frame2233.png"), width=Inches(3.55))
    caption(doc, "Figure 1. Real tracking data at t = 74.4 s: Voronoi space control, the flagged dangerous region, both teams, the ball, and the assigned fixer's suggested 3.0 m move.")

    doc.add_page_break()
    body(doc, "The gate changes what the system calls dangerous. Across a 475-frame sample, strongly-behind-the-attack primary selections fall from 4.8% to 0.0%, while ahead-of-ball or level selections rise from 53.3% to 64.4%. Eligible primary danger is resolved in 21.9% of frames; 64.8% remain possession/ball uncertain and 13.3% have known context but no eligible candidate. The system therefore shows both the gain in tactical relevance and the deliberate refusal to invent a danger when the context is uncertain.")
    body(doc, "The same conservatism carries into the counterfactual search. In a 601-frame demo segment, 48 frames resolve a primary region: 44% contain three distinct dangerous regions, 48% contain two, and 8% contain one, with de-duplication merging overlaps in 47 of 48 cases. Across the full 3,600-frame scan, only three frames yield a genuinely improving bounded reposition. In the illustrated case, a 3.0 m move reduces flagged-region severity by 0.00775 with zero new-gap penalty, producing net benefit +0.01326. The system thus turns 'where is the danger, and who should close it?' into a reproducible frame-level decision aid for opposition scouting, training-ground rehearsal, and post-match review. It does not claim globally optimal repositioning, validated scoring probability, or proven match-outcome effects; the bounded single-player search, one-match sample, and unvalidated severity/access proxies make this coach-facing decision support pending multi-match validation.")
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(1)
    p.add_run().add_picture(str(ROOT / "results/figures/dangerous_space_analytics_tracking_only.png"), width=Inches(7.15))
    caption(doc, "Figure 2. Public tracking-only Dangerous Space Repositioning Analytics dashboard. The reconstructed tactical radar shows player locations, Voronoi control, flagged regions, and the assigned fixer; the three derived panels summarize regional danger, opponent access, and spatial-balance/new-gap risk. No broadcast pixels are reproduced.")
    body(doc, "This research was developed in collaboration with SoccerSolver. SoccerSolver currently works with more than 10 football clubs.")
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
    set_font(p.add_run("Open-source repository: https://github.com/RupayanHalder39/MitSloanProblem7_Dangerous_Space_Repositioning_Football"), 10)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.core_properties.title = "Closing the Gap Attack-Gated Space Control and Bounded Counterfactual Repositioning in Soccer"
    doc.core_properties.subject = "MIT Sloan Sports Analytics Conference Soccer submission"
    doc.core_properties.author = ""
    doc.core_properties.last_modified_by = ""
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
