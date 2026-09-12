"""Binance Vision aggTrades download tests."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_agg_trades_day, fetch_binance_klines_range


def test_vision_agg_trades_one_day():
    df = fetch_agg_trades_day("BTCUSDT", date(2024, 9, 1), cache_only=True)
    assert len(df) > 100_000
    assert "quote_qty" in df.columns


def test_vision_klines_small_range():
    bars = fetch_binance_klines_range("BTCUSDT", "1h", "2024-09-01", "2024-09-02", cache_only=True)
    assert len(bars) >= 24
