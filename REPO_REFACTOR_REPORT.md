# Repository Refactor Report

**Branch:** `research/unified-tech-crypto-framework`  
**Date:** 2026-09-13  
**Scope:** PART 48 first delivery — framework only, **no full parameter sweeps**

---

## What changed

### 1. Documentation (`docs/`)

Created single source of truth for humans and AI:

- `THESIS.md` — Book A (Tech) / Book B (Crypto) market view
- `RESEARCH_HISTORY.md` — PROVEN / FAILED / WEAK / UNTESTED with preserved FAIL verdicts
- `DATA_POLICY.md` — no synthetic ticks, manifest policy
- `STRATEGY_TECH.md`, `STRATEGY_CRYPTO.md` — state machines & parameters
- `EXECUTION_MODEL.md`, `RISK_POLICY.md`
- `EXPERIMENTS.md`, `CURRENT_CONCLUSIONS.md`
- `CURSOR_HANDOFF.md` — includes **do-not-touch `uncertain-atlas`**

### 2. Configuration (`configs/`)

- `portfolio.yaml`, `fees.yaml`, `risk.yaml`, `universe.yaml`
- `experiments/` — tech_state_machine, crypto_regime, cross_market, gate_calibration
- Existing run configs preserved (`ab_etf_vs_perp.yaml`, `dual_engine_perp.yaml`, …)

### 3. Package layout (`src/`)

Migration-target package wrapping working `qtb/` modules:

- `src/data/` — Binance public, Gate, manifest, normalize
- `src/execution/` — limit fills, fees, funding, margin
- `src/strategies/`, `src/backtest/`, `src/analysis/`, `src/features/`

**`qtb/` unchanged as runtime engine** — tests still pass.

### 4. Scripts (`scripts/`)

- `download_binance.py`, `download_gate.py`, `build_manifest.py`
- `run_tech.py`, `run_crypto.py`, `run_cross_market.py`, `run_gate_oos.py`, `build_report.py`

### 5. Data policy (`.gitignore`)

- Ignores `data/raw/`, `data/cache/`, large CSV/ZIP/Parquet
- Tracks `data/manifests/` metadata only

### 6. Outputs archive

- **`outputs/research_sl_phase/`** — index for SL/ETF FAIL phase (reports stay at root paths)
- **`outputs/README.md`**, **`outputs/LIVE_CANDIDATES.md`** (low confidence placeholders)
- **`outputs/ab_etf_vs_perp/`**, **`outputs/dual_engine_perp/`** — **unchanged content**

### 7. Binance tick work (WIP on branch)

Continued from dual-engine branch (not part of refactor docs, but included):

- `qtb/data/binance_futures.py` — Vision aggTrades, ts_ms cache fix
- `qtb/dual/tick_*` — tick-precise fill path for SOXL/SNXX
- Config: Binance tech data, `tick_precise: true`, BTC C1 disabled

---

## What was preserved

| Item | Status |
|------|--------|
| `outputs/ab_etf_vs_perp/` full A/B report & JSON | ✅ Untouched |
| `outputs/dual_engine_perp/` FAIL verdict | ✅ Untouched |
| ETF grid FAIL conclusions | ✅ In RESEARCH_HISTORY |
| PERP > ETF for majors | ✅ Documented |
| 3x liq history (SOL/PENGU/PUMP) | ✅ Documented |
| Root legacy optimize scripts | ✅ Kept (marked legacy in archive) |
| **`uncertain-atlas/`** | ✅ **Not touched** (not on this branch) |

---

## What was NOT done (by design)

- Full Binance multi-year parameter sweeps
- Monte Carlo 1000-path production runs
- Gate Tech OOS calibration pass
- Merging `uncertain-atlas` branch
- Deleting `qtb/` or root legacy scripts (migration incremental)

---

## Data gaps (honest)

| Symbol / use | Gap |
|--------------|-----|
| SOXLUSDT Binance aggTrades | Available ~2025-05+; full manifest not built in this delivery |
| SNXXUSDT Binance aggTrades | Available ~2026-07+ |
| Gate SOXL/SNXX perp | Short history; many seed windows **STRUCTURAL_SEED_ONLY** |
| Gate funding | ~180d public depth; older bars may be zero-filled with warning |
| PENGU/PUMP Binance | List-date limited; meme cap 5% |
| Tick vs Gate fill | Binance structure ≠ Gate execution — OOS required |

---

## Next steps (after your confirmation)

1. Run `scripts/download_binance.py --detect-start` for BTC/ETH/SOL + SOXL/SNXX
2. `build_manifest.py` + per-bar aggTrades validation
3. **STEP 4:** Crypto 1.25–2x × ATR grid scan (Binance ticks, Base+Conservative)
4. **STEP 5:** Tech FSM tick-precise re-run — answer Q1–Q10 without bar fallback
5. **STEP 6:** Gate OOS on shortlisted params
6. **STEP 7–9:** Cross-market, portfolio, MC/plateau
7. Update `CURRENT_CONCLUSIONS.md` and `LIVE_CANDIDATES.md` with evidence classes

---

## How to verify this delivery

```bash
pytest -q
ls docs/
cat docs/RESEARCH_HISTORY.md
cat docs/CURSOR_HANDOFF.md  # uncertain-atlas out of scope
python scripts/download_binance.py --help
```

---

## PR summary

**What:** Research repo scaffold + docs + configs + download framework + `src/` migration layer.  
**Why:** Single auditable source of truth; separate structure research (Binance) from execution calibration (Gate).  
**Preserved:** All FAIL/STRONG conclusions and existing output directories.  
**Limitation:** No new sweeping backtests in this PR.  
**Next:** Binance manifest + tick-validated Tech/Crypto experiment matrix.
