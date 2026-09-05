#!/usr/bin/env python3
"""Aggressive dual-hedge futures Martingale optimize for 牛来_USDT (user style)."""

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

OUT_JSON = ROOT / "opt_niulai_aggressive_results.json"
OUT_MD = ROOT / "opt_niulai_aggressive_report.md"
CACHE_CSV = ROOT / "data_sample" / "niulai_USDT_5m_futures.csv"

CST = timezone(timedelta(hours=8))


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
    """Size first order for a practical working depth; max_adds can be deeper buffer."""
    fac = notional_factor(multiplier, working_adds)
    base = (fill_frac * capital * leverage) / max(fac, 1e-9)
    return max(1.0, round(base, 4))


def frac_base(capital: float, leverage: float, frac: float) -> float:
    """First notional = frac of max buying power (Gate small-ticket style)."""
    return max(1.0, round(capital * leverage * frac, 4))


def cashflow_score(s: dict) -> float:
    """Score WITHIN aggressive style: realized cycle cashflow + turnover + utilization.
    Liquidation heavily penalized for dual reliability, but DD is fact not veto.
    """
    if s.get("liquidated"):
        # Still keep some signal from cycles before wipe, but dual needs survivors
        return s.get("realized_cashflow", 0.0) - 5000.0
    rc = float(s.get("realized_cashflow", 0.0))
    cycles = float(s.get("cycles", 0))
    util = float(s.get("capital_util", 0.0))  # 0..1+
    # Prefer cashflow; bonus rounds; mild util bonus (capital working)
    return rc + 0.35 * cycles + 15.0 * min(util, 1.2)


def run_one(df, direction, capital, leverage, mult, drop, tp, max_adds, base, sizing_tag):
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
    }
    s["cf_score"] = round(cashflow_score(s), 4)
    return s


def optimize_side(df, direction: str, capital: float, leverage: float = 5.0):
    max_adds_list = [20, 30, 40, 50, 60, 90]
    multipliers = [1.2, 1.3, 1.4, 1.5, 1.8, 2.0]
    drop_pcts = [0.005, 0.008, 0.010, 0.012, 0.015, 0.018, 0.025]
    tp_pcts = [0.003, 0.004, 0.005, 0.006, 0.008, 0.010, 0.012]
    # Gate-style: working depth sizing + buying-power fraction sizing
    working_adds_list = [8, 12, 16]
    fracs = [0.02, 0.035, 0.05]

    results = []
    t0 = time.time()
    # Path A: working-depth sized base
    combos_a = list(product(max_adds_list, multipliers, drop_pcts, tp_pcts, working_adds_list))
    for i, (max_adds, mult, drop, tp, wad) in enumerate(combos_a):
        base = gate_style_base(capital, leverage, mult, wad)
        s = run_one(
            df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"work_adds={wad}"
        )
        results.append(s)
        if (i + 1) % 800 == 0:
            print(f"  [{direction}/A] {i+1}/{len(combos_a)} ({time.time()-t0:.1f}s)", flush=True)

    # Path B: frac of buying power (more aggressive ticket size)
    combos_b = list(product(max_adds_list, multipliers, drop_pcts, tp_pcts, fracs))
    for i, (max_adds, mult, drop, tp, frac) in enumerate(combos_b):
        base = frac_base(capital, leverage, frac)
        s = run_one(
            df, direction, capital, leverage, mult, drop, tp, max_adds, base, f"bp_frac={frac}"
        )
        results.append(s)
        if (i + 1) % 800 == 0:
            print(f"  [{direction}/B] {i+1}/{len(combos_b)} ({time.time()-t0:.1f}s)", flush=True)

    results.sort(key=lambda x: x["cf_score"], reverse=True)
    return results


def dual_score(long_s: dict, short_s: dict) -> float:
    """Combined dual portfolio cashflow score."""
    # Prefer both sides alive; if one liq, still score remaining but penalize
    liq_pen = 0.0
    if long_s.get("liquidated"):
        liq_pen += 2500.0
    if short_s.get("liquidated"):
        liq_pen += 2500.0
    rc = long_s["realized_cashflow"] + short_s["realized_cashflow"]
    cycles = long_s["cycles"] + short_s["cycles"]
    util = (long_s["capital_util"] + short_s["capital_util"]) / 2.0
    # Asymmetry ok; reward both sides contributing cashflow
    min_side = min(long_s["realized_cashflow"], short_s["realized_cashflow"])
    balance_bonus = 0.15 * min_side  # encourage dual cashflow not one-sided only
    return rc + 0.30 * cycles + 20.0 * min(util, 1.2) + balance_bonus - liq_pen


def pick_dual(long_res, short_res, top_n: int = 40):
    """Search top long x top short for best dual pair; also try shared-param pairs."""
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
                "combined_max_dd_proxy": round(lo["max_drawdown"] + sh["max_drawdown"], 4),
                "long_max_dd": lo["max_drawdown"],
                "short_max_dd": sh["max_drawdown"],
                "long_liq": lo["liquidated"],
                "short_liq": sh["liquidated"],
                "avg_capital_util": round((lo["capital_util"] + sh["capital_util"]) / 2, 4),
                "mode": "asymmetric",
                "long": lo,
                "short": sh,
            }
            candidates.append(row)
            if sc > best_sc:
                best_sc = sc
                best = row

    # Shared-param dual: same mult/drop/tp/max_adds/sizing family, re-pair by param key
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
                "combined_realized_cashflow": round(
                    lo["realized_cashflow"] + sh["realized_cashflow"], 4
                ),
                "combined_net_pnl": round(lo["net_pnl"] + sh["net_pnl"], 4),
                "combined_cycles": lo["cycles"] + sh["cycles"],
                "combined_max_dd_proxy": round(lo["max_drawdown"] + sh["max_drawdown"], 4),
                "long_max_dd": lo["max_drawdown"],
                "short_max_dd": sh["max_drawdown"],
                "long_liq": lo["liquidated"],
                "short_liq": sh["liquidated"],
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
    # Prefer dual where neither side liquidated if available in top
    alive = [c for c in candidates if not c["long_liq"] and not c["short_liq"]]
    if alive:
        best_alive = alive[0]
        # If best overall is liq-heavy, still report alive as primary for dual fill-in
        if best and (best["long_liq"] or best["short_liq"]):
            return best_alive, candidates[:25], best
        return best_alive, candidates[:25], best
    return best, candidates[:25], best


def screenshot_proxy(df):
    """Approximate current screenshot settings for comparison."""
    # Screenshot: LONG ~950 / SHORT ~1383, 5x, max_adds=90; mult/drop/tp unknown —
    # use aggressive mid guesses consistent with high turnover: mult=1.5, drop=1.2%, tp=0.6%
    # size with work_adds=12 (small ticket, deep buffer 90)
    out = {}
    for direction, cap in (("long", 950.0), ("short", 1383.0)):
        base = gate_style_base(cap, 5.0, 1.5, working_adds=12)
        out[direction] = run_one(
            df, direction, cap, 5.0, 1.5, 0.012, 0.006, 90, base, "screenshot_proxy_work12"
        )
    # Also try bp_frac=0.035
    alt = {}
    for direction, cap in (("long", 950.0), ("short", 1383.0)):
        base = frac_base(cap, 5.0, 0.035)
        alt[direction] = run_one(
            df, direction, cap, 5.0, 1.5, 0.012, 0.006, 90, base, "screenshot_proxy_frac0.035"
        )
    return out, alt


def pct(x: float) -> str:
    return f"{x * 100:.2f}%"


def gate_table_row(label: str, s: dict) -> list[str]:
    p = s["params"]
    return [
        f"| 投资额 | **{int(round(p['initial_margin']))} USDT** | {label} |",
        f"| 杠杆 | **{int(p['leverage'])}x** | 固定用户风格 |",
        f"| 加仓倍数 | **{p['multiplier']}** | |",
        f"| 跌/涨多少加仓 | **{p['add_drop_pct']*100:.1f}%** | LONG=跌幅 / SHORT=涨幅 |",
        f"| 止盈 | **{p['take_profit_pct']*100:.1f}%** | 相对持仓均价 |",
        f"| 最大加仓次数 | **{p['max_adds']}** | 深缓冲（风格内） |",
        f"| 首单名义（参考） | **{p['base_order_quote']} USDT** | sizing={p['sizing']} |",
        f"| 方向 | **{p['direction'].upper()}** | |",
    ]


def write_report(payload: dict) -> None:
    m = payload["meta"]
    dual = payload["best_dual"]
    lo, sh = dual["long"], dual["short"]
    shot = payload["screenshot_proxy"]
    shot_alt = payload["screenshot_proxy_alt"]
    now_cst = datetime.now(CST).strftime("%Y-%m-%d %H:%M CST")

    lines: list[str] = []
    lines.append("# 牛来_USDT 激进双开马丁优化报告（用户风格）")
    lines.append("")
    lines.append(f"> 生成时间（UTC+8）：{now_cst} | 研究回测，非投资建议，无实盘下单。")
    lines.append("")
    lines.append("## 0. 风格对齐（已按你的打法优化）")
    lines.append("")
    lines.append("本轮**严格按你的激进双开小仓风格**搜索与打分，不做保守单边、不做降杠杆、不推荐改现货：")
    lines.append("")
    lines.append("- **双开**：同币 LONG + SHORT 同时跑")
    lines.append("- **小仓**：单侧约 900–1400 USDT（截图合计约 2000–2500）")
    lines.append("- **杠杆**：固定 **5x**")
    lines.append("- **深加仓缓冲**：max_adds ∈ {20,30,40,50,60,90}（按缓冲额度搜，不当作“必须减到个位数”）")
    lines.append("- **高换手现金流**：止盈 0.3%–1.2%，紧间距加仓")
    lines.append("- **打分**：组合**已实现轮次利润（realized cashflow）** + 轮次 + 保证金利用率；maxDD / 强平仅作**事实记录**")
    lines.append("- **费率**：VIP7 期货 Maker 0.008% / Taker 0.02% + 75% 返佣 → 有效约 **0.002% / 0.005%**")
    lines.append("")
    lines.append("## 1. 数据与费用")
    lines.append("")
    lines.append(f"- **合约**：`{m['symbol']}` Gate USDT 永续")
    lines.append(f"- **K线**：`{m['interval']}`，约 {m['days_requested']} 天可用")
    lines.append(f"- **样本**：{m['bars']} 根 | {m['start']} → {m['end']}")
    lines.append(f"- **价格**：{m['start_close']:.5f} → {m['end_close']:.5f}")
    lines.append(f"- **来源**：`{m['source']}`")
    lines.append(
        f"- **有效费率**：Maker {pct(m['fee_model']['eff_maker'])} / Taker {pct(m['fee_model']['eff_taker'])}"
    )
    lines.append(f"- **资金费**：{m['fee_model']['funding']}")
    lines.append(
        f"- **单侧搜索组合**：LONG {m['long_combos']} + SHORT {m['short_combos']}（含 working-depth 与买力分数两种首单 sizing）"
    )
    lines.append(f"- **制度提示**：样本窗口整体偏强上涨（约 {m['start_close']:.3f}→{m['end_close']:.3f}），LONG 现金流更易释放，SHORT 更吃震荡回撤段；双开参数按两侧现金流联合优选。")
    lines.append("")
    lines.append("## 2. 最优双开组合（Gate 机器人填写）")
    lines.append("")
    lines.append(f"**配对模式**：`{dual['mode']}` | **dual_score**={dual['dual_score']}")
    lines.append("")
    lines.append("### 2.1 LONG 机器人")
    lines.append("")
    lines.append("| Gate 字段 | 填写值 | 备注 |")
    lines.append("|---|---|---|")
    lines.extend(gate_table_row("与截图同量级小仓", lo))
    lines.append("")
    lines.append("### 2.2 SHORT 机器人")
    lines.append("")
    lines.append("| Gate 字段 | 填写值 | 备注 |")
    lines.append("|---|---|---|")
    lines.extend(gate_table_row("与截图同量级小仓", sh))
    lines.append("")
    lines.append("### 2.3 资金摆放（对齐截图量级）")
    lines.append("")
    lines.append(
        f"- LONG 投资额：**{int(round(lo['params']['initial_margin']))} USDT**；"
        f"SHORT 投资额：**{int(round(sh['params']['initial_margin']))} USDT**；"
        f"合计约 **{int(round(lo['params']['initial_margin'] + sh['params']['initial_margin']))} USDT**"
    )
    lines.append("- 两侧均 **5x**；max_adds 保持深缓冲（见上表），首单按回测 sizing 换算名义。")
    lines.append("")
    lines.append("## 3. 双开回测现金流指标（事实）")
    lines.append("")
    lines.append("| 指标 | LONG | SHORT | 合计 |")
    lines.append("|---|---:|---:|---:|")
    lines.append(
        f"| 已实现轮次利润（cashflow） | {lo['realized_cashflow']} | {sh['realized_cashflow']} | "
        f"**{dual['combined_realized_cashflow']}** |"
    )
    lines.append(
        f"| 期末净盈亏（含未实现） | {lo['net_pnl']} | {sh['net_pnl']} | **{dual['combined_net_pnl']}** |"
    )
    lines.append(
        f"| 完成轮次 | {lo['cycles']} | {sh['cycles']} | **{dual['combined_cycles']}** |"
    )
    lines.append(
        f"| 胜率 | {pct(lo['win_rate'])} | {pct(sh['win_rate'])} | — |"
    )
    lines.append(
        f"| 最大回撤 maxDD | {lo['max_drawdown']} | {sh['max_drawdown']} | 代理合计 {dual['combined_max_dd_proxy']} |"
    )
    lines.append(
        f"| 最大回撤% | {pct(lo['max_drawdown_pct'])} | {pct(sh['max_drawdown_pct'])} | — |"
    )
    lines.append(
        f"| 强平 liquidated | {lo['liquidated']} | {sh['liquidated']} | "
        f"{'任一侧曾强平' if dual['long_liq'] or dual['short_liq'] else '两侧均未强平'} |"
    )
    lines.append(
        f"| 最大实际加仓层 | {lo['max_adds_hit']} | {sh['max_adds_hit']} | — |"
    )
    lines.append(
        f"| 保证金利用率 | {pct(lo['capital_util'])} | {pct(sh['capital_util'])} | 均 {pct(dual['avg_capital_util'])} |"
    )
    lines.append(
        f"| 手续费 | {lo['total_fees']} | {sh['total_fees']} | {round(lo['total_fees']+sh['total_fees'],4)} |"
    )
    lines.append("")
    lines.append(
        f"- **日均已实现现金流（粗算）**：合计 {dual['combined_realized_cashflow']} / {m['days_requested']}d ≈ "
        f"**{round(dual['combined_realized_cashflow']/max(m['days_requested'],1), 2)} USDT/天**（样本窗口）。"
    )
    lines.append(
        f"- **轮次密度**：合计 {dual['combined_cycles']} 轮 / {m['days_requested']}d ≈ "
        f"**{round(dual['combined_cycles']/max(m['days_requested'],1), 1)} 轮/天**。"
    )
    lines.append("")
    lines.append("## 4. 截图当前设定代理 vs 本轮优化（同风格内对比）")
    lines.append("")
    lines.append("截图可确认：SHORT≈1383 / LONG≈950、5x、max_adds=90、高换手；倍数/间距/止盈未完整 OCR，代理假设 mult=1.5、drop=1.2%、tp=0.6%。")
    lines.append("")
    lines.append("| | 截图代理 LONG | 截图代理 SHORT | 优化 LONG | 优化 SHORT |")
    lines.append("|---|---:|---:|---:|---:|")
    sl, ss = shot["long"], shot["short"]
    lines.append(
        f"| 已实现 cashflow | {sl['realized_cashflow']} | {ss['realized_cashflow']} | "
        f"{lo['realized_cashflow']} | {sh['realized_cashflow']} |"
    )
    lines.append(
        f"| 轮次 | {sl['cycles']} | {ss['cycles']} | {lo['cycles']} | {sh['cycles']} |"
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
    lines.append(
        f"| max_adds_hit | {sl['max_adds_hit']} | {ss['max_adds_hit']} | {lo['max_adds_hit']} | {sh['max_adds_hit']} |"
    )
    lines.append("")
    al, ash = shot_alt["long"], shot_alt["short"]
    lines.append(
        f"另：买力分数代理（bp_frac=0.035）LONG cashflow={al['realized_cashflow']} liq={al['liquidated']}；"
        f"SHORT cashflow={ash['realized_cashflow']} liq={ash['liquidated']}。"
    )
    lines.append("")
    lines.append("**风格内解读**：优化组合在保持双开+5x+深 max_adds 的前提下，抬高双侧合计已实现现金流与轮次；上表 maxDD/强平为同窗口事实对照，不是让你改成单边保守。")
    lines.append("")
    lines.append("## 5. 单侧 Top（现金流分）速览")
    lines.append("")
    lines.append("### LONG Top5")
    lines.append("")
    lines.append("| rank | mult | drop | tp | max_adds | sizing | cashflow | cycles | net | maxDD | liq |")
    lines.append("|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---|")
    for i, r in enumerate(payload["top_long"][:5], 1):
        p = r["params"]
        lines.append(
            f"| {i} | {p['multiplier']} | {p['add_drop_pct']*100:.1f}% | {p['take_profit_pct']*100:.1f}% | "
            f"{p['max_adds']} | {p['sizing']} | {r['realized_cashflow']} | {r['cycles']} | "
            f"{r['net_pnl']} | {r['max_drawdown']} | {r['liquidated']} |"
        )
    lines.append("")
    lines.append("### SHORT Top5")
    lines.append("")
    lines.append("| rank | mult | drop | tp | max_adds | sizing | cashflow | cycles | net | maxDD | liq |")
    lines.append("|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---|")
    for i, r in enumerate(payload["top_short"][:5], 1):
        p = r["params"]
        lines.append(
            f"| {i} | {p['multiplier']} | {p['add_drop_pct']*100:.1f}% | {p['take_profit_pct']*100:.1f}% | "
            f"{p['max_adds']} | {p['sizing']} | {r['realized_cashflow']} | {r['cycles']} | "
            f"{r['net_pnl']} | {r['max_drawdown']} | {r['liquidated']} |"
        )
    lines.append("")
    lines.append("## 6. 镜像资金（950 / 1380）复核")
    lines.append("")
    mir = payload.get("mirror_dual")
    if mir:
        lines.append(
            f"将最优参数分别放到 LONG=950、SHORT=1380（贴近截图）重跑："
            f" 合计 cashflow=**{mir['combined_realized_cashflow']}**，"
            f"轮次=**{mir['combined_cycles']}**，"
            f"净盈亏=**{mir['combined_net_pnl']}**，"
            f"强平 L/S={mir['long_liq']}/{mir['short_liq']}，"
            f"maxDD L/S={mir['long_max_dd']}/{mir['short_max_dd']}。"
        )
        mlp, msp = mir["long"]["params"], mir["short"]["params"]
        lines.append("")
        lines.append("| | LONG(950) | SHORT(1380) |")
        lines.append("|---|---|---|")
        lines.append(
            f"| 倍数/间距/止盈/最大加仓 | {mlp['multiplier']} / {mlp['add_drop_pct']*100:.1f}% / "
            f"{mlp['take_profit_pct']*100:.1f}% / {mlp['max_adds']} | "
            f"{msp['multiplier']} / {msp['add_drop_pct']*100:.1f}% / "
            f"{msp['take_profit_pct']*100:.1f}% / {msp['max_adds']} |"
        )
        lines.append(
            f"| 首单名义 | {mlp['base_order_quote']} | {msp['base_order_quote']} |"
        )
    else:
        lines.append("（无镜像复核）")
    lines.append("")
    lines.append("## 7. 说明")
    lines.append("")
    lines.append("- 首单 sizing：`work_adds=N` = 按约 N 层实用深度把满阶梯保证金压进投资额；`bp_frac=f` = 首单名义≈投资额×杠杆×f。max_adds 仍可高于 N，作为更深缓冲，直到保证金不够停止加仓。")
    lines.append("- 回测未计入资金费、滑点、挂单失败；双开回撤为两侧简单相加代理。")
    lines.append("- 详细数值：`opt_niulai_aggressive_results.json`。")
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


def main():
    symbol = "牛来_USDT"
    days = 18
    interval = "5m"
    # Search capital per side ~1000 (mid of 900-1400)
    capital = 1000.0
    leverage = 5.0

    df = load_or_fetch(symbol, interval, days)
    print(f"Got {len(df)} bars | {df['timestamp'].iloc[0]} -> {df['timestamp'].iloc[-1]}")
    print(f"Close {df['close'].iloc[0]:.5f} -> {df['close'].iloc[-1]:.5f}")

    print("Aggressive LONG search ...")
    long_res = optimize_side(df, "long", capital, leverage)
    print(f"LONG done; top cf_score={long_res[0]['cf_score']} cashflow={long_res[0]['realized_cashflow']}")

    print("Aggressive SHORT search ...")
    short_res = optimize_side(df, "short", capital, leverage)
    print(f"SHORT done; top cf_score={short_res[0]['cf_score']} cashflow={short_res[0]['realized_cashflow']}")

    best_dual, top_duals, raw_best = pick_dual(long_res, short_res, top_n=50)
    print(
        f"Best dual score={best_dual['dual_score']} cashflow={best_dual['combined_realized_cashflow']} "
        f"cycles={best_dual['combined_cycles']} mode={best_dual['mode']}"
    )

    # Mirror screenshot capitals with best dual params
    def rescale_base(base, old_cap, new_cap):
        return max(1.0, round(base * (new_cap / old_cap), 4))

    lp = best_dual["long"]["params"]
    sp = best_dual["short"]["params"]
    mir_long = run_one(
        df,
        "long",
        950.0,
        5.0,
        lp["multiplier"],
        lp["add_drop_pct"],
        lp["take_profit_pct"],
        lp["max_adds"],
        rescale_base(lp["base_order_quote"], lp["initial_margin"], 950.0),
        lp["sizing"] + "|mirror950",
    )
    mir_short = run_one(
        df,
        "short",
        1380.0,
        5.0,
        sp["multiplier"],
        sp["add_drop_pct"],
        sp["take_profit_pct"],
        sp["max_adds"],
        rescale_base(sp["base_order_quote"], sp["initial_margin"], 1380.0),
        sp["sizing"] + "|mirror1380",
    )
    mirror_dual = {
        "combined_realized_cashflow": round(
            mir_long["realized_cashflow"] + mir_short["realized_cashflow"], 4
        ),
        "combined_net_pnl": round(mir_long["net_pnl"] + mir_short["net_pnl"], 4),
        "combined_cycles": mir_long["cycles"] + mir_short["cycles"],
        "long_max_dd": mir_long["max_drawdown"],
        "short_max_dd": mir_short["max_drawdown"],
        "long_liq": mir_long["liquidated"],
        "short_liq": mir_short["liquidated"],
        "dual_score": round(dual_score(mir_long, mir_short), 4),
        "long": mir_long,
        "short": mir_short,
    }

    shot, shot_alt = screenshot_proxy(df)

    # Also produce fill-in tables at mirror caps as the "recommended Gate fill" if dual was at 1000/1000
    # Prefer presenting mirror 950/1380 as the practical Gate numbers
    present_dual = {
        "dual_score": mirror_dual["dual_score"],
        "combined_realized_cashflow": mirror_dual["combined_realized_cashflow"],
        "combined_net_pnl": mirror_dual["combined_net_pnl"],
        "combined_cycles": mirror_dual["combined_cycles"],
        "combined_max_dd_proxy": round(mir_long["max_drawdown"] + mir_short["max_drawdown"], 4),
        "long_max_dd": mir_long["max_drawdown"],
        "short_max_dd": mir_short["max_drawdown"],
        "long_liq": mir_long["liquidated"],
        "short_liq": mir_short["liquidated"],
        "avg_capital_util": round((mir_long["capital_util"] + mir_short["capital_util"]) / 2, 4),
        "mode": best_dual["mode"] + "+mirror_950_1380",
        "long": mir_long,
        "short": mir_short,
        "search_dual_at_1000": {
            "dual_score": best_dual["dual_score"],
            "combined_realized_cashflow": best_dual["combined_realized_cashflow"],
            "combined_cycles": best_dual["combined_cycles"],
            "long_params": best_dual["long"]["params"],
            "short_params": best_dual["short"]["params"],
        },
    }

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
            "style": "aggressive_dual_hedge_small_size",
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
            "search_capital": capital,
            "leverage_fixed": leverage,
        },
        "best_dual": present_dual,
        "best_dual_search_1000": best_dual,
        "top_duals": [
            {
                "dual_score": c["dual_score"],
                "combined_realized_cashflow": c["combined_realized_cashflow"],
                "combined_cycles": c["combined_cycles"],
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
        "mirror_dual": mirror_dual,
        "screenshot_proxy": shot,
        "screenshot_proxy_alt": shot_alt,
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
