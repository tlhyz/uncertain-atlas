"""Effective underlying beta for leveraged ETPs — placeholder for rolling regression."""

from __future__ import annotations

import numpy as np


def rolling_realized_beta(asset: np.ndarray, reference: np.ndarray, window: int = 24 * 20) -> np.ndarray:
    """Simple rolling beta(asset, reference). Returns NaN until window full."""
    n = len(asset)
    out = np.full(n, np.nan)
    for i in range(window, n):
        a = np.diff(np.log(np.maximum(asset[i - window : i + 1], 1e-12)))
        r = np.diff(np.log(np.maximum(reference[i - window : i + 1], 1e-12)))
        cov = np.cov(a, r)[0, 1]
        var = np.var(r)
        out[i] = cov / var if var > 1e-12 else np.nan
    return out
