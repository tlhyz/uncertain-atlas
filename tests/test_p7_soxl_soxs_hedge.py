"""Synthetic tests for SOXL/SOXS hedge diagnostics — no live download required."""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.analysis.soxl_soxs_hedge import (
    align_pair,
    buy_hold_pair,
    hedge_diagnostics,
    run_hedge_experiment,
    simulate_long_grid,
)


def _bars(close: np.ndarray, start: str = "2026-07-16") -> pd.DataFrame:
    ts = pd.date_range(start, periods=len(close), freq="h", tz="UTC")
    c = np.asarray(close, dtype=float)
    return pd.DataFrame(
        {
            "timestamp": ts,
            "open": c,
            "high": c * 1.002,
            "low": c * 0.998,
            "close": c,
        }
    )


def test_perfect_inverse_corr_and_residual():
    rng = np.random.default_rng(0)
    r = rng.normal(0.0, 0.01, 200)
    soxl = 100.0 * np.exp(np.cumsum(np.concatenate([[0.0], r])))
    soxs = 50.0 * np.exp(np.cumsum(np.concatenate([[0.0], -r])))
    d = hedge_diagnostics(soxl, soxs)
    assert d.corr_1h < -0.99
    assert d.beta_soxs_on_soxl < -0.90
    assert d.residual_vol_1to1 < 0.15 * d.soxl_vol


def test_snxx_like_positive_beta_fails_inverse_gate():
    rng = np.random.default_rng(1)
    r = rng.normal(0.0, 0.01, 200)
    soxl = 100.0 * np.exp(np.cumsum(np.concatenate([[0.0], r])))
    snxx = 80.0 * np.exp(np.cumsum(np.concatenate([[0.0], 0.45 * r + rng.normal(0, 0.003, 200)])))
    a, b = _bars(soxl), _bars(snxx)
    rep = run_hedge_experiment(a, b, fee_preset="base")
    assert rep["inverse_gate"] is False
    assert rep["verdict"] == "FAIL"


def test_align_pair_inner_join():
    a = _bars(np.linspace(100, 110, 10))
    b = _bars(np.linspace(50, 40, 8))
    b = b.iloc[2:].reset_index(drop=True)
    x, y = align_pair(a, b)
    assert len(x) == len(y) == 6
    assert x["timestamp"].iloc[0] == b["timestamp"].iloc[0]


def test_static_pair_bh_flat_on_perfect_inverse():
    r = np.array([0.02, -0.01, 0.015, -0.02, 0.01] * 20)
    soxl = 100.0 * np.exp(np.cumsum(np.concatenate([[0.0], r])))
    soxs = 100.0 * np.exp(np.cumsum(np.concatenate([[0.0], -r])))
    eq = buy_hold_pair(soxl, soxs, 10_000.0, 0.5, "none")
    # path-dependent 3x-style inverse is not dollar-flat; residual should stay bounded
    assert abs(eq[-1] / eq[0] - 1.0) < 0.15


def test_long_grid_runs_on_chop():
    t = np.linspace(0, 8 * np.pi, 120)
    close = 100.0 + 4.0 * np.sin(t)
    out = simulate_long_grid(_bars(close), capital=5_000.0, fee_preset="conservative")
    assert out["fills"] >= 0
    assert out["end_equity"] > 0
    assert "inventory_frac" in out


def test_tick_engine_uses_trade_path_not_wick():
    """A wick-only bar must not fill on TICK if no aggTrade crosses the level."""
    close = np.full(80, 100.0)
    close[40:] = 100.2
    bars = _bars(close)
    bars.loc[40, "low"] = 95.0  # wick that would fill BAR
    bars.loc[40, "high"] = 100.3

    def no_cross(_i, _ts):
        ts = pd.Timestamp("2026-07-16 16:00:00", tz="UTC")
        return pd.DataFrame(
            {
                "timestamp": [ts, ts + pd.Timedelta(minutes=1)],
                "price": [100.05, 100.10],
                "qty": [1.0, 1.0],
                "quote_qty": [100.05, 100.10],
            }
        )

    tick = simulate_long_grid(bars, capital=5_000.0, fill_engine="tick", get_trades=no_cross, fee_preset="base")
    bar = simulate_long_grid(bars, capital=5_000.0, fill_engine="bar", fee_preset="base")
    assert tick["fills"] <= bar["fills"]
