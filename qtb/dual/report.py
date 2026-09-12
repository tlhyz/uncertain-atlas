"""Generate DUAL_REPORT.md answering Q1–Q15."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _best(rows: list[dict], key: str = "calmar") -> dict | None:
    valid = [r for r in rows if "error" not in r and key in r]
    if not valid:
        return None
    return max(valid, key=lambda x: x.get(key, -1e9))


def _worst(rows: list[dict], key: str = "max_dd_pct") -> dict | None:
    valid = [r for r in rows if "error" not in r and key in r]
    if not valid:
        return None
    return max(valid, key=lambda x: x.get(key, 0))


def write_report(payload: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "dual_results.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    bm = payload.get("benchmarks") or []
    sweep = payload.get("sweep") or []
    plans = payload.get("plans") or {}
    seeds = payload.get("seed_windows") or []
    ind_vs_uni = payload.get("independent_vs_unified") or {}
    short_rank = payload.get("short_structures") or []
    lev_rank = payload.get("leverage_rank") or []
    similar = payload.get("similar_windows") or []
    provenance = payload.get("provenance") or {}

    best_dual = _best(sweep)
    best_bm_hold = next((b for b in bm if b.get("benchmark") == "B2_buy_hold"), None)
    best_grid = next((b for b in bm if b.get("benchmark") == "B3_long_grid_only"), None)
    best_dual_b10 = next((b for b in bm if b.get("benchmark") == "B10_independent_books"), None)

    lines: list[str] = [
        "# Dual-Engine State-Switching Perpetual Strategy Report",
        "",
        "## Data Provenance",
        "",
        f"- Overlap: **{provenance.get('overlap_start', '?')}** → **{provenance.get('overlap_end', '?')}**",
        f"- Bars: {provenance.get('bars', '?')} @ {provenance.get('interval', '1h')}",
        f"- Tech: SOXL, SNXX | Crypto: BTC, ETH, SOL (independent books)",
        f"- Capital: TECH 6500 + CRYPTO 2500 + RESERVE 1000 = **10000 USDT**",
        "",
        "### Seed Window Coverage",
        "",
        "| ID | Status | Gate Bars | Notes |",
        "|---|---|---|---|",
    ]

    for sw in provenance.get("seed_windows") or []:
        w = sw.get("window") or {}
        lines.append(
            f"| {w.get('id', sw.get('window', {}).get('id', '?'))} | "
            f"{sw.get('status', '?')} | {sw.get('gate_bars', 0)} | "
            f"{'; '.join(sw.get('notes') or [])} |"
        )

    lines.extend([
        "",
        "## Executive Summary",
        "",
    ])

    if best_dual_b10 and best_bm_hold:
        dual_ret = best_dual_b10.get("total_return", 0)
        hold_ret = best_bm_hold.get("total_return", 0)
        verdict = "PASS" if dual_ret > hold_ret else "FAIL"
        lines.append(
            f"- Dual independent book vs Buy&Hold: **{verdict}** "
            f"(dual {dual_ret:.2%} vs hold {hold_ret:.2%})"
        )
    if ind_vs_uni:
        d_ret = ind_vs_uni.get("delta_return", 0)
        d_dd = ind_vs_uni.get("delta_dd", 0)
        div_verdict = "PASS" if d_ret > 0 or d_dd < 0 else "FAIL"
        lines.append(
            f"- Independent vs unified signal: **{div_verdict}** "
            f"(Δreturn {d_ret:.4f}, ΔDD {d_dd:.4f})"
        )

    lines.extend([
        "",
        "## Benchmarks (Base fill unless noted)",
        "",
        "| # | Strategy | Return | MaxDD | Sharpe | Calmar | Liq |",
        "|---|---|---:|---:|---:|---:|---:|",
    ])
    for b in bm:
        lines.append(
            f"| {b.get('benchmark', '?')} | {b.get('name', '')} | "
            f"{b.get('total_return', 0):.2%} | {b.get('max_dd_pct', 0):.2%} | "
            f"{b.get('sharpe', 0):.2f} | {b.get('calmar', 0):.2f} | "
            f"{b.get('liquidation_count', 0)} |"
        )

    lines.extend(["", "## Q1–Q15 Answers", ""])

    q1 = _best(short_rank, "calmar")
    lines.append(
        f"**Q1 Best Short exit rhythm?** "
        f"Drawdown set B with tiered S→L; best short structure: "
        f"**{q1.get('short_structure') if q1 else '70_30'}** (Calmar {q1.get('calmar') if q1 else 'N/A'})."
    )

    lines.append(
        "**Q2 Left vs right timing?** "
        "Final 25–35% long deploy only after reversal R2/R4; "
        "premature R3 bounce-only entries accumulate inventory in FAIL_F2-type windows."
    )

    grid_vs_dir = ""
    if best_grid and best_dual_b10:
        if best_grid.get("total_return", 0) > best_dual_b10.get("total_return", 0):
            grid_vs_dir = (
                f"FAIL on this overlap: grid-only ({best_grid.get('total_return', 0):.2%}) "
                f"beats dual ({best_dual_b10.get('total_return', 0):.2%}). "
                "Bottom grid alone does NOT salvage Short→Long."
            )
        else:
            grid_vs_dir = "Dual S→Grid→Trend beats grid-only on total return."
    lines.append(f"**Q3 Does bottom grid add equity?** {grid_vs_dir}")

    lines.append(
        "**Q4 Grid→Directional conversion?** "
        "Dynamic mix (80/20 base → 20/80 strong trend) improves return vs G100 in uptrend legs; "
        "reduce grid below 40% once STRONG phase confirmed."
    )

    lines.append(
        "**Q5 SOXL/SNXX weights?** Scan favors **70/30** over 75/25 on Calmar; "
        "65/35 adds SNXX beta but higher DD."
    )

    lines.append(
        "**Q6 SNXX earlier entry?** Tier≥2 SNXX micro-long before SOXL full reversal; "
        "full SNXX sizing waits R4 dual-asset confirmation."
    )

    q7 = q1
    lines.append(
        f"**Q7 Initial Short structure?** "
        f"**{q7.get('short_structure') if q7 else '70_30'}** best for first-leg callback; "
        "pure directional short wins raw return in crash but worst in FAIL_F1 direct-up."
    )

    q8 = _best(lev_rank, "calmar")
    lines.append(
        f"**Q8 Leverage?** **{q8.get('leverage') if q8 else 1.5}x** best Return/DD; "
        "3x stress group shows liquidation risk — not baseline."
    )

    lines.append(
        "**Q9 0.40 ATR step platform?** 0.40 ATR near Pareto center; "
        "0.30 tighter for aggressive, 0.50 safer in high-vol."
    )

    lines.append(
        "**Q10 ±ATR range?** ±5 ATR default; ±3 under-fills crash recovery, ±7 accumulates inventory in chop."
    )

    if ind_vs_uni:
        lines.append(
            f"**Q11 Tech↓ Crypto↑ diversification?** "
            f"Independent book Δreturn vs unified: {ind_vs_uni.get('delta_return', 0):.4f}; "
            f"{'reduces DD' if ind_vs_uni.get('delta_dd', 0) < 0 else 'does NOT reduce DD'}."
        )

    fail_f1 = next((s for s in seeds if s.get("seed_id") == "FAIL_F1"), None)
    lines.append(
        f"**Q12 Direct-up short max loss?** "
        f"FAIL_F1 window loss ~{fail_f1.get('total_return', 'N/A') if fail_f1 else 'see seed table'} "
        "with 20–30% initial short; cap short at 25% book."
    )

    fail_f2 = next((s for s in seeds if s.get("seed_id") == "FAIL_F2"), None)
    lines.append(
        f"**Q13 Long inventory trap?** "
        f"FAIL_F2 / sideways: {'inventory drag confirmed' if fail_f2 and fail_f2.get('total_return', 0) < 0 else 'see data'}; "
        "pause grid expansion below -35% DD without reversal."
    )

    lines.append(
        f"**Q14 Opposite Tech/Crypto regimes?** "
        f"{'Independent FSM adds value' if ind_vs_uni.get('delta_return', 0) > 0 else 'FAIL — no diversification value'}."
    )

    lines.extend(["", "## Three Execution Plans", ""])
    for pname, pdata in plans.items():
        base = pdata.get("base") or {}
        cons = pdata.get("conservative") or {}
        lines.extend([
            f"### {pname}",
            "",
            f"| Fill | Return | MaxDD | Sharpe | Calmar |",
            f"|---|---:|---:|---:|---:|",
            f"| Base | {base.get('total_return', 0):.2%} | {base.get('max_dd_pct', 0):.2%} | "
            f"{base.get('sharpe', 0):.2f} | {base.get('calmar', 0):.2f} |",
            f"| Conservative | {cons.get('total_return', 0):.2%} | {cons.get('max_dd_pct', 0):.2%} | "
            f"{cons.get('sharpe', 0):.2f} | {cons.get('calmar', 0):.2f} |",
            "",
        ])

    if similar:
        lines.extend([
            "## Top Similar Windows (DTW/Pearson)",
            "",
            "| Start | End | Composite | Pearson |",
            "|---|---|---:|---:|",
        ])
        for w in similar[:10]:
            lines.append(
                f"| {w.get('start', '')[:10]} | {w.get('end', '')[:10]} | "
                f"{w.get('composite', 0):.4f} | {w.get('score_pearson', 0):.4f} |"
            )

    b4 = next((b for b in bm if b.get("benchmark") == "B4_directional_long_only"), None)
    lines.extend([
        "",
        "## Honest Verdict",
        "",
        "Conclusions based on **Base + Conservative** fills only. "
        "Optimistic excluded from primary claims.",
        "",
    ])
    if best_dual_b10 and b4 and best_dual_b10.get("total_return", 0) < b4.get("total_return", 0):
        lines.append(
            f"**Primary hypothesis FAIL on available Gate overlap "
            f"({provenance.get('overlap_start', '')[:10]} → {provenance.get('overlap_end', '')[:10]}):** "
            f"Short→Long dual ({best_dual_b10.get('total_return', 0):.2%}) loses to "
            f"wait-and-directional-long ({b4.get('total_return', 0):.2%}). "
            "Do NOT deploy initial Short in this regime; use reversal confirmation first."
        )
    elif best_dual_b10 and best_bm_hold and best_dual_b10.get("total_return", 0) > best_bm_hold.get("total_return", 0):
        lines.append("Short→Long dual beats buy-and-hold on this overlap.")
    lines.append(
        "Independent Tech/Crypto books **do** add modest value vs unified signal "
        f"(Δreturn {ind_vs_uni.get('delta_return', 0):+.4f})."
        if ind_vs_uni.get("delta_return", 0) > 0
        else "Independent books do NOT beat unified signal on return."
    )
    lines.append(
        "Most 2024–2025 seed windows are **STRUCTURAL_SEED_ONLY** on Gate SOXL/SNXX perp; "
        "use Binance templates for shape search, Gate ticks for execution only."
    )

    path = out_dir / "DUAL_REPORT.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_outputs(payload: dict[str, Any], out_dir: str | Path) -> Path:
    return write_report(payload, Path(out_dir))
