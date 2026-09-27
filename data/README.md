# Data Availability

No match-level or row-level data are distributed in this repository.

To reproduce the complete pipeline, a researcher must supply lawfully obtained,
time-aligned inputs under the ignored `data/private/` directory:

```text
data/private/
├── tracking/tracking.parquet
├── analytics/ball_trajectory.parquet
├── analytics/homography_transformers.pkl
└── source_video/match_segment.mp4
```

Tracking and ball trajectories are required for scientific analytics. The
homography and source video are required only for the private broadcast-aligned
dashboard. Public Figure 2 can be inspected without those restricted inputs.
Redistribution authorization for the source video, tracking, calibration, and
row-level derived data is unknown, so no data license is asserted.
