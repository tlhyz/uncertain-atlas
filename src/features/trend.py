"""Trend features — extend as needed."""

from __future__ import annotations

import numpy as np


def ema_cross(close: np.ndarray, fast: int = 12, slow: int = 24) -> np.ndarray:
    def _ema(x, span):
        alpha = 2 / (span + 1)
        out = np.empty_like(x)
        out[0] = x[0]
        for i in range(1, len(x)):
            out[i] = alpha * x[i] + (1 - alpha) * out[i - 1]
        return out

    ef = _ema(close, fast)
    es = _ema(close, slow)
    return (ef > es).astype(float)
