# P7-15 — listing-prefix 62d TICK flatten hedge

Verdict: **STOPPED** (same class as P7-07). Not a 62-day or 120-day hedge.

User book: 5x / 200 arithmetic / 5k+5k / flatten_survivor. Fills: **tick**.
Window 2026-05-15→07-15 is the listing prefix P7-07 never used.

## Results

| Run | Band | Window | Return | Max DD | Stop | Dead side |
|-----|------|--------|--------|--------|------|-----------|
| p715u | ±20U | 05-15→07-15 | +39.3% | −11.3% | **2026-05-26** | short −100% |
| p715p | ±20% | 05-15→07-15 | +34.5% | −6.7% | **2026-05-27** | short −100% |
| p715full | ±20U | 05-15→09-11 | +39.3% | −11.3% | **2026-05-26** | short −100% |

p715u: 10 win days, **50 zero days**. Long book +178% then flattened; short wiped.
p715full equals p715u equity — the book **does not restart**. The July dump that
killed the long in P7-07 is never seen because the pair is already cash.

JSON: `outputs/experiments/p7_15_listing_prefix_tick/compare.json`.

P7-14 BAR +37.6% happened to sit near the TICK number because the pair died in
~12 days; that is coincidence, not a reason to trust BAR on live windows.

## How +39% is fake as a hedge (≥5)

1. Strategy is off after **12 calendar days**. The other 50/108 days are empty.
2. Short liquidated; the +% is leftover **long** inventory marked then flattened.
3. Mirror of P7-07: there long died 07-28 and leftover short looked +15.6%.
4. 120d stitch proves flatten_survivor will not trade the second regime.
5. win_days 10/62 or 10/120 is not a hedge win rate.
6. No funding. Isolated 0.5% MMR.

## Comparison

| Window | First death | Locked look | Idle after |
|--------|-------------|-------------|------------|
| P7-15 05-15→07-15 | short 05-26 | +39.3% | 50d |
| P7-07 07-16→09-11 | long 07-28 | +15.6% | 45d |

Same rule, opposite side, same artifact.

## Do not

Quote +39% as live. Retry P3-11. Treat P7-14 BAR as confirmation.
