# Review Log — P5-04 OOS Holdout Report for Finalists

## Meta

- **date_utc:** 2026-09-14T08:55Z
- **task:** P5-04
- **method:** Temporal holdout (no retrain); train refs from in-sample experiments
- **source:** outputs/LIVE_CANDIDATES.md research rows
- **output:** outputs/experiments/p5_oos_holdout/oos_holdout.json

## Implementation

- **`src/analysis/oos_holdout.py`:** holdout splits, pass criteria, report builder, markdown render
- **`scripts/run_p5_oos_holdout.py`:** fresh holdout evals + Gate OOS blocked meta
- **`tests/test_oos_holdout.py`:** 4 tests (161 full suite green)

## Holdout policy

**temporal_holdout_no_retrain** — parameters fixed from in-sample research; holdout windows never used for tuning.

| Candidate | Train (reference) | Holdout | Holdout return | vs benchmark | OOS pass |
|-----------|-------------------|---------|----------------|--------------|----------|
| **btc_crypto_default** | 2020-2023 (−86.1% ref) | **2024** | **−86.44%** | B&H proxy −30% | **no** |
| **dual_tech_crypto_independent** | 65d −56.4% (P4) | **2026-08-26→09-11** (last 25%) | **−75.49%** | B&H −33.49% | **no** |

Gap BTC +0.37pp (stable); dual holdout **−19pp worse** than in-sample → degradation on recent window.

## Gate OOS

**BLOCKED** — `run_gate_oos.py` stub; P3-16 no MEDIUM tech candidate. Documented in report meta.

## Cross-check P5-03 calendar fold 2024

Calendar WF test 2024: **−86.44%** — matches P5-04 BTC holdout exactly (same window/params).

## Question

Do any LIVE_CANDIDATES research rows survive temporal OOS holdout?

## Findings

1. **Implementation:** PASS — structured JSON + markdown report.
2. **BTC default:** FAIL — holdout −86.44%; no edge vs in-sample catastrophic band.
3. **Dual independent:** FAIL — holdout −75.49% vs benchmark −33.49%; worse than 65d in-sample −56.4%.
4. **Gate OOS:** BLOCKED — not run.
5. **Verdict aggregate:** **0/2 pass** — no finalist ready for P6 promotion.

## Verdict

- **task_verdict:** **DONE**
- **implementation_verdict:** **PASS**
- **strategy_verdict:** **FAIL** — all finalists fail OOS holdout

## Red team (≥5)

1. BTC BAR fills — tick C1 also ~−87%; consistent but not tick holdout
2. Dual holdout only 16d — short; directional variance high
3. Train refs cited not re-run — holdout paths measured fresh
4. Benchmark −30% BTC proxy approximate — dual uses 65d B&H −33.49%
5. MEDIUM confidence rows in LIVE_CANDIDATES remain research-only

## Next

- P5-05 DD probability from MC (65d dual-book)
- P5-06 liquidation probability from MC
- Do not promote any row to P6 without OOS pass
