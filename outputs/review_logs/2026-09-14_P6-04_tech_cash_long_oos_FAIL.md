# Review Log — P6-04 Tech Row vs Cash→Long OOS

## Meta

- **date_utc:** 2026-09-14T10:32Z
- **task:** P6-04
- **method:** Temporal holdout last 25% of 65d window; Tech FSM vs B4 Cash→Long proxy
- **output:** outputs/experiments/p6_tech_cash_long_oos/tech_cash_long_oos.json

## Implementation

- **`src/analysis/tech_cash_long_oos.py`:** holdout eval + markdown render
- **`scripts/run_p6_tech_cash_long_oos.py`:** runner (P5-04 execution parity)
- **`tests/test_p6_tech_cash_long_oos.py`:** render smoke

## Holdout OOS (2026-08-26 → 2026-09-11, 387 bars)

| Strategy | Return | vs B4 |
|----------|-------:|------:|
| **B4 Cash→Long proxy** | **−0.38%** | — |
| Tech FSM (dual default) | **−75.49%** | **−75.12pp** |

Matches P5-04 dual holdout (−75.49%) — consistent measurement.

## In-sample reference (P3-12, full 65d)

| Strategy | Return | Delta |
|----------|-------:|------:|
| B4 | −25.19% | — |
| Tech FSM | −58.70% | −33.51pp |

OOS degradation: Tech holdout **−19pp worse** than in-sample (−75.5% vs −56.4% P4 ref); B4 nearly flat on holdout.

## Question

Can Tech row (Short→Long FSM) be a live candidate — does it beat Cash→Long OOS?

## Findings

1. **Verdict:** **FAIL** — Tech loses by **75pp** on holdout vs B4.
2. **Tech row stays LOW** — SOXL/SNXX entries remain research-only; no promotion path.
3. **C-05 reinforced:** Remove initial Short from baseline (P3-12 + OOS).
4. **B4 holdout −0.38%** — Cash→Long proxy not positive alpha either; neither strategy deployable.
5. **Best P3 knobs** (drawdown C −56%, G50 −58%) still ~−31pp behind B4 in-sample — OOS would fail harder.

## Verdict

- **task_verdict:** **done**
- **oos_verdict:** **FAIL**
- **live_candidate:** **NO** — Tech row does not beat Cash→Long OOS

## Red team (≥5)

1. B4 holdout uses bar path when tick_precise=False — may differ from P3 tick B4
2. Dual includes crypto book drag on holdout — tech-only isolation not run
3. Holdout 16d calendar — short window, high variance
4. B4 nearly flat holdout may be luck — still beats Tech by 75pp
5. SOXL/SNXX separate rows not individually tested — FSM is portfolio-level

## Next

- P6-05 final LIVE_CANDIDATES.md review (SOL demotion + Tech OOS footnote)
