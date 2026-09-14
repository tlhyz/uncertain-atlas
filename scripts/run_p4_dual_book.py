#!/usr/bin/env python3
"""Run P4 dual-book independent vs unified (65d) without full experiment matrix."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.dual.data import load_dual_dataset, write_provenance
from qtb.dual.experiments import compare_independent_vs_unified, portfolio_kwargs_from_config
from qtb.dual.run import load_dual_config


def main() -> int:
    cfg_path = sys.argv[1] if len(sys.argv) > 1 else "configs/experiments/dual_binance_tick_independent_vs_unified.yaml"
    cfg = load_dual_config(cfg_path)
    out_dir = Path(cfg["output_dir"])
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
    write_provenance(data, out_dir)
    pk = portfolio_kwargs_from_config(cfg, tick_precise=bool(cfg.get("tick_precise", True)))
    print(f"[p4] overlap {data.overlap_start} -> {data.overlap_end} bars={len(data.aligned_index)} kwargs={pk}")
    result = compare_independent_vs_unified(data, **pk)
    payload = {"independent_vs_unified": result, "provenance": data.provenance, "portfolio_kwargs": pk}
    (out_dir / "dual_results.json").write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    ind = result["independent"]
    print(
        f"[p4] independent return={100*ind['total_return']:.2f}% "
        f"crypto_max_dd={100*ind['crypto_max_dd_pct']:.2f}% "
        f"regime_A={result['regime_independent']['tech_down_crypto_up']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
