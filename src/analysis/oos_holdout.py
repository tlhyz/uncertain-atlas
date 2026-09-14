"""OOS holdout report utilities — STEP 9 (P5-04)."""

from __future__ import annotations

from typing import Any


def holdout_bar_split(n: int, holdout_fraction: float = 0.25) -> tuple[tuple[int, int], tuple[int, int]] | None:
    """Return (train_range, holdout_range) as half-open [i0, i1) bar indices."""
    if n < 200:
        return None
    cut = max(int(n * (1.0 - holdout_fraction)), 100)
    if cut >= n - 50:
        cut = n - max(50, int(n * 0.15))
    return (0, cut), (cut, n)


def holdout_year_split(
    years: list[int],
    *,
    holdout_year: int,
) -> tuple[list[int], list[int]] | None:
    """Train years strictly before *holdout_year*; holdout is *holdout_year*."""
    if holdout_year not in years:
        return None
    train = [y for y in years if y < holdout_year]
    if len(train) < 2:
        return None
    return train, [holdout_year]


def oos_pass(
    holdout: dict[str, Any],
    *,
    benchmark_return: float | None = None,
    min_return: float = 0.0,
) -> bool:
    """True when holdout beats benchmark (if set) and exceeds *min_return*."""
    ret = float(holdout.get("total_return", 0))
    if ret <= min_return:
        return False
    if benchmark_return is not None and ret <= benchmark_return:
        return False
    return True


def summarize_candidate(
    candidate_id: str,
    *,
    label: str,
    train: dict[str, Any] | None,
    holdout: dict[str, Any],
    holdout_window: str,
    train_window: str = "",
    benchmark_return: float | None = None,
    execution: str = "",
    notes: list[str] | None = None,
) -> dict[str, Any]:
    """Build one finalist OOS row."""
    row: dict[str, Any] = {
        "id": candidate_id,
        "label": label,
        "train_window": train_window,
        "holdout_window": holdout_window,
        "execution": execution,
        "holdout_return": float(holdout.get("total_return", 0)),
        "holdout_calmar": float(holdout.get("calmar", 0)),
        "holdout_max_dd_pct": float(holdout.get("max_dd_pct", 0)),
        "holdout_liquidated": int(holdout.get("liquidation_count", 0)) > 0,
        "oos_pass": oos_pass(holdout, benchmark_return=benchmark_return),
        "benchmark_return": benchmark_return,
        "notes": notes or [],
    }
    if train:
        row["train_return"] = float(train.get("total_return", 0))
        row["generalization_gap"] = row["train_return"] - row["holdout_return"]
    return row


def build_oos_report(
    candidates: list[dict[str, Any]],
    *,
    holdout_policy: str,
    meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Aggregate finalist OOS holdout report."""
    passed = [c for c in candidates if c.get("oos_pass")]
    return {
        "holdout_policy": holdout_policy,
        "meta": meta or {},
        "n_candidates": len(candidates),
        "n_pass": len(passed),
        "candidates": candidates,
        "verdict": "PASS" if passed else "FAIL",
        "all_fail": len(candidates) > 0 and not passed,
    }


def render_oos_markdown(report: dict[str, Any]) -> str:
    """Render human-readable OOS holdout report."""
    lines = [
        "# OOS Holdout Report — Finalists",
        "",
        f"- **Policy:** {report.get('holdout_policy')}",
        f"- **Verdict:** **{report.get('verdict')}** ({report.get('n_pass')}/{report.get('n_candidates')} pass)",
        "",
        "| ID | Holdout window | Return | Calmar | OOS pass |",
        "|----|----------------|-------:|-------:|:--------:|",
    ]
    for c in report.get("candidates") or []:
        ok = "yes" if c.get("oos_pass") else "**no**"
        lines.append(
            f"| {c.get('id')} | {c.get('holdout_window')} "
            f"| {100 * float(c.get('holdout_return', 0)):.2f}% "
            f"| {float(c.get('holdout_calmar', 0)):.2f} "
            f"| {ok} |"
        )
    gate = (report.get("meta") or {}).get("gate_oos")
    if gate:
        lines.extend(["", "## Gate OOS", "", f"- Status: **{gate.get('status')}** — {gate.get('reason', '')}"])
    lines.append("")
    return "\n".join(lines)
