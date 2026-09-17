"""Accounting invariant checks for backtest engines."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from qtb.ab.engine import EngineResult, _perp_upnl, _spot_equity, _PerpState, _perp_equity


class AccountingInvariantError(AssertionError):
    """Raised when equity conservation checks fail."""


def spot_equity(cash: float, qty: float, mark: float) -> float:
    return cash + qty * mark


def perp_equity_from_components(
    wallet: float,
    locked: float,
    reserve: float,
    qty: float,
    avg: float,
    mark: float,
    *,
    liquidated: bool = False,
    isolated: bool = False,
    include_reserve: bool = True,
) -> float:
    st = _PerpState(wallet=wallet + locked, reserve=reserve)  # wallet param includes free only
    # Reconstruct: _PerpState.wallet is free cash; locked separate
    st.wallet = wallet
    st.locked = locked
    st.qty = qty
    st.avg = avg
    st.liquidated = liquidated
    return _perp_equity(st, mark, include_reserve=include_reserve, isolated=isolated)


def implied_perp_locked(cash_component: float, inventory_value: float, equity: float) -> float:
    """From engine arrays: locked = cash + inventory_value − equity."""
    return cash_component + inventory_value - equity


def verify_spot_engine_result(
    result: EngineResult,
    closes: np.ndarray | list[float],
    *,
    tol: float = 1e-4,
) -> None:
    """Per-bar: equity == cash + qty * close."""
    closes_a = np.asarray(closes, dtype=float)
    n = len(result.equity)
    if len(closes_a) != n:
        raise AccountingInvariantError(f"closes length {len(closes_a)} != equity {n}")
    for i in range(n):
        expected = float(result.cash[i]) + float(result.position_qty[i]) * closes_a[i]
        actual = float(result.equity[i])
        if abs(actual - expected) > tol:
            raise AccountingInvariantError(
                f"spot bar {i}: equity={actual} expected={expected} "
                f"cash={result.cash[i]} qty={result.position_qty[i]} px={closes_a[i]}"
            )


def verify_perp_engine_result(
    result: EngineResult,
    *,
    tol: float = 1e-3,
) -> None:
    """Per-bar perp identity using engine's cash + inventory_value arrays."""
    n = len(result.equity)
    for i in range(n):
        eq = float(result.equity[i])
        cash = float(result.cash[i])
        inv = float(result.inventory_value[i])
        locked = implied_perp_locked(cash, inv, eq)
        if locked < -tol:
            raise AccountingInvariantError(f"perp bar {i}: implied locked={locked} < 0")
        upnl = inv - locked
        expected = cash + upnl
        if abs(eq - expected) > tol:
            raise AccountingInvariantError(
                f"perp bar {i}: equity={eq} expected={expected} cash={cash} inv={inv} locked={locked}"
            )


def verify_engine_result(
    result: EngineResult,
    bars: pd.DataFrame | None = None,
    *,
    tol: float = 1e-3,
) -> None:
    """Dispatch invariant checks by market type."""
    if result.market in ("spot", "cash"):
        if bars is not None and "close" in bars.columns:
            verify_spot_engine_result(result, bars["close"].to_numpy(), tol=tol)
        elif result.market == "cash":
            for i in range(len(result.equity)):
                if abs(float(result.equity[i]) - float(result.cash[i])) > tol:
                    raise AccountingInvariantError(f"cash bar {i}: equity != cash")
        return
    if result.market == "perp":
        verify_perp_engine_result(result, tol=tol)
        return


def assert_equity_non_negative(result: EngineResult, *, tol: float = 1e-9) -> None:
    if np.any(result.equity < -tol):
        idx = int(np.argmin(result.equity))
        raise AccountingInvariantError(f"negative equity at bar {idx}: {result.equity[idx]}")


def assert_no_money_from_nothing(
    initial: float,
    result: EngineResult,
    *,
    tol: float = 1e-6,
) -> None:
    """With zero trades, equity must equal initial."""
    if result.trades:
        return
    for i in range(len(result.equity)):
        if abs(float(result.equity[i]) - initial) > tol:
            raise AccountingInvariantError(
                f"bar {i}: no trades but equity={result.equity[i]} != initial={initial}"
            )
