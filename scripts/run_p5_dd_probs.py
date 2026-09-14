#!/usr/bin/env python3
"""P5-05 — DD>10/20/30% probability from block bootstrap MC (65d dual-book)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.monte_carlo import block_bootstrap_mc


def dd_probability_table(mc: dict) -> dict[str, dict[str, float]]:
    """Extract DD threshold probabilities per block size."""
    table: dict[str, dict[str, float]] = {}
    for blk, stats in (mc.get("blocks") or {}).items():
        table[blk] = {
            "prob_dd_10": float(stats.get("prob_dd_10", 0)),
            "prob_dd_20": float(stats.get("prob_dd_20", 0)),
            "prob_dd_30": float(stats.get("prob_dd_30", 0)),
            "prob_loss": float(stats.get("prob_loss", 0)),
            "median_max_dd": float(stats.get("median_max_dd", 0)),
            "p50_final": float(stats.get("p50_final", 0)),
        }
    return table


def render_dd_markdown(payload: dict) -> str:
    mc = payload.get("monte_carlo") or {}
    table = payload.get("dd_probabilities") or {}
    lines = [
        "# DD Probability Report — Block Bootstrap MC",
        "",
        f"- **Config:** {payload.get('config')}",
        f"- **Bars:** {payload.get('bars')}",
        f"- **Daily obs:** {mc.get('daily_obs')}",
        f"- **In-sample return:** {100 * float(mc.get('in_sample_return', 0)):.2f}%",
        f"- **Paths:** {mc.get('n_paths')}",
        "",
        "| Block | P(DD>10%) | P(DD>20%) | P(DD>30%) | P(loss) | Median max DD |",
        "|-------|----------:|----------:|----------:|--------:|--------------:|",
    ]
    for blk, row in sorted(table.items()):
        lines.append(
            f"| {blk} | {100 * row['prob_dd_10']:.1f}% | {100 * row['prob_dd_20']:.1f}% "
            f"| {100 * row['prob_dd_30']:.1f}% | {100 * row['prob_loss']:.1f}% "
            f"| {100 * row['median_max_dd']:.1f}% |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    cfg_path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "configs/experiments/dual_binance_tick_independent_vs_unified.yaml"
    )
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("outputs/experiments/p5_dd_probs_65d")
    out_dir.mkdir(parents=True, exist_ok=True)

    from qtb.dual.data import load_dual_dataset
    from qtb.dual.experiments import portfolio_kwargs_from_config
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
    print(f"[p5-05] dual book run bars={len(data.aligned_index)}...", flush=True)
    r = run_dual_portfolio(data, DualParams(unified_signal=False), name="dd_mc_source", **pk)
    mc = block_bootstrap_mc(
        r.total_equity,
        timestamps=r.timestamps,
        block_days=(1, 3, 5),
        n_paths=1000,
        initial=10_000.0,
        rng=__import__("numpy").random.default_rng(42),
    )
    in_sample_max_dd = float(getattr(r, "max_dd_pct", 0) or 0)
    payload = {
        "task": "P5-05",
        "source": "dual_book_independent",
        "config": cfg_path,
        "bars": len(data.aligned_index),
        "portfolio_kwargs": pk,
        "in_sample": {
            "total_return": float(r.total_equity[-1] / 10_000 - 1) if len(r.total_equity) else 0,
            "max_dd_pct": in_sample_max_dd,
            "liquidation_count": int(getattr(r, "liquidation_count", 0) or 0),
        },
        "monte_carlo": mc,
        "dd_probabilities": dd_probability_table(mc),
    }
    json_path = out_dir / "dd_probabilities.json"
    md_path = out_dir / "DD_PROB_REPORT.md"
    json_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    md_path.write_text(render_dd_markdown(payload), encoding="utf-8")
    print(f"[p5-05] wrote {json_path}", flush=True)
    ref = payload["dd_probabilities"].get("3d") or next(iter(payload["dd_probabilities"].values()), {})
    print(
        f"  3d: P(DD>10)={100*ref.get('prob_dd_10',0):.1f}% "
        f"P(DD>20)={100*ref.get('prob_dd_20',0):.1f}% "
        f"P(DD>30)={100*ref.get('prob_dd_30',0):.1f}%",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
