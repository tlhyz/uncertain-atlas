# Review Log — P2-04 SOL leverage scan

## Meta

- **date_utc:** 2026-09-13T05:44Z
- **experiment_id:** crypto_sol_leverage_scan
- **task:** P2-04
- **config:** configs/experiments/crypto_sol_leverage_scan.yaml
- **output:** outputs/experiments/crypto_sol_leverage_scan/CRYPTO_REPORT.md
- **runtime:** ~53 min (4 levels × ~19 min/level)
- **fill_mode:** base (tick-precise)

## Results (C1 window, SOL only)

| Lev | Return | MaxDD | Calmar | Liq |
|-----|--------|-------|--------|-----|
| 1.25 | **-88.01%** | 39.72% | -2.52 | 0 |
| 1.5 | **-88.01%** | 39.87% | -2.51 | 0 |
| 1.75 | **-88.01%** | 40.03% | -2.50 | 0 |
| 2.0 | **-88.01%** | 40.19% | -2.49 | 0 |

Final equity ~**1199 USDT** from 10000 at all leverage levels. `crypto_max_dd_pct=1.0` (100% crypto book drawdown) with `liquidation_count=0`.

## Verdict

- **task_verdict:** **PASS** (measurement complete, artifacts written)
- **strategy_verdict:** **FAIL** — no leverage sweet spot; catastrophic loss at all tested levels
- **Q-crypto-1 (SOL partial):** No viable 1.25–2.0x band; ranking by Calmar nominally favors 2.0 but all returns identical (~-88%)

## Red team (≥5)

1. Identical returns across leverage → exposure/utilization bug or wallet floor, not leverage effect  
2. crypto_max_dd_pct=1.0 with liq=0 → informal wipe vs formal liquidation mismatch  
3. C1 window single regime — SOL Sep–Nov 2024 may be hostile to grid FSM  
4. skip_tick_validation=true — data gaps could distort fills (SOL Sep-04 was fixed earlier)  
5. Conservative fill not run — Base-only ranking may be optimistic

## vs LEDGER-002

LEDGER-002 (majors 1.5–2x PERP > ETF) **does not apply to SOL grid FSM on this window** — measured FAIL overrides any prior bar-mode evidence for this config.

## Next

- Compare BTC/ETH leverage scans when complete  
- Investigate identical-return anomaly in portfolio accounting  
- Do not deploy SOL crypto grid on C1 parameters
