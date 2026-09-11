"""Spot moving grid (Gate-style 移动网格).

Narrow band of 20–30 arithmetic/geometric levels. Resting buys below price,
sells one grid above each filled buy. When last price leaves the band by one
grid, the whole window shifts and orders are re-hung — same as the native
spot-grid robot, not the futures classic_grid that halts on a range break.

Designed for Gate ETF spot pairs (SOXL3L / SOXL3S / SNXX3L / SNXX3S), not USDT-M perps.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.data.gatedata import DEFAULT_ETF_3X, DEFAULT_ETF_LONGS, ETF_FAMILIES, resolve_etf_markets
from qtb.engine.types import Book, OrderIntent

from .base import Strategy

SpacingMode = Literal["geometric", "arithmetic"]

__all__ = [
    "DEFAULT_ETF_3X",
    "DEFAULT_ETF_LONGS",
    "ETF_FAMILIES",
    "MovingGridStrategy",
    "bar_touch_path",
    "build_moving_levels",
    "count_pct_crosses",
    "remap_lots_shift_down",
    "remap_lots_shift_up",
    "resolve_etf_markets",
    "shift_levels",
]


def build_moving_levels(
    mid: float,
    grid_count: int,
    spacing_pct: float | None = None,
    mode: SpacingMode = "arithmetic",
    range_up_pct: float | None = None,
    range_down_pct: float | None = None,
) -> np.ndarray:
    """`grid_count` intervals (N+1 prices).

    Gate UI form: 上 `range_up_pct` / 下 `range_down_pct` / N 格 / 等差.
    Example: mid=100, ±5%, 20 grids → 95 … 105, step=0.5.
    """
    if mid <= 0:
        raise ValueError(f"mid price must be > 0, got {mid}")
    n = int(grid_count)
    if n < 2:
        raise ValueError(f"grid_count must be >= 2, got {n}")
    if range_up_pct is not None and range_down_pct is not None:
        lo = mid * (1.0 - float(range_down_pct))
        hi = mid * (1.0 + float(range_up_pct))
        if hi <= lo:
            raise ValueError(f"empty band lo={lo} hi={hi}")
        return np.linspace(lo, hi, n + 1)
    if spacing_pct is None or float(spacing_pct) <= 0:
        raise ValueError("need spacing_pct or range_up_pct/range_down_pct")
    s = float(spacing_pct)
    ks = np.arange(n + 1, dtype=float) - n / 2.0
    if mode == "arithmetic":
        return mid + (mid * s) * ks
    if mode == "geometric":
        return mid * np.power(1.0 + s, ks)
    raise ValueError(f"spacing mode must be geometric|arithmetic, got {mode!r}")


def count_pct_crosses(prices, pct: float) -> dict[str, float]:
    """How many times the tape walks through `pct` geometric grids.

    An up-cross is a completed +1 grid for a long clip; a down-cross is a new buy
    level, not income. This is the path, not a capital-constrained backtest.
    """
    arr = np.asarray(prices, dtype=float)
    arr = arr[np.isfinite(arr) & (arr > 0)]
    if len(arr) < 2 or float(pct) <= 0:
        return {"up_crosses": 0, "down_crosses": 0, "end_level": 0.0}
    level = float(arr[0])
    up = 0
    down = 0
    r = 1.0 + float(pct)
    for px in arr[1:]:
        px = float(px)
        while px >= level * r * (1.0 - 1e-12):
            level *= r
            up += 1
        while px <= level / r * (1.0 + 1e-12):
            level /= r
            down += 1
    return {"up_crosses": up, "down_crosses": down, "end_level": level}


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
        self.grid_count = int(cfg.get("grid_count") or 20)
        up = cfg.get("range_up_pct")
        down = cfg.get("range_down_pct")
        self.range_up_pct = None if up in (None, "") else float(up)
        self.range_down_pct = None if down in (None, "") else float(down)
        n = max(self.grid_count, 2)
        if cfg.get("spacing_pct") not in (None, ""):
            self.spacing_pct = float(cfg["spacing_pct"])
        elif self.range_up_pct is not None and self.range_down_pct is not None:
            self.spacing_pct = (self.range_up_pct + self.range_down_pct) / n
        else:
            self.spacing_pct = 0.005
        self.spacing_mode: SpacingMode = (  # type: ignore[assignment]
            str(cfg.get("spacing_mode") or "arithmetic").strip().lower()
        )
        if self.spacing_mode not in {"geometric", "arithmetic"}:
            raise ValueError(f"spacing_mode must be geometric|arithmetic, got {self.spacing_mode}")
        self.quote_capital = float(
            cfg.get("quote_capital") or cfg.get("long_capital") or cfg.get("initial_margin") or 2000.0
        )
        self.order_size_quote = float(cfg.get("order_size_quote") or (self.quote_capital / n))
        self.shift_on_exit = bool(cfg.get("shift_on_exit", True))
        self.open_base_inventory = bool(cfg.get("open_base_inventory", True))
        self.move_mode = str(cfg.get("move_mode") or "breakout").strip().lower()
        if self.move_mode not in {"breakout", "ma720"}:
            raise ValueError(f"move_mode must be breakout|ma720, got {self.move_mode}")
        up_stop = cfg.get("stop_move_up")
        down_stop = cfg.get("stop_move_down")
        self.stop_move_up = None if up_stop in (None, "") else float(up_stop)
        self.stop_move_down = None if down_stop in (None, "") else float(down_stop)
        self.ma_move_pct = float(cfg.get("ma_move_pct") or 0.0)
        self.levels: np.ndarray | None = None

    def books_spec(self) -> list[tuple[str, str, float]]:
        return [("spot", "long", self.quote_capital)]

    def setup(self, df: pd.DataFrame) -> None:
        mid = float(df["open"].iloc[0]) if "open" in df.columns else float(df["close"].iloc[0])
        self.levels = build_moving_levels(
            mid,
            self.grid_count,
            self.spacing_pct,
            self.spacing_mode,
            range_up_pct=self.range_up_pct,
            range_down_pct=self.range_down_pct,
        )

    def grid_range(self) -> tuple[float | None, float | None]:
        if self.levels is None or len(self.levels) == 0:
            return None, None
        return float(self.levels[0]), float(self.levels[-1])

    def on_bar(self, i: int, bar: dict[str, Any], books: dict[str, Book]) -> list[OrderIntent]:
        # Dedicated spot engine walks the intra-bar path; futures engine must not
        # treat this as a static classic grid.
        return []
