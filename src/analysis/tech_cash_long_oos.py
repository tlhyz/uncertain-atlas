"""P6-04 — Tech Short→Long vs Cash→Long (B4) OOS holdout evaluation."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal

from src.analysis.oos_holdout import holdout_bar_split, summarize_candidate
from src.analysis.walk_forward import slice_index_range


@dataclass
class TechCashLongOosReport:
    holdout_window: str
    holdout_bars: int
    tech_fsm_return: float
    b4_cash_long_return: float
    delta_pp: float
    tech_beats_b4: bool
    in_sample_tech_return: float
    in_sample_b4_return: float
    in_sample_delta_pp: float
    execution: str
    verdict: Literal["PASS", "FAIL"]
    notes: list[str]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _slice_bars(data, i0: int, i1: int):
    from qtb.dual.data import slice_window

    start, end = slice_index_range(data.aligned_index, i0, i1)
    return slice_window(data, start, end)


def _run_tech_fsm(data, i0: int, i1: int, *, initial: float, pk: dict) -> dict:
    from qtb.dual.experiments import summarize_portfolio
    from qtb.dual.portfolio import run_dual_portfolio
    from qtb.dual.universe import DualParams

    sub = _slice_bars(data, i0, i1)
    r = run_dual_portfolio(
        sub,
        DualParams(unified_signal=False),
        name=f"tech_fsm_{i0}_{i1}",
        fill_mode=str(pk.get("fill_mode", "base")),
        tick_precise=bool(pk.get("tick_precise", False)),
        crypto_tick_fills=bool(pk.get("crypto_tick_fills", False)),
        tech_tick_fills=bool(pk.get("tech_tick_fills", True)),
        tech_tick_only=bool(pk.get("tech_tick_only", False)),
    )
    return summarize_portfolio(r, initial=initial)


def _run_b4(data, i0: int, i1: int, *, initial: float, pk: dict) -> dict:
    from qtb.dual.experiments import summarize_portfolio
    from qtb.dual.portfolio import run_dual_portfolio
    from qtb.dual.universe import DualParams

    sub = _slice_bars(data, i0, i1)
    r = run_dual_portfolio(
        sub,
        DualParams(),
        name=f"B4_{i0}_{i1}",
        fill_mode=str(pk.get("fill_mode", "base")),
        benchmark="B4_directional_long_only",
        tick_precise=bool(pk.get("tick_precise", False)),
        tech_tick_fills=bool(pk.get("tech_tick_fills", True)),
    )
    return summarize_portfolio(r, initial=initial)


def evaluate_tech_vs_cash_long_oos(
    data,
    *,
    initial: float,
    holdout_fraction: float = 0.25,
    portfolio_kwargs: dict | None = None,
    in_sample_refs: tuple[float, float] | None = None,
) -> TechCashLongOosReport:
    """Compare default Tech FSM dual vs B4 Cash→Long proxy on temporal holdout."""
    pk = portfolio_kwargs or {}
    n = len(data.aligned_index)
    split = holdout_bar_split(n, holdout_fraction=holdout_fraction)
    if not split:
        raise ValueError(f"holdout split failed for n={n}")

    (_, _), (te0, te1) = split
    t0, t1 = slice_index_range(data.aligned_index, te0, te1)

    hold_tech = _run_tech_fsm(data, te0, te1, initial=initial, pk=pk)
    hold_b4 = _run_b4(data, te0, te1, initial=initial, pk=pk)

    if in_sample_refs is not None:
        full_tech_r, full_b4_r = in_sample_refs
    else:
        full_tech = _run_tech_fsm(data, 0, n, initial=initial, pk=pk)
        full_b4 = _run_b4(data, 0, n, initial=initial, pk=pk)
        full_tech_r = float(full_tech["total_return"])
        full_b4_r = float(full_b4["total_return"])

    tech_r = float(hold_tech["total_return"])
    b4_r = float(hold_b4["total_return"])
    delta_pp = (tech_r - b4_r) * 100.0
    beats = tech_r > b4_r

    notes = [
        "Tech FSM = dual independent book (default Short→Long path)",
        "B4 = directional-long-only Cash→Long proxy on SOXL tech leg",
        f"Holdout last {holdout_fraction:.0%} of aligned window",
    ]
    if not beats:
        notes.append("Tech FAIL vs B4 — do not promote Tech row to live candidate")

    return TechCashLongOosReport(
        holdout_window=f"{t0}→{t1}",
        holdout_bars=te1 - te0,
        tech_fsm_return=tech_r,
        b4_cash_long_return=b4_r,
        delta_pp=delta_pp,
        tech_beats_b4=beats,
        in_sample_tech_return=full_tech_r,
        in_sample_b4_return=full_b4_r,
        in_sample_delta_pp=(full_tech_r - full_b4_r) * 100.0,
        execution=str(pk.get("execution_label", "TICK tech + BAR crypto")),
        verdict="PASS" if beats else "FAIL",
        notes=notes,
    )


def render_tech_cash_long_markdown(report: TechCashLongOosReport) -> str:
    lines = [
        "# Tech vs Cash→Long OOS",
        "",
        f"- **Holdout:** {report.holdout_window} ({report.holdout_bars} bars)",
        f"- **Execution:** {report.execution}",
        f"- **Verdict:** **{report.verdict}**",
        "",
        "## Holdout (OOS)",
        "",
        "| Strategy | Return | vs B4 |",
        "|----------|-------:|------:|",
        f"| B4 Cash→Long proxy | {100*report.b4_cash_long_return:.2f}% | — |",
        f"| Tech FSM (dual default) | {100*report.tech_fsm_return:.2f}% | **{report.delta_pp:+.2f}pp** |",
        "",
        "## In-sample (full window reference)",
        "",
        f"| Tech FSM | {100*report.in_sample_tech_return:.2f}% |",
        f"| B4 | {100*report.in_sample_b4_return:.2f}% |",
        f"| Delta | {report.in_sample_delta_pp:+.2f}pp |",
        "",
        "## Notes",
        "",
    ]
    for n in report.notes:
        lines.append(f"- {n}")
    return "\n".join(lines) + "\n"
