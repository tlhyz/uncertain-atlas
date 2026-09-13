# Review Log — P3-02 Short init sweep started

**Date (UTC):** 2026-09-13T19:40Z  
**Task:** P3-02 (in_progress)  
**Verdict:** IN_PROGRESS

---

## Implementation

- Added `rank_short_init()` in `qtb/dual/experiments.py` — levels 0.10/0.15/0.20 with per-level logging
- Wired `run_short_init_rank` + `short_init_levels` in `qtb/dual/run.py`
- Config: `configs/experiments/dual_binance_tick_short_init.yaml`
- Test: `tests/test_dual_engine.py::test_rank_short_init_sweep`

## Job

tmux `p3-02-short-init` — log `/tmp/p3-02_short_init.log`  
Window: 65d Binance tick overlap (1546 bars), Base fill.

## Job status (2020Z)

| Level | Return | Calmar | Status |
|-------|--------|--------|--------|
| 10% | **-59.24%** | -1.86 | done |
| 15% | — | — | running |
| 20% | — | — | pending |

10% worse than default 20% (-58.70%) — lower short does not help.
