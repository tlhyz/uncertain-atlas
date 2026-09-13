# Research History

Evidence classification used throughout this repo:

| Label | Meaning |
|-------|---------|
| **PROVEN** | Survives Base+Conservative fills, OOS or multi-asset replication |
| **STRONG EVIDENCE** | Consistent across regimes/assets; minor caveats documented |
| **WEAK EVIDENCE** | Directionally suggestive; short history or single window |
| **FAILED** | Hypothesis rejected on real data |
| **UNTESTED** | Designed but not yet executed with full pipeline |

---

## Experiment 001 — Gate 3L ETF Spot Grid (SL / Niulai phase)

**Status:** **FAILED** (multiple runs)  
**Artifacts:** `outputs/research_sl_phase/`, root `opt_niulai_*_report.md`, `outputs/demo_niulai_aggressive_sl50/`

**Conclusions (PROVEN on real Gate ETF data):**

- Grid **realized profit does not cover inventory + directional loss** → **TOTAL EQUITY fails**.
- High ETF volatility increases grid crossing but **does not reliably increase total equity**.
- 3L ETF is **not** safe for unattended long-run automation despite “no traditional liquidation”.
- BTC/ETH/SOL 3L can show **90%+ max drawdown** in sustained down moves.

**Evidence class:** **PROVEN FAIL**

---

## Experiment 002 — ETF vs Perpetual A/B (`qtb/ab`)

**Status:** **STRONG EVIDENCE** (real Gate overlap, Base+Conservative)  
**Artifacts:** `outputs/ab_etf_vs_perp/AB_REPORT.md`

| Asset class | Verdict |
|-------------|---------|
| BTC, ETH, SOL, SOXL, SNXX, AAOI | **PERP 1.5–2x grid preferred** over 3L ETF grid |
| PENGU, PUMP | ETF grid won in sample (meme path) |
| 3x PERP unattended | **FAILED** — liquidations on SOL, PENGU, PUMP |

**Rebate:** 70% Gate rebate **does not rescue** wrong direction + inventory + ETF path drag.

**Evidence class:** **STRONG EVIDENCE** (majors); **WEAK** (meme sample)

---

## Experiment 003 — Dual-Engine Tech Short→Grid→Trend

**Status:** **FAILED** on available Gate overlap (Jul–Sep 2026)  
**Artifacts:** `outputs/dual_engine_perp/DUAL_REPORT.md`

- Dual independent book **−51%** vs buy-and-hold **−30%** on overlap → **FAIL**.
- Initial Short→Long **underperforms** wait-for-directional-long and grid-only baselines.
- Most 2024–2025 seed windows: **STRUCTURAL_SEED_ONLY** (no Gate perp bars).

**Binance tick migration (in progress):** SOXLUSDT/SNXXUSDT Vision aggTrades exist from ~2025-05 / 2026-07; re-run pending after unified framework.

**Evidence class:** **FAILED** (Gate overlap); **UNTESTED** (Binance tick-precise full matrix)

---

## Experiment 004 — Crypto Independent Regime Book

**Status:** **WEAK EVIDENCE** / **UNTESTED** full matrix  
**Artifacts:** partial in `outputs/dual_engine_perp/` (Δreturn vs unified +2.3% on short overlap)

- Independent books modestly beat unified Tech signal on same window.
- Full Binance multi-year decoupling (CRYPTO_C1 2024-09→11) **not yet re-run** on tick engine.

**Evidence class:** **WEAK EVIDENCE**

---

## What is NOT Alpha (do not re-litigate without new data)

1. Long-run **3L ETF grid** as core strategy → **FAILED**
2. **3x PERP** as unattended default → **FAILED** (liquidation history)
3. **ETF rebate alone** as edge → **FAILED**
4. **Tech signal driving Crypto book** → **design rejected** (independent FSM required)

---

## Current research priority (post-refactor)

**Regime Switching Alpha:** state detection + grid + directional rotation — **UNTESTED** at full rigor on Binance ticks + Gate OOS.

See `docs/CURRENT_CONCLUSIONS.md` and `docs/EXPERIMENTS.md`.
