"""Generate DUAL_REPORT.md answering Q1–Q15 from measured experiment payload."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _best(rows: list[dict], key: str = "calmar") -> dict | None:
    valid = [r for r in rows if "error" not in r and key in r]
    if not valid:
        return None
    return max(valid, key=lambda x: x.get(key, -1e9))


def _best_by_group(rows: list[dict], group_key: str, metric: str = "calmar") -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in rows:
        if "error" in r:
            continue
        val = r.get(group_key)
        if val is None and isinstance(r.get("tech"), dict):
            val = r["tech"].get(group_key)
        if val is None:
            continue
        key = str(val)
        if key not in out or r.get(metric, -1e9) > out[key].get(metric, -1e9):
            out[key] = r
    return out


def _fmt_row(r: dict | None, metric: str = "calmar") -> str:
    if not r:
        return "N/A (not measured)"
    return f"{r.get(metric, 'N/A'):.4f}" if isinstance(r.get(metric), (int, float)) else str(r.get(metric))


def _execution_label(provenance: dict[str, Any]) -> str:
    ex = provenance.get("execution") or ""
    src = provenance.get("source") or "unknown"
    if "tick" in str(ex).lower():
        return f"**TICK BACKTEST** ({src}; {ex})"
    return f"**BAR BACKTEST** ({src})"


def _build_q_answers(payload: dict[str, Any]) -> list[str]:
    bm = payload.get("benchmarks") or []
    sweep = [r for r in (payload.get("sweep") or []) if r.get("fill") == "base"]
    short_rank = payload.get("short_structures") or []
    lev_rank = payload.get("leverage_rank") or []
    grid_atr_rank = payload.get("grid_atr_rank") or []
    seeds = payload.get("seed_windows") or []
    ind_vs_uni = payload.get("independent_vs_unified") or {}
    stress = payload.get("stress_3x") or {}

    best_grid = next((b for b in bm if b.get("benchmark") == "B3_long_grid_only"), None)
    best_dual_b10 = next((b for b in bm if b.get("benchmark") == "B10_independent_books"), None)
    best_b4 = next((b for b in bm if b.get("benchmark") == "B4_directional_long_only"), None)

    dd_best = _best_by_group(sweep, "drawdown_set")
    rev_best = _best_by_group(sweep, "reversal")
    mix_best = _best_by_group(sweep, "grid_mix")
    weight_best = _best_by_group(sweep, "soxl_weight")
    q1_short = _best(short_rank, "calmar")
    q8_lev = _best(lev_rank, "calmar")
    q9_step = _best_by_group(grid_atr_rank, "grid_atr_step")
    q10_range = _best_by_group(grid_atr_rank, "grid_atr_range")
    best_atr = _best(grid_atr_rank, "calmar")

    lines: list[str] = []

    # Q1
    best_dd_set = max(dd_best.items(), key=lambda kv: kv[1].get("calmar", -1e9))[0] if dd_best else "B"
    lines.append(
        f"**Q1 Best Short exit rhythm?** "
        f"Sweep best drawdown set **{best_dd_set}** (Calmar {_fmt_row(dd_best.get(best_dd_set))}); "
        f"best short structure **{q1_short.get('short_structure') if q1_short else 'N/A'}** "
        f"(Calmar {_fmt_row(q1_short)})."
    )

    # Q2
    if rev_best:
        best_rev = max(rev_best.items(), key=lambda kv: kv[1].get("calmar", -1e9))
        rev_line = ", ".join(f"{k}: Calmar {v.get('calmar', 0):.2f}" for k, v in sorted(rev_best.items()))
        lines.append(
            f"**Q2 Left vs right timing?** Sweep reversal rules ({rev_line}). "
            f"Best: **{best_rev[0]}** (Calmar {best_rev[1].get('calmar', 0):.2f}). "
            f"Measured on overlap — not a universal timing claim."
        )
    else:
        lines.append("**Q2 Left vs right timing?** Not measured (sweep empty).")

    # Q3
    if best_grid and best_dual_b10:
        g_ret = best_grid.get("total_return", 0)
        d_ret = best_dual_b10.get("total_return", 0)
        if g_ret > d_ret:
            lines.append(
                f"**Q3 Does bottom grid add equity?** **FAIL** on overlap: grid-only ({g_ret:.2%}) "
                f"beats dual ({d_ret:.2%}). Bottom grid alone does NOT salvage Short→Long."
            )
        else:
            lines.append(
                f"**Q3 Does bottom grid add equity?** Dual ({d_ret:.2%}) beats grid-only ({g_ret:.2%}) on this overlap."
            )
    else:
        lines.append("**Q3 Does bottom grid add equity?** Not measured (missing benchmarks).")

    # Q4
    if mix_best:
        best_mix = max(mix_best.items(), key=lambda kv: kv[1].get("calmar", -1e9))
        lines.append(
            f"**Q4 Grid→Directional conversion?** Sweep grid_mix best **{best_mix[0]}** "
            f"(Calmar {best_mix[1].get('calmar', 0):.2f}, return {best_mix[1].get('total_return', 0):.2%})."
        )
    else:
        lines.append("**Q4 Grid→Directional conversion?** Not measured in sweep.")

    # Q5
    if weight_best:
        parts = ", ".join(
            f"{int(float(k)*100)}/{int((1-float(k))*100)}: Calmar {v.get('calmar', 0):.2f}"
            for k, v in sorted(weight_best.items(), key=lambda x: float(x[0]), reverse=True)
        )
        best_w = max(weight_best.items(), key=lambda kv: kv[1].get("calmar", -1e9))
        lines.append(
            f"**Q5 SOXL/SNXX weights?** Measured: {parts}. "
            f"Best Calmar: **{float(best_w[0]):.0%}/{1-float(best_w[0]):.0%}**."
        )
    else:
        lines.append("**Q5 SOXL/SNXX weights?** Not measured in sweep.")

    lines.append(
        "**Q6 SNXX earlier entry?** Not isolated in current sweep matrix — requires dedicated SNXX-lead experiment."
    )

    lines.append(
        f"**Q7 Initial Short structure?** Ranked: "
        + ", ".join(
            f"{r.get('short_structure')}: Calmar {r.get('calmar', 0):.2f}"
            for r in short_rank[:4]
        )
        + f". Best: **{q1_short.get('short_structure') if q1_short else 'N/A'}**."
    )

    lines.append(
        f"**Q8 Leverage?** Ranked: "
        + ", ".join(f"{r.get('leverage')}x: Calmar {r.get('calmar', 0):.2f}" for r in lev_rank)
        + f". Best: **{q8_lev.get('leverage') if q8_lev else 'N/A'}x**."
        + (f" 3x stress: return {stress.get('total_return', 0):.2%}, liq={stress.get('liquidation_count', 0)}." if stress else "")
    )

    if best_atr and q9_step:
        step_parts = ", ".join(
            f"{k}: Calmar {v.get('calmar', 0):.2f}" for k, v in sorted(q9_step.items(), key=lambda x: float(x[0]))
        )
        lines.append(
            f"**Q9 0.40 ATR step platform?** Measured grid_atr_step sweep: {step_parts}. "
            f"Best step **{best_atr.get('grid_atr_step')}** (Calmar {best_atr.get('calmar', 0):.2f}). "
            f"Plateau = multiple adjacent steps within 15% Calmar of best."
        )
    else:
        lines.append("**Q9 0.40 ATR step platform?** Not measured (grid_atr_rank missing).")

    if q10_range:
        rng_parts = ", ".join(
            f"±{k}: Calmar {v.get('calmar', 0):.2f}" for k, v in sorted(q10_range.items(), key=lambda x: float(x[0]))
        )
        best_rng = max(q10_range.items(), key=lambda kv: kv[1].get("calmar", -1e9))
        lines.append(
            f"**Q10 ±ATR range?** Measured: {rng_parts}. Best: **±{best_rng[0]}** ATR."
        )
    else:
        lines.append("**Q10 ±ATR range?** Not measured (grid_atr_rank missing).")

    d_ret = ind_vs_uni.get("delta_return", 0)
    d_dd = ind_vs_uni.get("delta_dd", 0)
    lines.append(
        f"**Q11 Tech↓ Crypto↑ diversification?** Δreturn {d_ret:+.4f}, ΔDD {d_dd:+.4f} "
        f"(independent − unified). {'Independent helps' if d_ret > 0 or d_dd < 0 else 'No measured benefit'}."
    )

    fail_f1 = next((s for s in seeds if s.get("seed_id") == "FAIL_F1"), None)
    if fail_f1 and fail_f1.get("status") == "STRUCTURAL_SEED_ONLY":
        lines.append("**Q12 Direct-up short max loss?** FAIL_F1 **STRUCTURAL_SEED_ONLY** — no execution backtest on Binance/Gate overlap.")
    elif fail_f1 and "total_return" in fail_f1:
        lines.append(
            f"**Q12 Direct-up short max loss?** FAIL_F1 measured return **{fail_f1.get('total_return', 0):.2%}** "
            f"(pattern: {fail_f1.get('pattern', '?')})."
        )
    else:
        lines.append("**Q12 Direct-up short max loss?** FAIL_F1 not executable on available data.")

    fail_f2 = next((s for s in seeds if s.get("seed_id") == "FAIL_F2"), None)
    if fail_f2 and fail_f2.get("status") == "STRUCTURAL_SEED_ONLY":
        lines.append("**Q13 Long inventory trap?** FAIL_F2 **STRUCTURAL_SEED_ONLY** — not execution-tested.")
    elif fail_f2 and "total_return" in fail_f2:
        lines.append(
            f"**Q13 Long inventory trap?** FAIL_F2 return **{fail_f2.get('total_return', 0):.2%}** "
            f"({'inventory drag' if fail_f2.get('total_return', 0) < 0 else 'see data'})."
        )
    else:
        lines.append("**Q13 Long inventory trap?** FAIL_F2 not executable on available data.")

    lines.append(
        f"**Q14 Opposite Tech/Crypto regimes?** "
        f"{'Independent FSM adds value' if d_ret > 0 else 'FAIL — no return benefit'} "
        f"(Δreturn {d_ret:+.4f}); DD {'improves' if d_dd < 0 else 'does not improve'} (ΔDD {d_dd:+.4f})."
    )

    lines.append(
        f"**Q15 Reserve / plans?** See Three Execution Plans below; best sweep Calmar {_fmt_row(_best(sweep))} "
        f"(params: {_best(sweep).get('params') if _best(sweep) else 'N/A'})."
    )

    return lines


def write_report(payload: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "dual_results.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    bm = payload.get("benchmarks") or []
    plans = payload.get("plans") or {}
    seeds = payload.get("seed_windows") or []
    ind_vs_uni = payload.get("independent_vs_unified") or {}
    similar = payload.get("similar_windows") or []
    provenance = payload.get("provenance") or {}

    best_dual_b10 = next((b for b in bm if b.get("benchmark") == "B10_independent_books"), None)
    best_bm_hold = next((b for b in bm if b.get("benchmark") == "B2_buy_hold"), None)
    best_b4 = next((b for b in bm if b.get("benchmark") == "B4_directional_long_only"), None)

    tech_syms = provenance.get("tech_symbols") or ["SOXL", "SNXX"]
    crypto_syms = provenance.get("crypto_symbols") or ["BTC", "ETH", "SOL"]

    lines: list[str] = [
        "# Dual-Engine State-Switching Perpetual Strategy Report",
        "",
        "## Data Provenance",
        "",
        f"- Overlap: **{provenance.get('overlap_start', '?')}** → **{provenance.get('overlap_end', '?')}**",
        f"- Bars: {provenance.get('bars', '?')} @ {provenance.get('interval', '1h')}",
        f"- Execution: {_execution_label(provenance)}",
        f"- Tech: {', '.join(tech_syms)} | Crypto: {', '.join(crypto_syms)} (independent books)",
        f"- Capital: TECH 6500 + CRYPTO 2500 + RESERVE 1000 = **10000 USDT**",
        "",
        "### Seed Window Coverage",
        "",
        "| ID | Status | Bars | Notes |",
        "|---|---|---|---|",
    ]

    for sw in provenance.get("seed_windows") or seeds:
        w = sw.get("window") or {}
        wid = w.get("id") or sw.get("seed_id", "?")
        lines.append(
            f"| {wid} | {sw.get('status', '?')} | {sw.get('gate_bars', sw.get('bars', 0))} | "
            f"{'; '.join(sw.get('notes') or [])} |"
        )

    lines.extend(["", "## Executive Summary", ""])

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

    lines.extend(["", "## Q1–Q15 Answers (from measured payload)", ""])
    lines.extend(_build_q_answers(payload))

    lines.extend(["", "## Three Execution Plans", ""])
    for pname, pdata in plans.items():
        base = pdata.get("base") or {}
        cons = pdata.get("conservative") or {}
        lines.extend([
            f"### {pname}",
            "",
            "| Fill | Return | MaxDD | Sharpe | Calmar |",
            "|---|---:|---:|---:|---:|",
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

    c1 = payload.get("binance_crypto_c1") or {}
    if c1 and "error" not in c1:
        lines.extend([
            "",
            "## CRYPTO_C1 — Binance aggTrades (2024-09 → 2024-11)",
            "",
            f"- aggTrades rows: {c1.get('aggTrades_cached_rows')}",
            f"- Independent return: **{c1.get('independent', {}).get('total_return', 0):.2%}**",
            f"- Unified return: **{c1.get('unified', {}).get('total_return', 0):.2%}**",
            f"- Δreturn: **{c1.get('delta_return', 0):+.4f}**",
            "",
        ])
    elif c1.get("error"):
        lines.extend([
            "",
            "## CRYPTO_C1 — Binance aggTrades",
            "",
            f"Not run: `{c1.get('error')}`",
            "",
        ])

    lines.extend([
        "",
        "## Honest Verdict",
        "",
        "Conclusions based on **Base + Conservative** fills only. Optimistic excluded.",
        "",
    ])

    if best_dual_b10 and best_b4 and best_dual_b10.get("total_return", 0) < best_b4.get("total_return", 0):
        lines.append(
            f"**Primary hypothesis FAIL on overlap "
            f"({str(provenance.get('overlap_start', ''))[:10]} → {str(provenance.get('overlap_end', ''))[:10]}):** "
            f"Short→Long dual ({best_dual_b10.get('total_return', 0):.2%}) loses to "
            f"directional-long ({best_b4.get('total_return', 0):.2%})."
        )
    elif best_dual_b10 and best_bm_hold and best_dual_b10.get("total_return", 0) > best_bm_hold.get("total_return", 0):
        lines.append("Short→Long dual beats buy-and-hold on this overlap.")

    d_ret = ind_vs_uni.get("delta_return", 0)
    if d_ret > 0:
        lines.append(f"Independent books beat unified on return (Δreturn {d_ret:+.4f}).")
    else:
        lines.append(f"Independent books do NOT beat unified on return (Δreturn {d_ret:+.4f}).")

    struct_only = sum(
        1 for sw in (provenance.get("seed_windows") or seeds)
        if sw.get("status") == "STRUCTURAL_SEED_ONLY"
    )
    if struct_only:
        lines.append(
            f"{struct_only} seed window(s) are **STRUCTURAL_SEED_ONLY** — no execution claims on those periods."
        )

    path = out_dir / "DUAL_REPORT.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_outputs(payload: dict[str, Any], out_dir: str | Path) -> Path:
    return write_report(payload, Path(out_dir))
