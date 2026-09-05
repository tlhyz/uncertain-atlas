"""Classic arithmetic / percent-spaced futures grid (long-biased or configurable)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from qtb.engine.types import Book, OrderIntent

from .base import Strategy


def build_levels(
    prices: pd.Series,
    lower: float | None,
    upper: float | None,
    grid_count: int,
    spacing_pct: float | None,
) -> np.ndarray:
    lo = float(lower) if lower is not None else float(prices.min()) * 0.98
    hi = float(upper) if upper is not None else float(prices.max()) * 1.02
    if hi <= lo:
        mid = float(prices.iloc[0])
        lo, hi = mid * 0.90, mid * 1.10
    if spacing_pct is not None and spacing_pct > 0:
        mid = (lo + hi) / 2.0
        step = mid * spacing_pct
        n = max(2, int((hi - lo) / max(step, 1e-12)))
        return np.linspace(lo, hi, n + 1)
    return np.linspace(lo, hi, max(int(grid_count), 2) + 1)


class ClassicGridStrategy(Strategy):
    name = "classic_grid"

    def __init__(self, cfg: dict[str, Any]):
        super().__init__(cfg)
        self.direction = str(cfg.get("direction") or "long")
        if self.direction == "dual":
            self.direction = "long"
        self.levels: np.ndarray | None = None
        self.order_size = float(cfg.get("order_size_quote") or 40.0)
        self.use_martingale = bool(cfg.get("martingale_addon"))
        self.multiplier = float(cfg.get("multiplier") or 1.5)
        self.max_adds = int(cfg.get("max_adds") or 40)

    def books_spec(self) -> list[tuple[str, str, float]]:
        cap = float(self.cfg.get("long_capital") or self.cfg.get("initial_margin") or 2000.0)
        return [("long", "long", cap)]

    def setup(self, df: pd.DataFrame) -> None:
        self.levels = build_levels(
            df["close"],
            self.cfg.get("lower"),
            self.cfg.get("upper"),
            int(self.cfg.get("grid_count") or 24),
            self.cfg.get("spacing_pct"),
        )

    def grid_range(self) -> tuple[float | None, float | None]:
        if self.levels is None or len(self.levels) == 0:
            return None, None
        return float(self.levels[0]), float(self.levels[-1])

    def on_bar(self, i: int, bar: dict[str, Any], books: dict[str, Book]) -> list[OrderIntent]:
        book = books.get("long")
        if book is None or book.halted or book.liquidated or self.levels is None:
            return []
        return grid_intents_for_book(book, self.levels, bar, self.order_size, self.use_martingale, self.multiplier, self.max_adds)


def grid_intents_for_book(
    book: Book,
    levels: np.ndarray,
    bar: dict[str, Any],
    order_size: float,
    use_martingale: bool,
    multiplier: float,
    max_adds: int,
) -> list[OrderIntent]:
    intents: list[OrderIntent] = []
    lo, hi = float(bar["low"]), float(bar["high"])
    n = len(levels)
    if book.direction == "long":
        # Buys at levels touched from above / inside bar
        for idx in range(n):
            lvl = float(levels[idx])
            if idx in book.lots:
                continue
            if lo <= lvl <= hi:
                if lvl <= float(bar["close"]) * 1.002:
                    if use_martingale and len(book.lots) >= max_adds:
                        continue
                    size = order_size
                    if use_martingale and book.lots:
                        size = order_size * (multiplier ** len(book.lots))
                    intents.append(
                        OrderIntent(
                            book=book.name,
                            side="buy",
                            price=lvl,
                            notional=size,
                            reason="grid_buy",
                            level_idx=idx,
                        )
                    )
        # Sells one level up
        for idx in list(book.lots.keys()):
            sell_idx = idx + 1
            if sell_idx >= n:
                continue
            sell_lvl = float(levels[sell_idx])
            if hi >= sell_lvl:
                qty = book.lots[idx]
                intents.append(
                    OrderIntent(
                        book=book.name,
                        side="sell",
                        price=sell_lvl,
                        qty=qty,
                        reduce_only=True,
                        reason="grid_sell_tp",
                        level_idx=idx,
                    )
                )
    else:
        # Short grid: sell (open) at higher levels, buy back one level down
        for idx in range(n - 1, -1, -1):
            lvl = float(levels[idx])
            if idx in book.lots:
                continue
            if lo <= lvl <= hi and lvl > float(bar["close"]) * 0.998 and hi >= lvl:
                if use_martingale and len(book.lots) >= max_adds:
                    continue
                size = order_size
                if use_martingale and book.lots:
                    size = order_size * (multiplier ** len(book.lots))
                intents.append(
                    OrderIntent(
                        book=book.name,
                        side="sell",
                        price=lvl,
                        notional=size,
                        reason="grid_short",
                        level_idx=idx,
                    )
                )
        for idx in list(book.lots.keys()):
            cover_idx = idx - 1
            if cover_idx < 0:
                continue
            cover_lvl = float(levels[cover_idx])
            if lo <= cover_lvl:
                qty = book.lots[idx]
                intents.append(
                    OrderIntent(
                        book=book.name,
                        side="buy",
                        price=cover_lvl,
                        qty=qty,
                        reduce_only=True,
                        reason="grid_cover_tp",
                        level_idx=idx,
                    )
                )
    return intents
