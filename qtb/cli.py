#!/usr/bin/env python3
"""qtb CLI: backtest | optimize | report | batch | screen."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from qtb.config import load_config
from qtb.live.broker import LiveBroker, is_dry_run_forced


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="qtb",
        description=(
            "Gate USDT-M backtest / optimize / report / screen "
            "(default mode=backtest, live is DRY_RUN stub)."
        ),
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_common(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("-c", "--config", default="", help="YAML/TOML config path")
        sp.add_argument("--symbol", default="", help="Override symbol, e.g. BTC_USDT")
        sp.add_argument("--interval", default="", help="1m/5m/15m/1h/4h/1d")
        sp.add_argument("--days", type=int, default=0)
        sp.add_argument("--cache-only", action="store_true")
        sp.add_argument("--prefer-sample", action="store_true")
        sp.add_argument("--output-dir", default="")
        sp.add_argument("--run-name", default="")
        sp.add_argument(
            "--strategy",
            default="",
            help="classic_grid|trend_grid|dual_grid|martingale|dual_martingale|moving_grid",
        )
        sp.add_argument("--stop-loss", type=float, default=-1.0, help="Investment SL 0.5 or 0.7")

    bt = sub.add_parser("backtest", help="Run a single backtest and write outputs/")
    add_common(bt)

    opt = sub.add_parser("optimize", help="Search + anti-overfit + ranked composite score")
    add_common(opt)
    opt.add_argument("--grid", default="", help="compact|medium|full")

    rp = sub.add_parser("report", help="Show / refresh artifacts from an existing run dir")
    rp.add_argument("run_dir", nargs="?", default="")
    rp.add_argument("-c", "--config", default="")
    rp.add_argument("--prefer-sample", action="store_true")

    bat = sub.add_parser("batch", help="Multi-symbol / multi-interval backtests")
    add_common(bat)

    live = sub.add_parser("live", help="Live stub (always DRY_RUN unless dangerous override)")
    live.add_argument("-c", "--config", default="")
    live.add_argument("--ping", action="store_true")

    from qtb.screen import add_screen_flags

    screen = sub.add_parser(
        "screen",
        help="Screen liquid Gate USDT perps for high vol + low path efficiency",
    )
    add_screen_flags(screen, batch_default=False)

    batch_screen = sub.add_parser(
        "batch-screen",
        help="Screen then batch-backtest top K picks (aggressive dual SL50)",
    )
    add_screen_flags(batch_screen, batch_default=True)

    fetf = sub.add_parser(
        "fetch-etf",
        help="Download official Gate spot deals (tick tape) for ETF underlyings",
    )
    fetf.add_argument(
        "--underlyings",
        default="soxl,snxx,eth,sol",
        help="soxl,snxx,eth,sol or raw pairs like ETH3L_USDT",
    )
    fetf.add_argument("--from", dest="deals_from", default="", help="YYYY-MM (default: last 3 complete months)")
    fetf.add_argument("--to", dest="deals_to", default="", help="YYYY-MM")
    fetf.add_argument(
        "--longs-only",
        action="store_true",
        help="SOXLG/SNXXG/ETH3L/SOL3L (tokenized SOXL/SNXX + ETH/SOL 3x long)",
    )
    fetf.add_argument("--cache-dir", default="", help="Override cache/spot_deals")
    return p


def _overrides(args: argparse.Namespace) -> dict[str, Any]:
    o: dict[str, Any] = {}
    if getattr(args, "symbol", ""):
        o["symbol"] = args.symbol
        # Reuse style YAML on another contract: don't keep the bundled sample unless asked.
        o["prefer_sample"] = False
    if getattr(args, "interval", ""):
        o["interval"] = args.interval
    if getattr(args, "days", 0):
        o["days"] = args.days
    if getattr(args, "cache_only", False):
        o["cache_only"] = True
    if getattr(args, "prefer_sample", False):
        o["prefer_sample"] = True
    if getattr(args, "output_dir", ""):
        o["output_dir"] = args.output_dir
    if getattr(args, "run_name", ""):
        o["run_name"] = args.run_name
    if getattr(args, "strategy", ""):
        o.setdefault("strategy", {})["name"] = args.strategy
    if getattr(args, "stop_loss", -1.0) is not None and getattr(args, "stop_loss", -1.0) >= 0:
        o.setdefault("risk", {})["investment_sl_pct"] = float(args.stop_loss)
    if getattr(args, "grid", ""):
        o.setdefault("optimize", {})["grid"] = args.grid
    if getattr(args, "deals_from", ""):
        o["deals_from"] = args.deals_from
    if getattr(args, "deals_to", ""):
        o["deals_to"] = args.deals_to
    return o


def _cfg(args: argparse.Namespace) -> dict[str, Any]:
    path = getattr(args, "config", "") or None
    return load_config(path, overrides=_overrides(args))


def cmd_backtest(args: argparse.Namespace) -> int:
    from qtb.runner import run_backtest_job

    cfg = _cfg(args)
    cfg["mode"] = "backtest"
    result, written = run_backtest_job(cfg)
    print(json.dumps({"metrics": result.metrics, "artifacts": written}, indent=2, ensure_ascii=False, default=str))
    print(f"\nsummary: {written.get('summary')}")
    return 0


def cmd_optimize(args: argparse.Namespace) -> int:
    from qtb.runner import run_optimize_job

    cfg = _cfg(args)
    result, opt, written = run_optimize_job(cfg)
    best = opt.get("best") or {}
    print(
        json.dumps(
            {
                "n_combos": opt.get("n_combos"),
                "best_params": best.get("params"),
                "best_score": best.get("score"),
                "metrics": result.metrics,
                "anti_overfit": {
                    "train_test": (opt.get("anti_overfit") or {}).get("train_test"),
                    "monte_carlo": (opt.get("anti_overfit") or {}).get("monte_carlo"),
                },
                "artifacts": written,
            },
            indent=2,
            ensure_ascii=False,
            default=str,
        )
    )
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    from qtb.runner import run_backtest_job, run_report_job

    if args.run_dir:
        info = run_report_job(args.run_dir)
        print(json.dumps(info, indent=2, ensure_ascii=False))
        summary = Path(info["summary"]) if "summary" in info else None
        if summary and summary.exists():
            print(summary.read_text(encoding="utf-8"))
        return 0
    cfg = _cfg(args)
    result, written = run_backtest_job(cfg)
    print(Path(written["summary"]).read_text(encoding="utf-8"))
    return 0


def cmd_batch(args: argparse.Namespace) -> int:
    from qtb.runner import run_batch_job

    cfg = _cfg(args)
    reports = run_batch_job(cfg)
    slim = [
        {"symbol": r["symbol"], "interval": r["interval"], "metrics": r["metrics"], "artifacts": r["artifacts"]}
        for r in reports
    ]
    print(json.dumps(slim, indent=2, ensure_ascii=False, default=str))
    return 0


def cmd_screen(args: argparse.Namespace) -> int:
    from qtb.screen import execute_screen

    return execute_screen(args)


def cmd_fetch_etf(args: argparse.Namespace) -> int:
    from qtb.data.gatedata import (
        DEFAULT_ETF_LONGS,
        default_deals_window,
        download_spot_deals,
        resolve_etf_markets,
    )

    if args.longs_only:
        markets = list(DEFAULT_ETF_LONGS)
    else:
        markets = resolve_etf_markets(args.underlyings)
    start = args.deals_from or ""
    end = args.deals_to or ""
    if not start or not end:
        d0, d1 = default_deals_window()
        start = start or d0
        end = end or d1
    root = Path(args.cache_dir) if args.cache_dir else None
    recs = download_spot_deals(markets, start, end, root=root)
    print(
        json.dumps(
            {
                "markets": markets,
                "from": start,
                "to": end,
                "ok": sum(1 for r in recs if r["status"] in {"ok", "skip"}),
                "missing": sum(1 for r in recs if r["status"] == "missing"),
                "records": recs,
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


def cmd_live(args: argparse.Namespace) -> int:
    cfg = _cfg(args)
    broker = LiveBroker(config=cfg)
    print(
        json.dumps(
            {
                "dry_run": broker.dry_run,
                "forced": is_dry_run_forced(cfg),
                "mode": cfg.get("mode"),
                "note": (cfg.get("live") or {}).get("note"),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    if args.ping:
        rec = broker.send_order({"symbol": cfg.get("symbol"), "side": "buy", "size": 1})
        print(json.dumps(rec, indent=2, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {
        "backtest": cmd_backtest,
        "optimize": cmd_optimize,
        "report": cmd_report,
        "batch": cmd_batch,
        "live": cmd_live,
        "screen": cmd_screen,
        "batch-screen": cmd_screen,
        "fetch-etf": cmd_fetch_etf,
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
