#!/usr/bin/env python3
"""Repo-root entry: same as soxl-lab/scripts/run_grid.py."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.soxl_grid_cli import main

if __name__ == "__main__":
    raise SystemExit(main())
