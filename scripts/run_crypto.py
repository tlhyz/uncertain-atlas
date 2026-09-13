#!/usr/bin/env python3
"""Run Crypto independent regime experiment (Book B)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.dual.crypto_run import main

if __name__ == "__main__":
    raise SystemExit(main())
