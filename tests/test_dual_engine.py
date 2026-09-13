"""Tests for dual-engine state-switching framework."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.dual.crypto_fsm import CryptoAssetFSM, CryptoBookFSM
from qtb.dual.portfolio import run_dual_portfolio
from qtb.dual.signals import compute_anchor, dd_tier, drawdown_from_anchor, grid_mix_fractions
from qtb.dual.tech_fsm import TechFSM
from qtb.dual.universe import DRAWDOWN_SETS, DualParams, CryptoParams, TECH_BOOK, plan_presets


def _bars(closes: list[float], start="2026-01-01", freq="1h") -> pd.DataFrame:
    ts = pd.date_range(start, periods=len(closes), freq=freq, tz="UTC")
    c = np.asarray(closes, dtype=float)
    o = np.r_[c[0], c[:-1]]
    h = np.maximum(o, c) * 1.002
    l = np.minimum(o, c) * 0.998
    return pd.DataFrame(
        {
            "timestamp": ts,
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "volume": 1000.0,
            "quote_volume": 1e6,
            "funding_rate": 0.0,
        }
    )


def _mini_dataset(n: int = 200) -> "DualDataset":
    from qtb.dual.data import DualDataset, MarketData, WindowCoverage
    from qtb.ab.data import SeriesMeta

    # crash then recovery path
    c = [100.0] * 30
    for i in range(40):
        c.append(100 - i * 1.5)
    for i in range(n - len(c)):
        c.append(max(c[-1] * 1.01, 40))
    c = c[:n]
    soxl = _bars(c)
    snxx = _bars([x * 1.2 for x in c])
    meta = SeriesMeta("SOXL", "futures", "1h", "test", str(soxl["timestamp"].iloc[0]), str(soxl["timestamp"].iloc[-1]), n, n, "")
    md_s = MarketData("SOXL", "SOXL_USDT", "1h", soxl, pd.DataFrame(), meta)
    md_n = MarketData("SNXX", "SNXX_USDT", "1h", snxx, pd.DataFrame(), meta)
    crypto = {}
    for sym, base in (("BTC", 50000), ("ETH", 3000), ("SOL", 150)):
        cc = [base * (1 + 0.001 * i) for i in range(n)]
        b = _bars(cc)
        crypto[sym] = MarketData(sym, f"{sym}_USDT", "1h", b, pd.DataFrame(), meta)
    return DualDataset(
        "1h",
        {"SOXL": md_s, "SNXX": md_n},
        crypto,
        pd.DatetimeIndex(soxl["timestamp"]),
        [],
        pd.Timestamp(soxl["timestamp"].iloc[0]),
        pd.Timestamp(soxl["timestamp"].iloc[-1]),
    )


def test_drawdown_tiers():
    th = DRAWDOWN_SETS["B"]
    assert dd_tier(-0.05, th) == 0
    assert dd_tier(-0.12, th) == 1
    assert dd_tier(-0.35, th) == 3


def test_grid_mix_dynamic():
    g, d = grid_mix_fractions("dynamic", "strong")
    assert g == 0.20 and d == 0.80


def test_tech_fsm_tier_progression():
    params = DualParams().tech
    fsm = TechFSM(params)
    close = np.linspace(100, 70, 200)
    high = close * 1.01
    low = close * 0.99
    snxx = close * 1.1
    anchor = compute_anchor(close, "start")
    dd = drawdown_from_anchor(close, anchor)
    tiers = []
    for i in range(50, 100):
        exp = fsm.on_bar(i, float(dd[i]), close, high, low, snxx)
        tiers.append(exp.dd_tier)
    assert max(tiers) >= 1


def test_crypto_fsm_independent():
    fsm = CryptoBookFSM(DualParams().crypto)
    n = 100
    close = np.linspace(100, 130, n)
    high = close * 1.01
    low = close * 0.99
    bars = {"BTC": {"close": close, "high": high, "low": low}}
    exp = fsm.on_bar(n - 1, bars, tech_signal_dd=-0.20, unified=False)
    assert "BTC" in exp
    # unified should differ
    exp_u = fsm.on_bar(n - 1, bars, tech_signal_dd=-0.20, unified=True)
    assert exp["BTC"].regime != exp_u["BTC"].regime or exp["BTC"].long_dir_frac != exp_u["BTC"].long_dir_frac


def test_bull_dynamic_sell_the_winner_mix():
    """P2-09: BULL + dynamic mix uses strong 20/80 — directional > grid (sell-the-winner)."""
    params = CryptoParams(grid_mix="dynamic", leverage=1.5)
    fsm = CryptoAssetFSM("BTC", params)
    g_strong, d_strong = grid_mix_fractions("dynamic", "strong")
    assert (g_strong, d_strong) == (0.20, 0.80)
    exp = fsm.exposure("BULL")
    assert exp.regime == "BULL"
    assert exp.long_dir_frac > exp.long_grid_frac
    # 20/80 mix × util 0.65 × lev 1.5 → dir/grid ratio = 4.0
    assert abs(exp.long_dir_frac / exp.long_grid_frac - 4.0) < 1e-6


def test_dual_portfolio_runs():
    data = _mini_dataset(180)
    r = run_dual_portfolio(data, DualParams(), name="test", fill_mode="base")
    assert len(r.total_equity) == 180
    assert r.final_equity > 0


def test_benchmark_cash():
    data = _mini_dataset(100)
    r = run_dual_portfolio(data, DualParams(), benchmark="B1_cash")
    assert abs(r.final_equity - 10000) < 100  # cash flat


def test_plan_presets_exist():
    plans = plan_presets()
    assert "稳健版" in plans
    assert "平衡版" in plans
    assert "激进版" in plans


def test_rank_short_init_sweep():
    from qtb.dual.experiments import rank_short_init

    data = _mini_dataset(120)
    rows = rank_short_init(data, levels=(0.10, 0.15, 0.20), tick_precise=False)
    assert len(rows) == 3
    assert {r["short_init_pct"] for r in rows} == {0.10, 0.15, 0.20}
    assert all("total_return" in r for r in rows)


def test_rank_short_structures_sweep():
    from qtb.dual.experiments import rank_short_structures

    data = _mini_dataset(120)
    rows = rank_short_structures(data, tick_precise=False)
    assert len(rows) == 4
    assert {r["short_structure"] for r in rows} == {"directional", "grid", "70_30", "50_50"}
    assert all("total_return" in r for r in rows)


def test_rank_drawdown_sets_sweep():
    from qtb.dual.experiments import rank_drawdown_sets

    data = _mini_dataset(120)
    rows = rank_drawdown_sets(data, tick_precise=False)
    assert len(rows) == 3
    assert {r["drawdown_set"] for r in rows} == {"A", "B", "C"}
    assert all("total_return" in r for r in rows)


def test_rank_right_side_reserve_sweep():
    from qtb.dual.experiments import rank_right_side_reserve

    data = _mini_dataset(120)
    rows = rank_right_side_reserve(data, tick_precise=False)
    assert len(rows) == 3
    assert {r["right_side_reserve_frac"] for r in rows} == {0.25, 0.30, 0.35}
    assert all("total_return" in r for r in rows)


def test_rank_soxl_snxx_weights_sweep():
    from qtb.dual.experiments import rank_soxl_snxx_weights

    data = _mini_dataset(120)
    rows = rank_soxl_snxx_weights(data, tick_precise=False)
    assert len(rows) == 3
    assert {r["soxl_weight"] for r in rows} == {0.75, 0.70, 0.65}
    assert all("total_return" in r for r in rows)


def test_rank_grid_mix_sweep():
    from qtb.dual.experiments import rank_grid_mix

    data = _mini_dataset(120)
    rows = rank_grid_mix(data, mixes=("G100", "dynamic"), tick_precise=False)
    assert len(rows) == 2
    assert {r["grid_mix"] for r in rows} == {"G100", "dynamic"}
    assert all("total_return" in r for r in rows)
