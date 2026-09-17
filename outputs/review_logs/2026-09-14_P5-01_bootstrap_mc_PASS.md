# Review Log — P5-01 Block Bootstrap Monte Carlo

## Meta

- **date_utc:** 2026-09-14T08:10Z
- **task:** P5-01
- **method:** Block bootstrap MC on dual-book independent equity; 1000 paths; block sizes 1/3/5 days
- **config:** configs/experiments/dual_binance_tick_dual_book_7d.yaml
- **output:** outputs/experiments/dual_binance_tick_dual_book_7d/bootstrap_mc.json

## Implementation

- **`src/analysis/monte_carlo.py`:** `daily_returns_from_equity`, `block_bootstrap_paths`, `summarize_bootstrap_paths`, `block_bootstrap_mc`
- **`scripts/run_p5_bootstrap_mc.py`:** dual-book source run → MC on `total_equity`
- **`tests/test_monte_carlo.py`:** reproducibility + 1000-path smoke (2 tests pass)
- **Fix:** `block_bootstrap_paths` now loops until `len(seq) >= n` (partial tail blocks no longer under-fill)

## Results — 7d dual-book independent (168 bars, 6 daily obs)

| Block | p50 final | prob_loss | prob_dd_10 | prob_dd_20 | prob_dd_30 |
|-------|-----------|-----------|------------|------------|------------|
| 1d | 21,225 | 13.5% | 21.1% | 2.0% | 0.0% |
| 3d | 11,366 | 17.5% | 13.8% | 0.7% | 0.0% |
| 5d | 10,692 | 19.2% | 15.5% | 1.2% | 0.0% |

In-sample: final 2,468 USDT (−75.32% from 10k). Bootstrap medians **above** in-sample final — resampling daily returns from a short window with one catastrophic day does not reproduce the full path dependency of the dual engine.

## Question

Is block bootstrap MC implemented and runnable at 1000 paths on dual-book equity?

## Findings

1. **Implementation:** PASS — 1000 paths × 3 block sizes; percentiles + prob_loss + prob_dd_10/20/30 exported.
2. **Unit tests:** PASS — reproducible RNG; full MC smoke OK.
3. **Sample size:** CONDITIONAL — only **6 daily observations** on 7d window; bootstrap distribution is **not** representative of 65d risk; run 65d MC before P5-05/P5-06 conclusions.
4. **Interpretation:** Median bootstrapped finals > in-sample final indicates positive daily-return days dominate resampling while the realized path had severe compounding loss — expected with tiny daily sample.

## Verdict

- **task_verdict:** **DONE**
- **implementation_verdict:** **PASS**
- **robustness_verdict:** **INCONCLUSIVE on 7d** — need 65d MC for decision use

## Red team (≥5)

1. 6 daily obs — bootstrap resamples same week repeatedly
2. Daily resample from hourly equity may miss intraday DD sequencing
3. Independent book only — unified liq path not bootstrapped here
4. Block sizes 1/3/5d on 6 obs — 5d blocks nearly span full sample
5. No liquidation flag in MC summary yet (P5-06 scope)

## Next

- P5-02 parameter plateau detector
- P5-05/P5-06: run 65d MC on dual-book reference equity; add liq probability if portfolio exposes it
- Optional: `configs/experiments/dual_binance_tick_independent_vs_unified.yaml` 65d MC (~24min source run)
