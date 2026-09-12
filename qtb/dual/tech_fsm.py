"""Tech book state machine: Short → Neutral → Long Grid → Directional Long."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

import numpy as np

from .signals import check_reversal, grid_mix_fractions, thresholds_for
from .universe import TechParams

TechPhase = Literal["T0", "T1", "T2", "T3", "T4", "REVERSAL", "TREND", "STRONG", "NEUTRAL"]


@dataclass
class TechExposure:
    """Target fractions of TECH_BOOK capital (0..1 each, not necessarily summing to 1)."""
    short_notional_frac: float = 0.0
    long_grid_frac: float = 0.0
    long_dir_frac: float = 0.0
    cash_frac: float = 1.0
    snxx_long_frac: float = 0.0
    phase: TechPhase = "T0"
    dd_tier: int = 0
    reversal_confirmed: bool = False
    allow_new_short: bool = True
    pause_long_grid: bool = False


@dataclass
class TechFSM:
    params: TechParams
    init_short_budget: float = 0.0
    remaining_short_frac: float = 1.0
    tier: int = 0
    reversal_confirmed: bool = False
    phase: TechPhase = "T0"
    trend_strength: int = 0
    last_dd: float = 0.0
    history: list[dict] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.init_short_budget = self.params.short_init_pct

    def _short_structure_split(self) -> tuple[float, float]:
        """Return (directional_short_frac, grid_short_frac) of short leg."""
        s = self.params.short_structure
        if s == "directional":
            return 1.0, 0.0
        if s == "grid":
            return 0.0, 1.0
        if s == "70_30":
            return 0.70, 0.30
        return 0.50, 0.50

    def on_bar(
        self,
        i: int,
        dd: float,
        close: np.ndarray,
        high: np.ndarray,
        low: np.ndarray,
        snxx_close: np.ndarray | None = None,
    ) -> TechExposure:
        th = thresholds_for(self.params.drawdown_set)
        new_tier = sum(1 for t in th if dd <= t)
        if new_tier > self.tier:
            self.tier = new_tier
            self._apply_tier_transition(new_tier)

        # Reversal confirmation for final 25-35% deployment
        if self.tier >= 2 and not self.reversal_confirmed:
            bounce = {"R1": 0.10, "R2": 0.15, "R3": 0.15, "R4": 0.10}.get(self.params.reversal, 0.15)
            if self.params.reversal == "R3":
                bounce = 0.15
            if check_reversal(
                self.params.reversal, i, close, high, low, snxx_close, bounce_pct=bounce
            ):
                self.reversal_confirmed = True
                self.phase = "REVERSAL"

        # Trend phase escalation
        if self.reversal_confirmed and dd > th[0] * 0.5:
            self.trend_strength += 1
            if self.trend_strength > 48:
                self.phase = "STRONG"
            elif self.trend_strength > 24:
                self.phase = "TREND"

        self.last_dd = dd
        exp = self._compute_exposure()
        self.history.append({"i": i, "dd": dd, "tier": self.tier, "phase": self.phase})
        return exp

    def _apply_tier_transition(self, tier: int) -> None:
        """S→L tier actions — reduce short, add long grid."""
        if tier == 1:
            self.remaining_short_frac *= 0.78  # ~22% short closed
            self.phase = "T1"
        elif tier == 2:
            self.remaining_short_frac *= 0.70  # ~30% more
            self.phase = "T2"
        elif tier == 3:
            self.remaining_short_frac = max(self.remaining_short_frac * 0.55, 0.20)
            self.phase = "T3"
        elif tier >= 4:
            self.remaining_short_frac = max(self.remaining_short_frac * 0.30, 0.05)
            self.phase = "T4"
        # forbid adding short on deeper drawdowns
        self.allow_new_short = tier == 0

    def _phase_key(self) -> str:
        if self.phase in ("T0", "T1", "T2"):
            return "base"
        if self.phase == "REVERSAL":
            return "reversal"
        if self.phase == "STRONG":
            return "strong"
        if self.phase in ("T3", "T4", "TREND"):
            return "trend"
        return "base"

    def _compute_exposure(self) -> TechExposure:
        p = self.params
        short_total = p.short_init_pct * self.remaining_short_frac * p.leverage
        short_total = min(short_total, 0.25 * p.leverage)  # cap at 25% book * lev

        dir_s, grid_s = self._short_structure_split()
        short_dir = short_total * dir_s
        short_grid = short_total * grid_s

        # Long deployment scales with tier
        long_budget = 0.0
        if self.tier >= 1:
            long_budget += 0.08 * self.tier
        if self.tier >= 2:
            long_budget += 0.05
        if self.reversal_confirmed:
            long_budget += 0.28  # final 25-35% on confirmation
        long_budget = min(long_budget, 0.85)

        g_frac, d_frac = grid_mix_fractions(p.grid_mix, self._phase_key())  # type: ignore[arg-type]
        long_grid = long_budget * g_frac * p.leverage
        long_dir = long_budget * d_frac * p.leverage

        snxx_long = 0.0
        if self.tier >= 2:
            snxx_long = long_budget * p.snxx_weight * 0.35 * p.leverage
        if self.tier >= 3:
            snxx_long = long_budget * p.snxx_weight * 0.65 * p.leverage

        used = short_total + long_budget * p.leverage
        cash = max(1.0 - min(used / max(p.leverage, 1.0), 0.95), 0.05)

        return TechExposure(
            short_notional_frac=short_dir + short_grid,
            long_grid_frac=long_grid,
            long_dir_frac=long_dir,
            cash_frac=cash,
            snxx_long_frac=snxx_long,
            phase=self.phase,
            dd_tier=self.tier,
            reversal_confirmed=self.reversal_confirmed,
            allow_new_short=self.tier == 0 and self.last_dd >= -0.05,
            pause_long_grid=self.last_dd < -0.35 and not self.reversal_confirmed,
        )


def tech_short_only_exposure(params: TechParams) -> TechExposure:
    """Benchmark: initial short only, no S→L."""
    s = params.short_init_pct * params.leverage
    return TechExposure(
        short_notional_frac=s,
        cash_frac=1.0 - min(s / params.leverage, 0.95),
        phase="T0",
    )


def tech_long_grid_only(params: TechParams) -> TechExposure:
    g = 0.60 * params.leverage
    return TechExposure(long_grid_frac=g, cash_frac=max(0.05, 1.0 - 0.60), phase="TREND")


def tech_directional_only(params: TechParams) -> TechExposure:
    d = 0.60 * params.leverage
    return TechExposure(long_dir_frac=d, cash_frac=max(0.05, 1.0 - 0.60), phase="STRONG")
