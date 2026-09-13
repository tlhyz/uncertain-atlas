# Review Log — P2-08 High-vol range regime auto-label sample

**Date (UTC):** 2026-09-13T05:50Z  
**Task:** P2-08  
**Verdict:** **PASS**

---

## Deliverable

Script: `scripts/crypto_regime_label_sample.py`  
Output: `outputs/experiments/crypto_regime_label_sample/REGIME_LABEL_SAMPLE.md`

Runs `CryptoAssetFSM.classify()` bar-by-bar on C1 klines (no tick backtest, ~0.6s).

---

## Findings (2024-09-01 → 2024-11-30)

| Symbol | RANGE_HIGH_VOL | RANGE_LOW_VOL | BULL | BEAR |
|--------|----------------|---------------|------|------|
| BTC | **0** (0%) | 2184 (100%) | 0 | 0 |
| ETH | **0** (0%) | 2183 (99.95%) | 0 | 1 |
| SOL | **3** (0.14%) | 2170 (99.36%) | 0 | 11 |

SOL high-vol samples: Nov-17 11:00 (1 bar), Nov-17 13:00–14:00 (2 bars).

---

## Interpretation

C1 window is overwhelmingly **RANGE_LOW_VOL** per FSM thresholds (`rv >= 0.012` for HIGH_VOL rarely triggered). Grid-heavy crypto params dominate this window; high-vol regime tests (P2 grid sweeps) operate mostly in low-vol classification.

---

## Tests

127 passed (no new test — script is deterministic label export).

---

## Next

Consider lowering `rv` threshold or adding rolling-window label audit if high-vol grid behavior needs isolated testing.
