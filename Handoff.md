# Public Submission Handoff

Status: conservative Problem 7 public release validated for publication.

## Research Status

The repository documents attack-gated dangerous-space detection and bounded single-player counterfactual repositioning on one 120-second match segment. It reports 3,600 frames, the audited 475-frame eligibility sample, the 601-frame multi-region segment, and the verified frame-2233 example. It makes no causal, global-optimum, calibrated-probability, or proven match-outcome claim.

## Final Deliverables

- Paper: `paper/Closing_the_Gap_MIT_Sloan_Public_Final.docx` and `.pdf`
- Figure 1: `results/figures/tracking_voronoi_assigned_fixer_frame2233.png`
- Figure 2: `results/figures/dangerous_space_analytics_tracking_only.png`
- Repository: `https://github.com/RupayanHalder39/MitSloanProblem7_Dangerous_Space_Repositioning_Football`

Figure 2 contains no broadcast pixels. Both private broadcast-derived videos, source footage, tracking/calibration, and row-level derived data remain excluded.

## Dependency Migration

The master project now contains project-local copies of required shared Voronoi/pitch-control modules, tactical coordinate/tracking/radar utilities, Roboflow sports helpers with their MIT notice, and project-controlled player-glyph helpers. Imports were updated to the Problem 7 package namespace. No symlinks were used and sibling sources were not modified.

## Validation

- Master suite: 129 passed.
- Public suite: 127 passed, 2 input-dependent tests skipped.
- Public validator: required files, links, figures, embedded paper images, scientific values, imports, licensing notice, restricted-file exclusions, portability, and repository URL checked.
- Final DOCX rendered to a two-page PDF; every page visually inspected with no clipping, overlap, distortion, or broadcast imagery.

## Licensing and Reproducibility

Project-controlled code uses a scoped MIT license. Vendored Roboflow sports helpers retain their upstream MIT notice. Media, data, photographs, and logos are outside the project code-license scope. Reproducibility is CONDITIONAL because lawful match tracking and derived inputs are not distributed.

AUTHORSHIP: PARTIAL. Rupayan Halder is confirmed; citation metadata remains provisional.

SAFE TO COMMIT: YES

SAFE TO PUSH: YES
