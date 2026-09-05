"""SL / TP / liq / range-break triggers + engine fire tests."""

from __future__ import annotations

import pandas as pd
import pytest

from qtb.config import default_config
from qtb.engine.backtest import run_backtest
from qtb.risk.exits import (
    RiskConfig,
    TrailingState,
    hit_investment_sl,
    hit_max_dd_stop,
    hit_per_trade_sl,
    hit_per_trade_tp,
    hit_portfolio_equity_sl,
    hit_portfolio_tp,
    near_liquidation,
    price_breaks_range,
    should_stop_adding,
    time_tp_due,
    trailing_stop_price,
)
from qtb.risk.liquidation import estimate_liq_price, force_exit_price


def test_per_trade_tp_sl():
    assert hit_per_trade_tp("long", 100.0, 101.5, 0.01)
    assert not hit_per_trade_tp("long", 100.0, 100.5, 0.01)
    assert hit_per_trade_tp("short", 100.0, 98.5, 0.01)
    assert hit_per_trade_sl("long", 100.0, 94.0, 0.05)
    assert hit_per_trade_sl("short", 100.0, 106.0, 0.05)
    assert not hit_per_trade_sl("long", 100.0, 96.0, 0.05)


def test_investment_sl_50_70():
    # 50% of 1000 investment → uPnL <= -500
    assert hit_investment_sl(-500.0, 1000.0, 0.50)
    assert not hit_investment_sl(-499.0, 1000.0, 0.50)
    assert hit_investment_sl(-700.0, 1000.0, 0.70)
    assert not hit_investment_sl(-699.0, 1000.0, 0.70)


def test_portfolio_and_dd_and_stop_adding():
    assert hit_portfolio_equity_sl(600.0, 1000.0, 0.30)
    assert hit_portfolio_tp(1300.0, 1000.0, 0.25)
    assert hit_max_dd_stop(0.41, 0.40)
    assert should_stop_adding(-350.0, 1000.0, 0.35)
    assert not should_stop_adding(-100.0, 1000.0, 0.35)


def test_liq_range_time_trailing():
    assert near_liquidation(5.0, 1000.0, 0.005, 0.20)  # maint=5, cushion=1 → 5 <= 6
    assert not near_liquidation(100.0, 1000.0, 0.005, 0.20)
    assert price_breaks_range(90.0, 100.0, 120.0)
    assert price_breaks_range(130.0, 100.0, 120.0)
    assert not price_breaks_range(110.0, 100.0, 120.0)
    assert time_tp_due(10, 8)
    assert not time_tp_due(3, 8)
    assert trailing_stop_price("long", 110.0, 0.02) == pytest.approx(107.8)
    assert trailing_stop_price("short", 90.0, 0.02) == pytest.approx(91.8)

    st = TrailingState()
    st.update("long", 103.0, 100.0, 0.02)
    assert st.activated
    assert st.extreme == 103.0


def test_liq_price_long_short():
    # Isolated long: P = (qty*avg - W) / (qty*(1-m))
    px = estimate_liq_price("long", 100.0, 1.0, 20.0, 0.005)
    assert px is not None and px < 100.0
    fx = force_exit_price("long", px, 0.20)
    assert fx is not None and fx > px


def _ohlcv(closes, highs=None, lows=None) -> pd.DataFrame:
    n = len(closes)
    idx = pd.date_range("2024-01-01", periods=n, freq="h", tz="UTC")
    highs = highs or [c * 1.001 for c in closes]
    lows = lows or [c * 0.999 for c in closes]
    return pd.DataFrame(
        {
            "timestamp": idx,
            "open": closes,
            "high": highs,
            "low": lows,
            "close": closes,
            "volume": [1.0] * n,
            "funding_rate": [0.0] * n,
        }
    )


def test_engine_investment_sl_fires():
    # Long martingale: price dumps so uPnL / capital <= -50%
    closes = [100.0] * 3 + [50.0] * 8
    df = _ohlcv(closes, highs=[c + 0.1 for c in closes], lows=[c - 0.1 for c in closes])
    cfg = default_config()
    cfg["prefer_sample"] = True
    cfg["strategy"] = {
        "name": "martingale",
        "direction": "long",
        "leverage": 5.0,
        "long_capital": 50.0,
        "initial_margin": 50.0,
        "multiplier": 1.2,
        "add_drop_pct": 0.50,
        "take_profit_pct": 0.50,
        "max_adds": 0,
        "base_order_quote": 80.0,
    }
    cfg["risk"] = RiskConfig(investment_sl_pct=0.50, force_exit_before_liq_buffer_pct=0.0, stop_if_price_breaks_range=False).__dict__
    cfg["costs"]["quanto"] = 0.01
    cfg["costs"]["min_order_size"] = 1.0
    cfg["costs"]["min_notional"] = 1.0
    cfg["costs"]["slippage_bps"] = 0.0
    cfg["costs"]["apply_funding"] = False
    result = run_backtest(cfg, df)
    reasons = [t.reason for t in result.trades]
    assert any(r == "investment_sl" for r in reasons)


def test_engine_per_trade_tp_fires():
    closes = [100.0] * 2 + [103.0] * 6
    highs = [c + 0.01 for c in closes]
    highs[2] = 102.0
    df = _ohlcv(closes, highs=highs, lows=[99.5] * len(closes))
    cfg = default_config()
    cfg["strategy"] = {
        "name": "martingale",
        "direction": "long",
        "leverage": 5.0,
        "long_capital": 500.0,
        "multiplier": 1.2,
        "add_drop_pct": 0.20,
        "take_profit_pct": 0.50,  # strategy TP far; risk TP closer
        "max_adds": 0,
        "base_order_quote": 50.0,
    }
    cfg["risk"] = RiskConfig(
        per_trade_tp_pct=0.015,
        investment_sl_pct=None,
        force_exit_before_liq_buffer_pct=0.0,
        stop_if_price_breaks_range=False,
    ).__dict__
    cfg["costs"]["quanto"] = 0.01
    cfg["costs"]["slippage_bps"] = 0.0
    cfg["costs"]["apply_funding"] = False
    result = run_backtest(cfg, df)
    assert any(t.reason == "per_trade_tp" for t in result.trades)
