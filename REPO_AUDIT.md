# REPO_AUDIT.md — gate-grid-martingale

> Phase 1A: Full repository audit  
> Date: 2026-09-13 UTC | Auditor: Phase 1 agent | Branch: `cursor/unified-tech-crypto-framework-cbaf`  
> Git HEAD: `0dc777f8` | Tests: **79 passed** in 6.89s

---

## 1. Repository Identity

| Field | Value |
|-------|-------|
| Name | gate-grid-martingale |
| Purpose | Multi-market grid / regime-switching quant research (Gate + Binance) |
| Version | 0.3.0 (`pyproject.toml`) |
| Active branch | `cursor/unified-tech-crypto-framework-cbaf` |
| Open PRs | #4 (ETF A/B), #6 (ETF A/B), #7 (dual-engine), #8 (unified framework) — **#8 is primary SSOT** |
| Out of scope | `uncertain-atlas/` on branch `cursor/uncertain-architecture-atlas-11a5` |

---

## 2. Architecture

```
configs/          Capital, fees, risk, experiment YAML — SSOT for parameters
docs/             Thesis, policies, ledger, handoff
qtb/              Working engine (CLI, A/B, dual, optimize, legacy backtest)
src/              Migration target — mostly thin re-exports to qtb/
scripts/          download_binance, download_gate, build_manifest, run_* stubs
tests/            13 modules, 79 tests
data/manifests/   Tracked checksum metadata (5 files)
cache/            Gitignored local aggTrades/OHLCV
outputs/          Tracked reports, JSON, review logs
```

**SSOT tension:** Documentation points to `src/` as target package, but **all runnable code lives in `qtb/`**. Migration incomplete.

---

## 3. Pull Request History

| PR | Branch | Title | Key Result | Status |
|----|--------|-------|------------|--------|
| #4 | gate-etf-deals | Gate 3L ETF tick research | **FAIL** — grid inventory loss | DRAFT |
| #6 | etf-vs-perp-ab | ETF vs PERP A/B | **STRONG** — PERP wins majors | OPEN |
| #7 | dual-engine-perp | Dual Tech/Crypto FSM | **FAIL** — Short→Long -51% vs B&H -30% | DRAFT |
| #8 | unified-framework | Docs + Binance ticks + review policy | Phase 1 SSOT; 7d tick FAIL | DRAFT |
| #5 | uncertain-atlas | Blockchain research | **Out of scope** | DRAFT |

---

## 4. Commit Timeline (Research-Relevant)

| Commit | Summary |
|--------|---------|
| `5e036069` | Fair Gate ETF vs PERP A/B engine |
| `84a16918` | Real-data A/B results; unattended verdict fix |
| `5c0cbf72` | Dual-engine Tech/Crypto FSM framework |
| `014d3f79` | Binance Vision aggTrades + crypto tick fills |
| `471d819a` | Research thesis, policies, history docs |
| `16da110e` | Centralized configs |
| `ad9aaca9` | Binance/Gate loaders, manifests, scripts |
| `0dc777f8` | P1 tick validation + 7d Binance smoke FAIL |

---

## 5. Outputs Inventory

| Directory | Experiment | Verdict | Precision |
|-----------|------------|---------|-----------|
| `outputs/research_sl_phase/` | 3L ETF grid SL phase | **FAIL** | BAR (Gate ETF) |
| `outputs/ab_etf_vs_perp/` | ETF vs PERP A/B | **STRONG** (majors PERP) | BAR (Gate) |
| `outputs/dual_engine_perp/` | Tech Short→Long FSM | **FAIL** | BAR (Gate) |
| `outputs/dual_engine_perp_binance_ticks/` | 7d tick smoke | **FAIL** | TICK (Binance) |
| `outputs/dual_engine_perp_binance_ticks_65d/` | 65d full window | **IN PROGRESS** | TICK |
| `outputs/demo_*` | Legacy BTC grid demos | Not primary evidence | Mixed |
| `outputs/review_logs/` | Session review trail | 1 FAIL log | — |

**Review log policy:** Operational — template, INDEX, HEARTBEAT, Cursor rule present.

---

## 6. Data Pipeline Audit (Phase 1D)

### Binance

| Component | File | Status |
|-----------|------|--------|
| aggTrades downloader | `qtb/data/binance_futures.py` | ✅ Vision daily ZIP + cache |
| klines | same | ✅ |
| CLI | `scripts/download_binance.py` | ✅ |
| Manifest builder | `scripts/build_manifest.py` | ⚠️ rows=0 bug for ETH |
| Tech validation | `qtb/dual/tick_validate.py` | ✅ SOXL 1546/1546, SNXX 1546/1546 |

### Gate

| Component | File | Status |
|-----------|------|--------|
| Candles | `qtb/data/candles.py` | ✅ REST + cache |
| Funding | `qtb/data/funding.py` | ✅ |
| Contracts | `qtb/data/contracts.py` | ✅ |
| Trades/ticks | — | ❌ Not implemented |

### Manifests (`data/manifests/`)

| Symbol | Days | Rows | Issue |
|--------|------|------|-------|
| SOXLUSDT | 65 | OK | — |
| SNXXUSDT | 65 | OK | — |
| BTCUSDT | 91 | OK | — |
| ETHUSDT | 4 | **0** | 291MB files but rows_est=0 — corrupt parse or manifest bug |
| SOLUSDT | 3 | **0** | Same |

### Data Policy Compliance

- ✅ No synthetic ticks in code path (`FORBIDDEN_SOURCES` in `qtb/ab/data.py`)
- ✅ STRUCTURAL_SEED_ONLY labeling in dual provenance
- ❌ DATA_QUALITY_REPORT gate not implemented
- ⚠️ Sep 12 Vision aggTrades empty — documented gap

---

## 7. Execution Engine Audit (Phase 1E)

| Feature | Location | Status |
|---------|----------|--------|
| Bar fills O/B/C | `qtb/ab/fills.py` | ✅ Tested |
| Tick fills | `qtb/dual/tick_fills.py` | ✅ Partially tested |
| A/B engine | `qtb/ab/engine.py` | ✅ Well tested |
| Dual portfolio | `qtb/dual/portfolio.py` | ✅ Smoke tested |
| Tech FSM | `qtb/dual/tech_fsm.py` | ⚠️ No leak tests |
| Crypto FSM | `qtb/dual/crypto_fsm.py` | ⚠️ Independence asserted, not fully tested |
| Legacy martingale | `qtb/engine/backtest.py` | ⚠️ Pre-refactor; martingale **forbidden** by policy |

**Fill mode policy:** Documented; Optimistic still callable — not blocked in code.

**Red-team finding:** `qtb/dual/report.py` Q1–Q15 answers appear **static** across Gate and Binance runs with different outcomes. Parameter recommendations (0.40 ATR, 70/30 weights) may not reflect executed sweeps.

---

## 8. Accounting Audit (Phase 1F)

| Check | Status |
|-------|--------|
| Equity formula documented | ✅ `qtb/ab/engine.py` |
| Perp uPnL + IM + reserve | ✅ Implemented |
| Trade-level fee/rebate/funding | ✅ `TradeRec` |
| Per-bar invariant assertion | ❌ Missing |
| Daily reconciliation | ❌ Missing |
| Property tests (flat price, 0 fee) | ❌ Missing |
| `ACCOUNTING_INVARIANTS.md` | ❌ Missing |

---

## 9. No-Future-Leak Audit (Phase 1G)

| Check | Status |
|-------|--------|
| `test_no_future_leak.py` | ❌ **Does not exist** |
| Signal implementation | `qtb/dual/signals.py` — docstring claims no leak |
| Regime features | `qtb/ab/regimes.py`, `src/features/regime.py` — untested |
| Walk-forward isolation | Not enforced |

---

## 10. Test Suite

| Module | Tests | Coverage Area |
|--------|-------|---------------|
| `test_ab_etf_perp.py` | 14 | A/B engine core |
| `test_dual_engine.py` | 7 | FSM + portfolio smoke |
| `test_tick_fills.py` | 2 | Tick fill + validation |
| `test_costs.py` | 8 | Fees, funding, slippage |
| `test_exits.py` | 7 | SL/TP, liquidation |
| `test_repo_framework.py` | 6 | Docs, configs, backlog |
| `test_data_policy.py` | 2 | Synthetic tick ban |
| Others | 33 | Fees, score, screen, niulai, dry_run, binance |

**Gaps:** no future leak, no accounting invariants, no property tests, no DATA quality gate tests.

---

## 11. Configuration SSOT

| File | Purpose |
|------|---------|
| `configs/portfolio.yaml` | 6500/2500/1000 capital split |
| `configs/fees.yaml` | Gate fee schedules |
| `configs/risk.yaml` | Leverage limits, meme cap |
| `configs/universe.yaml` | Asset lists |
| `configs/dual_engine_perp.yaml` | Primary dual config (Binance ticks) |
| `configs/experiments/*.yaml` | 7 experiment configs |

Configs are well-centralized. ✅

---

## 12. Stale Processes (Observed)

Two long-running backtests from **prior session** (not started in Phase 1):

1. `python3 -m qtb.cli dual -c configs/dual_engine_perp.yaml` — since Sep 12 (~36min CPU)
2. `python3 -m qtb.cli dual -c configs/experiments/dual_binance_tick_65d.yaml` — since 00:20 (~17min CPU)

**Recommendation:** Do not start new runs until DATA_QUALITY gate exists. Complete or kill stale runs before Phase 2.

---

## 13. Conclusions Integrity Check

| Prior Conclusion | Audit Verdict | Action |
|------------------|---------------|--------|
| 3L ETF grid FAIL | ✅ Supported by artifacts | Keep FAILED |
| PERP 1.5–2x STRONG | ✅ AB_REPORT on real Gate data | Keep STRONG |
| 3x PERP unattended FAIL | ✅ Liquidation history | Keep FAILED |
| Rebate not alpha FAIL | ✅ Q7–Q8 in AB report | Keep FAILED |
| Short→Long FAIL | ✅ Replicated Gate + Binance tick | Keep FAILED |
| Independent crypto WEAK | ✅ Single window partial | Keep WEAK |
| 0.40 ATR plateau WEAK | ⚠️ Template text only | **Downgrade confidence** — needs sweep |

**No conclusions overturned in Phase 1 audit.**

---

## 14. Phase 1 Verdict

| Criterion | Result |
|-----------|--------|
| Repo auditable | ✅ |
| History preserved | ✅ |
| Governance docs created | ✅ |
| Ready for mass research | ❌ |
| Ready for targeted Phase 2 #1 (Short vs Cash) | ⚠️ After infra tasks |

**Overall:** **CONDITIONAL PASS** — proceed to infra fixes (GAP_ANALYSIS §9), not parameter sweeps.
