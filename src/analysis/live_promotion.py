"""Live candidate promotion gate checklist (P6-02/03/05)."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

GateStatus = Literal["pass", "fail", "blocked", "conditional", "n/a"]

ASSET_GATE_IDS = ("BTC", "ETH", "SOL")


@dataclass(frozen=True)
class PromotionGate:
    gate_id: str
    label: str
    status: GateStatus
    evidence: str
    blocks_promotion: bool
    required: bool = True


@dataclass
class PromotionReport:
    asset: str
    current_confidence: str
    recommended_confidence: str
    promotion_verdict: Literal["PASS", "FAIL", "BLOCKED"]
    gates: list[PromotionGate] = field(default_factory=list)
    supporting: list[str] = field(default_factory=list)
    contradicting: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def n_blocking_failures(self) -> int:
        return sum(1 for g in self.gates if g.blocks_promotion and g.status in ("fail", "blocked"))

    def as_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["gates"] = [asdict(g) for g in self.gates]
        d["n_blocking_failures"] = self.n_blocking_failures
        return d


def _crypto_gates(asset: str) -> list[PromotionGate]:
    """Shared P5/P2 gates for BTC/ETH/SOL crypto grid rows."""
    oos = {
        "BTC": ("fail", "P5-04 holdout 2024: −86.44%; oos_pass=no"),
        "ETH": ("fail", "P5-04: ETH not holdout-tested; P2-03 all lev ~−87.5%"),
        "SOL": ("fail", "P5-04: SOL not holdout-tested; P2-04 all lev −88.01%"),
    }
    c1 = {
        "BTC": ("fail", "P2-02 C1 tick: all lev −87.06% to −87.47% (C-06)"),
        "ETH": ("fail", "P2-03 C1 tick: all lev ~−87.5% (C-06)"),
        "SOL": ("fail", "P2-04 C1 tick: all lev −88.01%; crypto_max_dd=100% (C-06)"),
    }
    ab = {
        "BTC": ("conditional", "C-02 A/B PERP>ETF BAR only; different engine than C1 FSM"),
        "ETH": ("conditional", "C-02 A/B PERP>ETF BAR only; different engine than C1 FSM"),
        "SOL": ("conditional", "C-02 A/B PERP>ETF BAR only; 3x liq history (C-03)"),
    }
    oos_status, oos_ev = oos[asset]
    c1_status, c1_ev = c1[asset]
    ab_status, ab_ev = ab[asset]

    return [
        PromotionGate(
            "oos_holdout",
            "Temporal OOS holdout pass",
            oos_status,
            oos_ev,
            blocks_promotion=oos_status == "fail",
        ),
        PromotionGate(
            "walk_forward",
            "Calendar walk-forward OOS",
            "fail",
            "P5-03 mean test −86.58% (BTC calendar folds)",
            blocks_promotion=True,
        ),
        PromotionGate(
            "mc_dd_tail",
            "Monte Carlo DD tail risk",
            "fail",
            "P5-05 P(DD>20%)=89% on 65d dual-book (crypto row inherits portfolio risk)",
            blocks_promotion=True,
        ),
        PromotionGate(
            "c1_tick_edge",
            "C1 tick-precise crypto grid edge",
            c1_status,
            c1_ev,
            blocks_promotion=c1_status == "fail",
        ),
        PromotionGate(
            "param_plateau",
            "Default ATR step on plateau",
            "fail",
            "P5-02 PLATEAU_INERT; 0.40 worst Calmar (W-02 retracted)",
            blocks_promotion=True,
        ),
        PromotionGate(
            "gate_fill_cal",
            "Gate execution fill calibration",
            "conditional",
            "P6-01 BAR BTC 1h fill_ratio 0.986; tick path N/A",
            blocks_promotion=False,
            required=False,
        ),
        PromotionGate(
            "ab_perp_vs_etf",
            "A/B PERP beats ETF (bar)",
            ab_status,
            ab_ev,
            blocks_promotion=False,
            required=False,
        ),
        PromotionGate(
            "portfolio_c07",
            "Dual-book robustness (C-07)",
            "fail",
            "C-07: OOS+MC gates FAIL; no live promotion",
            blocks_promotion=True,
        ),
    ]


def evaluate_promotion(asset: str, *, current_confidence: str = "MEDIUM") -> PromotionReport:
    asset = asset.upper()
    if asset not in ASSET_GATE_IDS:
        raise ValueError(f"unsupported asset {asset!r}; expected one of {ASSET_GATE_IDS}")

    gates = _crypto_gates(asset)
    blocking = [g for g in gates if g.blocks_promotion and g.status in ("fail", "blocked")]

    supporting = [g.evidence for g in gates if g.status in ("pass", "conditional") and not g.blocks_promotion]
    contradicting = [f"{g.gate_id}: {g.evidence}" for g in blocking]

    if any(g.status == "blocked" for g in gates if g.blocks_promotion):
        verdict: Literal["PASS", "FAIL", "BLOCKED"] = "BLOCKED"
        recommended = current_confidence
    elif blocking:
        verdict = "FAIL"
        recommended = "LOW"
    else:
        verdict = "PASS"
        recommended = "MEDIUM" if current_confidence == "LOW" else current_confidence

    notes = [
        "ROADMAP L11 requires OOS PASS + Robustness PASS + Base/Conservative PASS + Risk PASS",
        f"{len(blocking)} blocking gate(s) fail for {asset}",
    ]
    if verdict == "FAIL" and current_confidence == "MEDIUM":
        notes.append("Demote stale MEDIUM → LOW; A/B bar win does not satisfy P5 gates")

    return PromotionReport(
        asset=asset,
        current_confidence=current_confidence,
        recommended_confidence=recommended,
        promotion_verdict=verdict,
        gates=gates,
        supporting=supporting,
        contradicting=contradicting,
        notes=notes,
    )


def render_promotion_markdown(report: PromotionReport) -> str:
    lines = [
        f"# Promotion Gate — {report.asset}",
        "",
        f"- **Current confidence:** {report.current_confidence}",
        f"- **Recommended:** {report.recommended_confidence}",
        f"- **Verdict:** **{report.promotion_verdict}** ({report.n_blocking_failures} blocking failures)",
        "",
        "## Gates",
        "",
        "| Gate | Status | Blocks | Evidence |",
        "|------|--------|:------:|----------|",
    ]
    for g in report.gates:
        block = "yes" if g.blocks_promotion else "no"
        lines.append(f"| {g.label} | **{g.status}** | {block} | {g.evidence} |")

    lines.extend(["", "## Supporting (insufficient alone)", ""])
    for s in report.supporting:
        lines.append(f"- {s}")

    lines.extend(["", "## Contradicting", ""])
    for c in report.contradicting:
        lines.append(f"- {c}")

    lines.extend(["", "## Notes", ""])
    for n in report.notes:
        lines.append(f"- {n}")
    return "\n".join(lines) + "\n"
