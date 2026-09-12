"""CLI runner for dual-engine backtest job."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .data import load_dual_dataset, write_provenance
from .experiments import (
    compare_independent_vs_unified,
    run_benchmarks,
    run_fill_modes,
    run_parameter_sweep,
    run_plans,
    run_seed_windows,
    run_stress_leverage,
    rank_leverage,
    rank_short_structures,
)
from .report import write_outputs
from .window_search import search_similar_windows


def load_dual_config(path: str | None) -> dict[str, Any]:
    defaults: dict[str, Any] = {
        "interval": "1h",
        "cache_only": False,
        "output_dir": "outputs/dual_engine_perp",
        "run_benchmarks": True,
        "run_sweep": True,
        "sweep_max_runs": 24,
        "run_seed_windows": True,
        "run_plans": True,
        "run_similar_search": True,
        "run_stress": True,
        "fill_mode": "base",
    }
    if path:
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        defaults.update(raw)
    return defaults


def run_job(cfg: dict[str, Any]) -> dict[str, Any]:
    out_dir = Path(cfg.get("output_dir") or "outputs/dual_engine_perp")
    out_dir.mkdir(parents=True, exist_ok=True)
    interval = str(cfg.get("interval") or "1h")
    cache_only = bool(cfg.get("cache_only"))

    print(f"\n======== Dual-Engine Backtest {interval} ========")
    data = load_dual_dataset(interval, cache_only=cache_only)
    write_provenance(data, out_dir)
    print(f"overlap {data.overlap_start} -> {data.overlap_end} bars={len(data.aligned_index)}")

    payload: dict[str, Any] = {
        "provenance": data.provenance,
        "interval": interval,
    }

    if cfg.get("run_benchmarks", True):
        print("[run] benchmarks...")
        payload["benchmarks"] = run_benchmarks(data, fill_mode=str(cfg.get("fill_mode") or "base"))

    if cfg.get("run_sweep", True):
        print("[run] parameter sweep...")
        payload["sweep"] = run_parameter_sweep(
            data,
            max_runs=int(cfg.get("sweep_max_runs") or 24),
            fill_mode=str(cfg.get("fill_mode") or "base"),
        )

    if cfg.get("run_seed_windows", True):
        print("[run] seed windows...")
        payload["seed_windows"] = run_seed_windows(data)

    if cfg.get("run_plans", True):
        print("[run] three plans...")
        payload["plans"] = run_plans(data)

    print("[run] independent vs unified...")
    payload["independent_vs_unified"] = compare_independent_vs_unified(data)

    print("[run] short structure rank...")
    payload["short_structures"] = rank_short_structures(data)

    print("[run] leverage rank...")
    payload["leverage_rank"] = rank_leverage(data)

    payload["fill_modes"] = run_fill_modes(data)

    if cfg.get("run_stress", True):
        print("[run] 3x stress...")
        payload["stress_3x"] = run_stress_leverage(data)

    if cfg.get("run_similar_search", True):
        print("[run] similar window search...")
        try:
            payload["similar_windows"] = [w.as_dict() for w in search_similar_windows(data)]
        except Exception as exc:  # noqa: BLE001
            payload["similar_windows"] = [{"error": str(exc)}]

    report_path = write_outputs(payload, out_dir)
    print(f"\n[done] report -> {report_path}")
    return payload


def main(argv: list[str] | None = None) -> int:
    import argparse

    p = argparse.ArgumentParser(description="Dual-engine state-switching perpetual backtest")
    p.add_argument("-c", "--config", default="configs/dual_engine_perp.yaml")
    p.add_argument("--cache-only", action="store_true")
    p.add_argument("--output-dir", default="")
    args = p.parse_args(argv)
    cfg = load_dual_config(args.config)
    if args.cache_only:
        cfg["cache_only"] = True
    if args.output_dir:
        cfg["output_dir"] = args.output_dir
    run_job(cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
