#!/usr/bin/env python3
"""P7-01 coverage + P7-04 tick-precise SOXL/SOXS pair grid (default 0.40 / ±5)."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_binance_klines_range
from src.analysis.soxl_soxs_hedge import (
    DEFAULT_ATR_RANGE,
    DEFAULT_ATR_STEP,
    DayTradeCache,
    run_hedge_experiment,
    sweep_pair_grids,
    validate_tick_coverage,
)

OUT = ROOT / "outputs" / "experiments" / "soxl_soxs_hedge"
START = "2026-07-16"
END = "2026-09-11"


def _klines(symbol: str):
    import pandas as pd

    raw = fetch_binance_klines_range(symbol, "1h", START, END)
    return raw[["timestamp", "open", "high", "low", "close"]].copy()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    soxl = _klines("SOXLUSDT")
    soxs = _klines("SOXSUSDT")
    cov_l = validate_tick_coverage("SOXLUSDT", soxl)
    cov_s = validate_tick_coverage("SOXSUSDT", soxs)
    print("[coverage] SOXL", json.dumps(cov_l, indent=2))
    print("[coverage] SOXS", json.dumps(cov_s, indent=2))
    if not cov_l["pass"] or not cov_s["pass"]:
        payload = {"soxl": cov_l, "soxs": cov_s, "verdict": "BLOCKED", "reason": "tick coverage incomplete"}
        (OUT / "tick_coverage.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print("[p7] BLOCKED — finish SOXL/SOXS tick download first")
        return 2

    cache_l = DayTradeCache("SOXLUSDT")
    cache_s = DayTradeCache("SOXSUSDT")

    def gt_l(i, ts):
        return cache_l.for_bar(ts)

    def gt_s(i, ts):
        return cache_s.for_bar(ts)

    reports = {}
    for fee in ("base", "conservative"):
        reports[fee] = run_hedge_experiment(
            soxl,
            soxs,
            fee_preset=fee,  # type: ignore[arg-type]
            atr_step=DEFAULT_ATR_STEP,
            atr_range=DEFAULT_ATR_RANGE,
            fill_engine="tick",
            get_trades_soxl=gt_l,
            get_trades_soxs=gt_s,
        )
        print(f"\n======== tick {fee} step={DEFAULT_ATR_STEP} range={DEFAULT_ATR_RANGE} ========")
        print(json.dumps({k: v for k, v in reports[fee].items() if k != "strategies"}, indent=2))
        print(json.dumps(reports[fee]["strategies"], indent=2, default=str))

    print("[p7] default tick grids done; starting ATR sweep", flush=True)
    sweep = sweep_pair_grids(
        soxl,
        soxs,
        fee_preset="base",
        fill_engine="tick",
        get_trades_soxl=gt_l,
        get_trades_soxs=gt_s,
    )
    print("\n======== tick sweep (base) ========")
    print(json.dumps(sweep, indent=2))

    payload = {
        "generated": date.today().isoformat(),
        "coverage": {"SOXLUSDT": cov_l, "SOXSUSDT": cov_s},
        "default_grid": {"atr_step": DEFAULT_ATR_STEP, "atr_range": DEFAULT_ATR_RANGE},
        "reports": reports,
        "sweep": sweep,
    }
    path = OUT / "tick_hedge_report.json"
    path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    (OUT / "tick_coverage.json").write_text(json.dumps({"soxl": cov_l, "soxs": cov_s}, indent=2), encoding="utf-8")
    print(f"[p7] wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
