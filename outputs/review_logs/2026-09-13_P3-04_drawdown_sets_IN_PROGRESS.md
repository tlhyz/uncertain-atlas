# Review Log — P3-04 Drawdown set A/B/C (in progress)

**Date (UTC):** 2026-09-13T23:00Z  
**Task:** P3-04 (in_progress)  
**Verdict:** IN_PROGRESS

---

## Job

tmux `p3-04-drawdown-sets` — log `/tmp/p3-04_drawdown_sets.log`  
Config: `configs/experiments/dual_binance_tick_drawdown_sets.yaml`  
Sets: A (−8/−15/−25/−35%), B (−10/−20/−30/−40%, default), C (−12.5/−25/−37.5/−50%)

## Status (23:00Z)

| Set | Return | Calmar | Status |
|-----|--------|--------|--------|
| **A** (tighter) | **-67.88%** | -1.73 | done |
| B (default) | -58.70% (P3-01) | -1.88 | running 2/3 |
| C (wider) | — | — | pending |

## Early finding

Set **A worse than B** by −9.18pp — tighter drawdown tiers **accelerate** S→L transitions and increase loss vs default B. Not a rescue knob.

## ETA

~60min for B + C.
