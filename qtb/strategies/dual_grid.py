"""Symmetric long + short grid (dual hedge style, no martingale unless enabled)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from qtb.engine.types import Book, OrderIntent

from .base import Strategy
from .classic_grid import build_levels, grid_intents_for_book


class DualGridStrategy(Strategy):
    name = "dual_grid"

    def __init__(self, cfg: dict[str, Any]):
        super().__init__(cfg)
        self.levels: np.ndarray | None = None
        self.order_size = float(cfg.get("order_size_quote") or 40.0)
        self.use_martingale = bool(cfg.get("martingale_addon"))
        self.multiplier = float(cfg.get("multiplier") or 1.5)
        self.max_adds = int(cfg.get("max_adds") or 40)

    def books_spec(self) -> list[tuple[str, str, float]]:
        long_cap = float(self.cfg.get("long_capital") or 950.0)
        short_cap = float(self.cfg.get("short_capital") or 1380.0)
        return [("long", "long", long_cap), ("short", "short", short_cap)]

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
        if self.levels is None:
            return []
        intents: list[OrderIntent] = []
        for name in ("long", "short"):
            book = books.get(name)
            if book is None or book.halted or book.liquidated:
                continue
            intents.extend(
                grid_intents_for_book(
                    book, self.levels, bar, self.order_size, self.use_martingale, self.multiplier, self.max_adds
                )
            )
        return intents
