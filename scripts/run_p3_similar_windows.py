#!/usr/bin/env python3
"""P3-11: SOXL-only similar-window scan (do not align to SNXX)."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_binance_klines_range
from qtb.dual.window_search import search_similar_windows
from src.analysis.soxl_grid_cli import ohlc_1h_from_cached_ticks


def load_soxl_bars(start: str, end: str):
    try:
        bars = fetch_binance_klines_range("SOXLUSDT", "1h", start, end, cache_only=True)
        src = str(bars.attrs.get("source") or "klines_cache")
        return bars, src
    except RuntimeError:
        pass
    try:
        bars = fetch_binance_klines_range("SOXLUSDT", "1h", start, end, cache_only=False)
        src = str(bars.attrs.get("source") or "klines_download")
        return bars, src
    except Exception:
        bars = ohlc_1h_from_cached_ticks("SOXLUSDT", start, end)
        return bars, str(bars.attrs.get("source") or "ticks_resample")


def main() -> int:
    start, end = "2026-05-15", "2026-09-11"
    seed = "TECH_T3"
    horizon, step, top_k = 1440, 168, 20
    bars, src = load_soxl_bars(start, end)
    n = int(len(bars))
    max_slides = 1 + max(n - horizon, 0) // step if n >= 48 else 0
    data = SimpleNamespace(tech={"SOXL": SimpleNamespace(bars=bars)})
    wins = search_similar_windows(data, seed_id=seed, top_k=top_k, horizon_bars=horizon, step_bars=step)
    need_bars_for_20 = horizon + 19 * step
    payload = {
        "symbol": "SOXLUSDT",
        "start": start,
        "end": end,
        "bar_source": src,
        "n_bars": n,
        "seed": seed,
        "horizon_bars": horizon,
        "step_bars": step,
        "max_slides": max_slides,
        "n_hits": len(wins),
        "need_bars_for_top20": need_bars_for_20,
        "top20_structurally_possible": n >= need_bars_for_20,
        "windows": [w.as_dict() for w in wins],
    }
    out = ROOT / "outputs" / "experiments" / "dual_binance_tick_similar_windows"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "p3_11_listing_scan.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("n_bars", "max_slides", "n_hits", "top20_structurally_possible", "bar_source")}, indent=2))
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
