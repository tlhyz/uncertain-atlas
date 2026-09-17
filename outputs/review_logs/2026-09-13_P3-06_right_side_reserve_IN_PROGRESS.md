# Review Log — P3-06 Right-side reserve 25/30/35% (in progress)

**Date (UTC):** 2026-09-14T00:30Z  
**Task:** P3-06 (in_progress)  
**Verdict:** IN_PROGRESS

---

## Job

tmux `p3-06-right-side-reserve` — log `/tmp/p3-06_right_side_reserve.log`  
Config: `configs/experiments/dual_binance_tick_right_side_reserve.yaml`  
Levels: 25% / 30% / 35% long deployment on reversal confirm (default was 28%)

## Status (00:30Z)

| Level | Return | Calmar | vs baseline (−58.70%) |
|-------|--------|--------|------------------------|
| **25%** | **-58.92%** | -1.89 | −0.22pp |
| **30%** | **-59.30%** | -1.87 | **−0.60pp worse** |
| **35%** | — | — | running 3/3 (~10min) |

## Early finding

Higher reversal deploy **worsens** return monotonically so far (25% < 30% in loss magnitude). Default 28% not in sweep; nearest 30% is worse than P3-01 baseline.

## ETA

~20min for 35% → FAIL review expected (no level beats baselines).

Baseline dual (default 28%): -58.70% (P3-01 with drawdown B).

## ETA

~90min total (3 × ~30min).
