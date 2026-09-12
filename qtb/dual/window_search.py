"""DTW / Pearson / Spearman window similarity search on normalized paths."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd


def _pearson(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 3:
        return 0.0
    am, bm = a - np.mean(a), b - np.mean(b)
    den = float(np.sqrt(np.sum(am ** 2) * np.sum(bm ** 2)))
    return float(np.sum(am * bm) / den) if den > 1e-12 else 0.0


def _spearman(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 3:
        return 0.0
    ra = np.argsort(np.argsort(a))
    rb = np.argsort(np.argsort(b))
    return _pearson(ra.astype(float), rb.astype(float))

from .data import DualDataset, fetch_binance_futures_klines
from .universe import SEED_WINDOWS


@dataclass
class SimilarWindow:
    symbol: str
    start: str
    end: str
    score_pearson: float
    score_spearman: float
    score_dtw: float
    composite: float
    seed_id: str
    bars: int
    regime_hint: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "start": self.start,
            "end": self.end,
            "score_pearson": round(self.score_pearson, 4),
            "score_spearman": round(self.score_spearman, 4),
            "score_dtw": round(self.score_dtw, 4),
            "composite": round(self.composite, 4),
            "seed_id": self.seed_id,
            "bars": self.bars,
        }


def _normalize_path(close: np.ndarray) -> np.ndarray:
    """Log returns + cumulative drawdown features."""
    if len(close) < 5:
        return np.zeros(5)
    lr = np.diff(np.log(np.maximum(close, 1e-12)))
    peak = np.maximum.accumulate(close)
    dd = (close - peak) / np.maximum(peak, 1e-12)
    # pad lr to same length
    lr_p = np.zeros(len(close))
    lr_p[1:] = lr
    feat = np.column_stack([lr_p, dd])
    # z-score each column
    out = np.zeros_like(feat)
    for j in range(feat.shape[1]):
        col = feat[:, j]
        std = float(np.std(col))
        out[:, j] = (col - np.mean(col)) / std if std > 1e-12 else col
    return out.flatten()


def _dtw_distance(a: np.ndarray, b: np.ndarray) -> float:
    """Simple O(n*m) DTW on 1d arrays."""
    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return 1e9
    # downsample to max 120 points
    if n > 120:
        idx = np.linspace(0, n - 1, 120).astype(int)
        a = a[idx]
        n = len(a)
    if m > 120:
        idx = np.linspace(0, m - 1, 120).astype(int)
        b = b[idx]
        m = len(b)
    d = np.full((n + 1, m + 1), np.inf)
    d[0, 0] = 0.0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(a[i - 1] - b[j - 1])
            d[i, j] = cost + min(d[i - 1, j], d[i, j - 1], d[i - 1, j - 1])
    return float(d[n, m] / max(n, m))


def extract_template(seed_id: str, data: DualDataset) -> tuple[np.ndarray, str] | None:
    for sw in SEED_WINDOWS:
        if sw.id != seed_id:
            continue
        sym = sw.symbol
        md = data.tech.get(sym)
        if md is None:
            return None
        t0 = pd.Timestamp(sw.start, tz="UTC")
        t1 = pd.Timestamp(sw.end, tz="UTC")
        m = (md.bars["timestamp"] >= t0) & (md.bars["timestamp"] <= t1)
        sub = md.bars.loc[m]
        if len(sub) < 24:
            # try binance BTC as shape proxy for structural seeds
            try:
                bn = fetch_binance_futures_klines("BTCUSDT" if sym == "BTC" else "BTCUSDT", "1h")
                m2 = (bn["timestamp"] >= t0) & (bn["timestamp"] <= t1)
                sub = bn.loc[m2]
            except Exception:
                return None
        close = sub["close"].to_numpy(float)
        return _normalize_path(close), sw.id
    return None


def search_similar_windows(
    data: DualDataset,
    seed_id: str = "TECH_T2",
    top_k: int = 20,
    horizon_bars: int = 24 * 60,
    step_bars: int = 24 * 7,
) -> list[SimilarWindow]:
    """Scan SOXL Gate history for windows similar to seed template."""
    tpl = extract_template(seed_id, data)
    if tpl is None:
        return []
    template, sid = tpl
    close_full = data.tech["SOXL"].bars["close"].to_numpy(float)
    ts = data.tech["SOXL"].bars["timestamp"]
    n = len(close_full)
    results: list[SimilarWindow] = []

    for i0 in range(0, max(n - horizon_bars, 1), step_bars):
        i1 = min(i0 + horizon_bars, n)
        if i1 - i0 < 48:
            continue
        seg = close_full[i0:i1]
        norm = _normalize_path(seg)
        # align lengths via min len flatten compare
        m = min(len(template), len(norm))
        t_a = template[:m]
        t_b = norm[:m]
        pr = _pearson(t_a, t_b) if m > 3 else 0.0
        sr = _spearman(t_a, t_b) if m > 3 else 0.0
        dtw = _dtw_distance(t_a[:: max(1, m // 60)], t_b[:: max(1, m // 60)])
        dtw_score = 1.0 / (1.0 + dtw)
        comp = 0.35 * pr + 0.25 * sr + 0.40 * dtw_score
        results.append(
            SimilarWindow(
                symbol="SOXL",
                start=str(ts.iloc[i0]),
                end=str(ts.iloc[i1 - 1]),
                score_pearson=pr,
                score_spearman=sr,
                score_dtw=dtw_score,
                composite=comp,
                seed_id=sid,
                bars=i1 - i0,
            )
        )

    results.sort(key=lambda x: x.composite, reverse=True)
    return results[:top_k]
