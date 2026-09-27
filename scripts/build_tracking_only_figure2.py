#!/usr/bin/env python3
"""Build the public tracking-only Figure 2 from the private dashboard export.

The source dashboard is never copied to the public repository. This script
retains its derived 3D tactical radar and analytical charts, removes the
broadcast panel, and adds a plain-language interpretation panel.
"""
import argparse
from pathlib import Path

import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("results/figures/dangerous_space_analytics_tracking_only.png"))
    args = parser.parse_args()
    source = cv2.imread(str(args.source), cv2.IMREAD_COLOR)
    if source is None or source.shape[:2] != (1028, 1972):
        raise SystemExit("expected the audited 1972 x 1028 private dashboard export")

    header = source[0:34, :].copy()
    # The audited panel boundary is at x=1035. Starting earlier retains a
    # narrow strip of the broadcast panel even though the tactical radar is
    # visually dominant, so crop conservatively and resize only the radar.
    radar = source[34:548, 1035:1972].copy()
    charts = source[548:1028, :].copy()
    top = np.full((514, 1972, 3), (19, 28, 38), dtype=np.uint8)
    top[:, 986:1972] = cv2.resize(radar, (986, 514), interpolation=cv2.INTER_AREA)
    cv2.rectangle(top, (0, 0), (985, 513), (45, 61, 72), 2)
    cv2.putText(top, "TRACKING-ONLY TACTICAL VIEW", (52, 76), cv2.FONT_HERSHEY_SIMPLEX, 1.15, (245, 245, 245), 2, cv2.LINE_AA)
    lines = [
        "Player markers: reconstructed tracked locations",
        "Voronoi boundaries: nearest-player space control",
        "Orange regions: attack-gated dangerous space",
        "Cyan markers: assigned fixer and suggested move",
        "Bottom charts: danger, opponent access, and new-gap risk",
        "No broadcast pixels are included in this public figure",
    ]
    for index, line in enumerate(lines):
        color = (80, 210, 220) if index == 5 else (215, 222, 228)
        cv2.putText(top, line, (58, 145 + index * 48), cv2.FONT_HERSHEY_SIMPLEX, 0.72, color, 2, cv2.LINE_AA)
    output = np.vstack([header, top, charts])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(args.output), output):
        raise SystemExit("failed to write public figure")
    print(args.output)


if __name__ == "__main__":
    main()
