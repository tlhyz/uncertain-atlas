# Review Log — P2-07 BTC grid→Trend mix sweep

## Meta

- **date_utc:** 2026-09-13T15:50Z
- **experiment_id:** crypto_btc_grid_mix_scan
- **task:** P2-07
- **config:** configs/experiments/crypto_btc_grid_mix_scan.yaml
- **output:** outputs/experiments/crypto_btc_grid_mix_scan/CRYPTO_REPORT.md
- **runtime:** ~608min (~10h8m; 6 mixes × ~102min/mix)
- **fill_mode:** base (tick-precise)

## Results (C1 window, BTC only, lev 1.5, step/range default)

| Mix | Return | MaxDD | Calmar | Liq |
|-----|--------|-------|--------|-----|
| 80_20 | -87.35% | 5.82% | -17.18 | 0 |
| 60_40 | -87.97% | 5.39% | -18.56 | 0 |
| 50_50 | -88.43% | 6.37% | **-15.70** | 0 |
| 40_60 | -88.12% | 1.65% | -60.50 | 0 |
| **20_80** | **-89.06%** | 0.90% | **-111.12** | 0 |
| dynamic | -87.35% | 5.82% | -17.18 | 0 |

Return spread **1.71pp** (-89.06% to -87.35%). Final equity ~**1094–1265 USDT** from 10000. All `liquidation_count=0`.

## Key observations

- **20_80 worst return** (-89.06%) — trend-heavy mix amplifies C1 failure  
- **dynamic ≡ 80_20** — identical -87.35% / -17.18 (regime routing inert on C1)  
- Calmar rank favors 50_50 (-15.70) but return still -88.43% — not actionable  
- 40_60 anomalous Calmar (-60.50) with low MaxDD 1.65% — accounting artifact, not edge

## Verdict

- **task_verdict:** **PASS** (measurement complete, artifacts written)
- **strategy_verdict:** **FAIL** — no grid→Trend mix rescues C1 crypto FSM; all catastrophic ~-87 to -89%

## Red team (≥5)

1. All mixes ~-87 to -89% — same failure band as leverage/ATR sweeps  
2. dynamic identical to 80_20 — dynamic routing provides no benefit on C1  
3. 20_80 trend-heavy worst — contradicts hypothesis that more trend helps  
4. crypto_max_dd_pct vs ~87% return — informal wipe pattern  
5. Single C1 window; conservative fill not run  
6. ~102min/mix BTC tick runtime

## vs prior sweeps

Consistent with P2-02/05/06 FAIL band. Mix ratio tuning **inert** in failure regime.

## Next

- **P2 phase complete** — all P2 tasks done/blocked  
- P3-01 dual Binance tick re-run unblocked (P0-02 still blocked on PR merge)
