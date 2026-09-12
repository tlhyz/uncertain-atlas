"""ETF-native window search. Underlying dates are candidates only.

Confidence:
  REAL_GATE_ETF_WINDOW      — official Gate 3L/3S deals in the interval
  SYNTHETIC_GATE_ETF_WINDOW — stitched synthetic ETF NAV (Gate-rule path model)
  UNDERLYING_ONLY_CANDIDATE — no ETF series; MUST NOT enter strategy stats
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from typing import Literal

import numpy as np
import pandas as pd

from qtb.research.sl_phase.catalog import GRID_SPACINGS_FOR_SCAN, PRODUCTS, Window
from qtb.research.sl_phase.similarity import window_features

Confidence = Literal[
    "REAL_GATE_ETF_WINDOW",
    "SYNTHETIC_GATE_ETF_WINDOW",
    "UNDERLYING_ONLY_CANDIDATE",
]

REGIME_LABELS = (
    "drop_then_rise",
    "v_reversal",
    "double_bottom",
    "high_vol_chop",
    "rise_then_fall",
    "trend_up",
    "trend_down",
)

@dataclass
class EtfWindow:
    id: str
    market: str
    regime: str
    start: datetime
    bottom: datetime | None
    reversal: datetime | None
    end: datetime
    confidence: Confidence
    etf_ret: float
    max_dd: float
    max_rebound: float
    vol: float
    grid_cross: dict[str, int]
    source_candidate: str | None = None
    notes: str = ""
    n_hourly: int = 0

    def allowed_in_stats(self) -> bool:
        return self.confidence in {"REAL_GATE_ETF_WINDOW", "SYNTHETIC_GATE_ETF_WINDOW"}


def grid_cross_counts(px: np.ndarray, spacings: tuple[float, ...] = GRID_SPACINGS_FOR_SCAN) -> dict[str, int]:
    """Count theoretical geometric-step crosses on an ETF path (not fills)."""
    px = np.asarray(px, dtype=float)
    px = px[px > 0]
    out: dict[str, int] = {}
    if len(px) < 3:
        return {f"{s:.1%}": 0 for s in spacings}
    logp = np.log(px)
    for s in spacings:
        step = np.log(1.0 + s)
        if step <= 0:
            out[f"{s:.1%}"] = 0
            continue
        bins = np.floor(logp / step)
        out[f"{s:.1%}"] = int(np.sum(np.abs(np.diff(bins)) >= 1))
    return out


def classify_regime(px: np.ndarray) -> str:
    feat = window_features(px)
    if not feat:
        return "unknown"
    dd = feat["max_drawdown"]
    rb = feat["max_rebound"]
    lr = feat["log_return"]
    slope = feat["trend_slope"]
    # trough location
    i_lo = int(np.argmin(px))
    n = len(px)
    left = i_lo / max(n - 1, 1)
    if dd <= -0.20 and rb >= 0.30 and 0.15 <= left <= 0.85:
        if 0.35 <= left <= 0.65 and rb >= 0.45:
            return "v_reversal"
        return "drop_then_rise"
    if dd <= -0.12 and rb >= 0.12 and abs(lr) < 0.08:
        # two troughs
        if _double_bottom(px):
            return "double_bottom"
        return "high_vol_chop"
    if lr > 0.20 and dd > -0.15:
        return "trend_up"
    if lr < -0.20 and rb < 0.15:
        return "trend_down"
    if feat.get("max_drawdown", 0) > -0.08 and abs(lr) < 0.12 and feat.get("realized_vol", 0) > 0.8:
        return "high_vol_chop"
    if left < 0.35 and lr < 0 and feat.get("max_rebound", 0) < 0.15:
        return "rise_then_fall" if px[0] < np.max(px[: max(i_lo, 2)]) else "trend_down"
    if px[0] < np.max(px) * 0.85 and lr < -0.10:
        return "rise_then_fall"
    if slope > 0 and lr > 0:
        return "trend_up"
    if slope < 0 and lr < 0:
        return "trend_down"
    return "high_vol_chop"


def _double_bottom(px: np.ndarray) -> bool:
    if len(px) < 20:
        return False
    n = len(px)
    a = int(np.argmin(px[: n // 2 + 1]))
    b = int(np.argmin(px[n // 2 :]) + n // 2)
    if b - a < n * 0.15:
        return False
    mid = float(np.max(px[a : b + 1]))
    lo = min(float(px[a]), float(px[b]))
    if lo <= 0:
        return False
    similar = abs(px[a] - px[b]) / lo <= 0.12
    bounce = mid / lo - 1.0 >= 0.08
    return bool(similar and bounce)


def scan_etf_series(
    market: str,
    hourly: pd.Series,
    *,
    confidence: Confidence,
    lengths: tuple[int, ...] = (7, 14, 21, 30, 45, 60, 90),
    step_hours: int = 12,
    top_per_regime: int = 5,
) -> list[EtfWindow]:
    """Scan ETF own hourly series. Path-only. No strategy PnL."""
    if hourly is None or hourly.empty:
        return []
    idx = hourly.index
    px_all = hourly.to_numpy(dtype=float)
    found: list[EtfWindow] = []
    for days in lengths:
        n = max(8, days * 24)
        if n >= len(px_all):
            continue
        for start in range(0, len(px_all) - n, step_hours):
            sl = px_all[start : start + n]
            if np.any(sl <= 0):
                continue
            feat = window_features(sl)
            if not feat:
                continue
            regime = classify_regime(sl)
            i_lo = int(np.argmin(sl))
            # reversal = first bar after trough that is +12% off trough
            rev = None
            trough = float(sl[i_lo])
            for k in range(i_lo + 1, len(sl)):
                if sl[k] >= trough * 1.12:
                    rev = idx[start + k]
                    break
            found.append(
                EtfWindow(
                    id=f"{market}_{regime}_{days}d_{start}",
                    market=market,
                    regime=regime,
                    start=pd.Timestamp(idx[start]).to_pydatetime(),
                    bottom=pd.Timestamp(idx[start + i_lo]).to_pydatetime(),
                    reversal=None if rev is None else pd.Timestamp(rev).to_pydatetime(),
                    end=pd.Timestamp(idx[start + n - 1]).to_pydatetime(),
                    confidence=confidence,
                    etf_ret=float(np.exp(feat["log_return"]) - 1.0),
                    max_dd=feat["max_drawdown"],
                    max_rebound=feat["max_rebound"],
                    vol=feat["realized_vol"],
                    grid_cross=grid_cross_counts(sl),
                    n_hourly=n,
                )
            )
    # keep top per regime by |dd| * rebound * grid-cross(1%)
    kept: list[EtfWindow] = []
    for lab in REGIME_LABELS:
        sub = [w for w in found if w.regime == lab]
        sub.sort(key=lambda w: abs(w.max_dd) * (1.0 + w.max_rebound) * (1 + w.grid_cross.get("1.0%", 0) / 50.0), reverse=True)
        picked: list[EtfWindow] = []
        for w in sub:
            if any(not (w.end <= p.start or w.start >= p.end) for p in picked):
                continue
            picked.append(w)
            if len(picked) >= top_per_regime:
                break
        kept.extend(picked)
    return kept


def remap_candidate(
    cand: Window,
    market: str,
    hourly: pd.Series,
    *,
    confidence: Confidence,
    pad_days: tuple[int, ...] = (15, 30),
) -> EtfWindow:
    """Re-locate peak/trough/recovery on ETF series around a candidate calendar."""
    if hourly is None or hourly.empty:
        return EtfWindow(
            id=f"{cand.id}_{market}_NO_ETF",
            market=market,
            regime="unknown",
            start=datetime(cand.start.year, cand.start.month, cand.start.day, tzinfo=timezone.utc),
            bottom=None,
            reversal=None,
            end=datetime(cand.end.year, cand.end.month, cand.end.day, tzinfo=timezone.utc),
            confidence="UNDERLYING_ONLY_CANDIDATE",
            etf_ret=0.0,
            max_dd=0.0,
            max_rebound=0.0,
            vol=0.0,
            grid_cross={},
            source_candidate=cand.id,
            notes="No ETF series in pad. Underlying calendar only. EXCLUDED from strategy stats.",
        )
    best: EtfWindow | None = None
    for pad in pad_days:
        a = pd.Timestamp(cand.start, tz="UTC") - pd.Timedelta(days=pad)
        b = pd.Timestamp(cand.end, tz="UTC") + pd.Timedelta(days=pad)
        sl = hourly.loc[(hourly.index >= a) & (hourly.index < b)]
        if sl.empty or len(sl) < 12:
            continue
        px = sl.to_numpy(dtype=float)
        feat = window_features(px)
        if not feat:
            continue
        i_hi = int(np.argmax(px))
        i_lo = int(np.argmin(px))
        # recovery start: first +12% off trough after trough
        rev_i = None
        trough = float(px[i_lo])
        for k in range(i_lo + 1, len(px)):
            if px[k] >= trough * 1.12:
                rev_i = k
                break
        regime = classify_regime(px)
        w = EtfWindow(
            id=f"{cand.id}_{market}_pad{pad}",
            market=market,
            regime=regime,
            start=sl.index[0].to_pydatetime(),
            bottom=sl.index[i_lo].to_pydatetime(),
            reversal=None if rev_i is None else sl.index[rev_i].to_pydatetime(),
            end=sl.index[-1].to_pydatetime(),
            confidence=confidence,
            etf_ret=float(np.exp(feat["log_return"]) - 1.0),
            max_dd=feat["max_drawdown"],
            max_rebound=feat["max_rebound"],
            vol=feat["realized_vol"],
            grid_cross=grid_cross_counts(px),
            source_candidate=cand.id,
            notes=f"Remapped from underlying candidate {cand.id} ±{pad}d on {market}. peak_i={i_hi} trough_i={i_lo}",
            n_hourly=int(len(sl)),
        )
        if best is None or abs(w.max_dd) * (1 + w.max_rebound) > abs(best.max_dd) * (1 + best.max_rebound):
            best = w
    if best is None:
        return remap_candidate(cand, market, pd.Series(dtype=float), confidence="UNDERLYING_ONLY_CANDIDATE")
    return best


def series_confidence(market: str, start: date | datetime, end: date | datetime) -> Confidence:
    prod = PRODUCTS.get(market)
    if prod is None or prod.kind not in {"etf_3l", "etf_3s"}:
        return "UNDERLYING_ONLY_CANDIDATE"
    listed = prod.listed
    if listed is None:
        return "REAL_GATE_ETF_WINDOW"  # long-listed crypto 3L with deals
    s = start.date() if isinstance(start, datetime) else start
    e = end.date() if isinstance(end, datetime) else end
    if e < listed:
        return "SYNTHETIC_GATE_ETF_WINDOW"
    if s >= listed:
        return "REAL_GATE_ETF_WINDOW"
    return "SYNTHETIC_GATE_ETF_WINDOW"  # straddles listing; caller should split


def window_to_dict(w: EtfWindow) -> dict:
    d = asdict(w)
    for k in ("start", "bottom", "reversal", "end"):
        if d[k] is not None:
            d[k] = str(d[k])
    d["allowed_in_stats"] = w.allowed_in_stats()
    return d
