"""Strategy interface."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from qtb.engine.types import Book, OrderIntent


class Strategy:
    name = "base"

    def __init__(self, cfg: dict[str, Any]):
        self.cfg = cfg

    def books_spec(self) -> list[tuple[str, str, float]]:
        """Return (book_name, direction, capital) tuples."""
        raise NotImplementedError

    def setup(self, df: pd.DataFrame) -> None:
        return None

    def grid_range(self) -> tuple[float | None, float | None]:
        return None, None

    def on_bar(
        self,
        i: int,
        bar: dict[str, Any],
        books: dict[str, Book],
    ) -> list[OrderIntent]:
        raise NotImplementedError
