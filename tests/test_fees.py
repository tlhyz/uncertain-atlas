"""Smoke tests for fee/rebate math."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fees import VIP7_SPOT_70, effective_fee, fee_on_notional, compare_fee_drag


def test_effective_fee_formula():
    """Assert effective_fee = base * (1 - rebate)."""
    base = 0.0008
    rebate = 0.70
    assert effective_fee(base, rebate) == pytest.approx(base * (1 - rebate))
    assert effective_fee(0.00085, 0.70) == pytest.approx(0.00085 * 0.30)
    assert effective_fee(0.001, 0.0) == 0.001
    assert effective_fee(0.001, 1.0) == 0.0


def test_vip7_spot_70_preset():
    assert VIP7_SPOT_70.effective_maker == pytest.approx(0.0008 * 0.30)
    assert VIP7_SPOT_70.effective_taker == pytest.approx(0.00085 * 0.30)


def test_fee_on_notional():
    assert fee_on_notional(10_000, 0.00024) == pytest.approx(2.4)


def test_compare_fee_drag():
    d = compare_fee_drag(10_000, 0.0008, 0.70)
    assert d["fee_saved"] == pytest.approx(d["fee_no_rebate"] - d["fee_with_rebate"])
    assert d["fee_with_rebate"] == pytest.approx(10_000 * 0.0008 * 0.30)


def test_invalid_rebate():
    with pytest.raises(ValueError):
        effective_fee(0.001, 1.5)
