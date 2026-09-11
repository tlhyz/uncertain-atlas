"""High-level run helpers used by the CLI."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from qtb.config import dump_yaml, load_config
from qtb.data.load import load_deals_market, load_market, wants_deals_feed
from qtb.engine.backtest import BacktestResult, run_backtest
from qtb.optimize.search import run_optimize
from qtb.report.artifacts import write_report


def resolve_output_dir(cfg: dict[str, Any], suffix: str = "backtest") -> Path:
    root = Path(cfg.get("output_dir") or "outputs")
    name = str(cfg.get("run_name") or "").strip()
    if not name:
        sym = str(cfg.get("symbol") or "SYM").replace("/", "_")
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        name = f"{suffix}_{sym}_{cfg.get('interval', '1h')}_{ts}"
    out = root / name
    out.mkdir(parents=True, exist_ok=True)
    return out


def run_backtest_job(cfg: dict[str, Any]) -> tuple[BacktestResult, dict[str, str]]:
    df = load_deals_market(cfg) if wants_deals_feed(cfg) else load_market(cfg)
    result = run_backtest(cfg, df)
    out = resolve_output_dir(cfg, "backtest")
    written = write_report(result, out, config=cfg)
    try:
        dump_yaml(cfg, out / "input.yaml")
    except Exception:
        pass
    return result, written


def run_optimize_job(cfg: dict[str, Any]) -> tuple[BacktestResult, dict[str, Any], dict[str, str]]:
    df = load_deals_market(cfg) if wants_deals_feed(cfg) else load_market(cfg)
    opt = run_optimize(cfg, df)
    best_params = ((opt.get("best") or {}).get("params")) or {}
    from copy import deepcopy

    best_cfg = deepcopy(cfg)
    best_cfg.setdefault("strategy", {}).update(best_params)
    result = run_backtest(best_cfg, df)
    out = resolve_output_dir(cfg, "optimize")
    written = write_report(result, out, optimize=opt, config=best_cfg)
    return result, opt, written


def run_report_job(run_dir: str | Path) -> dict[str, str]:
    """Re-emit summary from an existing run directory (metrics + trades)."""
    run_dir = Path(run_dir)
    metrics_path = run_dir / "metrics.json"
    trades_path = run_dir / "trades.csv"
    if not metrics_path.exists():
        raise FileNotFoundError(f"no metrics.json in {run_dir}")
    summary_src = run_dir / "summary.md"
    if summary_src.exists():
        return {"summary": str(summary_src), "metrics": str(metrics_path), "trades": str(trades_path)}
    return {"metrics": str(metrics_path), "trades": str(trades_path)}


def run_batch_job(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    from copy import deepcopy

    batch = cfg.get("batch") or {}
    symbols = list(batch.get("symbols") or [cfg.get("symbol") or "BTC_USDT"])
    intervals = list(batch.get("intervals") or [cfg.get("interval") or "1h"])
    reports: list[dict[str, Any]] = []
    for symbol in symbols:
        for interval in intervals:
            one = deepcopy(cfg)
            one["symbol"] = symbol
            one["interval"] = interval
            one["run_name"] = f"batch_{symbol}_{interval}".replace("/", "_")
            result, written = run_backtest_job(one)
            reports.append(
                {
                    "symbol": symbol,
                    "interval": interval,
                    "metrics": result.metrics,
                    "artifacts": written,
                }
            )
    # Combined table
    out = Path(cfg.get("output_dir") or "outputs") / "batch_index.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Batch report",
        "",
        "| symbol | interval | net_pnl | grid_harvest | inventory_mtm | max_dd_pct | halted | cycles |",
        "|---|---|---:|---:|---:|---:|---|---:|",
    ]
    for r in reports:
        m = r["metrics"]
        lines.append(
            f"| {r['symbol']} | {r['interval']} | {m.get('net_pnl')} | {m.get('grid_harvest')} | "
            f"{m.get('inventory_mtm')} | {m.get('max_dd_pct')} | {m.get('halted')} | {m.get('cycles')} |"
        )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return reports
