# Review Log — P3-04 Drawdown set A/B/C sweep

## Meta

- **date_utc:** 2026-09-13T23:40Z
- **experiment_id:** dual_binance_tick_drawdown_sets
- **task:** P3-04
- **config:** configs/experiments/dual_binance_tick_drawdown_sets.yaml
- **output:** outputs/experiments/dual_binance_tick_drawdown_sets/dual_results.json
- **fill_mode:** base (tick_precise aggTrades)
- **runtime:** ~70min (3 sets × ~23min; job 22:30Z→23:40Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **precision:** TICK (DATA_QUALITY PASS, 41.3M aggTrade rows)

## Results (drawdown_set_rank)

| Set | Thresholds | Return | MaxDD | Calmar |
|-----|------------|--------|-------|--------|
| **A** (tighter) | −8/−15/−25/−35% | **-67.88%** | 57.66% | -1.73 | 1 liq |
| **B** (default) | −10/−20/−30/−40% | **-58.70%** | 52.76% | -1.88 | 0 |
| **C** (wider) | −12.5/−25/−37.5/−50% | **-56.08%** | 49.74% | **-1.99** (best) | 0 |

Sorted by return: **C > B > A**. Best Calmar: **C** (−1.99).

- C vs B: **+2.62pp** return, lower MaxDD (49.74% vs 52.76%)
- A vs B: **−9.18pp** return — tighter tiers hurt; **1 liquidation** on A

All sets still lose to B&H (−33.49%), Cash (0%), grid-only (−25.20%) from P3-01.

## Q-tech-1 partial (drawdown exit rhythm)

**Answer:** Wider set **C** is measurably best among A/B/C but still **FAIL** vs baselines. Tighter **A** is strictly worse. Default **B** is middle — not optimal within sweep.

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** **FAIL** — no drawdown set beats Cash, B&H, or grid-only; C best at −56.08% still catastrophic
- **C-05:** Reinforced **HIGH** — tier tuning cannot rescue Short→Long FSM for live deploy
- **Note:** C is only knob so far that **improves** dual vs default B on this window (+2.62pp) — not enough for MEDIUM candidate

## Red team (≥5)

1. C improvement may be slower S→L (less short reduction) — different risk profile not tested OOS
2. Only three discrete tier ladders — intermediate not scanned
3. Calmar "best" at −1.99 still deeply negative
4. Base fill only — conservative not run
5. Same 65d window — C could overfit single crash path

## Next

- P3-06 right-side reserve 25/30/35% (started)
- Do not promote drawdown set C without OOS + beat grid-only baseline
