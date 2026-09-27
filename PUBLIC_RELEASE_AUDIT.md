# Public Release Audit

Audit date: 2026-09-27

## Release Decision

This is a conservative code, tests, paper, figures, and aggregate-results release. Restricted match media and row-level data are excluded. Figure 2 replaces the recognizable broadcast panel with a tracking-only explanation panel while retaining the derived tactical radar and analytical charts.

SAFE TO COMMIT: YES

SAFE TO PUSH: YES

## Paper and Figures

- Paper: PASS. The reviewed scientific text was retained, the repository URL was inserted, and the final two-page DOCX/PDF were rendered and visually inspected.
- Figure 1: PASS. Original high-resolution tracking/Voronoi visualization for frame 2233, showing both teams, ball, flagged region, assigned fixer, and suggested 3.0 m move.
- Figure 2: PASS. Tracking-only Dangerous Space Repositioning Analytics dashboard. It contains no recognizable broadcast imagery or source-video pixels.
- Figure order and captions: PASS.

## Scientific Traceability

The implementation confirms the 30 fps, 3,600-frame segment; five severity weights; current/4 s/12 s/30 s attack estimator; 5 m backward tolerance; 30 m/0.15 reachability rule; maximum three regions; centroid/radius de-duplication; candidate-fixer factors; and <=3 m bounded search.

Validated outputs and the project traceability record support the reported values: 4.8% to 0.0%; 53.3% to 64.4%; 104/475 (21.9%) resolved; 308/475 (64.8%) uncertain; 63/475 (13.3%) known context with no candidate; 48 resolved frames in the 601-frame segment with 21/23/4 region counts and 47 de-duplication merges; three improving frames in the full scan; and frame 2233's 3.0 m move, 0.00775 severity reduction, zero new-gap penalty, and +0.01326 benefit.

Claims remain bounded: no global optimum, calibrated probability, causal effect, proven outcome improvement, or universal tactical superiority is asserted.

## Video Audit

| Private master file | Size | Duration | Class | Purpose | Broadcast visible | Authorization | Public status |
|---|---:|---:|---|---|---|---|---|
| `dangerous_space_repositioning_120s_final.mp4` | 244,612,120 bytes | 120.0 s | B | Full generated dashboard | Yes | Unknown | Excluded; also exceeds GitHub's 100 MB object limit |
| `dangerous_space_repositioning_20s_final.mp4` | 41,561,675 bytes | 20.03 s | B | Generated demonstration excerpt | Yes | Unknown | Excluded |

No tracking-only video was identified. Neither private video was modified or deleted.

## Data Policy

| Category | Required for full reproduction | Included publicly | Redistribution authorization | License |
|---|---|---|---|---|
| A. Source broadcast data | YES for broadcast-aligned dashboard | NO | UNKNOWN | None asserted |
| B. Tracking and calibration | YES | NO | UNKNOWN | None asserted |
| C. Row/frame-level derived data | YES when consuming cached outputs; otherwise regenerable | NO | UNKNOWN | None asserted |
| D. Aggregate research results | NO; verification output | YES | Project-controlled aggregate output | Covered only as documented output, not as a data license |
| E. Code | YES | YES | Known as classified below | Scoped MIT/upstream MIT |

Reproducibility is CONDITIONAL. Users must supply lawful tracking, ball trajectory, and—when recreating the private dashboard—homography calibration and source video.

## Code Provenance

| Class | Code family | Treatment |
|---|---|---|
| A. Original/project-controlled | Problem 7 analytics/dashboard, project-local shared analytics/tactical utilities, scripts, tests | Scoped MIT license |
| A. Original/project-controlled migration | Procedural player glyph helpers from the owner's sibling `offside_break` project | Documented in `NOTICE.md`; scoped MIT |
| B. Modified third-party | None identified | Not applicable |
| C. Unmodified vendored third-party | `src/dangerous_space_repositioning/sports/` from Roboflow `sports` | Upstream MIT notice retained |
| D. Unclear provenance | None identified | Not applicable |

The repository license does not cover footage, source/tracking data, row-level datasets, the researcher photograph, SoccerSolver logo, or third-party assets.

## Authorship and Citation

AUTHORSHIP: PARTIAL. Rupayan Halder is confirmed; no coauthors were invented. `CITATION.cff` is PROVISIONAL until the complete author list is finalized. This is not a technical release blocker.

## Security and Portability

- Secret scan: PASS. No passwords, API keys, tokens, credentials, cookies, SSH material, signed URLs, session files, or environment files are included.
- Portability: PASS. Runtime imports and data paths are project-local or command-line/user-supplied. No machine-specific user-home dependency remains.
- Symlinks: none.
- Caches/temp/archive/database files: excluded.
- Source footage, videos, parquet, pickle, and row-level data: absent.
- README and paper links/assets: resolved.
- Public tests: 127 passed, 2 skipped because restricted match inputs are absent. Master tests: 129 passed with authorized local inputs.

## Git-History Safety

The public repository was created from the audited package. Restricted media and data were never staged or committed. The intended publication history is one clean root commit.

## Remaining Non-Blocking Work

- Finalize the complete author list and citation metadata.
- Obtain explicit permission before ever adding source footage, broadcast-derived videos, tracking/calibration files, or row-level derived data.
