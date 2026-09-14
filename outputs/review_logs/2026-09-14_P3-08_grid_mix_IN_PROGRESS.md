# Review Log — P3-08 Grid→Trend stage mix G100/G75/G50/G25/dynamic (in progress)

**Date (UTC):** 2026-09-14T02:20Z  
**Task:** P3-08 (in_progress)  
**Verdict:** IN_PROGRESS

---

## Job

tmux `p3-08-grid-mix` — log `/tmp/p3-08_grid_mix.log`  
Config: `configs/experiments/dual_binance_tick_grid_mix.yaml`  
Mixes: G100 / G75 / G50 / G25 / dynamic

## Status (02:30Z)

| Mix | Return | Calmar | vs baseline (−58.70%) |
|-----|--------|--------|------------------------|
| **G100** | **-71.41%** | -2.07 | **−12.71pp worse** |
| G75 | — | — | running 2/5 (~3min) |
| G50 | — | — | pending |
| G25 | — | — | pending |
| dynamic | — | — | pending |

**Early finding:** Pure grid (G100) catastrophically worse than default dual. Less grid may help.

## Status (02:20Z)

| Mix | Return | Calmar | vs baseline (−58.70%) |
|-----|--------|--------|------------------------|
| G100 | — | — | running 1/5 (~10min) |
| G75 | — | — | pending |
| G50 | — | — | pending |
| G25 | — | — | pending |
| dynamic | — | — | pending |

DATA_QUALITY PASS (41.3M aggTrade rows). Overlap 1546 bars @ 1h.

## ETA

~110min total (5 × ~24min per prior sweeps).

Baseline dual (default grid mix): −58.70% (P3-01).
