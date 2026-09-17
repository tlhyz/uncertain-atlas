"""Gate vs Binance bar-path fill ratio calibration (BAR BACKTEST only).

Compares maker-first grid limit fills on overlapping 1h candles using each venue's
OHLC + quote volume. No synthetic ticks — participation budget drives fill drift.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.ab.fills import FillConfig, PendingFill, infer_tick, resolve_bar_fills
from qtb.ab.grids import grid_quote_size, native_spec

FillMode = Literal["base", "conservative"]


@dataclass
class VenueBarStats:
    bars: int = 0
    pending_orders: int = 0
    filled_orders: int = 0
    filled_notional: float = 0.0
    unfilled_orders: int = 0

    @property
    def fill_ratio_by_count(self) -> float:
        if self.pending_orders <= 0:
            return float("nan")
        return self.filled_orders / self.pending_orders

    @property
    def fill_ratio_by_notional(self) -> float:
        return float("nan")


@dataclass
class FillCalibrationReport:
    symbol: str
    interval: str
    overlap_start: str
    overlap_end: str
    n_bars: int
    atr_step: float
    atr_range: float
    target_notional: float
    binance: VenueBarStats = field(default_factory=VenueBarStats)
    gate: VenueBarStats = field(default_factory=VenueBarStats)
    volume_swap_gate_on_binance_ohlc: VenueBarStats = field(default_factory=VenueBarStats)
    mean_quote_volume_binance: float = 0.0
    mean_quote_volume_gate: float = 0.0
    volume_ratio_gate_over_binance: float = 0.0
    mean_abs_close_diff_bps: float = 0.0
    mean_abs_high_low_diff_bps: float = 0.0
    fill_ratio_gate_over_binance_count: float = 0.0
    fill_ratio_gate_over_binance_notional: float = 0.0
    fill_ratio_volume_swap_count: float = 0.0
    fill_ratio_volume_swap_notional: float = 0.0
    precision: str = "BAR BACKTEST"
    notes: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["binance"] = asdict(self.binance)
        d["gate"] = asdict(self.gate)
        d["volume_swap_gate_on_binance_ohlc"] = asdict(self.volume_swap_gate_on_binance_ohlc)
        return d


def _load_ohlcv_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    for col in ("open", "high", "low", "close", "quote_volume"):
        if col not in df.columns:
            raise ValueError(f"{path}: missing column {col}")
        df[col] = pd.to_numeric(df[col], errors="coerce")
    if "volume" in df.columns:
        df["volume"] = pd.to_numeric(df["volume"], errors="coerce")
    return df.dropna(subset=["timestamp", "open", "high", "low", "close", "quote_volume"]).sort_values("timestamp")


def _atr14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prev = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    return tr.rolling(14, min_periods=14).mean()


def _grid_pending(
    o: float,
    c: float,
    atr: float,
    *,
    atr_step: float,
    atr_range: float,
    target_notional: float,
) -> list[PendingFill]:
    """Long grid entry orders below mid (crypto default geometry)."""
    if atr <= 0 or not np.isfinite(atr):
        return []
    spec = native_spec(c, max(atr, c * 0.002), atr_step, atr_range, "geometric")
    empty = max(1, sum(1 for idx, lvl in enumerate(spec.levels) if lvl <= spec.mid))
    baseline = target_notional / empty
    pending: list[PendingFill] = []
    for idx, lvl in enumerate(spec.levels):
        if lvl > spec.mid:
            continue
        qsz = grid_quote_size(baseline, float(lvl), spec, "fixed_usdt", atr, atr, 1.0)
        if qsz >= 1.0:
            pending.append(PendingFill("buy", float(lvl), idx, notional=qsz, reason="grid_cal"))
    return pending


def _simulate_bar_fills(
    pending: list[PendingFill],
    o: float,
    h: float,
    l: float,
    c: float,
    quote_volume: float,
    cfg: FillConfig,
) -> tuple[int, float]:
    if not pending:
        return 0, 0.0
    fills = resolve_bar_fills(pending, o, h, l, c, quote_volume=quote_volume, cfg=cfg)
    notional = sum((f.notional or 0.0) + ((f.qty or 0.0) * f.price) for f in fills)
    return len(fills), float(notional)


def _accumulate(stats: VenueBarStats, pending: list[PendingFill], n_filled: int, notional: float) -> None:
    stats.bars += 1
    stats.pending_orders += len(pending)
    stats.filled_orders += n_filled
    stats.filled_notional += notional
    stats.unfilled_orders += max(len(pending) - n_filled, 0)


def align_gate_binance_bars(
    gate_df: pd.DataFrame,
    binance_df: pd.DataFrame,
) -> pd.DataFrame:
    g = gate_df.rename(
        columns={
            "open": "gate_open",
            "high": "gate_high",
            "low": "gate_low",
            "close": "gate_close",
            "quote_volume": "gate_quote_volume",
        }
    )
    b = binance_df.rename(
        columns={
            "open": "binance_open",
            "high": "binance_high",
            "low": "binance_low",
            "close": "binance_close",
            "quote_volume": "binance_quote_volume",
        }
    )
    merged = pd.merge(g, b, on="timestamp", how="inner")
    return merged.sort_values("timestamp").reset_index(drop=True)


def run_fill_calibration(
    gate_df: pd.DataFrame,
    binance_df: pd.DataFrame,
    *,
    atr_step: float = 0.40,
    atr_range: float = 5.0,
    target_notional: float = 500.0,
    fill_mode: FillMode = "base",
    min_bars: int = 100,
) -> FillCalibrationReport:
    aligned = align_gate_binance_bars(gate_df, binance_df)
    if len(aligned) < min_bars:
        raise ValueError(f"overlap too short: {len(aligned)} bars < min_bars={min_bars}")

    atr = _atr14(aligned["binance_high"], aligned["binance_low"], aligned["binance_close"])
    if fill_mode == "conservative":
        cfg = FillConfig.preset("conservative")
    else:
        cfg = FillConfig.preset("base")

    rep = FillCalibrationReport(
        symbol="BTC",
        interval="1h",
        overlap_start=str(aligned["timestamp"].iloc[0]),
        overlap_end=str(aligned["timestamp"].iloc[-1]),
        n_bars=len(aligned),
        atr_step=atr_step,
        atr_range=atr_range,
        target_notional=target_notional,
    )

    close_diff_bps: list[float] = []
    range_diff_bps: list[float] = []

    for i, row in aligned.iterrows():
        atr_val = float(atr.iloc[i]) if i < len(atr) and pd.notna(atr.iloc[i]) else float("nan")
        if not np.isfinite(atr_val) or atr_val <= 0:
            continue

        pending = _grid_pending(
            float(row["binance_open"]),
            float(row["binance_close"]),
            atr_val,
            atr_step=atr_step,
            atr_range=atr_range,
            target_notional=target_notional,
        )
        if not pending:
            continue

        tick = infer_tick(float(row["binance_close"]))
        fill_cfg = FillConfig(cfg.mode, cfg.participation, cfg.extra_ticks, cfg.extra_slip_bps, tick)

        b_n, b_not = _simulate_bar_fills(
            pending,
            float(row["binance_open"]),
            float(row["binance_high"]),
            float(row["binance_low"]),
            float(row["binance_close"]),
            float(row["binance_quote_volume"]),
            fill_cfg,
        )
        _accumulate(rep.binance, pending, b_n, b_not)

        g_n, g_not = _simulate_bar_fills(
            pending,
            float(row["gate_open"]),
            float(row["gate_high"]),
            float(row["gate_low"]),
            float(row["gate_close"]),
            float(row["gate_quote_volume"]),
            fill_cfg,
        )
        _accumulate(rep.gate, pending, g_n, g_not)

        vs_n, vs_not = _simulate_bar_fills(
            pending,
            float(row["binance_open"]),
            float(row["binance_high"]),
            float(row["binance_low"]),
            float(row["binance_close"]),
            float(row["gate_quote_volume"]),
            fill_cfg,
        )
        _accumulate(rep.volume_swap_gate_on_binance_ohlc, pending, vs_n, vs_not)

        bc = float(row["binance_close"])
        gc = float(row["gate_close"])
        if bc > 0:
            close_diff_bps.append(abs(gc - bc) / bc * 10_000.0)
        br = float(row["binance_high"] - row["binance_low"])
        gr = float(row["gate_high"] - row["gate_low"])
        if br > 0:
            range_diff_bps.append(abs(gr - br) / br * 10_000.0)

    rep.mean_quote_volume_binance = float(aligned["binance_quote_volume"].mean())
    rep.mean_quote_volume_gate = float(aligned["gate_quote_volume"].mean())
    if rep.mean_quote_volume_binance > 0:
        rep.volume_ratio_gate_over_binance = rep.mean_quote_volume_gate / rep.mean_quote_volume_binance
    rep.mean_abs_close_diff_bps = float(np.mean(close_diff_bps)) if close_diff_bps else float("nan")
    rep.mean_abs_high_low_diff_bps = float(np.mean(range_diff_bps)) if range_diff_bps else float("nan")

    if rep.binance.filled_orders > 0:
        rep.fill_ratio_gate_over_binance_count = rep.gate.filled_orders / rep.binance.filled_orders
    if rep.binance.filled_notional > 0:
        rep.fill_ratio_gate_over_binance_notional = rep.gate.filled_notional / rep.binance.filled_notional
    if rep.binance.filled_orders > 0:
        rep.fill_ratio_volume_swap_count = (
            rep.volume_swap_gate_on_binance_ohlc.filled_orders / rep.binance.filled_orders
        )
    if rep.binance.filled_notional > 0:
        rep.fill_ratio_volume_swap_notional = (
            rep.volume_swap_gate_on_binance_ohlc.filled_notional / rep.binance.filled_notional
        )

    rep.notes.append("BAR BACKTEST — no Gate aggTrades; volume + OHLC path drive fill drift")
    rep.notes.append("volume_swap isolates quote_volume effect using Binance OHLC")
    if rep.fill_ratio_gate_over_binance_count < 0.85:
        rep.notes.append("fill_ratio < 0.85 — lower live confidence for Binance-structure grids on Gate")
    return rep


def render_calibration_markdown(report: FillCalibrationReport) -> str:
    b, g = report.binance, report.gate
    lines = [
        "# Gate Fill Ratio Calibration vs Binance",
        "",
        f"- **Precision:** {report.precision}",
        f"- **Overlap:** {report.overlap_start} → {report.overlap_end} ({report.n_bars} bars)",
        f"- **Grid:** ATR step {report.atr_step}, range {report.atr_range}, target {report.target_notional} USDT",
        "",
        "## Venue divergence",
        "",
        f"| Metric | Value |",
        f"|--------|------:|",
        f"| Mean quote vol Binance | {report.mean_quote_volume_binance:,.0f} |",
        f"| Mean quote vol Gate | {report.mean_quote_volume_gate:,.0f} |",
        f"| Volume ratio Gate/Binance | {report.volume_ratio_gate_over_binance:.3f} |",
        f"| Mean |close| diff (bps) | {report.mean_abs_close_diff_bps:.2f} |",
        f"| Mean range diff (bps) | {report.mean_abs_high_low_diff_bps:.2f} |",
        "",
        "## Fill ratios (Gate / Binance, venue-native OHLC+volume)",
        "",
        f"| Metric | Binance | Gate | Gate/Binance |",
        f"|--------|--------:|-----:|-------------:|",
        f"| Pending orders | {b.pending_orders} | {g.pending_orders} | 1.000 |",
        f"| Filled orders | {b.filled_orders} | {g.filled_orders} | **{report.fill_ratio_gate_over_binance_count:.3f}** |",
        f"| Filled notional | {b.filled_notional:,.0f} | {g.filled_notional:,.0f} | **{report.fill_ratio_gate_over_binance_notional:.3f}** |",
        "",
        "## Volume-only swap (Binance OHLC, Gate quote_volume)",
        "",
        f"- Fill count ratio: **{report.fill_ratio_volume_swap_count:.3f}**",
        f"- Fill notional ratio: **{report.fill_ratio_volume_swap_notional:.3f}**",
        "",
        "## Notes",
        "",
    ]
    for note in report.notes:
        lines.append(f"- {note}")
    return "\n".join(lines) + "\n"
