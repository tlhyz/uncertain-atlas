#!/usr/bin/env python3
"""Gate OOS calibration entrypoint — delegates fill-ratio step to P6-01 runner."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    script = ROOT / "scripts" / "run_p6_gate_fill_calibration.py"
    print("Gate OOS calibration — fill_ratio step via run_p6_gate_fill_calibration.py")
    return subprocess.call([sys.executable, str(script)] + sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
