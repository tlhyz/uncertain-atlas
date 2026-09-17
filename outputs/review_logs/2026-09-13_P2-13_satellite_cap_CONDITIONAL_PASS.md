# Review Log — P2-13 PENGU/PUMP satellite cap 5% test

## Meta

- **date_utc:** 2026-09-13T06:50Z
- **experiment_id:** crypto_satellite_cap
- **task:** P2-13
- **script:** scripts/crypto_satellite_cap_test.py
- **output:** outputs/experiments/crypto_satellite_cap/CRYPTO_SATELLITE_REPORT.md
- **execution:** BAR (Gate 1h klines + funding)
- **fill_mode:** base

## Policy check (PASS)

Added `satellite_cap_budgets()` / `satellite_cap_ok()` in `qtb/dual/universe.py`:

- Combined meme budget = **500 USDT** (5% of 10k account)
- Even split: **250 USDT each** for PENGU + PUMP (2.5% each)
- `satellite_cap_ok`: **True**
- Max trade notional per leg ≤ budget × leverage (cap_respected=True)

Unit tests: `tests/test_satellite_cap.py` (3 passed).

## BAR backtest (Gate overlap ~Jul-2025→Sep-2026)

| Symbol | Budget | Return | MaxDD | Liq | Cap OK |
|--------|--------|--------|-------|-----|--------|
| PENGU | 250U (2.5%) | **-99.3%** | 99.3% | 0 | Y |
| PUMP | 250U (2.5%) | **-98.6%** | 98.6% | 0 | Y |

Final equity ~1.8U / 3.6U from 250U each at 1.0x leverage.

## C1 tick-precise integration (BLOCKED)

- No Binance aggTrades manifests for PENGUUSDT / PUMPUSDT
- C1 window (2024-09→11) predates Gate PENGU/PUMP listing (~Jul-2025)
- Cannot wire satellites into `load_binance_crypto_dataset` tick path without new data

## Verdict

- **task_verdict:** **PASS** (cap policy measured + enforced; artifacts written)
- **strategy_verdict:** **FAIL** — meme grid at 1.0x still wipes satellite sleeve on available Gate window
- **overall:** **CONDITIONAL PASS** (same pattern as P2-09: structural OK, full tick backtest blocked)

## Red team (≥5)

1. BAR mode ≠ tick-precise — fills optimistic vs Binance aggTrades path  
2. Gate window Jul-2025+ only — cannot test C1 decoupling hypothesis for memes  
3. -99% with liq=0 — informal wipe vs formal liquidation (same anomaly as P2-04 SOL)  
4. Even 5% cap does not prevent total loss of satellite sleeve — cap limits blast radius not alpha  
5. Prior A/B showed ETF win on memes (WEAK) — this grid FSM config contradicts that path

## vs LEDGER / X-02

Consistent with **X-02** (3x PERP unattended FAILED on PENGU/PUMP). Cap policy correctly limits account exposure to 5% but does not rescue strategy PnL.

## Next

- P2-14 CRYPTO_C1 full tick run (BTC/ETH/SOL only until meme manifests exist)  
- Do not promote meme satellites beyond LOW confidence in LIVE_CANDIDATES  
- When P2-02/03 complete, finalize Q-crypto-1
