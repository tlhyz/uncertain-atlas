"""P2-13 — meme satellite cap policy tests."""

from __future__ import annotations

from qtb.dual.universe import (
    CRYPTO_MEME,
    MEME_MAX_ACCOUNT_FRAC,
    TOTAL_CAPITAL,
    satellite_cap_budgets,
    satellite_cap_ok,
)


def test_satellite_cap_budgets_sum_to_five_percent():
    budgets = satellite_cap_budgets()
    assert set(budgets.keys()) == set(CRYPTO_MEME)
    assert abs(sum(budgets.values()) - TOTAL_CAPITAL * MEME_MAX_ACCOUNT_FRAC) < 1e-6
    assert satellite_cap_ok(budgets)
    per = TOTAL_CAPITAL * MEME_MAX_ACCOUNT_FRAC / len(CRYPTO_MEME)
    for sym in CRYPTO_MEME:
        assert abs(budgets[sym] - per) < 1e-6


def test_satellite_cap_rejects_over_budget():
    over = {"PENGU": 400.0, "PUMP": 200.0}
    assert not satellite_cap_ok(over)


def test_satellite_cap_even_split():
    budgets = satellite_cap_budgets(total=20_000.0, max_frac=0.10, symbols=("A", "B", "C"))
    assert budgets == {"A": 2000 / 3, "B": 2000 / 3, "C": 2000 / 3}
    assert satellite_cap_ok(budgets, total=20_000.0, max_frac=0.10)
