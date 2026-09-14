#!/usr/bin/env python3
"""P5-06 — liquidation probability from block bootstrap MC (65d dual-book)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.monte_carlo import block_bootstrap_mc


def _liq_row(mc: dict, in_sample: dict) -> dict:
    ref = (mc.get("blocks") or {}).get("3d") or {}
    return {
        "in_sample_liquidated": bool(in_sample.get("liquidated")),
        "in_sample_liquidation_count": int(in_sample.get("liquidation_count", 0)),
        "in_sample_crypto_max_dd_pct": float(in_sample.get("crypto_max_dd_pct", 0)),
        "prob_ruin_mc": float(ref.get("prob_ruin", 0)),
        "prob_liquidation_proxy_mc": float(ref.get("prob_liquidation_proxy", 0)),
        "liq_equity_frac": float(ref.get("liq_equity_frac", 0.12)),
        "prob_dd_30_mc": float(ref.get("prob_dd_30", 0)),
    }


def render_markdown(payload: dict) -> str:
    lines = [
        "# Liquidation Probability Report — Block Bootstrap MC",
        "",
        f"- **Config:** {payload.get('config')}",
        f"- **Bars:** {payload.get('bars')}",
        f"- **Proxy:** min path equity ≤ {100 * float(payload.get('liq_equity_frac', 0.12)):.0f}% initial (~88% account loss floor)",
        "",
        "| Book | In-sample liq | Crypto max DD | P(ruin) MC | P(liq proxy) MC |",
        "|------|:-------------:|--------------:|-----------:|----------------:|",
    ]
    for book, row in (payload.get("books") or {}).items():
        lines.append(
            f"| {book} | {row['in_sample_liquidation_count']} "
            f"| {100 * row['in_sample_crypto_max_dd_pct']:.1f}% "
            f"| {100 * row['prob_ruin_mc']:.1f}% "
            f"| {100 * row['prob_liquidation_proxy_mc']:.1f}% |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    cfg_path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "configs/experiments/dual_binance_tick_independent_vs_unified.yaml"
    )
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("outputs/experiments/p5_liq_probs_65d")
    out_dir.mkdir(parents=True, exist_ok=True)

    from qtb.dual.data import load_dual_dataset
    from qtb.dual.experiments import compare_independent_vs_unified, portfolio_kwargs_from_config
    from qtb.dual.portfolio import run_dual_portfolio
    from qtb.dual.run import load_dual_config
    from qtb.dual.universe import DualParams

    cfg = load_dual_config(cfg_path)
    data = load_dual_dataset(
        str(cfg.get("interval") or "1h"),
        cache_only=bool(cfg.get("cache_only")),
        start=str(cfg.get("data_start") or "2026-07-09"),
        end=str(cfg.get("data_end") or "").strip() or None,
        download_trades=bool(cfg.get("download_trades", True)),
        tech_tick_only=bool(cfg.get("tech_tick_only", True)),
        crypto_download_trades=cfg.get("crypto_download_trades"),
    )
    pk = portfolio_kwargs_from_config(cfg, tick_precise=bool(cfg.get("tick_precise", True)))
    initial = 10_000.0
    rng = __import__("numpy").random.default_rng(42)

    print(f"[p5-06] dual book bars={len(data.aligned_index)} independent...", flush=True)
    ind_r = run_dual_portfolio(data, DualParams(unified_signal=False), name="liq_ind", **pk)
    print("[p5-06] unified...", flush=True)
    uni_r = run_dual_portfolio(data, DualParams(unified_signal=True), name="liq_uni", **pk)

    from qtb.dual.experiments import summarize_portfolio

    books: dict[str, dict] = {}
    for label, r in (("independent", ind_r), ("unified", uni_r)):
        sm = summarize_portfolio(r, initial=initial)
        mc = block_bootstrap_mc(r.total_equity, timestamps=r.timestamps, n_paths=1000, initial=initial, rng=rng)
        in_sample = {
            "liquidated": bool(r.liquidated),
            "liquidation_count": int(r.liquidation_count),
            "crypto_max_dd_pct": float(sm.get("crypto_max_dd_pct", 0)),
            "max_dd_pct": float(sm.get("max_dd_pct", 0)),
            "total_return": float(sm.get("total_return", 0)),
        }
        books[label] = {**_liq_row(mc, in_sample), "monte_carlo": mc, "in_sample": in_sample}
        ref = books[label]
        print(
            f"  {label}: liq={ref['in_sample_liquidation_count']} "
            f"P(proxy)={100 * ref['prob_liquidation_proxy_mc']:.1f}%",
            flush=True,
        )

    payload = {
        "task": "P5-06",
        "config": cfg_path,
        "bars": len(data.aligned_index),
        "portfolio_kwargs": pk,
        "liq_equity_frac": 0.12,
        "books": {k: {kk: vv for kk, vv in v.items() if kk != "monte_carlo"} for k, v in books.items()},
        "monte_carlo": {k: v["monte_carlo"] for k, v in books.items()},
    }
    json_path = out_dir / "liq_probabilities.json"
    md_path = out_dir / "LIQ_PROB_REPORT.md"
    json_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    md_path.write_text(render_markdown(payload), encoding="utf-8")
    print(f"[p5-06] wrote {json_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
