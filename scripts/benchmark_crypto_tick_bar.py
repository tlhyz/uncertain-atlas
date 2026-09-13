#!/usr/bin/env python3
"""P2-15 — Benchmark BTC aggTrades I/O vs bar slice (not full backtest)."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import pandas as pd
from qtb.data.binance_futures import fetch_agg_trades_day, fetch_binance_klines_range, slice_trades_for_bar


def bench_symbol(symbol: str, start: str, end: str, *, cache_only: bool = True) -> dict:
    sym = symbol if symbol.endswith("USDT") else f"{symbol}USDT"
    t0 = time.perf_counter()
    kl = fetch_binance_klines_range(sym, "1h", start, end, cache_only=cache_only)
    t_kl = time.perf_counter() - t0

    days = pd.date_range(start, end, freq="D")
    t0 = time.perf_counter()
    cache: dict = {}
    row_counts: list[int] = []
    for d in days:
        df = fetch_agg_trades_day(sym, d.date(), cache_only=cache_only)
        cache[d.date()] = df
        row_counts.append(len(df))
    t_load = time.perf_counter() - t0

    t0 = time.perf_counter()
    total_ticks = 0
    for ts in kl["timestamp"]:
        sub = slice_trades_for_bar(cache[pd.Timestamp(ts).date()], pd.Timestamp(ts), "1h")
        total_ticks += len(sub)
    t_slice = time.perf_counter() - t0
    n_bars = len(kl)

    return {
        "symbol": sym,
        "start": start,
        "end": end,
        "bars": n_bars,
        "days": len(days),
        "day_rows": row_counts,
        "total_day_rows": sum(row_counts),
        "total_bar_ticks": total_ticks,
        "load_klines_s": round(t_kl, 3),
        "load_days_s": round(t_load, 3),
        "slice_bars_s": round(t_slice, 3),
        "ms_per_bar_slice": round(1000 * t_slice / max(n_bars, 1), 2),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Benchmark aggTrades load/slice")
    ap.add_argument("--symbol", default="BTC")
    ap.add_argument("--start", default="2024-09-01")
    ap.add_argument("--end", default="2024-09-05")
    args = ap.parse_args()
    r = bench_symbol(args.symbol, args.start, args.end)
    print(f"symbol={r['symbol']} bars={r['bars']} days={r['days']}")
    print(f"day_rows={r['day_rows']} total={r['total_day_rows']}")
    print(f"load_kl={r['load_klines_s']}s load_days={r['load_days_s']}s slice={r['slice_bars_s']}s ({r['ms_per_bar_slice']}ms/bar)")
    print(f"bar_ticks={r['total_bar_ticks']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
