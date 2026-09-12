"""Adversarial research invariants: ticks, contamination, path decay, window tags."""

from __future__ import annotations

from datetime import date, datetime, timezone

import numpy as np
import pandas as pd
import pytest

from qtb.data.gatedata import generate_sample_deals
from qtb.research.sl_phase.catalog import BASELINE_GRIDS, CANDIDATE_REGIMES, MAKER_FEE, TAKER_FEE
from qtb.research.sl_phase.etf_series import stitch_synth_then_real, synthesize_from_underlying
from qtb.research.sl_phase.fees_ledger import FeeLedger, assert_identity
from qtb.research.sl_phase.fills import FillPolicy, buy_matches, sell_matches
from qtb.research.sl_phase.geometric_grid import geometric_levels, GeometricSpotGrid
from qtb.research.sl_phase.windows import classify_regime, remap_candidate, series_confidence


def test_fees_are_external_config_not_guessed():
    assert MAKER_FEE == 0.0008
    assert TAKER_FEE == 0.00085


def test_fee_ledger_does_not_hide_rebate():
    led = FeeLedger(0.0008, 0.00085, 0.70, 0.001)
    led.charge(10_000, maker=True)
    assert led.gross_fee == pytest.approx(8.0)
    assert led.rebate_income == pytest.approx(5.6)
    assert led.net_trading_fee == pytest.approx(2.4)
    assert_identity(led)


def test_fills_base_requires_trade_through():
    pol = FillPolicy.of("base")
    assert buy_matches(0.99, 1.0, 0.01, pol) is True
    assert buy_matches(1.0, 1.0, 0.01, pol) is False
    assert sell_matches(1.01, 1.0, 0.01, pol) is True
    assert sell_matches(1.0, 1.0, 0.01, pol) is False


def test_geometric_levels_are_etf_prices():
    lv = geometric_levels(100.0, 0.60, 1.45, 56)
    assert lv[0] == pytest.approx(60.0)
    assert lv[-1] == pytest.approx(145.0)
    assert len(lv) == 57
    # geometric, not arithmetic
    r = lv[1] / lv[0]
    assert lv[2] / lv[1] == pytest.approx(r)


def test_synth_roundtrip_does_not_return_to_start():
    """100 → 80 → 100 on underlying must NOT restore 3L NAV to 100."""
    ts = pd.date_range("2024-01-01", periods=3, freq="D", tz="UTC")
    under = pd.DataFrame({"timestamp": ts, "price": [100.0, 80.0, 100.0]})
    syn = synthesize_from_underlying(under, side="3L", start_nav=100.0)
    assert syn["price"].iloc[-1] != pytest.approx(100.0, abs=0.5)
    assert syn["price"].iloc[-1] < 100.0


def test_stitch_scales_level_not_returns():
    ts0 = pd.date_range("2026-06-01", periods=3, freq="D", tz="UTC")
    ts1 = pd.date_range("2026-06-04", periods=2, freq="D", tz="UTC")
    synth = pd.DataFrame({"timestamp": ts0, "price": [1.0, 1.1, 1.2], "dealid": [1, 2, 3], "amount": 1.0, "side": "s"})
    real = pd.DataFrame({"timestamp": ts1, "price": [2.4, 2.5], "dealid": [4, 5], "amount": 1.0, "side": "b"})
    out, st = stitch_synth_then_real("X3L_USDT", synth, real)
    assert st.scale == pytest.approx(2.0)
    # first two synth returns preserved after scale
    r0 = out["price"].iloc[1] / out["price"].iloc[0]
    assert r0 == pytest.approx(1.1)
    assert out["price"].iloc[2] == pytest.approx(2.4)


def test_soxl_not_sox_9x_in_catalog():
    assert "NOT SOX 9x" in __import__("qtb.research.sl_phase.catalog", fromlist=["PRODUCTS"]).PRODUCTS["SOXL3L_USDT"].notes


def test_candidate_windows_are_not_auto_real():
    assert any(w.id == "S1" for w in CANDIDATE_REGIMES)
    assert series_confidence("SOXL3L_USDT", date(2024, 7, 1), date(2024, 9, 6)) == "SYNTHETIC_GATE_ETF_WINDOW"
    # remap with empty series → excluded
    w = remap_candidate(CANDIDATE_REGIMES[0], "SOXL3L_USDT", pd.Series(dtype=float), confidence="REAL_GATE_ETF_WINDOW")
    assert w.confidence == "UNDERLYING_ONLY_CANDIDATE"
    assert w.allowed_in_stats() is False


def test_grid_on_sample_tape_counts_inventory():
    tape = generate_sample_deals(n=200, mid=1.0, amp=0.05)
    eng = GeometricSpotGrid(
        symbol="TEST3L_USDT",
        capital=500.0,
        lower_mult=0.70,
        upper_mult=1.30,
        grid_n=10,
        fill_model="base",
        rebate_rate=0.0,
    )
    res = eng.run(tape)
    assert res.initial_market_buy > 0
    assert res.initial_taker_fee > 0
    # TOTAL EQUITY identity
    assert res.final_equity == pytest.approx(res.cash + res.base * res.last_px, rel=1e-6)


def test_baseline_grids_use_new_spec():
    assert BASELINE_GRIDS["SOXL3L_USDT"]["grid_n"] == 56
    assert BASELINE_GRIDS["SOXL3L_USDT"]["lower_mult"] == 0.60


def test_classify_drop_then_rise():
    # 100 → 60 → 110
    a = np.linspace(100, 60, 40)
    b = np.linspace(60, 110, 40)
    assert classify_regime(np.concatenate([a, b])) in {"drop_then_rise", "v_reversal"}
