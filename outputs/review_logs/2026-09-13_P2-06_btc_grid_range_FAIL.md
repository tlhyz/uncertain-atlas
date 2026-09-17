# Review Log — P2-06 BTC grid ATR range sweep

## Meta

- **date_utc:** 2026-09-13T11:00Z
- **experiment_id:** crypto_btc_grid_atr_range
- **task:** P2-06
- **config:** configs/experiments/crypto_btc_grid_atr_range.yaml
- **output:** outputs/experiments/crypto_btc_grid_atr_range/CRYPTO_REPORT.md
- **runtime:** ~330min (~5h30m; 3 ranges × ~110min/range est.)
- **fill_mode:** base (tick-precise)

## Results (C1 window, BTC only, step=0.40 ATR fixed, lev 1.5)

| Range | Return | MaxDD | Calmar | Liq |
|-------|--------|-------|--------|-----|
| ±3 ATR | **-86.90%** | 4.63% | **-21.57** | 0 |
| ±5 ATR (default) | -87.35% | 5.82% | -17.18 | 0 |
| ±7 ATR | -87.39% | 6.02% | -16.60 | 0 |

Final equity **1261–1310 USDT** from 10000. All `liquidation_count=0`.

## Verdict

- **task_verdict:** **PASS** (measurement complete, artifacts written)
- **strategy_verdict:** **FAIL** — no viable ±ATR range; all catastrophic ~-87%
- **Q-crypto-3:** Calmar nominally favors **±3 ATR** (-21.57) over default ±5 (-17.18), but all returns ~-87% — **not actionable**. Returns within ~0.5pp → inert plateau in failure band.

## Red team (≥5)

1. ±3/5/7 all collapse to ~13% of initial — range tuning does not rescue C1 crypto FSM  
2. Calmar ranking inverts vs return ranking (r3 best return AND best Calmar) — consistent but all FAIL  
3. Default r5.0 not optimal on Calmar but difference meaningless at -87% returns  
4. crypto_max_dd_pct 21–26% reported vs ~87% total return — accounting floor pattern persists  
5. Single C1 window; conservative fill not run  
6. ~110min/range runtime — pre-logging build had no per-variant logs

## vs LEDGER / C-06

Consistent with C-06 leverage FAIL (SOL/ETH ~-87–88%). Range sweep **inert** — same failure mode.

## Next

- P2-12 mark **done**; Q-crypto-3 finalized  
- P2-05 grid step sweep still running
