# Review Log — P7-07 user moving L+S hedge

## Meta

- **date_utc:** 2026-09-16T00:11Z
- **task:** P7-07
- **user spec:** moving grid + long/short hedge; 5x; 200 rungs; ±20U and ±20%; 5k+5k
- **engine:** shared band, same tick path, flatten survivor if either sleeve liquidates
- **output:** `outputs/experiments/soxl_user_ls_hedge/summary.json`

## Why rerun

P7-05 ran two isolated books. After the long wipe the short kept trading → leftover naked short, **not a hedge**.

## Results (TICK, Base 2 bps, 1392 bars)

| Mode | Combined ret | Combined DD | End | Long | Short | Stop | Win / zero days |
|------|--------------|-------------|-----|------|-------|------|-----------------|
| ±20U | **+15.61%** | **−6.03%** | 11561 | liq | flattened, qty 0 | bar 301 ≈ **2026-07-28** | 8 / 45 |
| ±20% | **+6.21%** | **−9.71%** | 10621 | liq | flattened, qty 0 | bar 301 ≈ **2026-07-28** | 9 / 45 |

Daily CSVs match JSON. Implied start capital 10,000.

## vs P7-05 (independent books)

±20U went from **−12.8% / −80%** to **+15.6% / −6%** only because the short was cashed when the long died, instead of riding another 45 days.

## Red team

1. Pair is dead after ~12 days — not a 58-day hedge.
2. Path luck: the dump that killed the long also made the short flatten in profit.
3. 45 zero-PnL days inflate “calm” DD vs a book that stayed in the market.
4. Long sleeve still −100% of its 5k. Isolated 5x on a 3× ETP is unchanged.
5. Funding omitted. Reanchor still clears lot maps without flattening qty before the stop.
6. Daily 50/50 (+2.9% / −2.3%) stayed invested the whole window.

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **STOPPED** — hedge rule works; book does not survive the first long liq
- **live:** **NO**
- **do not cite P7-05 as the user’s hedge**
