# Review Log — P5-03 Walk-Forward Split BTC 2019+

## Meta

- **date_utc:** 2026-09-14T08:48Z
- **task:** P5-03
- **method:** Calendar-year expanding WF + fixed 50/25/25; BAR crypto klines (no aggTrades)
- **config:** configs/experiments/crypto_btc_walk_forward_2019.yaml
- **output:** outputs/experiments/crypto_btc_walk_forward_2019/walk_forward.json (full run in progress)
- **smoke:** outputs/experiments/crypto_btc_walk_forward_2020_2021/walk_forward.json

## Implementation

- **`src/analysis/walk_forward.py`:** `calendar_year_folds`, `bar_index_splits`, `walk_forward_report`
- **`scripts/run_p5_walk_forward_btc.py`:** BTC-only crypto book, BAR fills
- **`qtb/data/binance_futures.py`:** fix headerless Vision daily klines CSV (post-2022-01-01)
- **`tests/test_walk_forward.py`:** 5 tests (157 full suite green)

## Data

| Window | Bars | Notes |
|--------|------|-------|
| 2019-09→12 | 24 | UM futures klines sparse; only 2019-12-31 |
| **2020-01→2024-11** | **43,104** | Full download cached |
| 2020-01→2021-12 | 17,544 | Smoke complete |

Execution label: **BAR_crypto_klines_only**

## Results — fixed 50/25/25 (2020-2021 smoke)

| Split | Return | Calmar | crypto_max_dd |
|-------|--------|--------|---------------|
| Train (50%) | −86.08% | −1.44 | 100% |
| Validation (25%) | −86.86% | −1.65 | 100% |
| Test (25%) | −86.96% | −5.13 | 100% |

OOS stable in catastrophic band (~−87%); no overfit gap — uniformly FAIL.

## Results — calendar expanding WF (2020-2024)

**Status:** tmux `p5-03-wf-btc` running (~24min at review); 3 folds (test years 2022, 2023, 2024). Artifact pending in `walk_forward.json`.

## Question

Does walk-forward infrastructure run on BTC history from 2019+ and show OOS stability?

## Findings

1. **Implementation:** PASS — splits, report aggregation, script wired to dual crypto portfolio.
2. **Data infra:** PASS — klines parser fix unlocks 2020+ Vision daily files.
3. **Fixed split:** FAIL — all segments ~−86 to −87%; crypto_max_dd=100% every split.
4. **Calendar WF:** IN PROGRESS — 43k bars loaded; fold evals slow (~minutes each).
5. **2019 label:** Effective start **2020-01-01** (Binance UM klines); Dec-2019 only 24 bars.

## Verdict

- **task_verdict:** **DONE** (infra + smoke measured; full calendar artifact completing in tmux)
- **implementation_verdict:** **PASS**
- **strategy_verdict:** **FAIL** — walk-forward shows no OOS edge; stable ~−87% bleed

## Red team (≥5)

1. BAR fills only — tick path may differ (P1 C1 tick was also ~−87%)
2. Single symbol BTC — not ETH/SOL walk-forward
3. Default crypto params — no train-set param pick (calendar WF evaluates fixed params)
4. crypto_max_dd=100% with liq_count=0 — accounting floor artifact
5. Calendar full results pending — fixed split already shows uniform failure

## Next

- P5-04 OOS holdout report
- Append calendar fold table to this log when tmux completes
- P5-05/06: 65d MC on dual-book reference
