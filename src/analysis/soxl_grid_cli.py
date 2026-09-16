"""Load a YAML grid spec, overlay CLI flags, run SOXL on real aggTrades."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Literal

import yaml

from qtb.data.binance_futures import fetch_binance_klines_range
from src.analysis.soxl_soxs_hedge import DayTradeCache
from src.analysis.user_moving_grid import run_user_hedge_pair, run_user_ls_pair

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "soxl-lab" / "params" / "run.yaml"
DEFAULT_OUT = ROOT / "soxl-lab" / "results" / "runs"

HedgeMode = Literal["flatten_survivor", "independent"]
RangeMode = Literal["usdt", "pct"]
FeePreset = Literal["base", "conservative"]
FillEngine = Literal["tick", "bar"]


@dataclass
class GridSpec:
    symbol: str = "SOXLUSDT"
    start: str = "2026-07-16"
    end: str = "2026-09-11"
    leverage: float = 5.0
    n_grids: int = 200
    capital_long: float = 5000.0
    capital_short: float = 5000.0
    range_mode: RangeMode = "usdt"
    range_usdt: float = 20.0
    range_pct: float = 0.20
    hedge: HedgeMode = "flatten_survivor"
    fee: FeePreset = "base"
    fills: FillEngine = "tick"
    tag: str = ""

    def folder_name(self) -> str:
        band = f"usdt{self.range_usdt:g}" if self.range_mode == "usdt" else f"pct{self.range_pct:g}"
        bits = [
            self.hedge.replace("_", "-"),
            band,
            f"lev{self.leverage:g}",
            f"g{self.n_grids}",
            f"L{self.capital_long:g}S{self.capital_short:g}",
            self.fills,
        ]
        if self.tag:
            bits.insert(0, self.tag)
        return "_".join(bits)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def spec_from_yaml(raw: dict[str, Any]) -> GridSpec:
    win = raw.get("window") or {}
    rng = raw.get("range") or {}
    return GridSpec(
        symbol=str(raw.get("symbol") or "SOXLUSDT"),
        start=str(win.get("start") or "2026-07-16"),
        end=str(win.get("end") or "2026-09-11"),
        leverage=float(raw.get("leverage") or 5),
        n_grids=int(raw.get("n_grids") or 200),
        capital_long=float(raw.get("capital_long") or raw.get("capital_per_side") or 5000),
        capital_short=float(raw.get("capital_short") or raw.get("capital_per_side") or 5000),
        range_mode=str(rng.get("mode") or "usdt"),  # type: ignore[arg-type]
        range_usdt=float(rng.get("usdt") or 20),
        range_pct=float(rng.get("pct") or 0.20),
        hedge=str(raw.get("hedge") or "flatten_survivor"),  # type: ignore[arg-type]
        fee=str(raw.get("fee") or "base"),  # type: ignore[arg-type]
        fills=str(raw.get("fills") or "tick"),  # type: ignore[arg-type]
        tag=str(raw.get("tag") or ""),
    )


def apply_cli(spec: GridSpec, ns: argparse.Namespace) -> GridSpec:
    d = asdict(spec)
    mapping = {
        "symbol": "symbol",
        "start": "start",
        "end": "end",
        "leverage": "leverage",
        "n_grids": "n_grids",
        "capital_long": "capital_long",
        "capital_short": "capital_short",
        "range_mode": "mode",
        "range_usdt": "range_usdt",
        "range_pct": "range_pct",
        "hedge": "hedge",
        "fee": "fee",
        "fills": "fills",
        "tag": "tag",
    }
    for field, flag in mapping.items():
        val = getattr(ns, flag, None)
        if val is not None:
            d[field] = val
    if ns.capital is not None:
        d["capital_long"] = ns.capital
        d["capital_short"] = ns.capital
    return GridSpec(**d)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="SOXL 逐笔移动网格。改 YAML 或用下面的参数覆盖后再跑。",
    )
    p.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="默认 soxl-lab/params/run.yaml")
    p.add_argument("--symbol", default=None)
    p.add_argument("--start", default=None, help="UTC 日 YYYY-MM-DD")
    p.add_argument("--end", default=None)
    p.add_argument("--leverage", type=float, default=None)
    p.add_argument("--n-grids", dest="n_grids", type=int, default=None)
    p.add_argument("--capital", type=float, default=None, help="多空各用这么多 U（同时改两边）")
    p.add_argument("--capital-long", dest="capital_long", type=float, default=None)
    p.add_argument("--capital-short", dest="capital_short", type=float, default=None)
    p.add_argument("--mode", choices=("usdt", "pct"), default=None, help="带宽：±N U 或 ±N%")
    p.add_argument("--range-usdt", dest="range_usdt", type=float, default=None, help="±U，mode=usdt 时生效")
    p.add_argument("--range-pct", dest="range_pct", type=float, default=None, help="±小数，0.2=20%")
    p.add_argument("--hedge", choices=("flatten_survivor", "independent"), default=None)
    p.add_argument("--fee", choices=("base", "conservative"), default=None)
    p.add_argument("--fills", choices=("tick", "bar"), default=None, help="结论用 tick；bar 只做快速试")
    p.add_argument("--tag", default=None, help="输出目录前缀")
    p.add_argument("--out", type=Path, default=None)
    return p


def _strip(rep: dict[str, Any], spec: GridSpec) -> dict[str, Any]:
    daily = rep["daily"]
    return {
        "spec": asdict(spec),
        "hedge_mode": rep.get("hedge_mode"),
        "pair_stopped": rep.get("pair_stopped"),
        "stop_bar": rep.get("stop_bar"),
        "return": rep["return"],
        "max_dd": rep["max_dd"],
        "end_equity": rep["end_equity"],
        "inventory_frac": rep["inventory_frac"],
        "net_qty_units": rep["net_qty_units"],
        "fills": rep["fills"],
        "turnover": rep["turnover"],
        "reanchors": rep["reanchors"],
        "liquidated_long": rep.get("liquidated_long"),
        "liquidated_short": rep.get("liquidated_short"),
        "long": {k: v for k, v in (rep.get("long") or {}).items() if k != "equity"},
        "short": {k: v for k, v in (rep.get("short") or {}).items() if k != "equity"},
        "n_days": int(len(daily)),
        "best_day": float(daily["daily_pnl"].max()) if len(daily) else None,
        "worst_day": float(daily["daily_pnl"].min()) if len(daily) else None,
        "mean_day": float(daily["daily_pnl"].mean()) if len(daily) else None,
        "win_days": int((daily["daily_pnl"] > 0).sum()) if len(daily) else 0,
        "zero_days": int((daily["daily_pnl"] == 0).sum()) if len(daily) else 0,
    }


def run_spec(spec: GridSpec, *, out_root: Path) -> Path:
    if spec.range_mode not in ("usdt", "pct"):
        raise ValueError(f"bad range_mode {spec.range_mode}")
    bars = fetch_binance_klines_range(spec.symbol, "1h", spec.start, spec.end)
    bars = bars[["timestamp", "open", "high", "low", "close"]].copy()
    get_trades = None
    empty_hours = 0
    if spec.fills == "tick":
        cache = DayTradeCache(spec.symbol)

        def get_trades(i, ts):  # type: ignore[misc]
            nonlocal empty_hours
            df = cache.for_bar(ts)
            if df is None or df.empty:
                empty_hours += 1
            return df

    kw = dict(
        range_mode=spec.range_mode,
        capital_long=spec.capital_long,
        capital_short=spec.capital_short,
        leverage=spec.leverage,
        range_usdt=spec.range_usdt,
        range_pct=spec.range_pct,
        n_grids=spec.n_grids,
        fee_preset=spec.fee,
        fill_engine=spec.fills,
        get_trades=get_trades,
    )
    if spec.hedge == "independent":
        rep = run_user_ls_pair(bars, **kw)
    else:
        rep = run_user_hedge_pair(bars, **kw)

    dest = out_root / spec.folder_name()
    dest.mkdir(parents=True, exist_ok=True)
    daily = rep["daily"]
    daily.to_csv(dest / "daily.csv", index=False)
    summary = _strip(rep, spec)
    summary["generated"] = date.today().isoformat()
    summary["n_bars"] = int(len(bars))
    summary["empty_tick_hours"] = empty_hours
    (dest / "summary.json").write_text(json.dumps(summary, indent=2, default=str) + "\n", encoding="utf-8")
    (dest / "spec.json").write_text(json.dumps(asdict(spec), indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("return", "max_dd", "end_equity", "pair_stopped", "liquidated_long", "liquidated_short", "n_days", "win_days")}, indent=2))
    print(f"wrote {dest}")
    if empty_hours:
        print(f"warning: {empty_hours} hours had no cached ticks (cache_only)")
    return dest


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg_path = args.config if args.config.is_absolute() else (ROOT / args.config if not args.config.exists() else args.config)
    if not cfg_path.exists() and args.config == DEFAULT_CONFIG:
        spec = GridSpec()
    else:
        spec = spec_from_yaml(load_yaml(cfg_path))
    spec = apply_cli(spec, args)
    out_root = args.out or DEFAULT_OUT
    if not out_root.is_absolute():
        out_root = ROOT / out_root
    run_spec(spec, out_root=out_root)
    return 0
