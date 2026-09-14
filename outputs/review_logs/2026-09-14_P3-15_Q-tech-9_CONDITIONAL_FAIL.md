# Review Log — P3-15 Answer Q-tech-9 grid in trend phase

## Meta

- **date_utc:** 2026-09-14T04:30Z
- **task:** P3-15
- **output:** outputs/experiments/Q_TECH_9_grid_in_trend_phase.md
- **method:** Synthesize P3-08 grid-mix sweep + P3-01 benchmarks (no new backtest)

## Question

What is optimal grid vs directional mix in trend phase?

## Answer

**CONDITIONAL FAIL.**

- **G50 (50/50)** best return −57.85% (+0.85pp vs default dynamic)
- **U-shaped:** G100 −71.41% worst; G25 −64.97% also bad
- Still **32.65pp behind** B3 long grid only (−25.20%)
- Grid in trend does not rescue FSM vs simpler baselines

## Verdict

- **task_verdict:** **PASS** (question answered from P3-08 measurement)
- **strategy_verdict:** **FAIL** — G50 not deployable; cap grid ~50% if trend phase kept
- **Q4 Grid→Directional:** Measured on Binance tick; dynamic ≡ baseline; G50 beats G100

## Red team (≥5)

1. +0.85pp may be noise
2. Discrete mix grid only
3. Short phase confounds trend mix
4. Gate narrative not replicated
5. G50 + drawdown C not joint-swept

## Next

- P3-16 Gate OOS on top-3 param sets (pending)
- P3-17 effective beta rolling (pending)
