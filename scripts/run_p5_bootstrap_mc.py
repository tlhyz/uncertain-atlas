#!/usr/bin/env python3
"""P5-01 — block bootstrap MC on dual-book equity curve."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.monte_carlo import block_bootstrap_mc


def main() -> int:
    from qtb.dual.data import load_dual_dataset
    from qtb.dual.experiments import portfolio_kwargs_from_config
    from qtb.dual.portfolio import run_dual_portfolio
    from qtb.dual.run import load_dual_config
    from qtb.dual.universe import DualParams

    cfg_path = sys.argv[1] if len(sys.argv) > 1 else "configs/experiments/dual_binance_tick_independent_vs_unified.yaml"
    cfg = load_dual_config(cfg_path)
    out_dir = Path(cfg.get("output_dir") or "outputs/experiments/p5_bootstrap_mc")
    out_dir.mkdir(parents=True, exist_ok=True)

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
    print(f"[p5] dual book run bars={len(data.aligned_index)}...", flush=True)
    r = run_dual_portfolio(data, DualParams(unified_signal=False), name="mc_source", **pk)
    mc = block_bootstrap_mc(
        r.total_equity,
        timestamps=r.timestamps,
        block_days=(1, 3, 5),
        n_paths=1000,
        initial=10_000.0,
        rng=__import__("numpy").random.default_rng(42),
    )
    payload = {
        "source": "dual_book_independent",
        "config": cfg_path,
        "bars": len(data.aligned_index),
        "portfolio_kwargs": pk,
        "monte_carlo": mc,
    }
    out_path = out_dir / "bootstrap_mc.json"
    out_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"[p5] wrote {out_path}", flush=True)
    for blk, stats in mc.get("blocks", {}).items():
        print(
            f"  {blk}: p50={stats['p50_final']:.0f} prob_loss={100*stats['prob_loss']:.1f}% "
            f"prob_dd20={100*stats['prob_dd_20']:.1f}%",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
