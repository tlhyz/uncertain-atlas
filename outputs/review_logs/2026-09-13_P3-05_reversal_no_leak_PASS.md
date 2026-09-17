# Review Log — P3-05 Reversal R1–R5 no-lookahead tests

## Meta

- **date_utc:** 2026-09-13T21:00Z
- **experiment_id:** TASK-0010 / P3-05
- **task:** P3-05
- **scope:** Unit tests + R5 implementation (not 65d backtest sweep)

## Implementation

- Added `reversal_r5()` — composite **2-of-4** vote across R1–R4 (`qtb/dual/signals.py`)
- Extended `ReversalRule` / `REVERSAL_RULES` to include **R5** (`qtb/dual/universe.py`)
- Wired `check_reversal("R5", ...)` and TechFSM bounce map
- Tests: `tests/test_no_future_leak.py::TestReversalRules`
  - `test_r5_causal` — future bar corruption does not change result at i
  - `test_check_reversal_causal` parametrized **R1–R5**

## R5 definition

At bar `i`, R5 fires when **≥2** of {R1 EMA cross, R2 swing break, R3 bounce %, R4 dual EMA} are true. Each sub-rule uses only data `≤ i` (inherits causality from R1–R4).

## Test results

```
tests/test_no_future_leak.py::TestReversalRules — 10 passed
Full suite — 136 passed
```

## Verdict

- **task_verdict:** **PASS** — all R1–R5 no-lookahead tests green; R5 previously missing from codebase
- **strategy_verdict:** N/A (infra/correctness task)

## Red team (≥5)

1. R5 composite may fire more often than any single rule — backtest impact untested until reversal sweep  
2. Sub-rule bounce_pct shared with R3 inside R5 — not independently tuned per sub-rule  
3. Tests use synthetic OHLC — real tick path not covered here  
4. R5 in FSM uses same tier≥2 gate as R1–R4 — integration not separately tested  
5. 2-of-4 threshold fixed — 3-of-4 not explored

## Next

- P3-03 short structure sweep (running)
- Optional: `rank_reversal` backtest sweep (separate backlog item if needed)
