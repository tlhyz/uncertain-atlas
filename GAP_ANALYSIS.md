# GAP_ANALYSIS.md — gate-grid-martingale

> Phase 1 audit: gaps between **current state** and **research system requirements** (user spec sections 0–104).  
> Date: 2026-09-13 | Branch: `cursor/unified-tech-crypto-framework-cbaf` | Tests: 79 pass

---

## Executive Summary

The repository has a **working research prototype** (Gate A/B, dual-engine FSM, Binance aggTrades pipeline, Base/Conservative fills) with **honest FAIL preservation**. It is **not yet** a robust autonomous research system. Critical gaps block credible Phase 2 experiments at scale.

**Top blockers (must fix before mass research):**

1. No `DATA_QUALITY_REPORT` gate — experiments can run on corrupt data (ETH manifest rows=0)
2. No `test_no_future_leak.py` — signal integrity unverified
3. No formal `ACCOUNTING_INVARIANTS` tests — equity conservation not asserted per bar
4. Dual report Q1–Q15 uses **static template text** — parameter recommendations may be fake
5. Monte Carlo, walk-forward, experiment output schema incomplete
6. `src/` migration layer mostly stubs — SSOT split between `qtb/` and `src/`

---

## 1. Data Layer (DATA-001 → DATA-018)

| ID | Requirement | Status | Gap |
|----|-------------|--------|-----|
| DATA-001 | Binance trades downloader | **Partial** | Vision aggTrades via `qtb/data/binance_futures.py` + `scripts/download_binance.py` |
| DATA-002 | Binance aggTrades | **Done** | SOXL/SNXX 65d validated; ETH/SOL cache corrupt (rows=0 in manifest) |
| DATA-003 | Binance funding | **Partial** | Used in engine; no standalone downloader test suite |
| DATA-004 | Binance klines | **Done** | Vision + REST fallback |
| DATA-005 | Gate trades | **Missing** | No tick/trade downloader; candles only |
| DATA-006 | Gate funding | **Done** | `qtb/data/funding.py` |
| DATA-007 | Contract metadata | **Partial** | `qtb/data/contracts.py` — no versioned history |
| DATA-008 | Symbol lifecycle | **Missing** | No listing/delisting tracker |
| DATA-009 | Tick size history | **Missing** | Static contract specs only |
| DATA-010 | Missing data detector | **Partial** | Tick validation in `tick_validate.py`; no unified detector |
| DATA-011 | Duplicate detector | **Missing** | — |
| DATA-012 | Outlier detector | **Missing** | — |
| DATA-013 | Clock normalization | **Partial** | ts_ms fix applied; no formal normalization module |
| DATA-014 | Checksum system | **Partial** | `src/data/manifest.py` sha256; build_manifest rows count bug |
| DATA-015 | Data manifest | **Partial** | 5 manifests; ETH rows=0 despite 291MB files |
| DATA-016 | Dataset versioning | **Missing** | No semver on datasets |
| DATA-017 | Cross-venue validation | **Missing** | Binance vs Gate price check not implemented |
| DATA-018 | Completeness score | **Missing** | — |

**DATA_QUALITY_REPORT gate:** **IMPLEMENTED** (`src/data/quality_gate.py`, dual integration, 9 tests).

**Unit tests per DATA task:** DATA-002 + quality gate covered; DATA-010 partial via gate checks.

---

## 2. Execution Layer (EXEC-001 → EXEC-015)

| ID | Requirement | Status | Gap |
|----|-------------|--------|-----|
| EXEC-001 | Limit order state machine | **Partial** | Bar + tick fill in `qtb/ab/fills.py`, `qtb/dual/tick_fills.py` |
| EXEC-002 | Partial fill | **Done** | Participation cap (20% base, 5% conservative) |
| EXEC-003 | Multi-grid jump protection | **Partial** | One fill per level in tick path |
| EXEC-004 | Maker/taker classification | **Partial** | Fee schedule; not full queue model |
| EXEC-005 | Volume cap | **Done** | quote_volume / aggTrade sum |
| EXEC-006 | Queue pessimism | **Partial** | Conservative +2 ticks, +3bps — not full queue sim |
| EXEC-007 | Funding settlement | **Done** | `qtb/costs/model.py` — tested |
| EXEC-008 | Isolated margin | **Done** | A/B + dual engines |
| EXEC-009 | Cross margin | **Missing** | Isolated only |
| EXEC-010 | Liquidation | **Done** | `qtb/risk/exits.py` — tested |
| EXEC-011 | Reserve margin | **Partial** | P1/P2/P3 reserve plans in dual |
| EXEC-012 | Fee | **Done** | `qtb/costs/` — tested |
| EXEC-013 | Rebate | **Done** | Gate rebate in A/B |
| EXEC-014 | Realized/unrealized accounting | **Partial** | In engine; no invariant tests |
| EXEC-015 | Daily equity reconciliation | **Missing** | — |

**Three fill modes:** Optimistic/Base/Conservative **implemented**. Policy enforced in docs; not enforced in code (optimistic still runnable).

---

## 3. Accounting

| Requirement | Status |
|-------------|--------|
| `ACCOUNTING_INVARIANTS` document | **Missing** |
| Per-bar equity conservation check | **Missing** |
| Property tests (0 fee + flat price = no profit) | **Missing** |
| Regression tests for known bugs | **Partial** (ts_ms fix not regression-tested) |

Equity formulas exist in `qtb/ab/engine.py` docstring but are **implicit**, not asserted.

---

## 4. No Future Leak

| Requirement | Status |
|-------------|--------|
| `test_no_future_leak.py` | **Missing** |
| Signal audit (EMA, ATR, swing, regime, beta) | **Docstring claims only** in `qtb/dual/signals.py` |
| Walk-forward parameter isolation | **Not enforced** |

---

## 5. Research Methodology Gaps

| Requirement | Status |
|-------------|--------|
| GRID_VALUE_ADD metric | **Not implemented** as standalone |
| Strategy comparison matrix (Cash, B&H, Grid, Short→Long, etc.) | **Partial** — dual benchmarks B1–B10 exist |
| Parameter plateau detector | **Stub** (`src/analysis/parameter_plateau.py`) |
| Walk-forward (Train/Val/OOS) | **Partial** in `qtb/ab/experiments.py`; not run |
| Monte Carlo block bootstrap | **Stub** (`src/analysis/monte_carlo.py` returns NOT_IMPLEMENTED) |
| Window miner | **Partial** (`qtb/dual/window_search.py`) |
| Similarity engine (DTW, Pearson, etc.) | **Partial** |
| Negative controls / placebo tests | **Missing** |
| Red team automation | **Manual** via review logs only |
| Auto-fix loop (max 3 rounds) | **Policy only** |
| ROBUSTNESS_SCORE | **Missing** |
| Rebate/funding/turnover decomposition | **Partial** in A/B report |

---

## 6. Experiment Infrastructure Gaps

| Requirement | Status |
|-------------|--------|
| `experiments/registry.yaml` | **Created Phase 1** (8 entries) |
| Standard output schema (report.md, summary.json, metrics.csv, config.yaml, data_manifest.json, audit.md) | **Partial** — dual/ab have subset |
| Auto-update RESEARCH_LEDGER | **Manual** |
| `NEXT_EXPERIMENTS.md` | **Created Phase 1** |
| `LIVE_CANDIDATES.md` | **Exists** — correctly shows no deploy-ready params |
| Paper trading engine | **Stub** (`qtb/live/` DRY_RUN only) |

---

## 7. Documentation Gaps (Resolved in Phase 1)

| Deliverable | Status |
|-------------|--------|
| `ROADMAP.md` | **Created** |
| `TASKS.md` + `tasks/` | **Created** |
| `docs/RESEARCH_LEDGER.md` | **Created** |
| `REPO_AUDIT.md` | **Created** |
| `PHASE1_SELF_AUDIT.md` | **Created** |
| `docs/CURRENT_CONCLUSIONS.md` | **Updated** |
| `docs/CURSOR_HANDOFF.md` | **Updated** |

---

## 8. Issues Blocking Credible Backtest

### Critical

1. **ETH/SOL aggTrades manifest rows=0** — corrupt cache or parser bug; crypto long-history research blocked
2. **No DATA_QUALITY_REPORT** — garbage-in-garbage-out risk
3. **Dual report static Q-answers** — conclusions in report body may not reflect actual sweep
4. **Stale backtest processes** — Sep 12 Gate dual + 65d Binance still running (resource waste; results not Phase 1)

### High

5. No accounting invariant tests
6. No future-leak tests
7. Tech history ~65d on Binance — most seed windows STRUCTURAL_SEED_ONLY
8. Gate vs Binance execution gap — no OOS calibration
9. PR #8 not merged — SSOT branch not on main

### Medium

10. `src/` stubs — confusing SSOT
11. Scripts `run_crypto.py`, `run_cross_market.py`, `run_gate_oos.py` are placeholders
12. Cross-margin not modeled
13. Effective beta module not built (`effective_beta.py`)

---

## 9. Phase 2 Entry Criteria

Phase 2 (first real research questions) may begin when **ALL** of:

- [x] TASK-0008 DATA_QUALITY_REPORT implemented + unit test
- [x] TASK-0009 ACCOUNTING_INVARIANTS + property tests green
- [ ] TASK-0010 test_no_future_leak.py green
- [ ] ETH/SOL aggTrades re-downloaded and manifest rows > 0
- [ ] Dual report generator fixed — Q-answers from actual sweep data
- [ ] 65d Binance tick run completed and logged (in progress)
- [ ] PR #8 merged or explicitly waived by maintainer

---

## 10. Recommended Fix Order

See `TASKS.md` and `NEXT_EXPERIMENTS.md` for prioritized task list.
