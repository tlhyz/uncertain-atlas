"""Spot moving grid (Gate-style 移动网格).

Narrow band of 20–30 arithmetic/geometric levels. Resting buys below price,
sells one grid above each filled buy. When last price leaves the band by one
grid, the whole window shifts and orders are re-hung — same as the native
spot-grid robot, not the futures classic_grid that halts on a range break.

Designed for Gate ETF spot pairs (SOXLG / ETH3L / …), not USDT-M perps.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.data.gatedata import DEFAULT_ETF_LONGS, ETF_FAMILIES, resolve_etf_markets
from qtb.engine.types import Book, OrderIntent

from .base import Strategy

SpacingMode = Literal["geometric", "arithmetic"]

__all__ = [
    "DEFAULT_ETF_LONGS",
    "ETF_FAMILIES",
    "MovingGridStrategy",
    "bar_touch_path",
    "build_moving_levels",
    "remap_lots_shift_down",
    "remap_lots_shift_up",
    "resolve_etf_markets",
    "shift_levels",
]


def build_moving_levels(
    mid: float,
    grid_count: int,
    spacing_pct: float,
    mode: SpacingMode = "geometric",
) -> np.ndarray:
    """`grid_count` intervals (N+1 prices) centered on `mid`."""
    if mid <= 0:
        raise ValueError(f"mid price must be > 0, got {mid}")
    n = int(grid_count)
    if n < 2:
        raise ValueError(f"grid_count must be >= 2, got {n}")
    s = float(spacing_pct)
    if s <= 0:
        raise ValueError(f"spacing_pct must be > 0, got {s}")
    ks = np.arange(n + 1, dtype=float) - n / 2.0
    if mode == "arithmetic":
        step = mid * s
        return mid + step * ks
    if mode == "geometric":
        return mid * np.power(1.0 + s, ks)
    raise ValueError(f"spacing mode must be geometric|arithmetic, got {mode!r}")


def shift_levels(
    levels: np.ndarray,
    direction: Literal["up", "down"],
    spacing_pct: float,
    mode: SpacingMode = "geometric",
) -> np.ndarray:
    """Slide the window by one grid (native robot re-hang)."""
    arr = np.asarray(levels, dtype=float)
    s = float(spacing_pct)
    if mode == "geometric":
        r = 1.0 + s
        return arr * r if direction == "up" else arr / r
    step = float(np.median(np.diff(arr))) if len(arr) > 1 else arr[0] * s
    if step <= 0:
        step = arr[0] * s
    return arr + step if direction == "up" else arr - step


def remap_lots_shift_up(lots: dict[int, float]) -> tuple[dict[int, float], float]:
    """Index i → i-1. Abandoned lowest lot becomes leftover inventory."""
    leftover = float(lots.get(0, 0.0))
    new = {i - 1: qty for i, qty in lots.items() if i > 0 and qty > 0}
    return new, leftover


def remap_lots_shift_down(lots: dict[int, float], max_buy_idx: int) -> tuple[dict[int, float], float]:
    """Index i → i+1. Abandoned highest buy-lot becomes leftover inventory."""
    leftover = float(lots.get(max_buy_idx, 0.0))
    new = {i + 1: qty for i, qty in lots.items() if i < max_buy_idx and qty > 0}
    return new, leftover


def bar_touch_path(open_: float, high: float, low: float, close: float) -> list[float]:
    """Deterministic intra-bar path for limit fills.

    Up-close bars: open → low → high → close (dip then rally).
    Down-close bars: open → high → low → close (rally then dump).
    """
    if close >= open_:
        return [open_, low, high, close]
    return [open_, high, low, close]


class MovingGridStrategy(Strategy):
    """Spot moving grid. Execution lives in `qtb.engine.spot_grid`."""

    name = "moving_grid"

    def __init__(self, cfg: dict[str, Any]):
        super().__init__(cfg)
        self.grid_count = int(cfg.get("grid_count") or 24)
        self.spacing_pct = float(cfg.get("spacing_pct") or 0.004)
        self.spacing_mode: SpacingMode = (  # type: ignore[assignment]
            str(cfg.get("spacing_mode") or "geometric").strip().lower()
        )
        if self.spacing_mode not in {"geometric", "arithmetic"}:
            raise ValueError(f"spacing_mode must be geometric|arithmetic, got {self.spacing_mode}")
        self.quote_capital = float(
            cfg.get("quote_capital") or cfg.get("long_capital") or cfg.get("initial_margin") or 2000.0
        )
        n = max(self.grid_count, 2)
        self.order_size_quote = float(cfg.get("order_size_quote") or (self.quote_capital / n))
        self.shift_on_exit = bool(cfg.get("shift_on_exit", True))
        self.levels: np.ndarray | None = None

    def books_spec(self) -> list[tuple[str, str, float]]:
        return [("spot", "long", self.quote_capital)]

    def setup(self, df: pd.DataFrame) -> None:
        mid = float(df["open"].iloc[0]) if "open" in df.columns else float(df["close"].iloc[0])
        self.levels = build_moving_levels(mid, self.grid_count, self.spacing_pct, self.spacing_mode)

    def grid_range(self) -> tuple[float | None, float | None]:
        if self.levels is None or len(self.levels) == 0:
            return None, None
        return float(self.levels[0]), float(self.levels[-1])

    def on_bar(self, i: int, bar: dict[str, Any], books: dict[str, Book]) -> list[OrderIntent]:
        # Dedicated spot engine walks the intra-bar path; futures engine must not
        # treat this as a static classic grid.
        return []
