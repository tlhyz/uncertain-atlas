# Review Log — P7-04 tick-precise SOXL/SOXS pair grid

## Meta

- **date_utc:** 2026-09-15T22:34Z
- **task:** P7-04
- **data_class:** **TICK** (path-exact aggTrades, Base + Conservative fills)
- **grid default:** ATR step **0.40**, range **±5** (LIVE_CANDIDATES / Tech template)
- **window:** 2026-07-16 09:00Z → 2026-09-11 23:00Z, 1383 aligned hours
- **output:** `outputs/experiments/soxl_soxs_hedge/tick_hedge_report.json`

## SOXL ticks confirmed

P7-01: 1392/1392 SOXL bars have aggTrades; 31.2M prints. Ready for tick fills.

## Inverse still holds (prices)

corr −0.988, β −0.991 — same as BAR. The **marks** hedge. The **grids** do not.

## Default grid 0.40 / ±5 (Base 2 bps, TICK)

| Strategy | Return | Max DD | Inventory / cap | Fills |
|----------|--------|--------|-----------------|-------|
| Pair SOXL+SOXS long grids | **−6.0%** | **−20.1%** | 85% | 371 |
| Same-symbol SOXL L+S | +12.3% | −17.7% | 78% | 2193 |
| SOXL-only long grid | +9.3% | −45.2% | 86% | 258 |
| Daily 50/50 B&H | +2.9% | **−2.3%** | — | — |

Conservative 4 bps: pair **−5.1% / DD −20.1%**. Ranking unchanged.

Pair equity vs SOXL path corr **+0.71** (BAR was −0.39). Tick fills leave residual **long SOXL** — not a hedge.

BAR P7-03 (+18.8% / −4.4%) is **overturned**: wick-touch overstated harvest.

## Param sweep (TICK, Base) — all FAIL

| step | range | pair ret | pair DD | vs same-LS DD |
|------|-------|----------|---------|---------------|
| 0.40 | ±3 | −4.7% | −12.6% | worse (−7.8%) |
| 0.50 | ±5 | +10.4% | −17.6% | worse (−16.5%) |
| 0.40 | ±5 | −6.0% | −20.1% | worse (−17.7%) |
| 0.30 | ±3 | −14.8% | −21.1% | worse (−13.4%) |

No spacing rescues the pair vs same-symbol L+S. None approach daily 50/50 DD −2.3%.

## Mechanism

1. Tick + participation cap (Base 20% / Cons 5%) → few pair fills (371 vs BAR 2196)
2. Both books accumulate inventory (85%) instead of cycling
3. SOXL is much thicker than SOXS (31M vs 7.7M prints) → asymmetric fill → leftover SOXL delta
4. Daily equal-notional rebalance **is** the hedge; adding grids re-introduces inventory risk

## Red team (≥5)

1. Funding still omitted (would worsen pair if both pay)
2. 57-day listing window only
3. Collapse of monotone ticks is exact for crossings but drops print timestamps
4. Same-symbol L+S short leg still BAR (pair longs are TICK) — does not help the pair
5. 0.50/±5 pair return +10% is one-window luck; DD still fails
6. Must not revive BAR P7-03 CONDITIONAL PASS

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **FAIL**
- **live:** **NO**
- **W-03 grid hedge:** **retract** — inverse marks ≠ grid hedge
- **Honest hedge on this window:** daily 50/50 rebalance, no grid
