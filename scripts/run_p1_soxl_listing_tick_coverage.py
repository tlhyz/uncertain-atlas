#!/usr/bin/env python3
"""P1-13: every listing 1h bar has cache_only aggTrades (no collapse)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_agg_trades_day, fetch_binance_klines_range


def main() -> int:
    start, end = "2026-05-15", "2026-09-11"
    bars = fetch_binance_klines_range("SOXLUSDT", "1h", start, end, cache_only=True)
    bars = bars[["timestamp", "open", "high", "low", "close"]].copy()
    bars["timestamp"] = pd.to_datetime(bars["timestamp"], utc=True)
    missing: list[str] = []
    empty_days: set[str] = set()
    close_err: list[float] = []
    have = 0
    by_day: dict = {}
    for ts, hi, lo, cl in zip(bars["timestamp"], bars["high"], bars["low"], bars["close"]):
        d = ts.date()
        if d not in by_day:
            raw = fetch_agg_trades_day("SOXLUSDT", d, cache_only=True)
            hours: dict = {}
            if raw is not None and not raw.empty:
                h = pd.to_datetime(raw["timestamp"], utc=True).dt.floor("h")
                for hour, grp in raw.groupby(h, sort=False):
                    hours[pd.Timestamp(hour)] = grp
            by_day[d] = hours
        hour = by_day[d].get(ts.floor("h"))
        if hour is None or hour.empty:
            missing.append(str(ts))
            empty_days.add(str(d))
            continue
        have += 1
        px = hour["price"].to_numpy(float)
        close_err.append(abs(float(px[-1]) / max(float(cl), 1e-12) - 1.0))
    n = int(len(bars))
    payload = {
        "symbol": "SOXLUSDT",
        "start": start,
        "end": end,
        "n_bars": n,
        "bars_with_trades": have,
        "bars_missing_trades": len(missing),
        "coverage": have / max(n, 1),
        "empty_days": sorted(empty_days),
        "missing_hours_head": missing[:12],
        "median_close_rel_err": float(np.median(close_err)) if close_err else None,
        "p99_close_rel_err": float(np.quantile(close_err, 0.99)) if close_err else None,
        "pass": len(missing) == 0 and have == n,
    }
    out = ROOT / "outputs" / "experiments" / "soxl_listing_tick_coverage"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "p1_13_coverage.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("n_bars", "bars_with_trades", "bars_missing_trades", "pass", "median_close_rel_err")}, indent=2))
    print(f"wrote {path}")
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
