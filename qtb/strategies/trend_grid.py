"""Trend grid: long grid in uptrend, short grid in downtrend (EMA filter)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from qtb.engine.types import Book, OrderIntent

from .base import Strategy
from .classic_grid import build_levels, grid_intents_for_book


class TrendGridStrategy(Strategy):
    name = "trend_grid"

    def __init__(self, cfg: dict[str, Any]):
        super().__init__(cfg)
        self.levels: np.ndarray | None = None
        self.ema: np.ndarray | None = None
        self.order_size = float(cfg.get("order_size_quote") or 40.0)
        self.threshold = float(cfg.get("trend_threshold") or 0.002)
        self.use_martingale = bool(cfg.get("martingale_addon"))
        self.multiplier = float(cfg.get("multiplier") or 1.5)
        self.max_adds = int(cfg.get("max_adds") or 40)
        self.regime: list[str] = []

    def books_spec(self) -> list[tuple[str, str, float]]:
        long_cap = float(self.cfg.get("long_capital") or self.cfg.get("initial_margin") or 2000.0)
        short_cap = float(self.cfg.get("short_capital") or long_cap)
        return [("long", "long", long_cap), ("short", "short", short_cap)]

    def setup(self, df: pd.DataFrame) -> None:
        self.levels = build_levels(
            df["close"],
            self.cfg.get("lower"),
            self.cfg.get("upper"),
            int(self.cfg.get("grid_count") or 24),
            self.cfg.get("spacing_pct"),
        )
        period = max(int(self.cfg.get("ema_period") or 48), 2)
        close = df["close"].astype(float)
        self.ema = close.ewm(span=period, adjust=False).mean().to_numpy()
        self.regime = []
        for i, px in enumerate(close.to_numpy()):
            ema = float(self.ema[i])
            if ema <= 0:
                self.regime.append("flat")
                continue
            rel = (px - ema) / ema
            if rel >= self.threshold:
                self.regime.append("up")
            elif rel <= -self.threshold:
                self.regime.append("down")
            else:
                self.regime.append("flat")

    def grid_range(self) -> tuple[float | None, float | None]:
        if self.levels is None or len(self.levels) == 0:
            return None, None
        return float(self.levels[0]), float(self.levels[-1])

    def on_bar(self, i: int, bar: dict[str, Any], books: dict[str, Book]) -> list[OrderIntent]:
        if self.levels is None:
            return []
        regime = self.regime[i] if i < len(self.regime) else "flat"
        intents: list[OrderIntent] = []
        if regime == "up":
            book = books.get("long")
            if book and not book.halted and not book.liquidated:
                intents.extend(
                    grid_intents_for_book(
                        book, self.levels, bar, self.order_size, self.use_martingale, self.multiplier, self.max_adds
                    )
                )
        elif regime == "down":
            book = books.get("short")
            if book and not book.halted and not book.liquidated:
                intents.extend(
                    grid_intents_for_book(
                        book, self.levels, bar, self.order_size, self.use_martingale, self.multiplier, self.max_adds
                    )
                )
        return intents
