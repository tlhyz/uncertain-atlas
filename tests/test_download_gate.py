"""Gate download script smoke tests."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_download_gate_btc_smoke():
    r = subprocess.run(
        [sys.executable, "scripts/download_gate.py", "--contract", "BTC_USDT", "--interval", "1h"],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert r.returncode == 0, r.stderr
    assert "bars=" in r.stdout
    # Gate REST cap ~720 bars for 1h recent window
    assert "720" in r.stdout or int(r.stdout.split("bars=")[-1].strip()) >= 100
