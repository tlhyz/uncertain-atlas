"""Martingale / dual-hedge Martingale (aggressive cashflow first-class mode)."""

from __future__ import annotations

from typing import Any

import pandas as pd

from qtb.engine.types import Book, OrderIntent

from .base import Strategy


_SKIP_SIDE_PREFIX = {"long_capital", "short_capital"}


def side_martingale_cfg(cfg: dict[str, Any], direction: str) -> dict[str, Any]:
    """Shared keys + optional nested {long|short} + prefixed long_* / short_*."""
    side = "long" if str(direction).lower() == "long" else "short"
    out = {k: v for k, v in cfg.items() if not isinstance(v, dict)}
    nested = cfg.get(side)
    if isinstance(nested, dict):
        out.update(nested)
    prefix = f"{side}_"
    for k, v in cfg.items():
        if k in _SKIP_SIDE_PREFIX or not k.startswith(prefix):
            continue
        out[k[len(prefix) :]] = v
    return out


def martingale_intents(book: Book, bar: dict[str, Any], cfg: dict[str, Any]) -> list[OrderIntent]:
    if book.halted or book.liquidated:
        return []
    if book.stopped_adding and book.in_position:
        return []  # risk layer handles exits; no new adds
    cfg = side_martingale_cfg(cfg, book.direction)
    base = float(cfg.get("base_order_quote") or 20.0)
    mult = float(cfg.get("multiplier") or 1.5)
    drop = float(cfg.get("add_drop_pct") or 0.015)
    tp = float(cfg.get("take_profit_pct") or 0.010)
    max_adds = int(cfg.get("max_adds") or 40)
    lo, hi, cl = float(bar["low"]), float(bar["high"]), float(bar["close"])
    intents: list[OrderIntent] = []

    if not book.in_position:
        intents.append(
            OrderIntent(
                book=book.name,
                side="buy" if book.direction == "long" else "sell",
                price=cl,
                notional=base,
                reason="mart_open",
            )
        )
        return intents

    # Per-trade TP from average (strategy-level; risk may also fire)
    if book.direction == "long":
        tp_px = book.avg_entry * (1.0 + tp)
        if hi >= tp_px:
            intents.append(
                OrderIntent(
                    book=book.name,
                    side="sell",
                    price=tp_px,
                    qty=book.qty,
                    reduce_only=True,
                    reason="mart_tp",
                )
            )
            return intents
        trigger = book.last_entry * (1.0 - drop)
        if (not book.stopped_adding) and lo <= trigger and book.adds < max_adds:
            notional = base * (mult ** (book.adds + 1))
            intents.append(
                OrderIntent(
                    book=book.name,
                    side="buy",
                    price=trigger,
                    notional=notional,
                    reason="mart_add",
                )
            )
    else:
        tp_px = book.avg_entry * (1.0 - tp)
        if lo <= tp_px:
            intents.append(
                OrderIntent(
                    book=book.name,
                    side="buy",
                    price=tp_px,
                    qty=book.qty,
                    reduce_only=True,
                    reason="mart_tp",
                )
            )
            return intents
        trigger = book.last_entry * (1.0 + drop)
        if (not book.stopped_adding) and hi >= trigger and book.adds < max_adds:
            notional = base * (mult ** (book.adds + 1))
            intents.append(
                OrderIntent(
                    book=book.name,
                    side="sell",
                    price=trigger,
                    notional=notional,
                    reason="mart_add",
                )
            )
    return intents


class MartingaleStrategy(Strategy):
    name = "martingale"

    def books_spec(self) -> list[tuple[str, str, float]]:
        direction = str(self.cfg.get("direction") or "long")
        if direction == "dual":
            direction = "long"
        cap = float(self.cfg.get("long_capital") if direction == "long" else self.cfg.get("short_capital"))
        if not cap:
            cap = float(self.cfg.get("initial_margin") or 1000.0)
        return [(direction, direction, cap)]

    def setup(self, df: pd.DataFrame) -> None:
        return None

    def on_bar(self, i: int, bar: dict[str, Any], books: dict[str, Book]) -> list[OrderIntent]:
        intents: list[OrderIntent] = []
        for book in books.values():
            intents.extend(martingale_intents(book, bar, self.cfg))
        return intents


class DualMartingaleStrategy(Strategy):
    """LONG + SHORT isolated books — aggressive dual-hedge cashflow."""

    name = "dual_martingale"

    def books_spec(self) -> list[tuple[str, str, float]]:
        long_cap = float(self.cfg.get("long_capital") or 950.0)
        short_cap = float(self.cfg.get("short_capital") or 1380.0)
        return [("long", "long", long_cap), ("short", "short", short_cap)]

    def setup(self, df: pd.DataFrame) -> None:
        return None

    def on_bar(self, i: int, bar: dict[str, Any], books: dict[str, Book]) -> list[OrderIntent]:
        intents: list[OrderIntent] = []
        for book in books.values():
            intents.extend(martingale_intents(book, bar, self.cfg))
        return intents
