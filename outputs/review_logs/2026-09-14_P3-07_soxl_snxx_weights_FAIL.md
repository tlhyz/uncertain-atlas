# Review Log — P3-07 SOXL/SNXX weight 75/25 70/30 65/35 sweep

## Meta

- **date_utc:** 2026-09-14T02:10Z
- **experiment_id:** dual_binance_tick_soxl_snxx_weights
- **task:** P3-07
- **config:** configs/experiments/dual_binance_tick_soxl_snxx_weights.yaml
- **output:** outputs/experiments/dual_binance_tick_soxl_snxx_weights/dual_results.json
- **fill_mode:** base (tick_precise aggTrades)
- **runtime:** ~77min (3 weights × ~26min; job 00:53Z→02:10Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **precision:** TICK (DATA_QUALITY PASS, 41.3M aggTrade rows)

## Results (soxl_snxx_weight_rank)

| SOXL/SNXX | Return | MaxDD | Calmar | Turnover | vs baseline (−58.70%) |
|-----------|--------|-------|--------|----------|------------------------|
| **70/30** (default, best) | **-58.70%** | 52.76% | **-1.88** | 33238 | match |
| 65/35 | -58.81% | 52.73% | -1.88 | 33253 | −0.11pp worse |
| 75/25 | -58.89% | 52.57% | -1.89 | 33270 | −0.19pp worse |

Sorted by return: **70/30 > 65/35 > 75/25**. Default weight is optimal within sweep.

- 70/30 **exactly reproduces** P3-01 baseline (−58.70%) — sanity check PASS
- Higher SOXL (75/25) strictly worst return; more SNXX (65/35) intermediate
- Turnover nearly identical (~33.2k) — weight shift does not materially change trading intensity

All weights still lose to B&H (−33.49%), Cash (0%), grid-only (−25.20%) from P3-01.

## Q-tech-5 partial (SOXL/SNXX weights)

**Answer:** Default **70/30 is best** among 75/25, 70/30, 65/35. No alternative split improves vs baseline; knob binds weakly (≤0.19pp spread).

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** **FAIL** — no weight split beats Cash, B&H, grid-only, or default dual
- **C-05:** Reinforced **HIGH** — book allocation tuning cannot rescue Short→Long FSM

## Red team (≥5)

1. Only three discrete splits — 72/28 or 68/32 not scanned
2. Spread ≤0.19pp — may be noise vs tick fill variance
3. SNXX lead/lag not isolated (Q-tech-6 still open)
4. Base fill only — conservative not run
5. Same 65d window — weight curve may not generalize

## Next

- P3-08 grid→Trend stage mix G100/G75/G50/G25/dynamic (started)
- Do not change default 70/30 without beat grid-only baseline
