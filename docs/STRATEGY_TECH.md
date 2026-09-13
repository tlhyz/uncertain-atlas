# Tech Strategy — Regime State Machine

See `configs/experiments/tech_state_machine.yaml` and `qtb/dual/tech_fsm.py`.

## States

| State | Description |
|-------|-------------|
| T0_SHORT | Tactical short 10–20% **total account** notional |
| T1_TRANSITION | Tiered short reduction on SOXL drawdown |
| T2_BOTTOM_GRID | Long grid dominant at lows |
| T3_REVERSAL | Grid + directional mix shifting |
| T4_TREND_LONG | Directional dominant |
| T5_OVERHEATED | De-risk |

## Drawdown sets (from anchor)

- **A:** −8 / −15 / −25 / −35%
- **B:** −10 / −20 / −30 / −40%
- **C:** ATR-based tiers

Anchor modes: strategy start, rolling 20d high, rolling 30d high.

## Right-side confirmation (25–35% book reserved)

Signals R1–R5 (4H EMA, swing break, bounce %, dual SOXL+SNXX, 2-of-4). **No future leak.**

## Grid → Trend mix stages

| Phase | Grid / Directional |
|-------|-------------------|
| Bottom | 80 / 20 |
| Early reversal | 60 / 40 |
| Trend | 40 / 60 |
| Strong trend | 20 / 80 |

Compare vs 100% grid, 100% directional, 50/50 fixed.

## Grid parameters

Geometric only. Spacing 0.30–0.60 ATR; range ±3/5/7 ATR. **No martingale.**

Re-anchor: OFF / 7D / DYNAMIC — on break below lower bound → **pause new longs**, not auto knife-catch.

## Leverage

Scan: 1.0 / 1.10 / 1.25 / 1.5x. Stress: 1.75 / 2.0. **3x forbidden as Tech default.**

Track **contract leverage** and **effective underlying beta** (`src/features/beta.py`).

## Seed & fail windows

Listed in `configs/universe.yaml`. Executable only when real perp data exists.

Similar real windows: DTW + Pearson + Spearman (`src/analysis/similarity.py`).

## Key questions Q1–Q10

Documented in experiment reports — see `docs/EXPERIMENTS.md`.

**Current honest status:** Short→Long **FAILED** on Gate overlap; Binance tick re-validation **PENDING**.
