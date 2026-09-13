# Review Log — P3-03 Short structure sweep

## Meta

- **date_utc:** 2026-09-13T22:30Z
- **experiment_id:** dual_binance_tick_short_structures
- **task:** P3-03
- **config:** configs/experiments/dual_binance_tick_short_structures.yaml
- **output:** outputs/experiments/dual_binance_tick_short_structures/dual_results.json
- **fill_mode:** base (tick_precise aggTrades)
- **runtime:** ~101min (4 structures × ~25min; job 20:49Z→22:30Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **precision:** TICK (DATA_QUALITY PASS, 41.3M aggTrade rows)

## Results (short_structures)

| Structure | Return | MaxDD | Calmar |
|-----------|--------|-------|--------|
| directional | **-58.70%** | 52.76% | -1.88 |
| grid | **-58.70%** | 52.76% | -1.88 |
| 70_30 (default) | **-58.70%** | 52.76% | -1.88 |
| 50_50 | **-58.70%** | 52.76% | -1.88 |

**All four variants bit-identical** to P3-01 dual baseline (−58.70%). Parameter `short_structure` has **zero effect** on measured outcomes.

All lose to B&H (−33.49%), Cash (0%), grid-only (−25.20%) from P3-01.

## Q-tech (short structure mix)

**Answer:** No actionable difference among directional / grid / 70_30 / 50_50 on 65d tick overlap. Short-phase structure tuning **cannot rescue** the Short→Long FSM.

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** **FAIL** — structure mix inert; no variant beats baselines
- **C-05:** Reinforced **HIGH** — do not deploy Short FSM; structure knob dead
- **Mechanism hypothesis:** Short grid vs directional split may not bind differently in tick fill path on this window (identical paths)

## Red team (≥5)

1. Inert result could indicate implementation bug — verify `_short_structure_split()` binds to fills (follow-up code audit)
2. Only four discrete mixes — intermediate 80/20 not tested
3. Effect might appear on FAIL_F1 direct-up window (P3-09 blocked on data)
4. Base fill only — conservative not run
5. Same 65d window — no OOS

## Next

- P3-04 drawdown set A/B/C sweep (started)
- Do not promote any short_structure variant
