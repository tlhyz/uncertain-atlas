# Review Log — P4-07 Margin/Reserve 80/20 70/30 60/40

## Meta

- **date_utc:** 2026-09-14T07:45Z
- **task:** P4-07
- **method:** `margin_frac` sweep within each book (deployed vs book reserve)
- **config:** configs/experiments/dual_binance_tick_margin_reserve_65d.yaml
- **output (7d):** outputs/experiments/dual_binance_tick_margin_reserve_7d/dual_results.json
- **output (65d):** in progress → outputs/experiments/dual_binance_tick_margin_reserve_65d/

## Implementation

Added `DualParams.margin_frac` (default **0.95** legacy) + `rank_margin_reserve()`:
- `tech_deploy = TECH_BOOK × margin_frac` → SOXL legs
- `tech_book_reserve = TECH_BOOK × (1 − margin_frac)` → SNXX leg
- `crypto_deploy / crypto_book_reserve` same split; crypto reserve added to global reserve pool

## Results — 7d dual-book smoke (2026-09-05→11, ~62s/level)

| Split | margin_frac | Return | MaxDD | Calmar |
|-------|-------------|--------|-------|--------|
| **60/40** | 0.60 | **−71.89%** | **5.66%** | **−17.67** |
| 70/30 | 0.70 | −73.05% | 6.84% | −14.63 |
| 80/20 | 0.80 | −73.69% | 7.98% | −12.53 |

**Best:** 60/40 (most reserve) — lowest DD and best (least bad) return on 7d.

## 65d dual-book (in progress)

Tmux `p4-07-margin-65d` started 07:32Z — ETA ~72min for 3 tick-tech levels.

Baseline reference (dual-book default margin_frac≈0.95): ind **−56.40%**, DD 51.07% (P4-03 JSON).

## Question

Does margin/reserve split 80/20 vs 70/30 vs 60/40 improve survivability without killing return?

## Findings

1. **Direction:** More reserve (60/40) → lower MaxDD and better return on 7d — aligns with `RISK_POLICY.md` reserve intent.
2. **Alpha:** FAIL — all splits deeply negative; no sweet spot for profit.
3. **Magnitude:** 7d DD 5–8% vs 65d baseline ~51% — short window understates tech drawdown; await 65d confirmation.
4. **Legacy mismatch:** Engine default was 95/5 hardcoded; config baseline is 70/30 — now parameterized.

## Verdict

- **task_verdict:** **DONE** (7d sweep complete; 65d running)
- **strategy_verdict:** **CONDITIONAL FAIL** — reserve helps DD monotonically on 7d but no positive alpha; prefer **60/40** if forced to choose
- **risk:** Reserve exhaustion not hit on 7d at any split

## Red team (≥5)

1. 7d window too short for 51% DD tech book behavior
2. BAR crypto fills on dual-book path
3. 65d results may reorder ranking
4. crypto reserve sits in global reserve pool — accounting simplification
5. SNXX leg absorbs full tech book reserve — may not match live ops

## Next

- Complete 65d margin sweep → update this log if ranking changes
- P4-08 funding stress deleverage rule test
- Consider setting default `margin_frac=0.70` to match `portfolio.yaml` baseline
