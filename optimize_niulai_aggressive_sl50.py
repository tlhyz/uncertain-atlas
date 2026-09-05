#!/usr/bin/env python3
"""Aggressive dual-hedge futures Martingale optimize for 牛来_USDT WITH stop_loss_pct=0.50."""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone, timedelta
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from data import fetch_gate_futures_candles
from fees import VIP7_FUTURES_75
from strategies.futures_martingale import FuturesMartingaleParams, FuturesMartingaleSimulator

OUT_JSON = ROOT / "opt_niulai_aggressive_sl50_results.json"
OUT_MD = ROOT / "opt_niulai_aggressive_sl50_report.md"
OUT_LOG = ROOT / "opt_niulai_aggressive_sl50_run.log"
CACHE_CSV = ROOT / "data_sample" / "niulai_USDT_5m_futures.csv"
PREV_JSON = ROOT / "opt_niulai_aggressive_results.json"
SL70_JSON = ROOT / "opt_niulai_aggressive_sl70_results.json"

CST = timezone(timedelta(hours=8))
STOP_LOSS_PCT = 0.50


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
    """Score WITHIN aggressive style: realized cashflow + turnover + util.
    Stop-outs / DD / liq are facts (liq still penalized for dual reliability).
    """
    if s.get("liquidated"):
        return s.get("realized_cashflow", 0.0) - 5000.0
    rc = float(s.get("realized_cashflow", 0.0))
    cycles = float(s.get("cycles", 0))
    util = float(s.get("capital_util", 0.0))
    return rc + 0.35 * cycles + 15.0 * min(util, 1.2)


def run_one(
    df,
    direction,
    capital,
    leverage,
    mult,
    drop,
    tp,
    max_adds,
    base,
    sizing_tag,
    stop_loss_pct: float | None = STOP_LOSS_PCT,
):
    params = FuturesMartingaleParams(
        base_order_quote=base,
        multiplier=mult,
        add_drop_pct=drop,
        take_profit_pct=tp,
        max_adds=max_adds,
        initial_margin=capital,
        leverage=float(leverage),
        direction=direction,
        fee_as_maker=False,
        stop_loss_pct=stop_loss_pct,
    )
    r = FuturesMartingaleSimulator(params, VIP7_FUTURES_75).run(df)
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


def optimize_side(df, direction: str, capital: float, leverage: float = 5.0):
    # Keep aggressive style; slightly leaner grid than full A×B to finish faster,
    # but still cover asymmetric dual search similar to prior run.
    max_adds_list = [20, 40, 60, 90]
    multipliers = [1.2, 1.3, 1.4, 1.5, 1.8, 2.0]
    drop_pcts = [0.008, 0.010, 0.012, 0.015, 0.018, 0.025, 0.040]
    tp_pcts = [0.004, 0.006, 0.008, 0.010, 0.012]
    working_adds_list = [8, 12, 16]
    fracs = [0.02, 0.035, 0.05]
    # Extra small fixed tickets (helps SHORT survive uptrend + SL)
    fixed_bases = [10.0, 15.0, 18.0, 25.0, 30.0, 40.0, 50.0]

    results = []
    t0 = time.time()
    combos_a = list(product(max_adds_list, multipliers, drop_pcts, tp_pcts, working_adds_list))
    for i, (max_adds, mult, drop, tp, wad) in enumerate(combos_a):
        base = gate_style_base(capital, leverage, mult, wad)
        s = run_one(
            df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"work_adds={wad}"
        )
        results.append(s)
        if (i + 1) % 600 == 0:
            print(f"  [{direction}/A] {i+1}/{len(combos_a)} ({time.time()-t0:.1f}s)", flush=True)

    combos_b = list(product(max_adds_list, multipliers, drop_pcts, tp_pcts, fracs))
    for i, (max_adds, mult, drop, tp, frac) in enumerate(combos_b):
        base = frac_base(capital, leverage, frac)
        s = run_one(
            df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"bp_frac={frac}"
        )
        results.append(s)
        if (i + 1) % 600 == 0:
            print(f"  [{direction}/B] {i+1}/{len(combos_b)} ({time.time()-t0:.1f}s)", flush=True)

    combos_c = list(product(max_adds_list, multipliers, drop_pcts, tp_pcts, fixed_bases))
    for i, (max_adds, mult, drop, tp, base) in enumerate(combos_c):
        s = run_one(
            df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"fixed_base={base}"
        )
        results.append(s)
        if (i + 1) % 800 == 0:
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
    balance_bonus = 0.15 * min_side
    return rc + 0.30 * cycles + 20.0 * min(util, 1.2) + balance_bonus - liq_pen


def pick_dual(long_res, short_res, top_n: int = 50):
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
                "combined_realized_cashflow": round(
                    lo["realized_cashflow"] + sh["realized_cashflow"], 4
                ),
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
    for sh in short_res[:250]:
        short_by.setdefault(pkey(sh), sh)
    for lo in long_res[:250]:
        k = pkey(lo)
        if k in short_by:
            sh = short_by[k]
            sc = dual_score(lo, sh)
            row = {
                "dual_score": round(sc, 4),
                "combined_realized_cashflow": round(
                    lo["realized_cashflow"] + sh["realized_cashflow"], 4
                ),
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


def screenshot_proxy(df, stop_loss_pct: float | None):
    out = {}
    for direction, cap in (("long", 950.0), ("short", 1383.0)):
        base = gate_style_base(cap, 5.0, 1.5, working_adds=12)
        out[direction] = run_one(
            df,
            direction,
            cap,
            5.0,
            1.5,
            0.012,
            0.006,
            90,
            base,
            "screenshot_proxy_work12",
            stop_loss_pct=stop_loss_pct,
        )
    alt = {}
    for direction, cap in (("long", 950.0), ("short", 1383.0)):
        base = frac_base(cap, 5.0, 0.035)
        alt[direction] = run_one(
            df,
            direction,
            cap,
            5.0,
            1.5,
            0.012,
            0.006,
            90,
            base,
            "screenshot_proxy_frac0.035",
            stop_loss_pct=stop_loss_pct,
        )
    return out, alt


def pct(x: float) -> str:
    return f"{x * 100:.4f}%"


def gate_equiv_price_sl(leverage: float, stop_loss_pct: float) -> float:
    """Rough Gate UI price-% equivalent when position notional ≈ IM*lev (full use)."""
    return stop_loss_pct / max(leverage, 1e-9)


def write_report(payload: dict) -> None:
    m = payload["meta"]
    dual = payload["best_dual"]
    lo, sh = dual["long"], dual["short"]
    shot = payload["screenshot_proxy_sl50"]
    prev = payload.get("compare_prev_no_sl") or {}
    now_cst = datetime.now(CST).strftime("%Y-%m-%d %H:%M CST")
    price_eq = gate_equiv_price_sl(5.0, STOP_LOSS_PCT)

    lines: list[str] = []
    lines.append("# 牛来_USDT 激进双开马丁优化报告（止损 SL50 / 用户风格）")
    lines.append("")
    lines.append(f"> 生成时间（UTC+8）：{now_cst} | 研究回测，非投资建议，无实盘下单。")
    lines.append("")
    lines.append("## 0. 风格对齐（已按你的打法优化，未改保守）")
    lines.append("")
    lines.append("本轮**严格按你的激进双开小仓风格**搜索与打分，**不**改成保守单边、**不**降杠杆、**不**推荐改现货：")
    lines.append("")
    lines.append("- **双开**：同币 LONG + SHORT 同时跑")
    lines.append("- **小仓**：LONG **950** / SHORT **1380**（合计约 **2330**，对齐截图）")
    lines.append("- **杠杆**：固定 **5x**")
    lines.append("- **深加仓缓冲**：Gate 填写 **max_adds=90**（回测实际触达可远低于 90，90 当缓冲额度）")
    lines.append("- **止损 SL50（本轮）**：见 §0.1")
    lines.append("- **高换手现金流**：紧止盈 + 风格内间距；打分看**已实现轮次利润 + 轮次 + 利用率**")
    lines.append("- **费率**：VIP7 期货 Maker 0.008% / Taker 0.02% + 75% 返佣 → 有效约 **0.002% / 0.005%**")
    lines.append("- maxDD / 强平 / **止损次数**只记**事实**，不作“请改保守”说教")
    lines.append("")
    lines.append("### 0.1 止损定义（务必读）")
    lines.append("")
    lines.append("**本回测主实现（investment drawdown / 投资额回撤止损）**：")
    lines.append("")
    lines.append("- 参数：`stop_loss_pct = 0.50`")
    lines.append("- 触发条件：开仓周期内 **未实现盈亏 uPnL / 该机器人投资额 initial_margin ≤ −0.50**")
    lines.append("- 动作：按触发价强制平掉**整仓**，兑现该周期亏损，计入 `stop_outs`，然后**允许开启新一轮**（继续跑，不是永久停机）")
    lines.append("- 意图对齐：截断单轮 −50% 投资额级别的浮亏，避免拖到强平；周期结束后重启")
    lines.append("")
    lines.append("**Gate 官方文档差异（务必对照填写）**：")
    lines.append("")
    lines.append("- Gate 帮助中心对期货马丁止损的写法是：**相对持仓均价的价格止损**")
    lines.append("  - 多：`止损价 = 均价 × (1 − 止损%)`")
    lines.append("  - 空：`止损价 = 均价 × (1 + 止损%)`")
    lines.append("- 且官方描述触发后常为 **策略终止**（terminate bot），与本回测「平仓后开新周期」不完全相同")
    lines.append(f"- 若要把「亏约 50% 投资额」粗映射成 Gate 价格止损%：在仓位名义≈投资额×杠杆（满用）时，约 **{price_eq*100:.1f}% 价格偏离均价**（= 50%/5x）")
    lines.append("- **本报告 Gate 填写表仍写 止损=50%**（按你要求的字段值）；请知悉：若 Gate UI 把 50% 解释成价格%，经济含义远大于「亏 50% 保证金」；若要接近本回测经济效果，Gate 价格止损可考虑填约 **10%**（=50%/5x），或确认 UI 是否支持按投资额/保证金亏损% 止损")
    lines.append("")
    lines.append("## 1. 数据与费用")
    lines.append("")
    lines.append(f"- **合约**：`{m['symbol']}` Gate USDT 永续")
    lines.append(f"- **K线**：`{m['interval']}`，约 {m['days_requested']} 天")
    lines.append(f"- **样本**：{m['bars']} 根 | {m['start']} → {m['end']}")
    lines.append(f"- **价格**：{m['start_close']:.5f} → {m['end_close']:.5f}（窗口偏强上涨）")
    lines.append(f"- **来源**：`{m['source']}`")
    lines.append(
        f"- **有效费率**：Maker {pct(m['fee_model']['eff_maker'])} / Taker {pct(m['fee_model']['eff_taker'])}"
    )
    lines.append(f"- **资金费**：{m['fee_model']['funding']}")
    lines.append(f"- **止损**：investment drawdown **{int(STOP_LOSS_PCT*100)}%** of initial_margin；周期止损后重启")
    lines.append(
        f"- **单侧搜索组合**：LONG {m['long_combos']} + SHORT {m['short_combos']}"
    )
    lines.append("")
    lines.append("## 2. 最优双开 — Gate 机器人填写表（含止损=50%）")
    lines.append("")
    lines.append(
        f"**配对模式**：`{dual['mode']}` | dual_score={dual['dual_score']} | "
        f"合计 stop_outs={dual.get('combined_stop_outs', lo['stop_outs']+sh['stop_outs'])}"
    )
    lines.append("")
    lines.append("### 2.1 LONG 机器人")
    lines.append("")
    lines.append("| Gate 字段 | 填写值 | 备注 |")
    lines.append("|---|---|---|")
    lp = lo["params"]
    lines.append(f"| 投资额 | **{int(round(lp['initial_margin']))} USDT** | 对齐截图 LONG |")
    lines.append(f"| 杠杆 | **{int(lp['leverage'])}x** | 固定 |")
    lines.append(f"| 加仓倍数 | **{lp['multiplier']}** | |")
    lines.append(f"| 跌多少加仓 | **{lp['add_drop_pct']*100:.1f}%** | LONG 看跌幅 |")
    lines.append(f"| 止盈 | **{lp['take_profit_pct']*100:.1f}%** | 相对持仓均价 |")
    lines.append(f"| 最大加仓次数 | **{lp['max_adds']}** | 深缓冲；本窗实际最高加仓层={lo['max_adds_hit']} |")
    lines.append(f"| 首单名义（参考） | **{lp['base_order_quote']} USDT** | sizing={lp['sizing']} |")
    lines.append(f"| 止损 | **50%** | 回测按 uPnL/投资额≤−50% 触发；Gate UI 若为价格%请见 §0.1 |")
    lines.append(f"| 方向 | **LONG** | |")
    lines.append("")
    lines.append("### 2.2 SHORT 机器人")
    lines.append("")
    lines.append("| Gate 字段 | 填写值 | 备注 |")
    lines.append("|---|---|---|")
    sp = sh["params"]
    lines.append(f"| 投资额 | **{int(round(sp['initial_margin']))} USDT** | 对齐截图 SHORT |")
    lines.append(f"| 杠杆 | **{int(sp['leverage'])}x** | 固定 |")
    lines.append(f"| 加仓倍数 | **{sp['multiplier']}** | |")
    lines.append(f"| 涨多少加仓 | **{sp['add_drop_pct']*100:.1f}%** | SHORT 看涨幅 |")
    lines.append(f"| 止盈 | **{sp['take_profit_pct']*100:.1f}%** | 相对持仓均价 |")
    lines.append(f"| 最大加仓次数 | **{sp['max_adds']}** | 深缓冲；本窗实际最高加仓层={sh['max_adds_hit']} |")
    lines.append(f"| 首单名义（参考） | **{sp['base_order_quote']} USDT** | sizing={sp['sizing']} |")
    lines.append(f"| 止损 | **50%** | 回测按 uPnL/投资额≤−50% 触发；Gate UI 若为价格%请见 §0.1 |")
    lines.append(f"| 方向 | **SHORT** | |")
    lines.append("")
    lines.append("### 2.3 资金摆放")
    lines.append("")
    lines.append(
        f"- LONG **{int(round(lp['initial_margin']))}** + SHORT **{int(round(sp['initial_margin']))}** ≈ "
        f"**{int(round(lp['initial_margin']+sp['initial_margin']))} USDT**"
    )
    lines.append("- 两侧均 **5x** + **max_adds 深缓冲** + **止损 50%**")
    lines.append("")
    lines.append("## 3. 双开回测现金流（事实，含 SL50）")
    lines.append("")
    lines.append("| 指标 | LONG | SHORT | 合计 |")
    lines.append("|---|---:|---:|---:|")
    lines.append(
        f"| 已实现轮次利润 cashflow | {lo['realized_cashflow']} | {sh['realized_cashflow']} | "
        f"**{dual['combined_realized_cashflow']}** |"
    )
    lines.append(
        f"| 期末净盈亏（含未实现） | {lo['net_pnl']} | {sh['net_pnl']} | **{dual['combined_net_pnl']}** |"
    )
    lines.append(
        f"| 完成轮次 | {lo['cycles']} | {sh['cycles']} | **{dual['combined_cycles']}** |"
    )
    lines.append(
        f"| 其中止损出场 stop_outs | {lo['stop_outs']} | {sh['stop_outs']} | "
        f"**{lo['stop_outs']+sh['stop_outs']}** |"
    )
    lines.append(
        f"| 止损兑现亏损合计 | {lo['stop_out_pnl_sum']} | {sh['stop_out_pnl_sum']} | "
        f"{round(lo['stop_out_pnl_sum']+sh['stop_out_pnl_sum'],4)} |"
    )
    lines.append(f"| 胜率 | {pct(lo['win_rate'])} | {pct(sh['win_rate'])} | — |")
    lines.append(
        f"| 最大回撤 maxDD | {lo['max_drawdown']} | {sh['max_drawdown']} | 代理合计 {dual['combined_max_dd_proxy']} |"
    )
    lines.append(
        f"| 最大回撤% | {pct(lo['max_drawdown_pct'])} | {pct(sh['max_drawdown_pct'])} | — |"
    )
    lines.append(
        f"| 强平 | {lo['liquidated']} | {sh['liquidated']} | "
        f"{'任一侧曾强平' if dual['long_liq'] or dual['short_liq'] else '两侧均未强平'} |"
    )
    lines.append(f"| 最大实际加仓层 | {lo['max_adds_hit']} | {sh['max_adds_hit']} | — |")
    lines.append(
        f"| 手续费 | {lo['total_fees']} | {sh['total_fees']} | {round(lo['total_fees']+sh['total_fees'],4)} |"
    )
    lines.append("")
    days = max(m["days_requested"], 1)
    lines.append(
        f"- **日均已实现现金流（粗算）**：{dual['combined_realized_cashflow']} / {days}d ≈ "
        f"**{round(dual['combined_realized_cashflow']/days, 2)} USDT/天**"
    )
    lines.append(
        f"- **轮次密度**：{dual['combined_cycles']} / {days}d ≈ "
        f"**{round(dual['combined_cycles']/days, 1)} 轮/天**"
    )
    lines.append("")
    sl70 = payload.get("compare_prev_sl70") or {}
    prev_hold = payload.get("compare_prev_params_with_sl50") or {}
    sl70_hold = payload.get("compare_sl70_params_with_sl50") or {}

    lines.append("## 4. 对比：无止损 vs SL70 vs 本轮 SL50")
    lines.append("")
    lines.append("三轮均为**同一激进双开风格**、同一 5m 窗口，各自在对应止损约束下重搜（参数不必相同）。")
    lines.append("")
    if prev or sl70:
        def _so(side, default=0):
            if side is None:
                return default
            return int(side.get("stop_outs", default) or 0)

        rows = []
        # compact 3-way totals table
        nosl_cf = prev.get("combined_realized_cashflow") if prev else None
        sl70_cf = sl70.get("combined_realized_cashflow") if sl70 else None
        sl50_cf = dual["combined_realized_cashflow"]
        nosl_cy = prev.get("combined_cycles") if prev else None
        sl70_cy = sl70.get("combined_cycles") if sl70 else None
        sl50_cy = dual["combined_cycles"]
        nosl_so = 0 if prev else None
        sl70_so = sl70.get("combined_stop_outs") if sl70 else None
        sl50_so = lo["stop_outs"] + sh["stop_outs"]
        nosl_dd = prev.get("combined_max_dd_proxy") if prev else None
        sl70_dd = sl70.get("combined_max_dd_proxy") if sl70 else None
        sl50_dd = dual["combined_max_dd_proxy"]
        nosl_np = prev.get("combined_net_pnl") if prev else None
        sl70_np = sl70.get("combined_net_pnl") if sl70 else None
        sl50_np = dual["combined_net_pnl"]

        def fmt(x):
            return "—" if x is None else x

        lines.append("| 指标 | 无SL合计 | SL70合计 | 本轮 SL50合计 |")
        lines.append("|---|---:|---:|---:|")
        lines.append(f"| cashflow | {fmt(nosl_cf)} | {fmt(sl70_cf)} | **{sl50_cf}** |")
        lines.append(f"| cycles | {fmt(nosl_cy)} | {fmt(sl70_cy)} | **{sl50_cy}** |")
        lines.append(f"| stop_outs | {fmt(nosl_so)} | {fmt(sl70_so)} | **{sl50_so}** |")
        lines.append(f"| net_pnl | {fmt(nosl_np)} | {fmt(sl70_np)} | **{sl50_np}** |")
        lines.append(f"| maxDD 代理合计 | {fmt(nosl_dd)} | {fmt(sl70_dd)} | **{sl50_dd}** |")
        lines.append("")

        if prev:
            pl, ps = prev["long"], prev["short"]
            lines.append("| 分侧 | 无SL LONG | 无SL SHORT | SL50 LONG | SL50 SHORT |")
            lines.append("|---|---:|---:|---:|---:|")
            lines.append(
                f"| cashflow | {pl['realized_cashflow']} | {ps['realized_cashflow']} | "
                f"{lo['realized_cashflow']} | {sh['realized_cashflow']} |"
            )
            lines.append(
                f"| cycles | {pl['cycles']} | {ps['cycles']} | {lo['cycles']} | {sh['cycles']} |"
            )
            lines.append(
                f"| stop_outs | {_so(pl)} | {_so(ps)} | {lo['stop_outs']} | {sh['stop_outs']} |"
            )
            lines.append(
                f"| maxDD | {pl['max_drawdown']} | {ps['max_drawdown']} | "
                f"{lo['max_drawdown']} | {sh['max_drawdown']} |"
            )
            lines.append("")
            cf_delta = sl50_cf - prev["combined_realized_cashflow"]
            lines.append(
                f"- **现金流差额（SL50 − 无SL）**：{round(cf_delta, 4)} USDT"
                "（更紧止损截断深亏轮，也会截断本可靠加仓摊薄后反弹收回的轮次）"
            )
        if sl70:
            sl70_lo, sl70_sh = sl70["long"], sl70["short"]
            lines.append("")
            lines.append("| 分侧 | SL70 LONG | SL70 SHORT | SL50 LONG | SL50 SHORT |")
            lines.append("|---|---:|---:|---:|---:|")
            lines.append(
                f"| cashflow | {sl70_lo['realized_cashflow']} | {sl70_sh['realized_cashflow']} | "
                f"{lo['realized_cashflow']} | {sh['realized_cashflow']} |"
            )
            lines.append(
                f"| cycles | {sl70_lo['cycles']} | {sl70_sh['cycles']} | {lo['cycles']} | {sh['cycles']} |"
            )
            lines.append(
                f"| stop_outs | {_so(sl70_lo)} | {_so(sl70_sh)} | {lo['stop_outs']} | {sh['stop_outs']} |"
            )
            lines.append(
                f"| maxDD | {sl70_lo['max_drawdown']} | {sl70_sh['max_drawdown']} | "
                f"{lo['max_drawdown']} | {sh['max_drawdown']} |"
            )
            lines.append("")
            cf70 = sl50_cf - sl70["combined_realized_cashflow"]
            lines.append(
                f"- **现金流差额（SL50 − SL70）**：{round(cf70, 4)} USDT"
            )
            so70 = sl70.get("combined_stop_outs")
            if so70 is not None:
                lines.append(
                    f"- **stop_outs**：SL70={so70} → SL50={sl50_so}（更紧投资额止损通常更早砍轮）"
                )
            lines.append(
                f"- **maxDD 代理合计**：SL70={sl70.get('combined_max_dd_proxy')} → SL50={sl50_dd}"
            )
        lines.append("- **参数是否同一套**：否，三轮各自在对应止损约束下重搜")
    else:
        lines.append("（未找到无SL / SL70 结果 JSON，跳过对比）")
    lines.append("")
    lines.append("### 4.1 截图代理（同开 SL50） vs 本轮优化")
    lines.append("")
    sl, ss = shot["long"], shot["short"]
    lines.append("| | 截图代理 LONG | 截图代理 SHORT | 优化 LONG | 优化 SHORT |")
    lines.append("|---|---:|---:|---:|---:|")
    lines.append(
        f"| cashflow | {sl['realized_cashflow']} | {ss['realized_cashflow']} | "
        f"{lo['realized_cashflow']} | {sh['realized_cashflow']} |"
    )
    lines.append(
        f"| cycles | {sl['cycles']} | {ss['cycles']} | {lo['cycles']} | {sh['cycles']} |"
    )
    lines.append(
        f"| stop_outs | {sl['stop_outs']} | {ss['stop_outs']} | {lo['stop_outs']} | {sh['stop_outs']} |"
    )
    lines.append(
        f"| net_pnl | {sl['net_pnl']} | {ss['net_pnl']} | {lo['net_pnl']} | {sh['net_pnl']} |"
    )
    lines.append(
        f"| maxDD | {sl['max_drawdown']} | {ss['max_drawdown']} | {lo['max_drawdown']} | {sh['max_drawdown']} |"
    )
    lines.append(
        f"| 强平 | {sl['liquidated']} | {ss['liquidated']} | {lo['liquidated']} | {sh['liquidated']} |"
    )
    lines.append("")
    shot_cf = sl["realized_cashflow"] + ss["realized_cashflow"]
    better = dual["combined_realized_cashflow"] > shot_cf
    lines.append(
        f"**相对截图代理**：优化合计 cashflow **{dual['combined_realized_cashflow']}** vs 代理 "
        f"**{round(shot_cf,4)}** → {'仍然更好' if better else '未超过代理（事实）'}。"
    )
    lines.append("")
    if prev_hold:
        phl, phs = prev_hold["long"], prev_hold["short"]
        lines.append("### 4.2 无SL最优参数 + 直接套上 SL50（未重搜）")
        lines.append("")
        lines.append("| | LONG | SHORT | 合计 |")
        lines.append("|---|---:|---:|---:|")
        lines.append(
            f"| cashflow | {phl['realized_cashflow']} | {phs['realized_cashflow']} | "
            f"**{prev_hold['combined_realized_cashflow']}** |"
        )
        lines.append(
            f"| cycles | {phl['cycles']} | {phs['cycles']} | **{prev_hold['combined_cycles']}** |"
        )
        lines.append(
            f"| stop_outs | {phl['stop_outs']} | {phs['stop_outs']} | "
            f"**{prev_hold['combined_stop_outs']}** |"
        )
        lines.append(
            f"| net_pnl | {phl['net_pnl']} | {phs['net_pnl']} | **{prev_hold['combined_net_pnl']}** |"
        )
        lines.append("")
        lines.append(
            f"- 无SL最优参数强制 SL50 后合计 cashflow **{prev_hold['combined_realized_cashflow']}**"
            f"（本轮重搜 SL50 为 **{dual['combined_realized_cashflow']}**）→ 止损开启后必须重搜票面/间距。"
        )
        lines.append("")
    if sl70_hold:
        shl, shs = sl70_hold["long"], sl70_hold["short"]
        lines.append("### 4.3 SL70最优参数 + 直接套上 SL50（未重搜）")
        lines.append("")
        lines.append("| | LONG | SHORT | 合计 |")
        lines.append("|---|---:|---:|---:|")
        lines.append(
            f"| cashflow | {shl['realized_cashflow']} | {shs['realized_cashflow']} | "
            f"**{sl70_hold['combined_realized_cashflow']}** |"
        )
        lines.append(
            f"| cycles | {shl['cycles']} | {shs['cycles']} | **{sl70_hold['combined_cycles']}** |"
        )
        lines.append(
            f"| stop_outs | {shl['stop_outs']} | {shs['stop_outs']} | "
            f"**{sl70_hold['combined_stop_outs']}** |"
        )
        lines.append(
            f"| net_pnl | {shl['net_pnl']} | {shs['net_pnl']} | **{sl70_hold['combined_net_pnl']}** |"
        )
        lines.append("")
        lines.append(
            f"- SL70最优参数强制 SL50 后合计 cashflow **{sl70_hold['combined_realized_cashflow']}**"
            f"（本轮重搜 SL50 为 **{dual['combined_realized_cashflow']}**）。"
        )
        lines.append("")

    lines.append("## 5. 单侧 Top 速览（SL50 风格内）")
    lines.append("")
    lines.append("### LONG Top5")
    lines.append("")
    lines.append("| rank | mult | drop | tp | base | cashflow | cycles | stop_outs | maxDD | liq |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for i, r in enumerate(payload["top_long"][:5], 1):
        p = r["params"]
        lines.append(
            f"| {i} | {p['multiplier']} | {p['add_drop_pct']*100:.1f}% | {p['take_profit_pct']*100:.1f}% | "
            f"{p['base_order_quote']} | {r['realized_cashflow']} | {r['cycles']} | {r['stop_outs']} | "
            f"{r['max_drawdown']} | {r['liquidated']} |"
        )
    lines.append("")
    lines.append("### SHORT Top5")
    lines.append("")
    lines.append("| rank | mult | drop | tp | base | cashflow | cycles | stop_outs | maxDD | liq |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for i, r in enumerate(payload["top_short"][:5], 1):
        p = r["params"]
        lines.append(
            f"| {i} | {p['multiplier']} | {p['add_drop_pct']*100:.1f}% | {p['take_profit_pct']*100:.1f}% | "
            f"{p['base_order_quote']} | {r['realized_cashflow']} | {r['cycles']} | {r['stop_outs']} | "
            f"{r['max_drawdown']} | {r['liquidated']} |"
        )
    lines.append("")
    lines.append("## 6. 说明")
    lines.append("")
    lines.append(
        "- 止损主逻辑：`(uPnL / initial_margin) <= -0.50` → 整仓止损平仓 → 计 stop_out → 开新周期。"
    )
    lines.append(
        "- Gate UI 止损字段若为「相对均价的价格%」，与本回测投资额回撤止损不等价；见 §0.1。"
    )
    lines.append("- 未计入资金费/滑点/挂单失败；双开回撤为两侧相加代理。")
    lines.append("- JSON：`opt_niulai_aggressive_sl50_results.json`")
    lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def load_or_fetch(symbol: str, interval: str, days: int):
    if CACHE_CSV.exists():
        df = __import__("pandas").read_csv(CACHE_CSV, parse_dates=["timestamp"])
        if len(df) > 1000:
            df.attrs["source"] = "cache_csv:" + CACHE_CSV.name
            print(f"Loaded cache {CACHE_CSV} bars={len(df)}")
            return df
    print(f"Fetching Gate futures {symbol} {interval} days={days} ...")
    df = fetch_gate_futures_candles(symbol, interval=interval, days=days)
    CACHE_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CACHE_CSV, index=False)
    print(f"Cached -> {CACHE_CSV}")
    return df


def load_prev_no_sl():
    if not PREV_JSON.exists():
        return None
    data = json.loads(PREV_JSON.read_text(encoding="utf-8"))
    bd = data.get("best_dual") or {}
    lo, sh = bd.get("long"), bd.get("short")
    if not lo or not sh:
        return None
    return {
        "combined_realized_cashflow": bd.get("combined_realized_cashflow"),
        "combined_net_pnl": bd.get("combined_net_pnl"),
        "combined_cycles": bd.get("combined_cycles"),
        "combined_max_dd_proxy": bd.get("combined_max_dd_proxy"),
        "long": lo,
        "short": sh,
        "params_differ": True,
        "note": "previous aggressive dual without stop-loss",
    }


def load_prev_sl70():
    if not SL70_JSON.exists():
        return None
    data = json.loads(SL70_JSON.read_text(encoding="utf-8"))
    bd = data.get("best_dual") or {}
    lo, sh = bd.get("long"), bd.get("short")
    if not lo or not sh:
        return None
    return {
        "combined_realized_cashflow": bd.get("combined_realized_cashflow"),
        "combined_net_pnl": bd.get("combined_net_pnl"),
        "combined_cycles": bd.get("combined_cycles"),
        "combined_stop_outs": bd.get("combined_stop_outs", (lo.get("stop_outs") or 0) + (sh.get("stop_outs") or 0)),
        "combined_max_dd_proxy": bd.get("combined_max_dd_proxy"),
        "long": lo,
        "short": sh,
        "params_differ": True,
        "note": "previous aggressive dual with stop_loss_pct=0.70",
        "mode": bd.get("mode"),
        "dual_score": bd.get("dual_score"),
    }


def _holdout_pair(df, long_p, short_p, tag: str):
    hl = run_one(
        df,
        "long",
        long_p["initial_margin"],
        long_p["leverage"],
        long_p["multiplier"],
        long_p["add_drop_pct"],
        long_p["take_profit_pct"],
        long_p["max_adds"],
        long_p["base_order_quote"],
        long_p.get("sizing", "hold") + "|" + tag,
        stop_loss_pct=STOP_LOSS_PCT,
    )
    hs = run_one(
        df,
        "short",
        short_p["initial_margin"],
        short_p["leverage"],
        short_p["multiplier"],
        short_p["add_drop_pct"],
        short_p["take_profit_pct"],
        short_p["max_adds"],
        short_p["base_order_quote"],
        short_p.get("sizing", "hold") + "|" + tag,
        stop_loss_pct=STOP_LOSS_PCT,
    )
    return {
        "combined_realized_cashflow": round(hl["realized_cashflow"] + hs["realized_cashflow"], 4),
        "combined_cycles": hl["cycles"] + hs["cycles"],
        "combined_stop_outs": hl["stop_outs"] + hs["stop_outs"],
        "combined_net_pnl": round(hl["net_pnl"] + hs["net_pnl"], 4),
        "combined_max_dd_proxy": round(hl["max_drawdown"] + hs["max_drawdown"], 4),
        "long": hl,
        "short": hs,
        "note": tag,
    }


def main():
    symbol = "牛来_USDT"
    days = 18
    interval = "5m"
    # Direct Gate-aligned capitals (user style)
    long_cap = 950.0
    short_cap = 1380.0
    leverage = 5.0

    df = load_or_fetch(symbol, interval, days)
    print(f"Got {len(df)} bars | {df['timestamp'].iloc[0]} -> {df['timestamp'].iloc[-1]}")
    print(f"Close {df['close'].iloc[0]:.5f} -> {df['close'].iloc[-1]:.5f}")
    print(f"Stop-loss ENABLED: investment drawdown {STOP_LOSS_PCT:.0%} of initial_margin")

    print("Aggressive LONG search @950 with SL50 ...")
    long_res = optimize_side(df, "long", long_cap, leverage)
    print(
        f"LONG done; top cf_score={long_res[0]['cf_score']} cashflow={long_res[0]['realized_cashflow']} "
        f"stop_outs={long_res[0]['stop_outs']}"
    )

    print("Aggressive SHORT search @1380 with SL50 ...")
    short_res = optimize_side(df, "short", short_cap, leverage)
    print(
        f"SHORT done; top cf_score={short_res[0]['cf_score']} cashflow={short_res[0]['realized_cashflow']} "
        f"stop_outs={short_res[0]['stop_outs']}"
    )

    best_dual, top_duals, raw_best = pick_dual(long_res, short_res, top_n=50)
    # Prefer presenting with max_adds=90 buffer when tied-ish: bump mode tag
    present = dict(best_dual)
    present["mode"] = best_dual["mode"] + "_aggressive_dual_sl50_buf90"
    # If best max_adds < 90, also evaluate same params with max_adds=90 buffer (usually identical if not hitting)
    def with_buf90(side_s):
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
            stop_loss_pct=STOP_LOSS_PCT,
        )

    mir_long = with_buf90(best_dual["long"])
    mir_short = with_buf90(best_dual["short"])
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
        "mode": "asymmetric_aggressive_dual_sl50_buf90",
        "long": mir_long,
        "short": mir_short,
        "search_best_before_buf90": {
            "dual_score": best_dual["dual_score"],
            "long_params": best_dual["long"]["params"],
            "short_params": best_dual["short"]["params"],
        },
    }

    print(
        f"Best dual score={present['dual_score']} cashflow={present['combined_realized_cashflow']} "
        f"cycles={present['combined_cycles']} stop_outs={present['combined_stop_outs']} mode={present['mode']}"
    )

    shot_sl, shot_sl_alt = screenshot_proxy(df, STOP_LOSS_PCT)
    shot_nosl, _ = screenshot_proxy(df, None)
    prev = load_prev_no_sl()
    sl70_prev = load_prev_sl70()

    prev_with_sl = None
    if prev:
        prev_with_sl = _holdout_pair(
            df, prev["long"]["params"], prev["short"]["params"], "nosl_params_sl50_holdout"
        )
        prev_with_sl["note"] = "previous no-SL aggressive params re-run with SL50 (not re-optimized)"

    sl70_with_sl50 = None
    if sl70_prev:
        sl70_with_sl50 = _holdout_pair(
            df, sl70_prev["long"]["params"], sl70_prev["short"]["params"], "sl70_params_sl50_holdout"
        )
        sl70_with_sl50["note"] = "previous SL70 aggressive params re-run with SL50 (not re-optimized)"

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
            "style": "aggressive_dual_hedge_small_size_sl50",
            "stop_loss": {
                "pct": STOP_LOSS_PCT,
                "mode": "investment_drawdown",
                "rule": "trigger when uPnL/initial_margin <= -stop_loss_pct; close cycle; allow new cycle",
                "gate_ui_note": (
                    "Gate docs: SL% of avg entry price; bot may terminate. "
                    f"Approx price% for same margin loss at {leverage}x full use ≈ "
                    f"{STOP_LOSS_PCT/leverage:.2%}"
                ),
            },
            "fee_model": {
                "maker_base": VIP7_FUTURES_75.maker_rate,
                "taker_base": VIP7_FUTURES_75.taker_rate,
                "rebate": VIP7_FUTURES_75.rebate_rate,
                "eff_maker": VIP7_FUTURES_75.effective_maker,
                "eff_taker": VIP7_FUTURES_75.effective_taker,
                "funding": "omitted (4h funding not in backtest)",
            },
            "long_combos": len(long_res),
            "short_combos": len(short_res),
            "long_capital": long_cap,
            "short_capital": short_cap,
            "leverage_fixed": leverage,
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
        "top_long": long_res[:15],
        "top_short": short_res[:15],
        "screenshot_proxy_sl50": shot_sl,
        "screenshot_proxy_sl50_alt": shot_sl_alt,
        "screenshot_proxy_no_sl": shot_nosl,
        "compare_prev_no_sl": prev,
        "compare_prev_sl70": sl70_prev,
        "compare_prev_params_with_sl50": prev_with_sl,
        "compare_sl70_params_with_sl50": sl70_with_sl50,
        "raw_best_maybe_liq": {
            "dual_score": raw_best["dual_score"] if raw_best else None,
            "long_liq": raw_best["long_liq"] if raw_best else None,
            "short_liq": raw_best["short_liq"] if raw_best else None,
        },
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    write_report(payload)
    print(f"Wrote {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
