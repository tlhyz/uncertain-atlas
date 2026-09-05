"""Reusable aggressive dual-hedge futures Martingale optimizer (any Gate contract)."""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone, timedelta
from itertools import product
from pathlib import Path
from typing import Any, Iterable, Literal

import pandas as pd

from fees import VIP7_FUTURES_75
from strategies.futures_martingale import FuturesMartingaleParams, FuturesMartingaleSimulator

ROOT = Path(__file__).resolve().parent
CST = timezone(timedelta(hours=8))

GridSize = Literal["compact", "medium", "full"]


def notional_factor(multiplier: float, max_adds: int) -> float:
    n = max_adds + 1
    if abs(multiplier - 1.0) < 1e-12:
        return float(n)
    return (multiplier**n - 1.0) / (multiplier - 1.0)


def gate_style_base(
    capital: float,
    leverage: float,
    multiplier: float,
    working_adds: int,
    fill_frac: float = 0.88,
) -> float:
    fac = notional_factor(multiplier, working_adds)
    base = (fill_frac * capital * leverage) / max(fac, 1e-9)
    return max(1.0, round(base, 4))


def frac_base(capital: float, leverage: float, frac: float) -> float:
    return max(1.0, round(capital * leverage * frac, 4))


def cashflow_score(s: dict) -> float:
    if s.get("liquidated"):
        return float(s.get("realized_cashflow", 0.0)) - 5000.0
    rc = float(s.get("realized_cashflow", 0.0))
    cycles = float(s.get("cycles", 0))
    util = float(s.get("capital_util", 0.0))
    return rc + 0.35 * cycles + 15.0 * min(util, 1.2)


def run_one(
    df: pd.DataFrame,
    direction: str,
    capital: float,
    leverage: float,
    mult: float,
    drop: float,
    tp: float,
    max_adds: int,
    base: float,
    sizing_tag: str,
    stop_loss_pct: float | None,
    fee_config=VIP7_FUTURES_75,
) -> dict[str, Any]:
    params = FuturesMartingaleParams(
        base_order_quote=base,
        multiplier=mult,
        add_drop_pct=drop,
        take_profit_pct=tp,
        max_adds=max_adds,
        initial_margin=capital,
        leverage=float(leverage),
        direction=direction,  # type: ignore[arg-type]
        fee_as_maker=False,
        stop_loss_pct=stop_loss_pct,
    )
    r = FuturesMartingaleSimulator(params, fee_config).run(df)
    s = r.summary()
    realized = float(r.stats.get("cycle_pnls_sum", 0.0))
    max_margin = float(r.stats.get("max_margin_used", 0.0))
    s["realized_cashflow"] = round(realized, 4)
    s["avg_cycle_pnl"] = round(float(r.stats.get("avg_cycle_pnl", 0.0)), 4)
    s["max_adds_hit"] = int(r.stats.get("max_adds_hit", 0))
    s["max_margin_used"] = round(max_margin, 2)
    s["capital_util"] = round(max_margin / max(capital, 1e-9), 4)
    s["open_qty"] = round(float(r.stats.get("open_position_qty", 0.0)), 6)
    s["avg_entry"] = round(float(r.stats.get("avg_entry", 0.0)), 6)
    s["stop_outs"] = int(r.stats.get("stop_outs", 0))
    s["stop_out_pnl_sum"] = round(float(r.stats.get("stop_out_pnl_sum", 0.0)), 4)
    s["params"] = {
        "direction": direction,
        "max_adds": max_adds,
        "multiplier": mult,
        "add_drop_pct": drop,
        "take_profit_pct": tp,
        "leverage": leverage,
        "base_order_quote": base,
        "initial_margin": capital,
        "sizing": sizing_tag,
        "stop_loss_pct": stop_loss_pct,
        "stop_loss_mode": "investment_drawdown" if stop_loss_pct else None,
    }
    s["cf_score"] = round(cashflow_score(s), 4)
    return s


def search_grids(grid: GridSize = "compact") -> dict[str, list]:
    """
    Parameter grids. compact finishes quickly; full matches prior niulai aggressive search.
    """
    if grid == "full":
        return {
            "max_adds": [20, 40, 60, 90],
            "multipliers": [1.2, 1.3, 1.4, 1.5, 1.8, 2.0],
            "drops": [0.008, 0.010, 0.012, 0.015, 0.018, 0.025, 0.040],
            "tps": [0.004, 0.006, 0.008, 0.010, 0.012],
            "working_adds": [8, 12, 16],
            "fracs": [0.02, 0.035, 0.05],
            "fixed_bases": [10.0, 15.0, 18.0, 25.0, 30.0, 40.0, 50.0],
        }
    if grid == "medium":
        return {
            "max_adds": [40, 60, 90],
            "multipliers": [1.3, 1.5, 1.8, 2.0],
            "drops": [0.010, 0.012, 0.015, 0.025],
            "tps": [0.006, 0.008, 0.010],
            "working_adds": [8, 12],
            "fracs": [0.02, 0.035],
            "fixed_bases": [15.0, 25.0, 40.0],
        }
    # compact — default for CLI (14d / multi-coin)
    return {
        "max_adds": [40, 90],
        "multipliers": [1.3, 1.5, 2.0],
        "drops": [0.010, 0.015, 0.025],
        "tps": [0.006, 0.010],
        "working_adds": [12],
        "fracs": [0.035],
        "fixed_bases": [20.0, 40.0],
    }


def estimate_combos(grid: GridSize = "compact") -> int:
    g = search_grids(grid)
    n = (
        len(g["max_adds"])
        * len(g["multipliers"])
        * len(g["drops"])
        * len(g["tps"])
    )
    # A + B + C sizing branches
    return n * (len(g["working_adds"]) + len(g["fracs"]) + len(g["fixed_bases"]))


def optimize_side(
    df: pd.DataFrame,
    direction: str,
    capital: float,
    leverage: float = 5.0,
    stop_loss_pct: float | None = 0.5,
    grid: GridSize = "compact",
    progress_every: int = 200,
) -> list[dict[str, Any]]:
    g = search_grids(grid)
    results: list[dict[str, Any]] = []
    t0 = time.time()

    combos_a = list(product(g["max_adds"], g["multipliers"], g["drops"], g["tps"], g["working_adds"]))
    for i, (max_adds, mult, drop, tp, wad) in enumerate(combos_a):
        base = gate_style_base(capital, leverage, mult, wad)
        results.append(
            run_one(df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"work_adds={wad}", stop_loss_pct)
        )
        if progress_every and (i + 1) % progress_every == 0:
            print(f"  [{direction}/A] {i+1}/{len(combos_a)} ({time.time()-t0:.1f}s)", flush=True)

    combos_b = list(product(g["max_adds"], g["multipliers"], g["drops"], g["tps"], g["fracs"]))
    for i, (max_adds, mult, drop, tp, frac) in enumerate(combos_b):
        base = frac_base(capital, leverage, frac)
        results.append(
            run_one(df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"bp_frac={frac}", stop_loss_pct)
        )
        if progress_every and (i + 1) % progress_every == 0:
            print(f"  [{direction}/B] {i+1}/{len(combos_b)} ({time.time()-t0:.1f}s)", flush=True)

    combos_c = list(product(g["max_adds"], g["multipliers"], g["drops"], g["tps"], g["fixed_bases"]))
    for i, (max_adds, mult, drop, tp, base) in enumerate(combos_c):
        results.append(
            run_one(df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"fixed_base={base}", stop_loss_pct)
        )
        if progress_every and (i + 1) % progress_every == 0:
            print(f"  [{direction}/C] {i+1}/{len(combos_c)} ({time.time()-t0:.1f}s)", flush=True)

    results.sort(key=lambda x: x["cf_score"], reverse=True)
    return results


def dual_score(long_s: dict, short_s: dict) -> float:
    liq_pen = 0.0
    if long_s.get("liquidated"):
        liq_pen += 2500.0
    if short_s.get("liquidated"):
        liq_pen += 2500.0
    rc = long_s["realized_cashflow"] + short_s["realized_cashflow"]
    cycles = long_s["cycles"] + short_s["cycles"]
    util = (long_s["capital_util"] + short_s["capital_util"]) / 2.0
    min_side = min(long_s["realized_cashflow"], short_s["realized_cashflow"])
    return rc + 0.30 * cycles + 20.0 * min(util, 1.2) + 0.15 * min_side - liq_pen


def pick_dual(long_res, short_res, top_n: int = 40):
    L = long_res[:top_n]
    S = short_res[:top_n]
    best = None
    best_sc = -1e18
    candidates = []

    for lo in L:
        for sh in S:
            sc = dual_score(lo, sh)
            row = {
                "dual_score": round(sc, 4),
                "combined_realized_cashflow": round(lo["realized_cashflow"] + sh["realized_cashflow"], 4),
                "combined_net_pnl": round(lo["net_pnl"] + sh["net_pnl"], 4),
                "combined_cycles": lo["cycles"] + sh["cycles"],
                "combined_stop_outs": lo["stop_outs"] + sh["stop_outs"],
                "combined_max_dd_proxy": round(lo["max_drawdown"] + sh["max_drawdown"], 4),
                "long_max_dd": lo["max_drawdown"],
                "short_max_dd": sh["max_drawdown"],
                "long_liq": lo["liquidated"],
                "short_liq": sh["liquidated"],
                "long_stop_outs": lo["stop_outs"],
                "short_stop_outs": sh["stop_outs"],
                "avg_capital_util": round((lo["capital_util"] + sh["capital_util"]) / 2, 4),
                "mode": "asymmetric",
                "long": lo,
                "short": sh,
            }
            candidates.append(row)
            if sc > best_sc:
                best_sc = sc
                best = row

    def pkey(s):
        p = s["params"]
        return (p["multiplier"], p["add_drop_pct"], p["take_profit_pct"], p["max_adds"], p["sizing"])

    short_by = {}
    for sh in short_res[:200]:
        short_by.setdefault(pkey(sh), sh)
    for lo in long_res[:200]:
        k = pkey(lo)
        if k in short_by:
            sh = short_by[k]
            sc = dual_score(lo, sh)
            row = {
                "dual_score": round(sc, 4),
                "combined_realized_cashflow": round(lo["realized_cashflow"] + sh["realized_cashflow"], 4),
                "combined_net_pnl": round(lo["net_pnl"] + sh["net_pnl"], 4),
                "combined_cycles": lo["cycles"] + sh["cycles"],
                "combined_stop_outs": lo["stop_outs"] + sh["stop_outs"],
                "combined_max_dd_proxy": round(lo["max_drawdown"] + sh["max_drawdown"], 4),
                "long_max_dd": lo["max_drawdown"],
                "short_max_dd": sh["max_drawdown"],
                "long_liq": lo["liquidated"],
                "short_liq": sh["liquidated"],
                "long_stop_outs": lo["stop_outs"],
                "short_stop_outs": sh["stop_outs"],
                "avg_capital_util": round((lo["capital_util"] + sh["capital_util"]) / 2, 4),
                "mode": "shared_params",
                "long": lo,
                "short": sh,
            }
            candidates.append(row)
            if sc > best_sc:
                best_sc = sc
                best = row

    candidates.sort(key=lambda x: x["dual_score"], reverse=True)
    alive = [c for c in candidates if not c["long_liq"] and not c["short_liq"]]
    if alive:
        best_alive = alive[0]
        if best and (best["long_liq"] or best["short_liq"]):
            return best_alive, candidates[:25], best
        return best_alive, candidates[:25], best
    return best, candidates[:25], best


def with_buf90(df, side_s, stop_loss_pct: float | None):
    p = side_s["params"]
    if p["max_adds"] >= 90:
        return side_s
    return run_one(
        df,
        p["direction"],
        p["initial_margin"],
        p["leverage"],
        p["multiplier"],
        p["add_drop_pct"],
        p["take_profit_pct"],
        90,
        p["base_order_quote"],
        p["sizing"] + "|buf90",
        stop_loss_pct,
    )


def demo_fixed(
    df: pd.DataFrame,
    stop_loss_pct: float | None = 0.7,
    long_cap: float = 950.0,
    short_cap: float = 1380.0,
    leverage: float = 5.0,
    mult: float = 1.5,
    drop: float = 0.012,
    tp: float = 0.006,
    max_adds: int = 90,
) -> dict[str, Any]:
    """Single fixed-param dual run (fast demo)."""
    lo = run_one(
        df, "long", long_cap, leverage, mult, drop, tp, max_adds,
        gate_style_base(long_cap, leverage, mult, 12), "demo_work12", stop_loss_pct,
    )
    sh = run_one(
        df, "short", short_cap, leverage, mult, drop, tp, max_adds,
        gate_style_base(short_cap, leverage, mult, 12), "demo_work12", stop_loss_pct,
    )
    return {
        "dual_score": round(dual_score(lo, sh), 4),
        "combined_realized_cashflow": round(lo["realized_cashflow"] + sh["realized_cashflow"], 4),
        "combined_net_pnl": round(lo["net_pnl"] + sh["net_pnl"], 4),
        "combined_cycles": lo["cycles"] + sh["cycles"],
        "combined_stop_outs": lo["stop_outs"] + sh["stop_outs"],
        "combined_max_dd_proxy": round(lo["max_drawdown"] + sh["max_drawdown"], 4),
        "long_liq": lo["liquidated"],
        "short_liq": sh["liquidated"],
        "mode": "fixed_demo",
        "long": lo,
        "short": sh,
    }


def _safe_tag(symbol: str) -> str:
    return "".join(ch if (ch.isalnum() or ch in "_-") else "_" for ch in symbol)


def write_brief_report(payload: dict, path: Path) -> None:
    m = payload["meta"]
    dual = payload["best_dual"]
    lo, sh = dual["long"], dual["short"]
    sl = m.get("stop_loss", {})
    sl_pct = sl.get("pct")
    now_cst = datetime.now(CST).strftime("%Y-%m-%d %H:%M CST")
    lines = [
        f"# {m['symbol']} 激进双开马丁优化报告",
        "",
        f"> 生成时间（UTC+8）：{now_cst} | 研究回测，非投资建议，无实盘下单。",
        "",
        "## 风格",
        "",
        "- 双开 LONG + SHORT；小仓深 max_adds；高换手现金流打分",
        f"- 止损 stop_loss_pct={sl_pct}（投资额回撤：uPnL/initial_margin ≤ -SL → 平仓后开新周期）",
        f"- 费率：VIP7 期货 + 75% 返佣 → Maker {m['fee_model']['eff_maker']} / Taker {m['fee_model']['eff_taker']}",
        f"- 搜索网格：`{m.get('grid')}`（每侧约 {m.get('combos_per_side')} 组）",
        "",
        "## 数据",
        "",
        f"- 合约 `{m['symbol']}` | {m['interval']} | ~{m['days_requested']}d | bars={m['bars']}",
        f"- {m['start']} → {m['end']} | close {m['start_close']} → {m['end_close']}",
        f"- 来源 `{m['source']}` | api_calls={m.get('api_calls')}",
        "",
        "## 最优双开（Gate 填写参考）",
        "",
        f"mode=`{dual['mode']}` dual_score={dual['dual_score']} cashflow={dual['combined_realized_cashflow']} "
        f"cycles={dual['combined_cycles']} stop_outs={dual.get('combined_stop_outs')}",
        "",
        "### LONG",
        "",
        "| 字段 | 值 |",
        "|---|---|",
    ]
    lp = lo["params"]
    for k, label in (
        ("initial_margin", "投资额"),
        ("leverage", "杠杆"),
        ("multiplier", "加仓倍数"),
        ("add_drop_pct", "跌多少加仓"),
        ("take_profit_pct", "止盈"),
        ("max_adds", "最大加仓"),
        ("base_order_quote", "首单名义"),
        ("stop_loss_pct", "止损(投资额%)"),
    ):
        v = lp[k]
        if isinstance(v, float) and k.endswith("pct") and v is not None:
            v = f"{v*100:.2f}%"
        lines.append(f"| {label} | **{v}** |")
    lines += ["", "### SHORT", "", "| 字段 | 值 |", "|---|---|"]
    sp = sh["params"]
    for k, label in (
        ("initial_margin", "投资额"),
        ("leverage", "杠杆"),
        ("multiplier", "加仓倍数"),
        ("add_drop_pct", "涨多少加仓"),
        ("take_profit_pct", "止盈"),
        ("max_adds", "最大加仓"),
        ("base_order_quote", "首单名义"),
        ("stop_loss_pct", "止损(投资额%)"),
    ):
        v = sp[k]
        if isinstance(v, float) and k.endswith("pct") and v is not None:
            v = f"{v*100:.2f}%"
        lines.append(f"| {label} | **{v}** |")
    lines += [
        "",
        "## 回测事实",
        "",
        "| 指标 | LONG | SHORT | 合计 |",
        "|---|---:|---:|---:|",
        f"| cashflow | {lo['realized_cashflow']} | {sh['realized_cashflow']} | **{dual['combined_realized_cashflow']}** |",
        f"| net_pnl | {lo['net_pnl']} | {sh['net_pnl']} | **{dual['combined_net_pnl']}** |",
        f"| cycles | {lo['cycles']} | {sh['cycles']} | **{dual['combined_cycles']}** |",
        f"| stop_outs | {lo['stop_outs']} | {sh['stop_outs']} | **{dual.get('combined_stop_outs')}** |",
        f"| maxDD | {lo['max_drawdown']} | {sh['max_drawdown']} | {dual['combined_max_dd_proxy']} |",
        f"| liquidated | {lo['liquidated']} | {sh['liquidated']} | — |",
        "",
        "## 风险提示",
        "",
        "- 回测 ≠ 实盘；未计入资金费/滑点；无下单、无 API Key。",
        "- Gate UI 止损若为「相对均价价格%」，与本回测投资额回撤止损不等价。",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def run_aggressive_dual(
    df: pd.DataFrame,
    symbol: str,
    stop_loss: float = 0.5,
    long_cap: float = 950.0,
    short_cap: float = 1380.0,
    leverage: float = 5.0,
    grid: GridSize = "compact",
    days: int = 14,
    interval: str = "5m",
    out_prefix: str | None = None,
    buf90: bool = True,
) -> dict[str, Any]:
    """
    Full optimize pipeline for any futures contract.
    Default grid=compact so `cli.py optimize --days 14` finishes in reasonable time.
    Use --grid full for the heavy niulai-style search.
    """
    combos = estimate_combos(grid)
    print(
        f"Optimize {symbol} SL={stop_loss} grid={grid} (~{combos} combos/side) "
        f"LONG@{long_cap} SHORT@{short_cap} lev={leverage}x"
    )
    if grid == "full":
        print(
            "NOTE: --grid full is heavy (≈10k+ sims/side). "
            "Prefer --grid compact|medium unless you need the full sweep."
        )

    t0 = time.time()
    long_res = optimize_side(df, "long", long_cap, leverage, stop_loss, grid=grid)
    print(f"LONG top cf={long_res[0]['cf_score']} cashflow={long_res[0]['realized_cashflow']}")
    short_res = optimize_side(df, "short", short_cap, leverage, stop_loss, grid=grid)
    print(f"SHORT top cf={short_res[0]['cf_score']} cashflow={short_res[0]['realized_cashflow']}")

    best_dual, top_duals, raw_best = pick_dual(long_res, short_res, top_n=40)
    present = dict(best_dual)
    if buf90:
        mir_long = with_buf90(df, best_dual["long"], stop_loss)
        mir_short = with_buf90(df, best_dual["short"], stop_loss)
        present = {
            "dual_score": round(dual_score(mir_long, mir_short), 4),
            "combined_realized_cashflow": round(
                mir_long["realized_cashflow"] + mir_short["realized_cashflow"], 4
            ),
            "combined_net_pnl": round(mir_long["net_pnl"] + mir_short["net_pnl"], 4),
            "combined_cycles": mir_long["cycles"] + mir_short["cycles"],
            "combined_stop_outs": mir_long["stop_outs"] + mir_short["stop_outs"],
            "combined_max_dd_proxy": round(mir_long["max_drawdown"] + mir_short["max_drawdown"], 4),
            "long_max_dd": mir_long["max_drawdown"],
            "short_max_dd": mir_short["max_drawdown"],
            "long_liq": mir_long["liquidated"],
            "short_liq": mir_short["liquidated"],
            "long_stop_outs": mir_long["stop_outs"],
            "short_stop_outs": mir_short["stop_outs"],
            "avg_capital_util": round((mir_long["capital_util"] + mir_short["capital_util"]) / 2, 4),
            "mode": f"{best_dual['mode']}_aggressive_dual_sl{int(stop_loss*100)}_buf90",
            "long": mir_long,
            "short": mir_short,
            "search_best_before_buf90": {
                "dual_score": best_dual["dual_score"],
                "long_params": best_dual["long"]["params"],
                "short_params": best_dual["short"]["params"],
            },
        }

    elapsed = round(time.time() - t0, 2)
    tag = _safe_tag(symbol)
    sl_tag = f"sl{int(round(stop_loss * 100))}" if stop_loss else "nosl"
    prefix = out_prefix or str(ROOT / f"opt_{tag}_{sl_tag}")
    out_json = Path(f"{prefix}_results.json")
    out_md = Path(f"{prefix}_report.md")

    payload = {
        "meta": {
            "symbol": symbol,
            "interval": interval,
            "days_requested": days,
            "bars": len(df),
            "start": str(df["timestamp"].iloc[0]),
            "end": str(df["timestamp"].iloc[-1]),
            "start_close": float(df["close"].iloc[0]),
            "end_close": float(df["close"].iloc[-1]),
            "source": df.attrs.get("source"),
            "api_calls": df.attrs.get("api_calls"),
            "style": "aggressive_dual_hedge",
            "grid": grid,
            "combos_per_side": combos,
            "elapsed_sec": elapsed,
            "stop_loss": {
                "pct": stop_loss,
                "mode": "investment_drawdown",
                "rule": "uPnL/initial_margin <= -stop_loss_pct → close cycle → new cycle",
            },
            "fee_model": {
                "maker_base": VIP7_FUTURES_75.maker_rate,
                "taker_base": VIP7_FUTURES_75.taker_rate,
                "rebate": VIP7_FUTURES_75.rebate_rate,
                "eff_maker": VIP7_FUTURES_75.effective_maker,
                "eff_taker": VIP7_FUTURES_75.effective_taker,
                "funding": "omitted",
            },
            "long_capital": long_cap,
            "short_capital": short_cap,
            "leverage_fixed": leverage,
            "long_combos": len(long_res),
            "short_combos": len(short_res),
        },
        "best_dual": present,
        "top_duals": [
            {
                "dual_score": c["dual_score"],
                "combined_realized_cashflow": c["combined_realized_cashflow"],
                "combined_cycles": c["combined_cycles"],
                "combined_stop_outs": c.get("combined_stop_outs"),
                "mode": c["mode"],
                "long_liq": c["long_liq"],
                "short_liq": c["short_liq"],
                "long_params": c["long"]["params"],
                "short_params": c["short"]["params"],
            }
            for c in top_duals[:15]
        ],
        "top_long": long_res[:10],
        "top_short": short_res[:10],
        "raw_best_maybe_liq": {
            "dual_score": raw_best["dual_score"] if raw_best else None,
            "long_liq": raw_best["long_liq"] if raw_best else None,
            "short_liq": raw_best["short_liq"] if raw_best else None,
        },
    }
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    write_brief_report(payload, out_md)
    print(f"Wrote {out_json}")
    print(f"Wrote {out_md}")
    print(
        f"Done in {elapsed}s | dual_score={present['dual_score']} "
        f"cashflow={present['combined_realized_cashflow']} cycles={present['combined_cycles']}"
    )
    return payload
