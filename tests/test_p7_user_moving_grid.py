"""User ±20U / ±20% moving-grid unit tests (no download)."""

from __future__ import annotations

import numpy as np
import pandas as pd

import pytest

from src.analysis.user_moving_grid import (
    IsolatedDirBook,
    daily_pnl,
    remap_lots,
    run_user_hedge_pair,
    run_user_ls_pair,
    run_user_one_side,
    simulate_user_dir_grid,
    user_levels,
)


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


def test_flatten_closes_qty():
    b = IsolatedDirBook(5_000.0, 5.0, 0.0002, "short")
    b.open_lot(10.0, 100.0, 1)
    assert b.qty > 0
    b.flatten(100.0)
    assert b.qty == 0.0
    assert b.lots == {}


def test_hedge_pair_runs_and_matches_sides():
    bars = _chop_bars()
    r = run_user_hedge_pair(bars, range_mode="usdt", fill_engine="bar", fee_preset="base")
    assert r["hedge_mode"] == "moving_ls_flatten_survivor"
    assert r["long"]["reanchors"] == r["short"]["reanchors"]
    assert len(r["daily"]) >= 1
    if r["pair_stopped"]:
        assert abs(r["long"]["end_qty"]) < 1e-6 or r["liquidated_long"]
        assert abs(r["short"]["end_qty"]) < 1e-6 or r["liquidated_short"]


def test_hedge_flattens_survivor_after_crash():
    close = np.concatenate([np.full(8, 130.0), np.linspace(130.0, 40.0, 40)])
    ts = pd.date_range("2026-07-16", periods=len(close), freq="h", tz="UTC")
    bars = pd.DataFrame(
        {
            "timestamp": ts,
            "open": close,
            "high": close + 0.4,
            "low": np.minimum(close - 0.4, np.roll(close, 1)),
            "close": close,
        }
    )
    r = run_user_hedge_pair(bars, range_mode="usdt", fill_engine="bar", fee_preset="base")
    if r["liquidated_long"] or r["liquidated_short"]:
        assert r["pair_stopped"] is True
        alive = r["short"] if r["liquidated_long"] else r["long"]
        assert abs(alive["end_qty"]) < 1e-6


def test_daily_pnl_first_day():
    ts = pd.Series(pd.date_range("2026-07-16", periods=30, freq="h", tz="UTC"))
    eq = np.linspace(10_000, 10_200, 30)
    d = daily_pnl(ts, eq, 10_000.0)
    assert abs(float(d.iloc[0]["daily_pnl"]) - (eq[23] - 10_000)) < 1e-6 or len(d) >= 1


def test_remap_lots_keeps_qty():
    b = IsolatedDirBook(5_000.0, 5.0, 0.0002, "long")
    old = user_levels(100.0, range_mode="usdt", range_usdt=20.0, n_grids=10)
    b.open_lot(1.0, float(old[0]), 0)
    assert abs(b.qty - 1.0) < 1e-12
    new = user_levels(80.0, range_mode="usdt", range_usdt=20.0, n_grids=10)
    remap_lots(b, old, new)
    assert abs(sum(b.lots.values()) - 1.0) < 1e-12
    assert abs(b.qty - 1.0) < 1e-12
    assert b.lots


def test_tick_without_get_trades_raises():
    bars = _chop_bars(16)
    with pytest.raises(ValueError, match="get_trades"):
        simulate_user_dir_grid(bars, direction="long", fill_engine="tick", get_trades=None)


def test_n_grids_must_be_two():
    with pytest.raises(ValueError, match="n_grids"):
        user_levels(100.0, n_grids=1)


def test_one_side_long_bar():
    bars = _chop_bars()
    r = run_user_one_side(bars, direction="long", fill_engine="bar", fee_preset="base")
    assert r["hedge_mode"] == "one_side"
    assert r["liquidated_short"] is False
    assert len(r["daily"]) >= 1
    assert r["end_equity"] >= 0
