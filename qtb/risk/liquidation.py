"""Isolated-margin liquidation price estimates (approximate, research-grade)."""

from __future__ import annotations

from typing import Literal

Direction = Literal["long", "short"]


def estimate_liq_price(
    direction: Direction,
    avg_entry: float,
    qty: float,
    wallet_plus_margin: float,
    maintenance_rate: float,
) -> float | None:
    """
    Isolated approx: equity = wallet_free + locked_margin + uPnL.
    Liquidation when equity <= notional * maint.

    For long:  (W + qty*(P-avg)) <= qty*P*m
      W + qty*P - qty*avg <= qty*P*m
      W - qty*avg <= qty*P*(m-1)
      P >= (qty*avg - W) / (qty*(1-m))   if we solve the equality
    Actually we want the P where equality holds.

    Long: W + qty*(P-avg) = qty*P*m
          W - qty*avg = qty*P*m - qty*P = qty*P*(m-1)
          P = (W - qty*avg) / (qty*(m-1)) = (qty*avg - W) / (qty*(1-m))
    Short: W + qty*(avg-P) = qty*P*m
           W + qty*avg = qty*P + qty*P*m = qty*P*(1+m)
           P = (W + qty*avg) / (qty*(1+m))
    """
    if qty <= 0 or avg_entry <= 0:
        return None
    m = max(float(maintenance_rate), 0.0)
    w = float(wallet_plus_margin)
    if direction == "long":
        denom = qty * (1.0 - m)
        if denom <= 0:
            return None
        return (qty * avg_entry - w) / denom
    denom = qty * (1.0 + m)
    if denom <= 0:
        return None
    return (w + qty * avg_entry) / denom


def force_exit_price(
    direction: Direction,
    liq_price: float | None,
    buffer_pct: float,
) -> float | None:
    """Price at which we flatten *before* estimated liq (buffer as fraction of liq distance)."""
    if liq_price is None or liq_price <= 0:
        return None
    buf = max(float(buffer_pct), 0.0)
    if direction == "long":
        # liq is below entry; exit a bit above liq
        return liq_price * (1.0 + buf)
    return liq_price * (1.0 - buf)
