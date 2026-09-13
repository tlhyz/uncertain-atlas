# Review Log — P3-02 Short init 10/15/20% sweep

## Meta

- **date_utc:** 2026-09-13T21:10Z
- **experiment_id:** dual_binance_tick_short_init
- **task:** P3-02
- **config:** configs/experiments/dual_binance_tick_short_init.yaml
- **output:** outputs/experiments/dual_binance_tick_short_init/dual_results.json
- **fill_mode:** base (tick_precise aggTrades)
- **runtime:** ~100min (3 levels × ~30min; job started 19:30Z, finished ~21:10Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **precision:** TICK (DATA_QUALITY PASS, 41.3M aggTrade rows)

## Results (short_init_rank)

| Init short | Return | MaxDD | Calmar | vs P3-01 default (20%) |
|------------|--------|-------|--------|-------------------------|
| **10%** | **-59.24%** | 53.34% | **-1.86** (best Calmar) | −0.54pp worse return |
| **15%** | **-58.97%** | 53.03% | -1.87 | −0.27pp worse return |
| **20%** (default) | **-58.70%** | 52.76% | -1.88 | baseline (matches P3-01) |

Sorted by Calmar (higher = better): 10% > 15% > 20%. Sorted by return: 20% > 15% > 10%.

All levels lose to B&H (−33.49%), Cash (0%), and long-only grid (−25.20%) from P3-01.

## Q-tech-2 (initial short %)

**Answer:** No deployable sweet spot. Higher initial short fraction **reduces loss magnitude** monotonically (20% best return) but **all levels FAIL**. Lower init (10%) increases drawdown and worsens return — opposite of a rescue knob.

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** **FAIL** — no short_init level beats Cash, B&H, or grid-only baselines
- **C-05:** Reinforced **HIGH** — initial Short FSM not salvageable via init fraction alone
- **P3-13 partial:** Q-tech-2 answered for 10/15/20%; no MEDIUM+ candidate

## Red team (≥5)

1. Only three levels tested — 5% or 25% might differ (unlikely given monotonic trend)
2. Crypto book flat (0% DD) — sweep isolates Tech leg only; dual headline unchanged in ranking order
3. Calmar vs return tradeoff — 10% “best Calmar” still −59% return; not actionable
4. Base fill only — conservative not run on this sweep
5. Same 65d window as P1-11/P3-01 — no OOS confirmation

## Next

- P3-03 short structure directional vs grid vs 70/30 vs 50/50 (config ready)
- Do not promote any short_init level to live candidates
