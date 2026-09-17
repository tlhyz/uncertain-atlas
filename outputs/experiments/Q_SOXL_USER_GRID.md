# Q: Is the user SOXL 5x moving L+S grid tradeable?

**Answer: NO.** Confidence HIGH on the written book (5x / 200 / ±20U / flatten).
Legitimate terminal: no edge that survives as a hedge.

## The written book

5x isolated, 200 arithmetic rungs, moving band ±20 USDT (also tested ±20%),
5k long + 5k short, flatten the survivor on first liquidation. Tick fills.

## Evidence

| ID | Window | Fills | Result |
|----|--------|-------|--------|
| P7-05 | 07-16→09-11 | tick | Independent L+S **FAIL** — long liq, leftover short |
| P7-07 | 07-16→09-11 | tick | Flatten **STOPPED 07-28** long liq; +15.6% then 45 zero days |
| P7-15 | 05-15→07-15 / 120d | tick | Flatten **STOPPED 05-26** short liq; +39.3% then cash; 120d does not restart |
| P7-16–18 | 05-15→09-11 | tick | Death cliff ±20U **(2.5, 3]**; 2x±20U +70% this path; 2x±20% **−20.5%** |
| P7-19 | 05-15→09-11 | tick | `restart_survivor` **FAIL** — 3 deaths, leftover re-levered, inv 14× |

SOXL buy-and-hold 05-15→09-11: **−24.4%**. Honest no-grid hedge remains daily 50/50 (W-03).

## What is not a counterexample

- BAR +37% on the prefix (P7-14) — wick, same class as overturned P7-03.
- Flatten +15.6% / +39.3% — locked survivor PnL + empty days.
- 2x/2.5x ±20U +70%/+86% — not 5x; inventory 1.8–2.3; ±20% loses.
- Restart +271% — three wipes, forbidden-adjacent recovery.

## Do not

Deploy 5x flatten. Switch default to 2x. Quote restart. Retry P3-11. Commit ticks.
