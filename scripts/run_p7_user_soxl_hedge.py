#!/usr/bin/env python3
"""P7-07: user moving dual-side hedge — 5x, ±20U and ±20%, 5k+5k.

Shared band. Both legs see the same ticks. If either sleeve liquidates,
flatten the survivor so the leftover is not a naked directional book.
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_binance_klines_range
from src.analysis.soxl_soxs_hedge import DayTradeCache
from src.analysis.user_moving_grid import run_user_hedge_pair

OUT = ROOT / "outputs" / "experiments" / "soxl_user_ls_hedge"
START = "2026-07-16"
END = "2026-09-11"


def _klines():
    raw = fetch_binance_klines_range("SOXLUSDT", "1h", START, END)
    return raw[["timestamp", "open", "high", "low", "close"]].copy()


def _strip(rep: dict) -> dict:
    daily = rep["daily"]
    return {
        "range_mode": rep["range_mode"],
        "fill_engine": rep["fill_engine"],
        "fee_preset": rep["fee_preset"],
        "hedge_mode": rep.get("hedge_mode"),
        "pair_stopped": rep.get("pair_stopped"),
        "stop_bar": rep.get("stop_bar"),
        "return": rep["return"],
        "max_dd": rep["max_dd"],
        "end_equity": rep["end_equity"],
        "inventory_frac": rep["inventory_frac"],
        "net_qty_units": rep["net_qty_units"],
        "fills": rep["fills"],
        "turnover": rep["turnover"],
        "reanchors": rep["reanchors"],
        "liquidated_long": rep["liquidated_long"],
        "liquidated_short": rep["liquidated_short"],
        "long": rep["long"],
        "short": rep["short"],
        "n_days": int(len(daily)),
        "best_day": float(daily["daily_pnl"].max()) if len(daily) else None,
        "worst_day": float(daily["daily_pnl"].min()) if len(daily) else None,
        "mean_day": float(daily["daily_pnl"].mean()) if len(daily) else None,
        "win_days": int((daily["daily_pnl"] > 0).sum()) if len(daily) else 0,
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    bars = _klines()
    cache = DayTradeCache("SOXLUSDT")

    def gt(_i, ts):
        return cache.for_bar(ts)

    summary = {
        "generated": date.today().isoformat(),
        "window": f"{START}->{END}",
        "n_bars": int(len(bars)),
        "hedge_mode": "moving_ls_flatten_survivor",
        "variants": {},
    }
    for mode in ("usdt", "pct"):
        print(f"[p7-07] hedge tick base range_mode={mode}", flush=True)
        rep = run_user_hedge_pair(bars, range_mode=mode, fill_engine="tick", fee_preset="base", get_trades=gt)
        daily = rep["daily"]
        daily.to_csv(OUT / f"{mode}20_hedge_daily.csv", index=False)
        summary["variants"][mode] = _strip(rep)
        print(json.dumps(summary["variants"][mode], indent=2, default=str), flush=True)

    path = OUT / "summary.json"
    path.write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    print(f"[p7-07] wrote {path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
