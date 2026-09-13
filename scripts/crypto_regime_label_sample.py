#!/usr/bin/env python3
"""P2-08 — Sample crypto FSM regime labels on C1 window (no backtest)."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.dual.crypto_fsm import CryptoAssetFSM
from qtb.dual.universe import CryptoParams


def load_close_series(symbol: str, start: str, end: str) -> tuple[list, list, list, list]:
    from qtb.data.binance_futures import fetch_binance_klines_range, normalize_symbol

    sym = normalize_symbol(symbol)
    df = fetch_binance_klines_range(sym, "1h", start, end, cache_only=True)
    if df.empty:
        raise RuntimeError(f"no klines for {sym} {start}->{end}")
    ts = df["timestamp"].tolist()
    close = df["close"].to_numpy(float)
    high = df["high"].to_numpy(float)
    low = df["low"].to_numpy(float)
    return ts, close, high, low


def sample_regimes(
    symbols: list[str],
    start: str,
    end: str,
) -> dict:
    out: dict = {"start": start, "end": end, "symbols": {}}
    for sym in symbols:
        ts, close, high, low = load_close_series(sym, start, end)
        fsm = CryptoAssetFSM(sym, CryptoParams())
        counts: Counter[str] = Counter()
        segments: list[dict] = []
        cur_regime: str | None = None
        seg_start = 0
        for i in range(len(close)):
            regime = fsm.classify(i, close, high, low)
            counts[regime] += 1
            if regime != cur_regime:
                if cur_regime is not None:
                    segments.append({
                        "regime": cur_regime,
                        "start": str(ts[seg_start]),
                        "end": str(ts[i - 1]),
                        "bars": i - seg_start,
                    })
                cur_regime = regime
                seg_start = i
        if cur_regime is not None:
            segments.append({
                "regime": cur_regime,
                "start": str(ts[seg_start]),
                "end": str(ts[-1]),
                "bars": len(close) - seg_start,
            })
        hv_segments = [s for s in segments if s["regime"] == "RANGE_HIGH_VOL"]
        out["symbols"][sym] = {
            "bars": len(close),
            "regime_counts": dict(counts),
            "regime_frac": {k: round(v / len(close), 4) for k, v in counts.items()},
            "range_high_vol_segments": hv_segments[:10],
            "range_high_vol_total_bars": counts.get("RANGE_HIGH_VOL", 0),
        }
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Crypto regime auto-label sample (P2-08)")
    p.add_argument("--symbols", nargs="+", default=["BTC", "ETH", "SOL"])
    p.add_argument("--start", default="2024-09-01")
    p.add_argument("--end", default="2024-11-30")
    p.add_argument(
        "--output-dir",
        default="outputs/experiments/crypto_regime_label_sample",
    )
    args = p.parse_args()

    payload = sample_regimes(args.symbols, args.start, args.end)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "regime_label_sample.json"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        "# Crypto Regime Label Sample (P2-08)",
        "",
        f"Window: {args.start} → {args.end}",
        "",
    ]
    for sym, data in payload["symbols"].items():
        lines.append(f"## {sym} ({data['bars']} bars)")
        lines.append("")
        lines.append("| Regime | Bars | Frac |")
        lines.append("|--------|-----:|-----:|")
        for reg, cnt in sorted(data["regime_counts"].items(), key=lambda x: -x[1]):
            lines.append(f"| {reg} | {cnt} | {data['regime_frac'][reg]:.2%} |")
        lines.append("")
        lines.append(f"RANGE_HIGH_VOL segments (first 10): {len(data['range_high_vol_segments'])} shown")
        for seg in data["range_high_vol_segments"][:5]:
            lines.append(f"- {seg['start']} → {seg['end']} ({seg['bars']} bars)")
        lines.append("")
    md_path = out_dir / "REGIME_LABEL_SAMPLE.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[done] {json_path}")
    print(f"[done] {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
