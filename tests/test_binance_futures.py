"""Binance Vision aggTrades download tests."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_agg_trades_day, fetch_binance_klines_range


def test_vision_soxl_agg_trades_one_day():
    df = fetch_agg_trades_day("SOXLUSDT", date(2026, 7, 15), cache_only=False, force_refresh=True)
    assert len(df) > 100
    assert "quote_qty" in df.columns
    assert df["timestamp"].min().year == 2026
    df2 = fetch_agg_trades_day("SOXLUSDT", date(2026, 7, 15), cache_only=True)
    assert len(df2) == len(df)
    assert df2["timestamp"].min().year == 2026
