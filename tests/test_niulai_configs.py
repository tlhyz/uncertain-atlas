"""Aggressive dual-hedge niulai configs + asymmetric long/short params."""

from __future__ import annotations

from pathlib import Path

from qtb.config import load_config
from qtb.engine.backtest import run_backtest
from qtb.optimize.search import _custom_grid
from qtb.risk.exits import RiskConfig
from qtb.strategies.martingale import side_martingale_cfg

ROOT = Path(__file__).resolve().parents[1]


def test_side_martingale_cfg_asymmetric():
    cfg = {
        "multiplier": 1.5,
        "add_drop_pct": 0.015,
        "take_profit_pct": 0.012,
        "max_adds": 90,
        "long_capital": 950.0,
        "short_capital": 1380.0,
        "long": {"multiplier": 1.4, "add_drop_pct": 0.025, "base_order_quote": 237.5},
        "short": {"multiplier": 1.2, "add_drop_pct": 0.040},
        "short_base_order_quote": 291.9385,
    }
    lo = side_martingale_cfg(cfg, "long")
    sh = side_martingale_cfg(cfg, "short")
    assert lo["multiplier"] == 1.4
    assert lo["add_drop_pct"] == 0.025
    assert lo["base_order_quote"] == 237.5
    assert lo["long_capital"] == 950.0
    assert sh["multiplier"] == 1.2
    assert sh["add_drop_pct"] == 0.040
    assert sh["base_order_quote"] == 291.9385
    assert sh["take_profit_pct"] == 0.012
    assert sh["max_adds"] == 90


def test_load_niulai_backtest_configs():
    sl50 = load_config(ROOT / "configs/backtest_niulai_aggressive_sl50.yaml")
    sl70 = load_config(ROOT / "configs/backtest_niulai_aggressive_sl70.yaml")
    assert sl50["symbol"] == "牛来_USDT"
    assert sl50["interval"] == "5m"
    assert sl50["days"] == 18
    assert sl50["strategy"]["name"] == "dual_martingale"
    assert sl50["strategy"]["long_capital"] == 950.0
    assert sl50["strategy"]["short_capital"] == 1380.0
    assert sl50["strategy"]["max_adds"] == 90
    assert sl50["strategy"]["long"]["multiplier"] == 1.4
    assert sl50["strategy"]["short"]["add_drop_pct"] == 0.040
    assert sl50["risk"]["investment_sl_pct"] == 0.50
    assert sl50["costs"]["vip_tier"] == 7
    assert sl50["costs"]["rebate_rate"] == 0.75
    assert sl70["risk"]["investment_sl_pct"] == 0.70
    assert sl70["strategy"]["long"]["multiplier"] == 1.8
    assert sl70["strategy"]["short"]["multiplier"] == 1.3


def test_load_niulai_optimize_compact_grid():
    cfg = load_config(ROOT / "configs/optimize_niulai_aggressive_sl50.yaml")
    opt = cfg["optimize"]
    assert opt["grid"] == "compact"
    assert opt["anti_overfit"] is True
    grid = _custom_grid(opt)
    assert grid is not None
    n = 1
    for v in grid.values():
        n *= len(v)
    assert n <= 32
    assert 1.4 in grid["long_multiplier"]
    assert 0.040 in grid["short_add_drop_pct"]


def test_engine_uses_asymmetric_drops():
    import pandas as pd

    # Short only: with 4% drop, a +2% rally should NOT add; +4.1% should.
    closes = [100.0, 100.0, 102.0, 104.2, 104.2]
    highs = [100.2, 100.2, 102.1, 104.3, 104.3]
    lows = [99.8, 99.8, 101.8, 103.9, 103.9]
    idx = pd.date_range("2024-01-01", periods=5, freq="h", tz="UTC")
    df = pd.DataFrame(
        {
            "timestamp": idx,
            "open": closes,
            "high": highs,
            "low": lows,
            "close": closes,
            "volume": [1.0] * 5,
            "funding_rate": [0.0] * 5,
        }
    )
    from qtb.config import default_config

    cfg = default_config()
    cfg["strategy"] = {
        "name": "dual_martingale",
        "leverage": 5.0,
        "long_capital": 950.0,
        "short_capital": 1380.0,
        "max_adds": 90,
        "take_profit_pct": 0.50,
        "long": {"multiplier": 1.4, "add_drop_pct": 0.50, "base_order_quote": 40.0},
        "short": {"multiplier": 1.2, "add_drop_pct": 0.040, "base_order_quote": 40.0},
    }
    cfg["risk"] = RiskConfig(
        investment_sl_pct=0.50,
        force_exit_before_liq_buffer_pct=0.0,
        stop_if_price_breaks_range=False,
    ).__dict__
    cfg["costs"]["quanto"] = 0.01
    cfg["costs"]["min_order_size"] = 1.0
    cfg["costs"]["slippage_bps"] = 0.0
    cfg["costs"]["apply_funding"] = False
    result = run_backtest(cfg, df)
    short_adds = [t for t in result.trades if t.book == "short" and t.reason == "mart_add"]
    assert len(short_adds) >= 1
    assert any(abs(t.price - 104.0) < 0.15 for t in short_adds)
