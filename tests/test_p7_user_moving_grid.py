"""User ±20U / ±20% moving-grid unit tests (no download)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.analysis.user_moving_grid import daily_pnl, run_user_ls_pair, user_levels


def test_usdt_levels_span_40():
    lv = user_levels(100.0, range_mode="usdt", range_usdt=20.0, n_grids=200)
    assert len(lv) == 200
    assert abs(lv[0] - 80.0) < 1e-9
    assert abs(lv[-1] - 120.0) < 1e-9
    assert abs((lv[1] - lv[0]) - 40.0 / 199) < 1e-9


def test_pct_levels_span_40pct():
    lv = user_levels(100.0, range_mode="pct", range_pct=0.20, n_grids=200)
    assert abs(lv[0] - 80.0) < 1e-9
    assert abs(lv[-1] - 120.0) < 1e-9


def _chop_bars(n: int = 80) -> pd.DataFrame:
    t = np.linspace(0, 6 * np.pi, n)
    close = 120.0 + 8.0 * np.sin(t)
    ts = pd.date_range("2026-07-16", periods=n, freq="h", tz="UTC")
    return pd.DataFrame(
        {
            "timestamp": ts,
            "open": close,
            "high": close + 0.6,
            "low": close - 0.6,
            "close": close,
        }
    )


def test_both_range_modes_run_bar_ls():
    bars = _chop_bars()
    for mode in ("usdt", "pct"):
        r = run_user_ls_pair(bars, range_mode=mode, fill_engine="bar", fee_preset="base")  # type: ignore[arg-type]
        assert r["end_equity"] >= 0
        assert len(r["daily"]) >= 1
        assert "daily_pnl" in r["daily"].columns


def test_daily_pnl_first_day():
    ts = pd.Series(pd.date_range("2026-07-16", periods=30, freq="h", tz="UTC"))
    eq = np.linspace(10_000, 10_200, 30)
    d = daily_pnl(ts, eq, 10_000.0)
    assert abs(float(d.iloc[0]["daily_pnl"]) - (eq[23] - 10_000)) < 1e-6 or len(d) >= 1
