# Review Log — P7-03 same-symbol L+S vs SOXL+SOXS pair long-grids

## Meta

- **date_utc:** 2026-09-15T21:55Z
- **task:** P7-03
- **data_class:** **BAR** (1h Vision klines; tick-precise fills **not** used)
- **window:** 2026-07-16 → 2026-09-11, 1383 bars
- **fees:** Base 2 bps + Conservative 4 bps (both reported)
- **engine:** `src/analysis/soxl_soxs_hedge.py` independent ATR long/short grids (0.40 step, ±5 ATR)
- **capital:** 10_000 USDT split 50/50 on two-book variants

## Hypothesis

Same-symbol long grid + short grid on SOXL leaves inventory drift in a trend.
SOXL long-grid + SOXS long-grid (SOXS already shorts the semiconductor book) should
cancel residual delta and keep two-sided grid harvest.

## Results (Base 2 bps)

| Strategy | Return | Max DD | End inventory / cap | Fills |
|----------|--------|--------|---------------------|-------|
| Pair SOXL+SOXS long grids | **+18.81%** | **−4.43%** | 23.3% | 2196 |
| Same-symbol SOXL L+S | +14.54% | −6.67% | **35.1%** | 3601 |
| SOXL-only long grid | +13.84% | −7.87% | ~0 | 1666 |
| B&H SOXL | −19.86% | −47.3% | — | — |
| B&H 50/50 static | −15.04% | −20.2% | — | — |
| B&H 50/50 daily rebalance | +2.94% | **−2.26%** | — | — |

Conservative 4 bps: pair **+17.25% / DD −4.48%**; same-symbol L+S +11.80% / −7.47%.
Fee does **not** flip the ranking.

## What this confirms about the user's pain

Same-symbol L+S **does** leave a large leftover book (35% notional, net short ~29 units).
Pair inventory is lower (23%) and DD is better. That matches “库存偏移 / 单边风险大”.

## What this does **not** prove

- **Not live.** BAR fills assume every level inside the bar range is touched.
- **Daily 50/50 B&H has a better DD (−2.26%)** than the pair grid. Complexity must earn its keep: the grid earns more return on this window, but a dumb daily rebalance is safer on drawdown.
- Static 50/50 **loses −15%** — classic 3x product decay if you do not rebalance. Do not “set and forget” both ETFs/perps.
- No funding, no OOS, no tick engine, no liquidation path.
- Residual vol is 16% of SOXL vol — a one-sided gap still hurts.

## Red team (≥5)

1. BAR penetration overstates grid harvest (Optimistic vs tick)
2. Turnover ~79× capital on pair — live fees/rebates/queue position matter
3. SOXL-only ending inventory ≈ 0 may be path luck + reanchor, not robustness
4. 57-day listing sample; crash-bounce regime (same as SNXX overlap)
5. Daily B&H DD wins — grid may be fitting chop, not a structural edge
6. No funding on UM perps
7. Thin SOXS prints some days
8. Must not promote to LIVE without P5/P6 gates

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **CONDITIONAL PASS** vs same-symbol L+S on this BAR window
- **live:** **NO** — research only; next is tick-precise fill + funding + OOS

## Next

- Finish P7-01 tick cache + manifest
- Tick-VWAP / tick-precise pair grid (do not promote on BAR alone)
- Compare pair grid vs daily 50/50 as the honest baseline (not vs SOXL B&H)
