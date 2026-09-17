#!/usr/bin/env python3
"""P7-01/02/03: download SOXS (optional) + BAR hedge experiment vs SOXL."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import pandas as pd

from qtb.data.binance_futures import fetch_agg_trades_range, fetch_binance_klines_range
from src.analysis.soxl_soxs_hedge import run_hedge_experiment

OUT = ROOT / "outputs" / "experiments" / "soxl_soxs_hedge"
SOXS_START = "2026-07-16"
SOXS_END = "2026-09-14"
OVERLAP_END = "2026-09-11"


def _klines(symbol: str, start: str, end: str) -> pd.DataFrame:
    raw = fetch_binance_klines_range(symbol, "1h", start, end)
    if raw.empty:
        raise RuntimeError(f"no klines for {symbol} {start}->{end}")
    return pd.DataFrame(
        {
            "timestamp": pd.to_datetime(raw["timestamp"], utc=True),
            "open": raw["open"].astype(float),
            "high": raw["high"].astype(float),
            "low": raw["low"].astype(float),
            "close": raw["close"].astype(float),
        }
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--download-ticks", action="store_true", help="SOXS aggTrades to cache/")
    p.add_argument("--start", default=SOXS_START)
    p.add_argument("--end", default=SOXS_END)
    args = p.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    if args.download_ticks:
        print(f"[p7] downloading SOXSUSDT ticks {args.start} -> {args.end}")
        df = fetch_agg_trades_range("SOXSUSDT", args.start, args.end)
        print(f"[p7] SOXS ticks rows={len(df)}")

    soxl = _klines("SOXLUSDT", args.start, min(args.end, OVERLAP_END))
    soxs = _klines("SOXSUSDT", args.start, min(args.end, OVERLAP_END))
    reports = {}
    for fee in ("base", "conservative"):
        reports[fee] = run_hedge_experiment(soxl, soxs, fee_preset=fee)  # type: ignore[arg-type]
        print(f"\n======== {fee} ========")
        print(json.dumps({k: v for k, v in reports[fee].items() if k != "strategies"}, indent=2))
        print(json.dumps(reports[fee]["strategies"], indent=2, default=str))

    payload = {
        "generated": date.today().isoformat(),
        "soxs_listed": f"{SOXS_START} -> {SOXS_END}",
        "reports": reports,
    }
    path = OUT / "hedge_report.json"
    path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"[p7] wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
