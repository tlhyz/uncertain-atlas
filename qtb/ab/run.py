"""CLI runner for the ETF vs perpetual A/B research job."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from .data import load_pair_data, write_provenance
from .experiments import (
    decide_pair,
    monte_carlo,
    run_long_pair,
    run_portfolio,
    run_short_pair,
    run_windows,
    walk_forward,
)
from .report import write_outputs
from .universe import long_pairs


def load_ab_config(path: str | None) -> dict[str, Any]:
    defaults = {
        "initial_capital": 1000.0,
        "pairs": ["BTC", "ETH", "SOL", "PENGU", "PUMP", "SOXL", "SNXX", "AAOI"],
        "primary_interval": "1h",
        "fine_interval": "5m",
        "run_fine": True,
        "run_short": True,
        "run_windows": True,
        "run_walk_forward": True,
        "run_monte_carlo": True,
        "run_portfolio": True,
        "mc_paths": 1000,
        "horizons": [7, 14, 30, 60, 90],
        "spot_rebate": 0.70,
        "futures_rebate": 0.75,
        "spot_maker_fee": 0.0008,
        "spot_taker_fee": 0.00085,
        "futures_maker_fee": 0.00008,
        "futures_taker_fee": 0.0002,
        "cache_only": False,
        "output_dir": "outputs/ab_etf_vs_perp",
    }
    if path:
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        defaults.update(raw)
    return defaults


def run_job(cfg: dict[str, Any]) -> dict[str, Any]:
    out_dir = Path(cfg.get("output_dir") or "outputs/ab_etf_vs_perp")
    out_dir.mkdir(parents=True, exist_ok=True)
    interval = str(cfg.get("primary_interval") or "1h")
    cache_only = bool(cfg.get("cache_only"))
    names = list(cfg.get("pairs") or [])
    pairs = long_pairs(names)
    pair_payloads: list[dict[str, Any]] = []
    pair_data = {}
    windows_meta = []

    for pair in pairs:
        print(f"\n======== {pair.name} {interval} ========")
        try:
            data = load_pair_data(pair, interval, cache_only=cache_only, include_short=bool(cfg.get("run_short")))
        except Exception as exc:  # noqa: BLE001
            pair_payloads.append({
                "pair": pair.name,
                "error": str(exc),
                "no_direct_perp": pair.no_direct_perp,
                "rows": [],
            })
            print(f"[skip] {pair.name}: {exc}")
            continue
        pair_data[pair.name] = data
        windows_meta.append(data.window)
        print(f"overlap {data.window.ab_start} -> {data.window.ab_end} bars={data.window.bars}")
        bundle = run_long_pair(data, cfg)
        if cfg.get("run_windows", True):
            bundle["windows"] = run_windows(data, cfg)
        if cfg.get("run_walk_forward", True) and pair.name in {"BTC", "ETH", "SOL"}:
            bundle["walk_forward"] = walk_forward(data, cfg)
        if cfg.get("run_monte_carlo", True):
            bundle["monte_carlo"] = monte_carlo(data, cfg)
        if cfg.get("run_short", True):
            bundle["short"] = run_short_pair(data, cfg)
        bundle["decision"] = decide_pair(bundle)
        pair_payloads.append(bundle)
        # persist incrementally
        (out_dir / f"{pair.name}_{interval}.json").write_text(
            json.dumps({k: v for k, v in bundle.items() if k != "curves"}, indent=2, ensure_ascii=False, default=str),
            encoding="utf-8",
        )

    # optional 5m recent confirmation (does not replace 1h conclusions)
    fine = None
    if cfg.get("run_fine") and pair_data:
        fine = {}
        fiv = str(cfg.get("fine_interval") or "5m")
        for name, _d in list(pair_data.items()):
            if name not in {"BTC", "ETH", "SOL"}:
                continue
            print(f"\n======== {name} {fiv} (confirmation) ========")
            try:
                fd = load_pair_data(_d.pair, fiv, cache_only=cache_only, include_short=False)
                fb = run_long_pair(fd, cfg)
                fb["decision"] = decide_pair(fb)
                fine[name] = {
                    "window": fd.window.as_dict(),
                    "decision": fb["decision"],
                    "core": {
                        "etf": next((r for r in fb["rows"] if r["name"] == "A2_etf_native_atr_d0.0_reb_base"), None),
                        "perp3": next((r for r in fb["rows"] if r["name"] == "B_perp_3.0x_iso_P1_d0.0_reb_base"), None),
                    },
                }
            except Exception as exc:  # noqa: BLE001
                fine[name] = {"error": str(exc)}

    portfolio = {}
    if cfg.get("run_portfolio", True):
        print("\n======== portfolio ========")
        portfolio = run_portfolio(pair_data, cfg)

    payload = {
        "config": {k: v for k, v in cfg.items() if k != "api_key"},
        "data_limits": {
            "gate_max_bars": 10_000,
            "primary_interval": interval,
            "fine_interval": cfg.get("fine_interval"),
            "tick_history": "insufficient_for_requested_windows",
            "nav_history": False,
            "synthetic_ticks": False,
        },
        "pairs": pair_payloads,
        "fine_interval_confirmation": fine,
        "portfolio": portfolio,
    }
    write_provenance(out_dir / "provenance.json", windows_meta, extra=payload["data_limits"])
    written = write_outputs(out_dir, payload)
    print(json.dumps({"written": written, "pairs": [p.get("pair") for p in pair_payloads]}, indent=2))
    return payload


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Fair Gate 3L ETF vs perpetual grid A/B")
    p.add_argument("-c", "--config", default="configs/ab_etf_vs_perp.yaml")
    p.add_argument("--cache-only", action="store_true")
    p.add_argument("--pairs", default="", help="comma list, e.g. BTC,ETH,SOL")
    p.add_argument("--output-dir", default="")
    p.add_argument("--skip-fine", action="store_true")
    p.add_argument("--skip-mc", action="store_true")
    args = p.parse_args(argv)
    cfg = load_ab_config(args.config if Path(args.config).exists() else None)
    if args.cache_only:
        cfg["cache_only"] = True
    if args.pairs:
        cfg["pairs"] = [x.strip().upper() for x in args.pairs.split(",") if x.strip()]
    if args.output_dir:
        cfg["output_dir"] = args.output_dir
    if args.skip_fine:
        cfg["run_fine"] = False
    if args.skip_mc:
        cfg["run_monte_carlo"] = False
    run_job(cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
