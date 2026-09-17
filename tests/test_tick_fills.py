"""Tick fill precision tests."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.ab.fills import FillConfig, PendingFill
from qtb.dual.tick_fills import resolve_tick_fills
from qtb.dual.tick_validate import validate_bars_vs_ticks


def _synthetic_trades(prices: list[float], start="2024-09-01", freq="min") -> pd.DataFrame:
    ts = pd.date_range(start, periods=len(prices), freq=freq, tz="UTC")
    rows = []
    for p, t in zip(prices, ts):
        rows.append({"timestamp": t, "price": p, "qty": 0.01, "quote_qty": p * 0.01})
    return pd.DataFrame(rows)


def test_tick_path_does_not_fill_all_skipped_levels():
    # Price drops 100 -> 95 -> 90 but tiny volume — only one grid buy should fill
    trades = _synthetic_trades([100.0, 99.0, 98.0, 97.0, 96.0, 95.0, 94.0, 93.0, 92.0, 91.0, 90.0])
    pending = [
        PendingFill("buy", 99.0, 0, notional=100.0, reason="g0"),
        PendingFill("buy", 95.0, 1, notional=100.0, reason="g1"),
        PendingFill("buy", 90.0, 2, notional=100.0, reason="g2"),
    ]
    cfg = FillConfig.preset("base")
    fills = resolve_tick_fills(pending, trades, cfg, bar_open=100.0, bar_close=90.0)
    assert len(fills) <= 2
    assert len({f.level_idx for f in fills}) == len(fills)


def test_validate_bars_vs_ticks_passes_on_consistent_data():
    bars = pd.DataFrame(
        {
            "timestamp": pd.date_range("2024-09-01", periods=1, freq="1h", tz="UTC"),
            "open": [100.0],
            "high": [101.0],
            "low": [99.0],
            "close": [100.5],
            "quote_volume": [5000.0],
        }
    )
    trades = pd.DataFrame(
        {
            "timestamp": pd.date_range("2024-09-01", periods=5, freq="min", tz="UTC"),
            "price": [100.0, 101.0, 99.0, 100.0, 100.5],
            "quote_qty": [1000.0, 1000.0, 1000.0, 1000.0, 1000.0],
        }
    )
    v = validate_bars_vs_ticks(bars, trades, "BTC", min_coverage=0.0)
    assert v.passed
