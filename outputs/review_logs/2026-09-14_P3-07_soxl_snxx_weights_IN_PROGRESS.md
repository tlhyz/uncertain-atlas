# Review Log — P3-07 SOXL/SNXX weight 75/25 70/30 65/35 (in progress)

**Date (UTC):** 2026-09-14T00:53Z  
**Task:** P3-07 (in_progress)  
**Verdict:** IN_PROGRESS

---

## Job

tmux `p3-07-soxl-snxx-weights` — log `/tmp/p3-07_soxl_snxx_weights.log`  
Config: `configs/experiments/dual_binance_tick_soxl_snxx_weights.yaml`  
Weights: SOXL 75/70/65% vs SNXX 25/30/35% (default ~70/30 from P3-01 baseline)

## Status (01:40Z)

| Weight | Return | Calmar | vs baseline (−58.70%) |
|--------|--------|--------|------------------------|
| **75/25** | **-58.89%** | -1.89 | −0.19pp worse |
| 70/30 | — | — | running 2/3 (~20min) |
| 65/35 | — | — | pending |

## Status (01:30Z)

| Weight | Return | Calmar | vs baseline (−58.70%) |
|--------|--------|--------|------------------------|
| **75/25** | **-58.89%** | -1.89 | −0.19pp worse |
| 70/30 | — | — | running 2/3 (~13min) |
| 65/35 | — | — | pending |

## Status (01:20Z)

| Weight | Return | Calmar | vs baseline (−58.70%) |
|--------|--------|--------|------------------------|
| **75/25** | **-58.89%** | -1.89 | −0.19pp worse |
| 70/30 | — | — | running 2/3 (~3min) |
| 65/35 | — | — | pending |

**Early finding:** 75/25 slightly worse than default 70/30 baseline (−58.70%). 70/30 in sweep should match baseline if implementation correct.

## Status (01:10Z)

| Weight | Return | Calmar | vs baseline (−58.70%) |
|--------|--------|--------|------------------------|
| 75/25 | — | — | running 1/3 (~17min) |
| 70/30 | — | — | pending |
| 65/35 | — | — | pending |

## Status (01:00Z)

| Weight | Return | Calmar | vs baseline (−58.70%) |
|--------|--------|--------|------------------------|
| 75/25 | — | — | running 1/3 (~7min) |
| 70/30 | — | — | pending |
| 65/35 | — | — | pending |

DATA_QUALITY PASS (41.3M aggTrade rows). Overlap 1546 bars @ 1h.

## Status (00:53Z)

| Weight | Return | Calmar | vs baseline (−58.70%) |
|--------|--------|--------|------------------------|
| 75/25 | — | — | running 1/3 |
| 70/30 | — | — | pending |
| 65/35 | — | — | pending |

DATA_QUALITY PASS (41.3M aggTrade rows). Overlap 1546 bars @ 1h.

## ETA

~70min total (3 × ~24min per prior P3 sweeps).

Baseline dual (default weights): −58.70% (P3-01).
