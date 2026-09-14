# Review Log — P3-06 Right-side reserve 25/30/35% (in progress)

**Date (UTC):** 2026-09-14T00:10Z  
**Task:** P3-06 (in_progress)  
**Verdict:** IN_PROGRESS

---

## Job

tmux `p3-06-right-side-reserve` — log `/tmp/p3-06_right_side_reserve.log`  
Config: `configs/experiments/dual_binance_tick_right_side_reserve.yaml`  
Levels: 25% / 30% / 35% long deployment on reversal confirm (default was 28%)

## Status (00:10Z)

| Level | Return | Calmar | Status |
|-------|--------|--------|--------|
| **25%** | **-58.92%** | -1.89 | done (−0.22pp vs baseline) |
| **30%** (≈default 28%) | — | — | running 2/3 (~10min) |
| 35% | — | — | pending |

## Early finding

25% **slightly worse** than default dual −58.70% — less reversal deploy hurts slightly.

## ETA

~50min for 30% + 35%.

Baseline dual (default 28%): -58.70% (P3-01 with drawdown B).

## ETA

~90min total (3 × ~30min).
