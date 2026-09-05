"""Shared engine types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

from qtb.risk.exits import TrailingState

Direction = Literal["long", "short"]


@dataclass
class OrderIntent:
    book: str
    side: Literal["buy", "sell"]
    price: float
    notional: float | None = None
    qty: float | None = None
    reduce_only: bool = False
    reason: str = ""
    level_idx: int | None = None


@dataclass
class Trade:
    trade_id: int
    timestamp: Any
    symbol: str
    book: str
    side: str
    price: float
    qty: float
    notional: float
    fee: float
    slippage: float
    reason: str
    realized_pnl: float
    equity_after: float
    cycle_id: int
    direction: str


@dataclass
class Book:
    name: str
    direction: Direction
    initial: float
    wallet: float
    margin_locked: float = 0.0
    qty: float = 0.0
    avg_entry: float = 0.0
    last_entry: float = 0.0
    adds: int = 0
    bars_in_trade: int = 0
    cycle_id: int = 0
    halted: bool = False
    liquidated: bool = False
    stopped_adding: bool = False
    trailing: TrailingState = field(default_factory=TrailingState)
    scaled_taken: set[int] = field(default_factory=set)
    lots: dict[int, float] = field(default_factory=dict)
    cycles: int = 0
    wins: int = 0
    cycle_pnls: list[float] = field(default_factory=list)
    stop_outs: int = 0
    max_adds_hit: int = 0
    max_margin_used: float = 0.0
    max_float_loss: float = 0.0
    cycle_realized: float = 0.0

    @property
    def in_position(self) -> bool:
        return self.qty > 0

    def unrealized(self, price: float) -> float:
        if self.qty <= 0:
            return 0.0
        if self.direction == "long":
            return self.qty * (price - self.avg_entry)
        return self.qty * (self.avg_entry - price)

    def equity(self, price: float) -> float:
        if self.liquidated:
            return 0.0
        if self.qty <= 0:
            return self.wallet
        return self.wallet + self.margin_locked + self.unrealized(price)

    def reset_position(self) -> None:
        self.qty = 0.0
        self.avg_entry = 0.0
        self.last_entry = 0.0
        self.adds = 0
        self.bars_in_trade = 0
        self.margin_locked = 0.0
        self.trailing = TrailingState()
        self.scaled_taken = set()
        self.lots = {}
        self.stopped_adding = False
