"""Pure trigger functions for TP / SL / risk exits (unit-testable, no I/O)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Direction = Literal["long", "short"]


@dataclass
class ScaledTpLevel:
    profit_pct: float
    close_frac: float


@dataclass
class RiskConfig:
    per_trade_tp_pct: float | None = None
    per_trade_sl_pct: float | None = None
    investment_sl_pct: float | None = 0.50  # 50% / 70% of investment (user style)
    portfolio_tp_pct: float | None = None
    portfolio_equity_sl_pct: float | None = None
    max_drawdown_stop_pct: float | None = None
    stop_adding_float_loss_pct: float | None = None
    force_exit_before_liq_buffer_pct: float = 0.20
    stop_if_price_breaks_range: bool = True
    trailing_tp_pct: float | None = None
    trailing_activation_pct: float | None = None
    time_tp_bars: int | None = None
    scaled_tp: list[ScaledTpLevel] = field(default_factory=list)
    maintenance_rate: float = 0.005

    @classmethod
    def from_dict(cls, d: dict[str, Any], maintenance_rate: float = 0.005) -> RiskConfig:
        scaled_raw = d.get("scaled_tp") or []
        scaled: list[ScaledTpLevel] = []
        for item in scaled_raw:
            if isinstance(item, ScaledTpLevel):
                scaled.append(item)
            elif isinstance(item, dict):
                scaled.append(
                    ScaledTpLevel(
                        profit_pct=float(item["profit_pct"]),
                        close_frac=float(item["close_frac"]),
                    )
                )
        return cls(
            per_trade_tp_pct=_f(d.get("per_trade_tp_pct")),
            per_trade_sl_pct=_f(d.get("per_trade_sl_pct")),
            investment_sl_pct=_f(d.get("investment_sl_pct")),
            portfolio_tp_pct=_f(d.get("portfolio_tp_pct")),
            portfolio_equity_sl_pct=_f(d.get("portfolio_equity_sl_pct")),
            max_drawdown_stop_pct=_f(d.get("max_drawdown_stop_pct")),
            stop_adding_float_loss_pct=_f(d.get("stop_adding_float_loss_pct")),
            force_exit_before_liq_buffer_pct=float(d.get("force_exit_before_liq_buffer_pct") or 0.20),
            stop_if_price_breaks_range=bool(d.get("stop_if_price_breaks_range", True)),
            trailing_tp_pct=_f(d.get("trailing_tp_pct")),
            trailing_activation_pct=_f(d.get("trailing_activation_pct")),
            time_tp_bars=_i(d.get("time_tp_bars")),
            scaled_tp=scaled,
            maintenance_rate=float(d.get("maintenance_rate") or maintenance_rate),
        )


def _f(v: Any) -> float | None:
    if v is None or v == "" or v is False:
        return None
    return float(v)


def _i(v: Any) -> int | None:
    if v is None or v == "" or v is False:
        return None
    return int(v)


def hit_per_trade_tp(direction: Direction, avg_entry: float, price: float, tp_pct: float) -> bool:
    if tp_pct <= 0 or avg_entry <= 0:
        return False
    if direction == "long":
        return price >= avg_entry * (1.0 + tp_pct)
    return price <= avg_entry * (1.0 - tp_pct)


def hit_per_trade_sl(direction: Direction, avg_entry: float, price: float, sl_pct: float) -> bool:
    if sl_pct <= 0 or avg_entry <= 0:
        return False
    if direction == "long":
        return price <= avg_entry * (1.0 - sl_pct)
    return price >= avg_entry * (1.0 + sl_pct)


def hit_investment_sl(upnl: float, investment: float, sl_pct: float) -> bool:
    """uPnL / investment <= -sl_pct (50% / 70% of bot investment)."""
    if sl_pct <= 0 or investment <= 0:
        return False
    return upnl / investment <= -sl_pct


def hit_portfolio_equity_sl(equity: float, initial: float, sl_pct: float) -> bool:
    if sl_pct <= 0 or initial <= 0:
        return False
    return equity <= initial * (1.0 - sl_pct)


def hit_portfolio_tp(equity: float, initial: float, tp_pct: float) -> bool:
    if tp_pct <= 0 or initial <= 0:
        return False
    return equity >= initial * (1.0 + tp_pct)


def hit_max_dd_stop(dd_pct: float, threshold: float) -> bool:
    if threshold <= 0:
        return False
    return dd_pct >= threshold


def should_stop_adding(upnl: float, investment: float, threshold: float) -> bool:
    if threshold <= 0 or investment <= 0:
        return False
    return upnl / investment <= -threshold


def near_liquidation(
    equity: float,
    notional: float,
    maintenance_rate: float,
    buffer_pct: float,
) -> bool:
    """True when equity is within `buffer_pct` of maintenance margin (or already below)."""
    if notional <= 0:
        return False
    maint = abs(notional) * max(maintenance_rate, 0.0)
    cushion = maint * max(buffer_pct, 0.0)
    return equity <= maint + cushion or equity <= 0


def price_breaks_range(price: float, lower: float | None, upper: float | None) -> bool:
    if lower is not None and price < lower:
        return True
    if upper is not None and price > upper:
        return True
    return False


def time_tp_due(bars_in_trade: int, limit: int | None) -> bool:
    if limit is None or limit <= 0:
        return False
    return bars_in_trade >= limit


def trailing_stop_price(direction: Direction, extreme: float, trail_pct: float) -> float:
    """Give-back from the best favorable extreme."""
    if trail_pct <= 0 or extreme <= 0:
        return extreme
    if direction == "long":
        return extreme * (1.0 - trail_pct)
    return extreme * (1.0 + trail_pct)


@dataclass
class TrailingState:
    activated: bool = False
    extreme: float = 0.0

    def update(self, direction: Direction, price: float, avg_entry: float, activation_pct: float | None) -> None:
        if avg_entry <= 0:
            return
        if direction == "long":
            fav = (price - avg_entry) / avg_entry
            if not self.activated:
                if activation_pct is None or fav >= activation_pct:
                    self.activated = True
                    self.extreme = price
            elif price > self.extreme:
                self.extreme = price
        else:
            fav = (avg_entry - price) / avg_entry
            if not self.activated:
                if activation_pct is None or fav >= activation_pct:
                    self.activated = True
                    self.extreme = price
            elif self.extreme <= 0 or price < self.extreme:
                self.extreme = price
