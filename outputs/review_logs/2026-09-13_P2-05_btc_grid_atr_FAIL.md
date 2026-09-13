# Review Log — P2-05 BTC grid ATR step sweep

## Meta

- **date_utc:** 2026-09-13T12:10Z
- **experiment_id:** crypto_btc_grid_atr_step
- **task:** P2-05
- **config:** configs/experiments/crypto_btc_grid_atr_step.yaml
- **output:** outputs/experiments/crypto_btc_grid_atr_step/CRYPTO_REPORT.md
- **runtime:** ~419min (~6h59m; 4 steps × ~105min/step est.)
- **fill_mode:** base (tick-precise)

## Results (C1 window, BTC only, range=±5 ATR fixed, lev 1.5)

| Step | Return | Calmar | Liq |
|------|--------|--------|-----|
| 0.30 | -87.39% | -16.61 | 0 |
| **0.40 (default)** | **-87.35%** | **-17.18** | 0 |
| 0.50 | -87.55% | -15.33 | 0 |
| 0.60 | -87.35% | -17.17 | 0 |

Final equity **1245–1265 USDT** from 10000. All `liquidation_count=0`.

## Plateau check (pre-registered)

- Return spread **0.20pp** (-87.35% to -87.55%) — flat **failure-band plateau**, not actionable
- **0.40 NOT in top-3 by Calmar** (rank 4/4; 0.50 best Calmar at -15.33)
- Top-3 returns within ≤10% of best — yes, but all ~-87%

## Verdict

- **task_verdict:** **PASS** (measurement complete, artifacts written)
- **strategy_verdict:** **FAIL** — no viable ATR step; spacing tuning inert on C1
- **Q-crypto-2 / W-02:** **FAIL** — 0.40 ATR **not** on parameter plateau; prior LOW-confidence claim **not supported**

## Red team (≥5)

1. All steps ~-87% — same failure mode as leverage/range sweeps  
2. 0.50 Calmar best but still -87.55% return — not deployable  
3. Default 0.40 worst Calmar — do not promote W-02  
4. crypto_max_dd_pct 25–27% vs ~87% return — accounting floor  
5. ~105min/step runtime; pre-logging build had no per-step logs  
6. Single C1 window; conservative fill not run

## Next

- P2-11 mark **done**; Q-crypto-2 finalized  
- Await P2-02 full BTC leverage scan
