#!/usr/bin/env python3
"""Validate the conservative public package without restricted inputs."""
import csv
import hashlib
import importlib
import re
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
URL = "https://github.com/RupayanHalder39/MitSloanProblem7_Dangerous_Space_Repositioning_Football"
SOCCERSOLVER = "This research was developed in collaboration with SoccerSolver. SoccerSolver currently works with more than 10 football clubs."
FIG1 = "079f9a63b982404447dc259190276131"
FIG2 = "7c5605ecaaff787257d4936a6ce0552f"

def md5(path):
    return hashlib.md5(path.read_bytes()).hexdigest()

def main():
    required = ["README.md", "LICENSE", "NOTICE.md", "CITATION.cff", "PUBLIC_RELEASE_AUDIT.md", "Handoff.md",
                "docs/THIRD_PARTY_ROBOFLOW_SPORTS_LICENSE.txt", "paper/Closing_the_Gap_MIT_Sloan_Public_Final.docx",
                "paper/Closing_the_Gap_MIT_Sloan_Public_Final.pdf", "results/figures/tracking_voronoi_assigned_fixer_frame2233.png",
                "results/figures/dangerous_space_analytics_tracking_only.png", "results/tables/verified_summary.csv",
                "assets/RupayanHalder.jpeg", "assets/SoccerSolverLogo.png"]
    missing = [p for p in required if not (ROOT / p).is_file()]
    if missing: raise SystemExit(f"missing files: {missing}")
    readme = (ROOT / "README.md").read_text()
    if URL not in readme or SOCCERSOLVER not in readme: raise SystemExit("README URL or SoccerSolver statement mismatch")
    links = re.findall(r"!?(?:\[[^]]*\])\(([^)]+)\)", readme)
    broken = [x for x in links if not x.startswith(("http://", "https://", "mailto:")) and not (ROOT / x.split("#",1)[0]).exists()]
    if broken: raise SystemExit(f"broken links: {broken}")
    text = "\n".join(p.read_text(errors="replace") for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in {".md",".py",".txt",".cff",".csv"})
    for term in ["/Users/" + "rupayan/", "Public GitHub " + "URL", "ANON" + "YMIZED"]:
        if term in text: raise SystemExit(f"forbidden public text: {term}")
    restricted = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in {".mp4",".mov",".avi",".mkv",".parquet",".pkl",".pickle",".db",".sqlite",".sqlite3"}]
    if restricted: raise SystemExit(f"restricted media/data present: {restricted}")
    if list(ROOT.rglob("__pycache__")) or list(ROOT.rglob("*.pyc")): raise SystemExit("cache files present")
    if [p for p in ROOT.rglob("*") if p.is_symlink()]: raise SystemExit("symlinks present")
    if md5(ROOT / "results/figures/tracking_voronoi_assigned_fixer_frame2233.png") != FIG1: raise SystemExit("Figure 1 changed")
    if md5(ROOT / "results/figures/dangerous_space_analytics_tracking_only.png") != FIG2: raise SystemExit("Figure 2 changed")
    with ZipFile(ROOT / "paper/Closing_the_Gap_MIT_Sloan_Public_Final.docx") as z:
        xml = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", z.read("word/document.xml").decode()))
        if hashlib.md5(z.read("word/media/image1.png")).hexdigest() != FIG1: raise SystemExit("embedded Figure 1 mismatch")
        if hashlib.md5(z.read("word/media/image2.png")).hexdigest() != FIG2: raise SystemExit("embedded Figure 2 mismatch")
    for phrase in [URL, SOCCERSOLVER, "475-frame sample", "4.8% to 0.0%", "53.3% to 64.4%", "21.9%", "64.8%", "13.3%",
                   "601-frame demo segment", "48 frames", "47 of 48", "full 3,600-frame scan", "only three frames", "3.0 m move",
                   "0.00775", "+0.01326", "Figure 1.", "Figure 2.", "No broadcast pixels"]:
        if phrase not in xml: raise SystemExit(f"paper missing: {phrase}")
    with (ROOT / "results/tables/verified_summary.csv").open() as f:
        summary = {r["metric"]: r["value"] for r in csv.DictReader(f)}
    expected = {"frames":"3600","sampled_frames":"475","demo_resolved_primary_frames":"48","dedup_merged_cases":"47",
                "improving_bounded_frames":"3","illustrated_move_m":"3.0","illustrated_severity_reduction":"0.00775",
                "illustrated_new_gap_penalty":"0","illustrated_net_benefit":"0.01326"}
    if {k:summary.get(k) for k in expected} != expected: raise SystemExit("verified summary mismatch")
    for module in ["dangerous_space_repositioning.analytics.dangerous_space", "dangerous_space_repositioning.analytics.counterfactual_repositioning",
                   "dangerous_space_repositioning.analytics.multi_region", "dangerous_space_repositioning.dashboard.voronoi_radar"]:
        importlib.import_module(module)
    print("public package validation passed")

if __name__ == "__main__": main()
