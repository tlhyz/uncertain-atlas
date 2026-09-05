"""Cost model: rebate, slippage, funding, quanto / min size."""

from __future__ import annotations

import pytest

from qtb.costs import (
    VIP7_FUTURES_75,
    VIP7_SPOT_70,
    CostModel,
    apply_slippage,
    compare_fee_drag,
    effective_fee,
    fee_on_notional,
    fee_preset,
    funding_pnl,
    round_to_quanto,
)


def test_effective_fee_formula():
    assert effective_fee(0.0008, 0.70) == pytest.approx(0.0008 * 0.30)
    assert effective_fee(0.0002, 0.75) == pytest.approx(0.00005)
    assert effective_fee(0.001, 0.0) == 0.001
    assert effective_fee(0.001, 1.0) == 0.0


def test_invalid_rebate_and_fee():
    with pytest.raises(ValueError):
        effective_fee(0.001, 1.5)
    with pytest.raises(ValueError):
        effective_fee(-0.1, 0.5)


def test_vip7_presets():
    assert VIP7_SPOT_70.effective_maker == pytest.approx(0.0008 * 0.30)
    assert VIP7_FUTURES_75.effective_taker == pytest.approx(0.0002 * 0.25)
    fut = fee_preset("futures", vip_tier=7, rebate_rate=0.75)
    assert fut.effective_maker == pytest.approx(0.00008 * 0.25)


def test_fee_on_notional_and_drag():
    assert fee_on_notional(10_000, 0.00024) == pytest.approx(2.4)
    d = compare_fee_drag(10_000, 0.0008, 0.70)
    assert d["fee_saved"] == pytest.approx(d["fee_no_rebate"] - d["fee_with_rebate"])


def test_slippage_against_taker():
    assert apply_slippage(100.0, "buy", 10) == pytest.approx(100.1)
    assert apply_slippage(100.0, "sell", 10) == pytest.approx(99.9)
    with pytest.raises(ValueError):
        apply_slippage(100.0, "hold", 1)


def test_funding_long_pays_when_rate_positive():
    assert funding_pnl(2.0, 50.0, 0.0001) == pytest.approx(-0.01)
    assert funding_pnl(-2.0, 50.0, 0.0001) == pytest.approx(0.01)


def test_quanto_and_min_size():
    assert round_to_quanto(0.00025, 0.0001) == pytest.approx(0.0002)
    cm = CostModel(quanto=0.0001, min_order_size=1.0, min_notional=1.0, slippage_bps=0.0)
    qty = cm.size_from_notional(14.0, 70_000.0)  # 0.0002 BTC
    assert qty == pytest.approx(0.0002)
    assert cm.accept_order(0.0002, 70_000.0)
    assert not cm.accept_order(0.00005, 70_000.0)  # < 1 contract
    assert not cm.accept_order(0.0002, 1.0)  # notional 0.0002 < 1


def test_cost_model_fee_uses_rebate():
    cm = CostModel(use_maker=False, slippage_bps=0.0)
    fee = cm.fee(10_000)
    assert fee == pytest.approx(10_000 * VIP7_FUTURES_75.effective_taker)
