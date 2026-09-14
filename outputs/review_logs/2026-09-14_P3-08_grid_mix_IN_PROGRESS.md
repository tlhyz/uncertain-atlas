# Review Log — P3-08 Grid→Trend stage mix G100/G75/G50/G25/dynamic (in progress)

**Date (UTC):** 2026-09-14T02:20Z  
**Task:** P3-08 (in_progress)  
**Verdict:** IN_PROGRESS

---

## Job

tmux `p3-08-grid-mix` — log `/tmp/p3-08_grid_mix.log`  
Config: `configs/experiments/dual_binance_tick_grid_mix.yaml`  
Mixes: G100 / G75 / G50 / G25 / dynamic

## Status (03:10Z)

| Mix | Return | Calmar | vs baseline (−58.70%) |
|-----|--------|--------|------------------------|
| G100 | -71.41% | -2.07 | −12.71pp worse |
| G75 | -59.53% | -2.29 | −0.83pp worse |
| **G50** | **-57.85%** | **-1.96** | **+0.85pp better** |
| G25 | — | — | running 4/5 (~3min) |
| dynamic | — | — | pending |

**Finding:** G50 **beats default dual** on this window (+0.85pp). First P3 knob to improve vs baseline since drawdown set C (−56.08%). Still FAIL vs B&H/grid-only.

## Status (03:00Z)

| Mix | Return | Calmar | vs baseline (−58.70%) |
|-----|--------|--------|------------------------|
| G100 | -71.41% | -2.07 | −12.71pp worse |
| G75 | -59.53% | -2.29 | −0.83pp worse |
| G50 | — | — | running 3/5 (~10min) |
| G25 | — | — | pending |
| dynamic | — | — | pending |

## Status (02:50Z)

| Mix | Return | Calmar | vs baseline (−58.70%) |
|-----|--------|--------|------------------------|
| G100 | -71.41% | -2.07 | −12.71pp worse |
| **G75** | **-59.53%** | -2.29 | −0.83pp worse |
| G50 | — | — | running 3/5 (~3min) |
| G25 | — | — | pending |
| dynamic | — | — | pending |

**Finding:** Less grid helps monotonically so far (G75 >> G100). Still worse than default dual.

## Status (02:40Z)

| Mix | Return | Calmar | vs baseline (−58.70%) |
|-----|--------|--------|------------------------|
| **G100** | **-71.41%** | -2.07 | −12.71pp worse |
| G75 | — | — | running 2/5 (~10min) |
| G50 | — | — | pending |
| G25 | — | — | pending |
| dynamic | — | — | pending |

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
