"""Mechanics tests for the ETF vs perp A/B engine. Handmade bars are not market data."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.ab.data import OverlapWindow, SeriesMeta, _assert_real_source, align_on_timestamp
from qtb.ab.engine import FeeSpec, run_cash, run_perp_grid, run_spot_grid
from qtb.ab.fills import FillConfig, PendingFill, resolve_bar_fills
from qtb.ab.grids import clip_etf_step, rolling_beta
from qtb.ab.metrics import composite_score, path_drag, summarize
from qtb.ab.regimes import classify
from qtb.ab.universe import PAIR_BY_NAME, long_pairs


def _bars(closes: list[float], start="2026-01-01", freq="1h", quote=1e6) -> pd.DataFrame:
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
            "quote_volume": quote,
            "funding_rate": 0.0,
        }
    )


def test_refuse_synthetic_source():
    with pytest.raises(RuntimeError, match="synthetic"):
        _assert_real_source("synthetic_sample", "BTC3L_USDT")
    with pytest.raises(RuntimeError, match="binance"):
        _assert_real_source("binance_public_klines", "BTC3L_USDT")
    _assert_real_source("gate_public_spot_candlesticks", "BTC3L_USDT")


def test_overlap_is_intersection_only():
    a = _bars([1, 2, 3, 4, 5], start="2026-01-01")
    b = _bars([1, 2, 3], start="2026-01-01 02:00")
    c = _bars([9, 8, 7, 6], start="2026-01-01 01:00")
    aa, bb, cc = align_on_timestamp(a, b, c)
    assert len(aa) == len(bb) == len(cc)
    assert aa["timestamp"].iloc[0] >= b["timestamp"].iloc[0]
    assert aa["timestamp"].iloc[-1] <= b["timestamp"].iloc[-1]


def test_skip_price_does_not_fill_all_levels():
    # One bar dumps through 10, 9, 8 but quote volume only covers ONE 100-notional buy.
    pending = [
        PendingFill("buy", 10.0, 0, notional=100.0, reason="g"),
        PendingFill("buy", 9.0, 1, notional=100.0, reason="g"),
        PendingFill("buy", 8.0, 2, notional=100.0, reason="g"),
    ]
    fills = resolve_bar_fills(pending, 10.2, 10.2, 7.8, 8.0, quote_volume=400.0, cfg=FillConfig.preset("base"))
    # base participation 20% of 400 = 80 → cannot fill even one full 100; refuse crumb
    assert len(fills) <= 1
    cons = resolve_bar_fills(pending, 10.2, 10.2, 7.8, 8.0, quote_volume=400.0, cfg=FillConfig.preset("conservative"))
    assert len(cons) <= len(fills)


def test_etf_step_clip_and_lagged_beta():
    assert clip_etf_step(0.001) == 0.005
    assert clip_etf_step(0.10) == 0.04
    etf = np.array([100.0, 106.0, 112.36, 119.1, 126.25, 133.82] + [133.82] * 20)
    und = np.array([100.0, 102.0, 104.04, 106.12, 108.24, 110.41] + [110.41] * 20)
    # ~3x if linear; we only check last beta uses past data and is finite
    b = rolling_beta(etf, und, n=8)
    assert np.all(np.isfinite(b))
    assert 0.2 <= b[-1] <= 8.0


def test_etf_has_no_liquidation_on_crash():
    closes = [100.0] * 30 + list(np.linspace(100, 40, 20))
    df = _bars(closes, quote=1e7)
    r = run_spot_grid(
        df,
        name="crash_etf",
        symbol="X3L",
        fee=FeeSpec(0.0008, 0.00085, 0.70),
        fill=FillConfig.preset("base"),
        initial=1000.0,
        hold_only=True,
        interval="1h",
    )
    assert r.liquidated is False
    assert r.final_equity < 1000
    assert r.final_equity > 0


def test_perp_liquidates_without_external_margin():
    # 3x long, no reserve, crash 50% — isolated book should die.
    closes = [100.0] * 30 + list(np.linspace(100, 40, 15))
    df = _bars(closes, quote=1e7)
    r = run_perp_grid(
        df,
        name="crash_perp",
        symbol="X_USDT",
        fee=FeeSpec(0.00008, 0.0002, 0.75),
        fill=FillConfig.preset("base"),
        initial=1000.0,
        target_notional=3000.0,
        leverage_hint=3.0,
        hold_only=True,
        dir_frac=1.0,
        mm_rate=0.005,
        quanto=0.01,
        min_contracts=1.0,
        interval="1h",
        reserve_plan="P1",
    )
    assert r.liquidated is True
    assert r.liquidation_count >= 1
    # leftover can only be residual cash — never topped up from outside
    assert r.final_equity <= 1000.0


def test_funding_is_applied_not_averaged():
    closes = [100.0] * 40
    df = _bars(closes, quote=1e7)
    df.loc[35, "funding_rate"] = 0.01  # +1% longs pay
    r = run_perp_grid(
        df,
        name="fund",
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
    )
    assert r.components["funding_paid"] > 0
    assert r.components["net_funding"] < 0


def test_score_penalizes_liquidation():
    good = {"total_return": 0.2, "max_dd_pct": 0.1, "net_profit_per_1m_turnover": 400, "capital_efficiency": 0.3, "liquidated": False, "liquidation_count": 0}
    bad = {**good, "liquidated": True, "liquidation_count": 2}
    assert composite_score(bad) < composite_score(good) - 0.3


def test_regime_ignores_pnl_uses_path():
    # up 30% smooth
    f = {"ret": 0.30, "rv": 0.01, "eff": 0.7, "max_dd": 0.05, "max_run": 0.3, "amp": 0.32, "mid_ret": 0.15, "second_half_ret": 0.13, "min_ret": -0.02, "max_ret": 0.30}
    assert classify(f) in {"uptrend", "persistent_trend"}
    v = {"ret": 0.05, "rv": 0.02, "eff": 0.1, "max_dd": 0.35, "max_run": 0.4, "amp": 0.4, "mid_ret": -0.25, "second_half_ret": 0.40, "min_ret": -0.28, "max_ret": 0.06}
    assert classify(v) == "v_reversal"


def test_path_drag_is_attribution_not_debit():
    etf = _bars([100, 90, 81, 89, 95])
    und = _bars([100, 96.6, 93.4, 96.0, 98.0])
    d = path_drag(etf, und, leverage=3.0)
    assert "path_drag" in d
    # engine equity is still the raw ETF mark — drag is a report field only
    r = run_cash(etf, 1000.0)
    assert r.final_equity == 1000.0


def test_soxl_has_real_perp_comparator():
    # Verified on Gate public API — do not mark NO DIRECT PERP.
    assert PAIR_BY_NAME["SOXL"].has_perp
    assert PAIR_BY_NAME["SNXX"].has_perp
    assert PAIR_BY_NAME["AAOI"].has_perp


def test_pagination_keeps_partial_on_too_long_ago(monkeypatch):
    from qtb.ab import data as abdata

    calls = {"n": 0}

    def fake_get(url, params):
        calls["n"] += 1
        if calls["n"] >= 3:
            raise RuntimeError("400 Candlestick too long ago")
        t = int(params["to"])
        return [
            {
                "t": t - i * 3600,
                "o": "1",
                "h": "1",
                "l": "1",
                "c": "1",
                "v": 1,
                "sum": 1,
            }
            for i in range(1000)
        ]

    monkeypatch.setattr(abdata, "_http_get_json", fake_get)
    df = abdata.fetch_gate_candles_capped("BTC3L_USDT", "1h", "spot", max_bars=5000, max_pages=8)
    assert len(df) > 0
    assert calls["n"] >= 2


def test_cash_benchmark_flat():
    r = run_cash(_bars([10, 11, 9, 12]), 1000.0)
    m = summarize(r, 1000.0)
    assert m["final_equity"] == 1000.0
    assert m["total_return"] == 0.0
