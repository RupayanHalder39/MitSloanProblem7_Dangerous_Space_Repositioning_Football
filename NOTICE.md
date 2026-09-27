# License and Provenance Notice

## Project-controlled code

The scoped MIT license covers the Problem 7 analytics and dashboard code,
project-local shared analytics and tactical utilities, scripts, tests, and
project-authored documentation. The procedural player glyph helpers were
migrated from the project-controlled `offside_break` research workspace to
remove a sibling-project runtime dependency.

## Third-party code

`src/dangerous_space_repositioning/sports/` is an unmodified vendored subset
of Roboflow's `sports` project. It remains governed by the upstream MIT notice
in `docs/THIRD_PARTY_ROBOFLOW_SPORTS_LICENSE.txt`.

Runtime dependencies in `requirements.txt` are not vendored and retain their
own upstream licenses. No modified third-party code or code of unclear
provenance was identified in the public source tree.

## Excluded material

The project license grants no rights to source broadcast footage, source or
tracking data, calibration files, row-level derived datasets, the researcher
photograph, the SoccerSolver logo, or third-party assets. Figure 2 is a
project-generated tracking-only public reconstruction and contains no
broadcast pixels.
