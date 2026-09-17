"""Tests for P6-01 Gate fill ratio calibration."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.gate_fill_calibration import (
    align_gate_binance_bars,
    render_calibration_markdown,
    run_fill_calibration,
)


def _synthetic_bars(n: int = 200, *, qv_binance: float = 1e6, qv_gate: float = 5e5) -> tuple[pd.DataFrame, pd.DataFrame]:
    ts = pd.date_range("2026-07-09", periods=n, freq="1h", tz="UTC")
    close = 70_000 + pd.Series(range(n)).astype(float) * 10.0
    ohlc = pd.DataFrame(
        {
            "timestamp": ts,
            "open": close - 50,
            "high": close + 200,
            "low": close - 200,
            "close": close,
            "volume": 1000.0,
            "quote_volume": qv_binance,
        }
    )
    gate = ohlc.copy()
    gate["quote_volume"] = qv_gate
    gate["close"] = close + 5.0
    return gate, ohlc


def test_align_gate_binance_bars():
    gate, binance = _synthetic_bars(50)
    merged = align_gate_binance_bars(gate, binance)
    assert len(merged) == 50
    assert "gate_close" in merged.columns and "binance_close" in merged.columns


def test_run_fill_calibration_lower_gate_volume():
    gate, binance = _synthetic_bars(200, qv_binance=2e6, qv_gate=4e5)
    rep = run_fill_calibration(gate, binance, min_bars=100)
    assert rep.n_bars >= 100
    assert rep.binance.filled_orders >= rep.gate.filled_orders
    assert rep.fill_ratio_gate_over_binance_count <= 1.0
    md = render_calibration_markdown(rep)
    assert "Gate Fill Ratio Calibration" in md
