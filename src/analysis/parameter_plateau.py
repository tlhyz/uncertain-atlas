"""Parameter plateau detection — STEP 9 implementation placeholder."""

from __future__ import annotations

from typing import Any


def is_plateau(results: list[dict[str, Any]], param_key: str, metric: str = "calmar", tol: float = 0.15) -> bool:
    if len(results) < 3:
        return False
    vals = sorted(r.get(metric, 0) for r in results)
    return (max(vals) - min(vals)) / max(abs(max(vals)), 1e-9) <= tol
