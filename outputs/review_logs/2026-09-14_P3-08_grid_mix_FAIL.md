# Review Log — P3-08 Grid→Trend stage mix G100/G75/G50/G25/dynamic sweep

## Meta

- **date_utc:** 2026-09-14T04:00Z
- **experiment_id:** dual_binance_tick_grid_mix
- **task:** P3-08
- **config:** configs/experiments/dual_binance_tick_grid_mix.yaml
- **output:** outputs/experiments/dual_binance_tick_grid_mix/dual_results.json
- **fill_mode:** base (tick_precise aggTrades)
- **runtime:** ~110min (5 mixes × ~22min; job 02:10Z→04:00Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **precision:** TICK (DATA_QUALITY PASS, 41.3M aggTrade rows)

## Results (grid_mix_rank)

| Mix | Return | MaxDD | Calmar | vs baseline (−58.70%) |
|-----|--------|-------|--------|------------------------|
| **G50** (best return) | **-57.85%** | 50.73% | -1.96 | **+0.85pp better** |
| dynamic (default) | -58.70% | 52.76% | **-1.88** (best Calmar) | match |
| G75 | -59.53% | 43.36% | -2.29 | −0.83pp worse |
| G25 | -64.97% | 42.02% | -2.37 | −6.27pp worse |
| G100 | -71.41% | 48.27% | -2.07 | −12.71pp worse |

Sorted by return: **G50 > dynamic > G75 > G25 > G100**. U-shaped curve — too much grid (G100) or too little (G25) both hurt.

- **G50** is sweet spot (+0.85pp vs default); **dynamic** reproduces P3-01 baseline exactly
- G100 pure grid worst (−71.41%); confirms grid-heavy short phase destructive on this window
- MaxDD lowest at G25/G75 but return worse — risk/return tradeoff not actionable

All mixes still lose to B&H (−33.49%), Cash (0%), grid-only (−25.20%) from P3-01.

## Q-tech-9 partial (grid in trend phase)

**Answer:** 50/50 grid/trend mix **modestly beats** default dynamic on return (+0.85pp) but **FAIL** vs baselines. Not deployable; G50 candidate for P3-16 OOS only.

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** **FAIL** — no mix beats Cash, B&H, or grid-only; G50 best at −57.85% still catastrophic
- **C-05:** Reinforced **HIGH** — grid/trend mix tuning cannot rescue FSM for live deploy

## Red team (≥5)

1. G50 +0.85pp may be noise on single 65d window
2. dynamic ≡ default — sweep validates implementation but limits discovery
3. G25/G75 MaxDD lower but return worse — not a usable tradeoff
4. Base fill only — conservative not run
5. Grid mix interacts with drawdown set C (−56.08%) — combined sweep not run

## Next

- P3-11 similar-window search (started)
- Note G50 + drawdown C as P3-16 OOS candidate pair; do not promote without beat grid-only
