#!/usr/bin/env python3
"""改 soxl-lab/params/run.yaml 或加命令行参数，用本机真实逐笔跑 SOXL 网格。"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.analysis.soxl_grid_cli import main

if __name__ == "__main__":
    raise SystemExit(main())
