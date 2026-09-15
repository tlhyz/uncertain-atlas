# Review Log — P7-05 user SOXL 5x moving grid (TICK both legs)

## Meta

- **date_utc:** 2026-09-15T23:51Z
- **task:** P7-05
- **data_class:** **TICK** (aggTrades, Base 2 bps, both long and short)
- **user spec:** 5x isolated, 200 arithmetic rungs, moving (reanchor on band exit), 5000U long + 5000U short
- **range modes:** **±20 USDT** and **±20%** (both requested)
- **window:** 2026-07-16 → 2026-09-11, 1392 1h bars, 58 UTC days
- **output:** `outputs/experiments/soxl_user_ls_grid/summary.json`

## Results (independently recomputed from daily CSVs)

| Mode | Return | Max DD | End equity | Long | Short | Fills | Reanchors | Win days |
|------|--------|--------|------------|------|-------|-------|-----------|----------|
| ±20U | **−12.78%** | **−80.16%** | 8722.23 | **liquidated (−100%)** | +74.44% / DD −85.50% | 846 | 14 | 28/58 |
| ±20% | **−18.65%** | **−77.16%** | 8134.94 | **liquidated (−100%)** | +62.70% / DD −80.74% | 858 | 10 | 29/58 |

Best / worst UTC day: ±20U +4606.53 / −5543.72 (2026-08-18 / 2026-07-30). ±20% +4033.87 / −4854.54 (same dates).

After the long book is wiped, combined equity **is** the leftover short. Residual inventory 2.11× / 1.85× total capital (4.22× / 3.70× on the 5k short sleeve). That is not a hedge.

## Mechanism

SOXL printed **85.94–191.10** on this cache. A ±20U band is ~10–20% of mid at the high and a thin slice of the full path. 5x isolated + 200 tight rungs + a one-way dump (2026-07-30) takes the long sleeve through isolated MMR. Widening to ±20% did not save the long; it lost more on the full window.

Moving-grid reanchor recenters rungs and **clears the lot map without flattening qty**. Take-profit levels after a reanchor do not remember pre-reanchor lots. P7-05 numbers are exact under that rule.

## Red team (≥5)

1. Isolated 5x on a 3× ETP perp is leveraged-on-leveraged; long wipe is structural, not a one-tick glitch.
2. Combined book after liq is a naked leftover short, not L+S.
3. Funding omitted (would tax the surviving short).
4. One 58-day listing/overlap window.
5. Reanchor lot-map wipe can overstate inventory drift vs a broker that cancels-and-replaces working orders only.
6. Do not mix this with P7-04 +12.3% (that short leg was BAR, 1x ATR template).

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **FAIL** both ±20U and ±20%
- **live:** **NO**
- **soxl-lab:** classified under `soxl-lab/results/p7_05_*.json`
