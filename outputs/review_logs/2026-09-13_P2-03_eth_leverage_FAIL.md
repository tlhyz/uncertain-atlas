# Review Log — P2-03 ETH leverage scan

## Meta

- **date_utc:** 2026-09-13T07:50Z
- **experiment_id:** crypto_eth_leverage_scan
- **task:** P2-03
- **config:** configs/experiments/crypto_eth_leverage_scan.yaml
- **output:** outputs/experiments/crypto_eth_leverage_scan/CRYPTO_REPORT.md
- **runtime:** ~172 min (~2h52m; 4 levels × ~43 min/level)
- **fill_mode:** base (tick-precise)

## Results (C1 window, ETH only)

| Lev | Return | MaxDD | Calmar | Liq |
|-----|--------|-------|--------|-----|
| 1.25 | **-87.86%** | 17.06% | -5.86 | 0 |
| 1.5 | **-87.74%** | 17.27% | -5.79 | 0 |
| 1.75 | **-87.61%** | 17.40% | -5.74 | 0 |
| 2.0 | **-87.50%** | 17.58% | -5.69 | 0 |

Final equity **1214–1250 USDT** from 10000. `crypto_max_dd_pct=1.0` with `liquidation_count=0`.

## Verdict

- **task_verdict:** **PASS** (measurement complete, artifacts written)
- **strategy_verdict:** **FAIL** — no leverage sweet spot; catastrophic loss at all tested levels
- **Q-crypto-1 (ETH):** Calmar ranking favors 2.0x but all returns ~-87.5%; not actionable

## Red team (≥5)

1. Returns vary slightly by leverage (unlike SOL identical -88%) but all catastrophic — no deployable band  
2. crypto_max_dd_pct=1.0 with liq=0 → informal wipe vs formal liquidation mismatch  
3. C1 single window — ETH Sep–Nov 2024 hostile to grid FSM  
4. skip_tick_validation=true — manifests pre-validated but conservative fill not run  
5. ~43 min/level vs SOL ~19 min — ETH tick volume; results still FAIL regardless of runtime

## vs LEDGER-002

LEDGER-002 (majors 1.5–2x PERP > ETF) **does not apply to ETH grid FSM on C1 tick engine** — measured FAIL.

## Next

- Await P2-02 BTC scan (running ~5h+)  
- Update Q-crypto-1 ETH section complete  
- Do not deploy ETH crypto grid on C1 parameters
