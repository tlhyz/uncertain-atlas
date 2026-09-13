"""Accounting invariant and property tests."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from qtb.ab.accounting_check import (
    AccountingInvariantError,
    assert_equity_non_negative,
    assert_no_money_from_nothing,
    implied_perp_locked,
    perp_equity_from_components,
    spot_equity,
    verify_engine_result,
    verify_perp_engine_result,
    verify_spot_engine_result,
)
from qtb.ab.engine import FeeSpec, run_cash, run_perp_grid, run_spot_grid
from qtb.ab.fills import FillConfig
from src.data.quality_gate import count_csv_rows


def _bars(closes, quote=1e6):
    n = len(closes)
    ts = pd.date_range("2024-01-01", periods=n, freq="h", tz="UTC")
    return pd.DataFrame(
        {
            "timestamp": ts,
            "open": closes,
            "high": [c * 1.001 for c in closes],
            "low": [c * 0.999 for c in closes],
            "close": closes,
            "volume": [100.0] * n,
            "quote_volume": [quote] * n,
            "funding_rate": [0.0] * n,
        }
    )


def test_spot_equity_formula():
    assert spot_equity(1000.0, 2.0, 50.0) == 1100.0


def test_perp_equity_components_cross():
    eq = perp_equity_from_components(
        wallet=700.0, locked=200.0, reserve=100.0, qty=1.0, avg=90.0, mark=100.0
    )
    assert abs(eq - (700 + 200 + 100 + 10)) < 1e-9


def test_cash_benchmark_invariants():
    bars = _bars([10.0, 11.0, 9.0, 12.0])
    r = run_cash(bars, 1000.0)
    verify_engine_result(r, bars)
    assert_no_money_from_nothing(1000.0, r)


def test_spot_grid_equity_conservation():
    bars = _bars(list(np.linspace(100, 105, 30)), quote=5e6)
    r = run_spot_grid(
        bars,
        name="spot_test",
        symbol="ETF",
        fee=FeeSpec(0.0008, 0.00085, 0.7),
        fill=FillConfig.preset("base"),
        initial=1000.0,
        interval="1h",
    )
    verify_spot_engine_result(r, bars["close"].to_numpy())
    assert_equity_non_negative(r)


def test_perp_hold_flat_zero_fee_funding_unchanged():
    bars = _bars([100.0] * 40, quote=1e7)
    r = run_perp_grid(
        bars,
        name="flat",
        symbol="X_USDT",
        fee=FeeSpec(0.0, 0.0, 0.0),
        fill=FillConfig.preset("base"),
        initial=1000.0,
        target_notional=3000.0,
        leverage_hint=3.0,
        hold_only=True,
        dir_frac=1.0,
        mm_rate=0.005,
        quanto=0.01,
        interval="1h",
        reserve_plan="P1",
    )
    verify_perp_engine_result(r)
    # Open uses margin from wallet — total equity (incl reserve) still ~1000 at flat mark
    assert abs(r.final_equity - 1000.0) < 1.0


def test_deterministic_replay_perp():
    bars = _bars(list(np.linspace(100, 90, 25)), quote=2e6)
    kw = dict(
        name="det",
        symbol="X_USDT",
        fee=FeeSpec(0.00008, 0.0002, 0.75),
        fill=FillConfig.preset("base"),
        initial=1000.0,
        target_notional=2000.0,
        leverage_hint=2.0,
        hold_only=True,
        dir_frac=0.5,
        mm_rate=0.005,
        quanto=0.01,
        interval="1h",
    )
    r1 = run_perp_grid(bars, **kw)
    r2 = run_perp_grid(bars, **kw)
    np.testing.assert_allclose(r1.equity, r2.equity, rtol=0, atol=1e-9)
    assert r1.final_equity == r2.final_equity


def test_implied_locked_non_negative():
    bars = _bars(list(np.linspace(100, 95, 20)), quote=3e6)
    r = run_perp_grid(
        bars,
        name="x",
        symbol="X_USDT",
        fee=FeeSpec(0.00008, 0.0002, 0.75),
        fill=FillConfig.preset("conservative"),
        initial=1000.0,
        target_notional=2500.0,
        leverage_hint=2.0,
        mm_rate=0.005,
        quanto=0.01,
        interval="1h",
    )
    for i in range(len(r.equity)):
        locked = implied_perp_locked(float(r.cash[i]), float(r.inventory_value[i]), float(r.equity[i]))
        assert locked >= -1e-6, f"bar {i} locked={locked}"


def test_verify_engine_result_raises_on_corrupt():
    bars = _bars([100.0, 101.0])
    r = run_cash(bars, 1000.0)
    r.equity[1] = 999.0  # corrupt
    with pytest.raises(AccountingInvariantError):
        verify_engine_result(r, bars)


def test_regression_ts_ms_row_count(tmp_path):
    """Regression: legacy timestamp CSV must count rows (build_manifest fix)."""
    p = tmp_path / "legacy.csv"
    pd.DataFrame(
        {"timestamp": ["2024-09-01 00:00:00+00:00", "2024-09-01 00:00:01+00:00"], "price": [1.0, 2.0]}
    ).to_csv(p, index=False)
    assert count_csv_rows(p) == 2
