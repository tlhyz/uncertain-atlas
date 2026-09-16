"""Load a YAML grid spec, overlay CLI flags, run SOXL on real aggTrades."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, fields
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Literal

import pandas as pd
import yaml

from qtb.data.binance_futures import (
    fetch_agg_trades_day,
    fetch_binance_klines_range,
    list_cached_trade_days,
    list_klines_cache_ranges,
    missing_trade_days,
)
from src.analysis.soxl_soxs_hedge import DayTradeCache
from src.analysis.user_moving_grid import run_user_hedge_pair, run_user_ls_pair, run_user_one_side

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = ROOT / "soxl-lab" / "params" / "run.yaml"
DEFAULT_OUT = ROOT / "soxl-lab" / "results" / "runs"

HedgeMode = Literal["flatten_survivor", "independent"]
RangeMode = Literal["usdt", "pct"]
FeePreset = Literal["base", "conservative"]
FillEngine = Literal["tick", "bar"]
Sides = Literal["both", "long", "short"]

EPILOG = """
例子：
  python3 soxl-lab/scripts/run_grid.py --list-cache
  python3 soxl-lab/scripts/run_grid.py --check
  python3 soxl-lab/scripts/run_grid.py
  python3 soxl-lab/scripts/run_grid.py --leverage 3 --n-grids 80 --range-usdt 15
  python3 soxl-lab/scripts/run_grid.py --mode pct --range-pct 0.10 --hedge independent --start 2026-08-01 --end 2026-08-31 --tag aug
  python3 soxl-lab/scripts/run_grid.py --fills bar --start 2026-07-16 --end 2026-07-18
  python3 soxl-lab/scripts/run_grid.py --sides long --fills bar --start 2026-07-16 --end 2026-07-18

逐笔 CSV 故意不进 git（大约 3 GB，本机 cache/）。改参数前先 --list-cache / --check。
"""


def _coalesce(*vals: Any, default: Any = None) -> Any:
    for v in vals:
        if v is not None:
            return v
    return default


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
    sides: Sides = "both"
    tag: str = ""

    def folder_name(self) -> str:
        band = f"usdt{self.range_usdt:g}" if self.range_mode == "usdt" else f"pct{self.range_pct:g}"
        win = f"{self.start.replace('-', '')}-{self.end.replace('-', '')}"
        book = self.hedge.replace("_", "-") if self.sides == "both" else f"{self.sides}-only"
        bits = [
            book,
            band,
            f"lev{self.leverage:g}",
            f"g{self.n_grids}",
            f"L{self.capital_long:g}S{self.capital_short:g}",
            self.fills,
            win,
        ]
        if self.tag:
            bits.insert(0, self.tag)
        return "_".join(bits)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def spec_from_yaml(raw: dict[str, Any]) -> GridSpec:
    """Accept run.yaml and the 01_yours_moving_grid.yaml draft schema."""
    win = raw.get("window") if isinstance(raw.get("window"), dict) else {}
    rng = raw.get("range") if isinstance(raw.get("range"), dict) else {}
    range_modes = raw.get("range_modes") if isinstance(raw.get("range_modes"), dict) else {}
    usdt_blk = range_modes.get("usdt") if isinstance(range_modes.get("usdt"), dict) else {}
    pct_blk = range_modes.get("pct") if isinstance(range_modes.get("pct"), dict) else {}
    sides_blk = raw.get("sides")

    capital_per = _coalesce(raw.get("capital_per_side"), raw.get("capital_per_side_usdt"))
    cap_l = _coalesce(raw.get("capital_long"), capital_per, 5000)
    cap_s = _coalesce(raw.get("capital_short"), capital_per, 5000)
    sides: Sides = "both"
    if isinstance(sides_blk, dict):
        cap_l = _coalesce(raw.get("capital_long"), sides_blk.get("long"), capital_per, 5000)
        cap_s = _coalesce(raw.get("capital_short"), sides_blk.get("short"), capital_per, 5000)
    elif isinstance(sides_blk, str) and sides_blk in ("both", "long", "short"):
        sides = sides_blk  # type: ignore[assignment]
    elif isinstance(raw.get("side"), str) and raw["side"] in ("both", "long", "short"):
        sides = raw["side"]

    start = _coalesce(win.get("start"), raw.get("start"), "2026-07-16")
    end = _coalesce(win.get("end"), raw.get("end"), "2026-09-11")
    return GridSpec(
        symbol=str(_coalesce(raw.get("symbol"), "SOXLUSDT")),
        start=str(start),
        end=str(end),
        leverage=float(_coalesce(raw.get("leverage"), 5)),
        n_grids=int(_coalesce(raw.get("n_grids"), 200)),
        capital_long=float(cap_l),
        capital_short=float(cap_s),
        range_mode=str(_coalesce(rng.get("mode"), raw.get("range_mode"), "usdt")),  # type: ignore[arg-type]
        range_usdt=float(_coalesce(rng.get("usdt"), usdt_blk.get("range_usdt"), 20)),
        range_pct=float(_coalesce(rng.get("pct"), pct_blk.get("range_pct"), 0.20)),
        hedge=str(_coalesce(raw.get("hedge"), "flatten_survivor")),  # type: ignore[arg-type]
        fee=_normalize_fee(raw.get("fee")),
        fills=_normalize_fills(raw.get("fills")),
        sides=sides,
        tag=str(_coalesce(raw.get("tag"), "")),
    )


def _normalize_fills(raw: Any) -> FillEngine:
    if raw is None:
        return "tick"
    if isinstance(raw, dict):
        raw = raw.get("engine") or raw.get("mode") or "tick"
    s = str(raw).strip().lower()
    if s in ("tick", "tick_precise", "tick_precise_aggtrades", "aggtrades"):
        return "tick"
    if s in ("bar", "bar_ohlc", "ohlc"):
        return "bar"
    return s  # type: ignore[return-value]


def _normalize_fee(raw: Any) -> FeePreset:
    if raw is None:
        return "base"
    if isinstance(raw, dict):
        # 01_yours draft lists both bps; runner default stays Base.
        return "base"
    s = str(raw).strip().lower()
    if s in ("base", "2bps", "2"):
        return "base"
    if s in ("conservative", "4bps", "4"):
        return "conservative"
    return s  # type: ignore[return-value]


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
        "sides": "sides",
        "tag": "tag",
    }
    for field, flag in mapping.items():
        val = getattr(ns, flag, None)
        if val is not None:
            d[field] = val
    if getattr(ns, "capital", None) is not None:
        d["capital_long"] = ns.capital
        d["capital_short"] = ns.capital
    allowed = {f.name for f in fields(GridSpec)}
    return GridSpec(**{k: v for k, v in d.items() if k in allowed})


def validate_spec(spec: GridSpec) -> list[str]:
    errs: list[str] = []
    if spec.leverage <= 0:
        errs.append("leverage 必须 > 0")
    if spec.n_grids < 2:
        errs.append("n_grids 必须 >= 2")
    if spec.capital_long < 0 or spec.capital_short < 0:
        errs.append("本金不能为负")
    if spec.sides == "both" and spec.capital_long <= 0 and spec.capital_short <= 0:
        errs.append("多空本金不能都为 0")
    if spec.sides == "long" and spec.capital_long <= 0:
        errs.append("只做多时 capital_long 必须 > 0")
    if spec.sides == "short" and spec.capital_short <= 0:
        errs.append("只做空时 capital_short 必须 > 0")
    if spec.range_mode not in ("usdt", "pct"):
        errs.append(f"range_mode 只能是 usdt/pct，收到 {spec.range_mode}")
    if spec.range_mode == "usdt" and spec.range_usdt <= 0:
        errs.append("mode=usdt 时 range_usdt 必须 > 0")
    if spec.range_mode == "pct" and spec.range_pct <= 0:
        errs.append("mode=pct 时 range_pct 必须 > 0")
    if spec.hedge not in ("flatten_survivor", "independent"):
        errs.append(f"hedge 只能是 flatten_survivor/independent，收到 {spec.hedge}")
    if spec.fee not in ("base", "conservative"):
        errs.append(f"fee 只能是 base/conservative，收到 {spec.fee}")
    if spec.fills not in ("tick", "bar"):
        errs.append(f"fills 只能是 tick/bar，收到 {spec.fills}")
    if spec.sides not in ("both", "long", "short"):
        errs.append(f"sides 只能是 both/long/short，收到 {spec.sides}")
    try:
        d0 = date.fromisoformat(spec.start)
        d1 = date.fromisoformat(spec.end)
    except ValueError:
        errs.append(f"日期格式必须 YYYY-MM-DD：{spec.start} / {spec.end}")
        return errs
    if d0 > d1:
        errs.append(f"start {spec.start} 晚于 end {spec.end}")
    return errs


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="SOXL 逐笔移动网格。改 YAML 或用下面的参数覆盖后再跑。",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--config", type=Path, default=None, help="默认 soxl-lab/params/run.yaml；也认 01_yours_moving_grid.yaml")
    p.add_argument("--symbol", default=None)
    p.add_argument("--start", default=None, help="UTC 日 YYYY-MM-DD")
    p.add_argument("--end", default=None)
    p.add_argument("--leverage", type=float, default=None)
    p.add_argument("--n-grids", dest="n_grids", type=int, default=None)
    p.add_argument("--capital", type=float, default=None, help="多空各用这么多 U（同时改两边）")
    p.add_argument("--capital-long", dest="capital_long", type=float, default=None)
    p.add_argument("--capital-short", dest="capital_short", type=float, default=None)
    p.add_argument("--mode", choices=("usdt", "pct"), default=None, help="带宽：±N U 或 ±N%%")
    p.add_argument("--range-usdt", dest="range_usdt", type=float, default=None, help="±U，mode=usdt 时生效")
    p.add_argument("--range-pct", dest="range_pct", type=float, default=None, help="±小数，0.2=20%%")
    p.add_argument("--hedge", choices=("flatten_survivor", "independent"), default=None)
    p.add_argument("--sides", choices=("both", "long", "short"), default=None, help="默认 both=多空；可只跑一边")
    p.add_argument("--fee", choices=("base", "conservative"), default=None)
    p.add_argument("--fills", choices=("tick", "bar"), default=None, help="结论用 tick；bar 只做快速试")
    p.add_argument("--tag", default=None, help="输出目录前缀")
    p.add_argument("--out", type=Path, default=None)
    p.add_argument("--list-cache", action="store_true", help="只看本机逐笔/K线覆盖，不跑回测")
    p.add_argument("--check", action="store_true", help="打印参数 + 窗口缺不缺逐笔，不跑回测")
    p.add_argument("--allow-empty-ticks", action="store_true", help="缺天也继续跑（默认 tick 模式缺天直接拒绝）")
    p.add_argument("--bars-from-ticks", action="store_true", help="1h OHLC 一律从逐笔重采样，不用 K 线缓存")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--json-only", action="store_true", help="只打 summary JSON")
    p.add_argument("--progress-every", dest="progress_every", type=int, default=24, help="隔多少根 1h 打一行进度，0=关")
    return p


def resolve_config(path: Path) -> Path:
    if path.is_absolute() and path.exists():
        return path
    for c in (path, Path.cwd() / path, ROOT / path):
        if c.exists():
            return c
    raise FileNotFoundError(f"找不到配置：{path}")


def cache_inventory(symbol: str) -> dict[str, Any]:
    days = list_cached_trade_days(symbol)
    klines = list_klines_cache_ranges(symbol, "1h")
    gaps: list[str] = []
    if days:
        d = days[0]
        have = set(days)
        while d <= days[-1]:
            if d not in have:
                gaps.append(d.isoformat())
            d += timedelta(days=1)
    return {
        "symbol": symbol,
        "tick_days": len(days),
        "tick_start": days[0].isoformat() if days else None,
        "tick_end": days[-1].isoformat() if days else None,
        "tick_gaps": gaps,
        "klines_1h": [{"start": a.isoformat(), "end": b.isoformat()} for a, b in klines],
    }


def window_missing_ticks(spec: GridSpec) -> list[str]:
    d0 = date.fromisoformat(spec.start)
    d1 = date.fromisoformat(spec.end)
    return [d.isoformat() for d in missing_trade_days(spec.symbol, d0, d1)]


def ohlc_1h_from_cached_ticks(symbol: str, start: str, end: str) -> pd.DataFrame:
    t0 = date.fromisoformat(start)
    t1 = date.fromisoformat(end)
    parts: list[pd.DataFrame] = []
    d = t0
    while d <= t1:
        raw = fetch_agg_trades_day(symbol, d, cache_only=True)
        d += timedelta(days=1)
        if raw is None or raw.empty:
            continue
        s = raw.set_index(pd.to_datetime(raw["timestamp"], utc=True))["price"]
        bar = s.resample("1h").ohlc().dropna(how="any")
        if bar.empty:
            continue
        parts.append(bar)
    if not parts:
        raise RuntimeError(f"本机 cache 没有 {symbol} {start}→{end} 的逐笔，做不出 1h K 线")
    out = pd.concat(parts).sort_index()
    out = out[~out.index.duplicated(keep="last")].reset_index()
    out = out.rename(columns={out.columns[0]: "timestamp"})
    out.attrs["source"] = "aggTrades_resampled_1h"
    return out[["timestamp", "open", "high", "low", "close"]]


def load_bars(spec: GridSpec, *, from_ticks: bool) -> tuple[pd.DataFrame, str]:
    if from_ticks:
        bars = ohlc_1h_from_cached_ticks(spec.symbol, spec.start, spec.end)
        return bars, str(bars.attrs.get("source") or "aggTrades_resampled_1h")
    try:
        bars = fetch_binance_klines_range(spec.symbol, "1h", spec.start, spec.end, cache_only=True)
        return bars[["timestamp", "open", "high", "low", "close"]].copy(), str(
            bars.attrs.get("source") or "binance_vision_klines_cached"
        )
    except RuntimeError:
        bars = ohlc_1h_from_cached_ticks(spec.symbol, spec.start, spec.end)
        return bars, str(bars.attrs.get("source") or "aggTrades_resampled_1h")


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


def write_report_md(dest: Path, spec: GridSpec, summary: dict[str, Any], bar_source: str) -> None:
    hedge_cn = {
        "flatten_survivor": "移动多空对冲（一边爆仓就平另一边）",
        "moving_ls_flatten_survivor": "移动多空对冲（一边爆仓就平另一边）",
        "independent": "两本独立账（一边爆了另一边继续）",
        "one_side": "只做一边",
    }
    mode_cn = "±{:.4g} U".format(spec.range_usdt) if spec.range_mode == "usdt" else "±{:.4g}%".format(spec.range_pct * 100)
    stopped = ""
    if summary.get("pair_stopped"):
        stopped = (
            f"\n> **中途停机** stop_bar={summary.get('stop_bar')}。"
            "后面很多天 daily_pnl=0 不是对冲在赚钱，是空仓。\n"
        )
    lines = [
        f"# {spec.folder_name()}",
        "",
        *([stopped] if stopped else []),
        "| 项 | 值 |",
        "|----|----|",
        f"| 标的 | {spec.symbol} |",
        f"| 窗口 | {spec.start} → {spec.end} |",
        f"| 账本 | {hedge_cn.get(str(summary.get('hedge_mode') or spec.hedge), spec.hedge)} / sides={spec.sides} |",
        f"| 杠杆 | {spec.leverage:g}x 逐仓 |",
        f"| 格子 | {spec.n_grids} 等差 |",
        f"| 带宽 | {mode_cn} |",
        f"| 本金 | 多 {spec.capital_long:g} + 空 {spec.capital_short:g} |",
        f"| 成交 | {spec.fills} / fee={spec.fee} |",
        f"| K线来源 | {bar_source} |",
        f"| 收益 | {summary['return']:+.4%} |",
        f"| 回撤 | {summary['max_dd']:.4%} |",
        f"| 期末 | {summary['end_equity']:.2f} |",
        f"| 多头爆仓 | {summary.get('liquidated_long')} |",
        f"| 空头爆仓 | {summary.get('liquidated_short')} |",
        f"| 赢/平日 | {summary.get('win_days')} / {summary.get('zero_days')} （共 {summary.get('n_days')}） |",
        f"| 空小时 | {summary.get('empty_tick_hours')} |",
        "",
        "同目录：`spec.json` `summary.json` `daily.csv`。",
        "",
    ]
    (dest / "README.md").write_text("\n".join(lines), encoding="utf-8")


def print_cache(symbol: str, *, json_only: bool) -> int:
    inv = cache_inventory(symbol)
    if json_only:
        print(json.dumps(inv, indent=2, ensure_ascii=False))
        return 0 if inv["tick_days"] else 1
    if not inv["tick_days"]:
        print(f"{symbol} 本机 cache/ 没有逐笔 CSV。")
        return 1
    gap = f"缺口 {len(inv['tick_gaps'])} 天：{inv['tick_gaps'][:8]}" if inv["tick_gaps"] else "无缺口"
    print(f"{symbol} 逐笔：{inv['tick_start']} → {inv['tick_end']}  {inv['tick_days']} 天  {gap}")
    print("（CSV 只留本机 cache/，不进 git，大约 3 GB）")
    if inv["klines_1h"]:
        for r in inv["klines_1h"]:
            print(f"1h K线缓存：{r['start']} → {r['end']}")
    else:
        print("1h K线缓存：无（跑的时候会从逐笔重采样）")
    return 0


def print_check(spec: GridSpec, *, json_only: bool) -> int:
    errs = validate_spec(spec)
    miss = window_missing_ticks(spec) if not errs else []
    payload = {"spec": asdict(spec), "folder": spec.folder_name(), "errors": errs, "missing_tick_days": miss}
    if json_only:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(asdict(spec), indent=2, ensure_ascii=False))
        print(f"输出目录名：{spec.folder_name()}")
        if errs:
            print("参数错误：")
            for e in errs:
                print(f"  - {e}")
        elif miss and spec.fills == "tick":
            print(f"窗口缺逐笔 {len(miss)} 天（前几个）：{miss[:8]}")
            print("补齐 cache/ 或加 --allow-empty-ticks；默认拒绝开跑。")
        elif miss:
            print(f"fills=bar：窗口缺逐笔 {len(miss)} 天，这次还能跑，结论不要当 tick。")
        else:
            print(f"窗口 {spec.start}→{spec.end} 逐笔齐，可以跑。")
    if errs:
        return 2
    if miss and spec.fills == "tick":
        return 3
    return 0


def run_spec(
    spec: GridSpec,
    *,
    out_root: Path,
    allow_empty_ticks: bool = False,
    bars_from_ticks: bool = False,
    quiet: bool = False,
    json_only: bool = False,
    progress_every: int = 24,
) -> Path:
    errs = validate_spec(spec)
    if errs:
        raise ValueError("；".join(errs))
    miss = window_missing_ticks(spec) if spec.fills == "tick" else []
    if miss and spec.fills == "tick" and not allow_empty_ticks:
        raise FileNotFoundError(
            f"窗口缺逐笔 {len(miss)} 天（例如 {miss[:5]}）。先 --list-cache，或 --allow-empty-ticks。"
        )

    bars, bar_source = load_bars(spec, from_ticks=bars_from_ticks)
    if bars.empty:
        raise RuntimeError(f"没有 K 线：{spec.symbol} {spec.start}→{spec.end}")

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

    n_bars = int(len(bars))

    def on_bar(i: int, ts: pd.Timestamp, eq: float) -> None:
        if quiet or json_only or progress_every <= 0:
            return
        if i == 0 or (i + 1) % progress_every == 0 or i + 1 == n_bars:
            print(f"  {pd.Timestamp(ts).date()}  {i + 1}/{n_bars}  equity={eq:.2f}", flush=True)

    shared = dict(
        range_mode=spec.range_mode,
        leverage=spec.leverage,
        range_usdt=spec.range_usdt,
        range_pct=spec.range_pct,
        n_grids=spec.n_grids,
        fee_preset=spec.fee,
        fill_engine=spec.fills,
        get_trades=get_trades,
        on_bar=on_bar,
    )
    if spec.sides == "long":
        rep = run_user_one_side(bars, direction="long", capital=spec.capital_long, **shared)
    elif spec.sides == "short":
        rep = run_user_one_side(bars, direction="short", capital=spec.capital_short, **shared)
    elif spec.hedge == "independent":
        if not quiet and not json_only:
            print("independent：先跑多头整段，再跑空头整段（进度日期会走两遍）", flush=True)
        rep = run_user_ls_pair(bars, capital_long=spec.capital_long, capital_short=spec.capital_short, **shared)
    else:
        if spec.sides == "both" and not quiet and not json_only:
            print("flatten_survivor：同一条移动带，一边爆仓就平另一边", flush=True)
        rep = run_user_hedge_pair(bars, capital_long=spec.capital_long, capital_short=spec.capital_short, **shared)

    dest = out_root / spec.folder_name()
    dest.mkdir(parents=True, exist_ok=True)
    daily = rep["daily"]
    daily.to_csv(dest / "daily.csv", index=False)
    summary = _strip(rep, spec)
    summary["generated"] = date.today().isoformat()
    summary["n_bars"] = n_bars
    summary["empty_tick_hours"] = empty_hours
    summary["bar_source"] = bar_source
    (dest / "summary.json").write_text(json.dumps(summary, indent=2, default=str) + "\n", encoding="utf-8")
    (dest / "spec.json").write_text(json.dumps(asdict(spec), indent=2) + "\n", encoding="utf-8")
    write_report_md(dest, spec, summary, bar_source)
    headline = {k: summary[k] for k in ("return", "max_dd", "end_equity", "pair_stopped", "liquidated_long", "liquidated_short", "n_days", "win_days")}
    print(json.dumps(headline, indent=2, ensure_ascii=False))
    if not json_only:
        print(f"wrote {dest}")
        if empty_hours:
            print(f"warning: {empty_hours} hours had no cached ticks (cache_only)")
        if summary.get("pair_stopped"):
            print("warning: pair_stopped — 后面的零收益日是空仓，不是对冲还在干活")
    return dest


def load_spec(args: argparse.Namespace) -> GridSpec:
    if args.config is not None:
        spec = spec_from_yaml(load_yaml(resolve_config(args.config)))
    elif DEFAULT_CONFIG.exists():
        spec = spec_from_yaml(load_yaml(DEFAULT_CONFIG))
    else:
        spec = GridSpec()
    return apply_cli(spec, args)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.list_cache and args.config is None and args.start is None and args.end is None:
        if args.symbol:
            return print_cache(args.symbol, json_only=args.json_only)
        try:
            return print_cache(load_spec(args).symbol, json_only=args.json_only)
        except FileNotFoundError:
            return print_cache("SOXLUSDT", json_only=args.json_only)

    try:
        spec = load_spec(args)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 2

    if args.list_cache:
        return print_cache(spec.symbol, json_only=args.json_only)
    if args.check:
        return print_check(spec, json_only=args.json_only)

    out_root = args.out or DEFAULT_OUT
    if not out_root.is_absolute():
        out_root = ROOT / out_root
    try:
        run_spec(
            spec,
            out_root=out_root,
            allow_empty_ticks=args.allow_empty_ticks,
            bars_from_ticks=args.bars_from_ticks,
            quiet=args.quiet,
            json_only=args.json_only,
            progress_every=args.progress_every,
        )
    except (ValueError, FileNotFoundError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0
