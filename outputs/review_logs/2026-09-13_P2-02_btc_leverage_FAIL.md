# Review Log — P2-02 BTC leverage scan

## Meta

- **date_utc:** 2026-09-13T15:40Z
- **experiment_id:** crypto_btc_leverage_scan
- **task:** P2-02
- **config:** configs/experiments/crypto_btc_leverage_scan.yaml
- **output:** outputs/experiments/crypto_btc_leverage_scan/CRYPTO_REPORT.md
- **runtime:** ~420min (~7h; restart 08:40Z; 4 levels × ~105min/level)
- **fill_mode:** base (tick-precise)

## Results (C1 window, BTC only)

| Lev | Return | MaxDD | Calmar | Final | Liq |
|-----|--------|-------|--------|-------|-----|
| 1.25 | **-87.47%** | 5.92% | -16.89 | 1253 | 0 |
| 1.5 | **-87.35%** | 5.82% | -17.18 | 1265 | 0 |
| 1.75 | **-87.32%** | 6.82% | **-14.67** | 1268 | 0 |
| 2.0 | **-87.06%** | 6.00% | -16.65 | 1294 | 0 |

Return spread **0.41pp** (-87.47% to -87.06%). Final equity **1253–1294 USDT** from 10000. `liquidation_count=0`; `crypto_max_dd_pct` 24–27%.

## Verdict

- **task_verdict:** **PASS** (measurement complete, artifacts written)
- **strategy_verdict:** **FAIL** — no leverage sweet spot; catastrophic loss at all tested levels
- **Q-crypto-1 (BTC):** Calmar rank favors 1.75x; 2.0x best return but all ~-87% — **not actionable**

## Red team (≥5)

1. All levels ~-87% — same catastrophic band as ETH/SOL leverage sweeps  
2. Calmar ranking inverts vs return ranking (1.75x best Calmar, 2.0x best return) — not deployable either way  
3. crypto_max_dd_pct ~25% vs ~87% return — informal wipe vs formal liquidation mismatch  
4. C1 single window — BTC Sep–Nov 2024 hostile to crypto grid FSM  
5. skip_tick_validation=true — manifests pre-validated; conservative fill not run  
6. ~105min/level BTC tick runtime — P2-15 bottleneck confirmed; results FAIL regardless

## vs LEDGER-002

LEDGER-002 (majors 1.5–2x PERP > ETF) **does not apply to BTC grid FSM on C1 tick engine** — measured FAIL.

## Next

- P2-10 Q-crypto-1 finalize **done**  
- Await P2-07 grid mix dynamic (~16:00Z)  
- Do not deploy BTC crypto grid on C1 parameters
