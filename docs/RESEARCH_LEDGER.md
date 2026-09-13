# Research Ledger — gate-grid-martingale

> **Single source of truth for all experimental evidence.**  
> Classification: `CONFIRMED` | `STRONG EVIDENCE` | `WEAK EVIDENCE` | `FAILED` | `UNTESTED` | `INVALIDATED`  
> Last updated: 2026-09-13 (Phase 1 audit)

**Rules:**
- Every entry cites artifacts (path + git commit where available).
- FAIL entries are permanent unless **INVALIDATED** with full evidence chain.
- Do not re-litigate settled FAILs without new data or methodology fix.

---

## Ledger Index

| ID | Hypothesis | Status | PR / Commit |
|----|------------|--------|-------------|
| [LEDGER-001](#ledger-001-3l-etf-spot-grid) | Long-run 3L ETF grid covers inventory loss | **FAILED** | #4 |
| [LEDGER-002](#ledger-002-majors-perp-15-2x-vs-etf) | Majors prefer 1.5–2x PERP grid over 3L ETF | **STRONG EVIDENCE** | #6 |
| [LEDGER-003](#ledger-003-tech-shortlong-fsm) | Tech Short→Grid→Trend beats Cash→Long | **FAILED** | #7, #8 |
| [LEDGER-004](#ledger-004-crypto-independent-book) | Independent Crypto book improves portfolio | **WEAK EVIDENCE** | partial |
| [LEDGER-005](#ledger-005-rebate-as-alpha) | Gate rebate is primary alpha | **FAILED** | #6 |
| [LEDGER-006](#ledger-006-3x-perp-unattended) | 3x PERP safe for unattended | **FAILED** | #6 |
| [LEDGER-007](#ledger-007-regime-switching-alpha) | Regime switching > pure grid | **UNTESTED** | — |
| [LEDGER-008](#ledger-008-grid-value-add) | Grid adds total equity vs same exposure | **UNTESTED** | — |
| [LEDGER-009](#ledger-009-040-atr-plateau) | 0.40 ATR is robust parameter plateau | **WEAK EVIDENCE** | prior sweeps |
| [LEDGER-010](#ledger-010-cross-market-decoupling) | Tech/Crypto independent books reduce DD | **UNTESTED** | — |

---

## LEDGER-001: 3L ETF Spot Grid

**Status:** **FAILED** (CONFIRMED on real Gate ETF data)

**Hypothesis:** High-volatility 3L ETF is suitable for long-run unattended grid trading because frequent crossings generate stable realized profit.

**Result:** Grid realized profit **does not cover** inventory accumulation + directional loss → **negative total equity**.

**Key evidence:**
- 90%+ max drawdown on BTC/ETH/SOL 3L paths in sustained down moves
- "No traditional liquidation" ≠ low risk
- Artifacts: `outputs/research_sl_phase/`, `outputs/demo_niulai_aggressive_sl50/`, root `opt_niulai_*_report.md`

**Contradicting:** None on real data.

**Do not retry without:** New execution model + explicit GRID_VALUE_ADD test + OOS.

---

## LEDGER-002: Majors PERP 1.5–2x vs ETF

**Status:** **STRONG EVIDENCE**

**Hypothesis:** For BTC, ETH, SOL, SOXL, SNXX, AAOI — underlying perpetual grid at 1.5–2x leverage outperforms 3L ETF grid on total equity (Base + Conservative fills).

**Result:** PERP wins 6/8 assets on Gate real overlap. Meme (PENGU, PUMP) ETF won in sample — **WEAK** due to short history + liquidation on 3x PERP.

**Key evidence:**
- `outputs/ab_etf_vs_perp/AB_REPORT.md`
- Commit `84a16918`, PR #6
- Fill modes: Base + Conservative only

**Caveats:**
- BAR BACKTEST (not tick-precise)
- Gate funding history ~180d cap
- SOXL/SNXX sample may be short on Gate

**Contradicting:** PENGU/PUMP ETF win (WEAK — meme, liq on 3x PERP)

---

## LEDGER-003: Tech Short→Long FSM

**Status:** **FAILED** (STRONG EVIDENCE — replicated on two venues + tick path)

**Hypothesis:** Tech book should start with tactical Short, reduce on drawdown tiers, bottom grid, reversal confirm, then Grid→Trend long — beating simple Cash→Long.

**Results:**

| Run | Window | Dual Return | Buy&Hold | Precision | Verdict |
|-----|--------|-------------|----------|-----------|---------|
| Gate overlap | 2026-07-14 → 09-12 (1458 bars) | **-51.05%** | -30.07% | BAR | FAIL |
| Binance tick 7d | 2026-09-05 → 09-11 (168 bars) | **-77.82%** | +1.03% | TICK | FAIL |

**Key evidence:**
- `outputs/dual_engine_perp/DUAL_REPORT.md` (PR #7)
- `outputs/dual_engine_perp_binance_ticks/DUAL_REPORT.md` (PR #8)
- Review log: `outputs/review_logs/2026-09-13_P1_tick_validation_PASS_7d_smoke_FAIL.md`

**Additional FAIL sub-claims:**
- Bottom grid alone (-26% Gate / -25% Binance 7d) beats dual Short→Long
- B4 directional long only (-17% Gate / -25% Binance 7d) beats dual
- Initial Short is tactical hedge only — **not validated as net-positive**

**Pending:** 65d Binance tick run (EXP-005) — may refine magnitude, unlikely to overturn FAIL direction.

**Contradicting:** None to date.

---

## LEDGER-004: Crypto Independent Book

**Status:** **WEAK EVIDENCE**

**Hypothesis:** Crypto book with independent regime FSM improves total return and/or reduces DD vs unified Tech-driven signal.

**Result:** On Gate overlap, independent books Δreturn +2.3% vs unified, ΔDD -2.06%. On Binance 7d tick window: **no benefit** (Δreturn 0).

**Key evidence:** `outputs/dual_engine_perp/DUAL_REPORT.md` Q11/Q14

**Blocker for upgrade:** Full Binance multi-year tick run + cross-regime classification (EXP-CRYPTO-006, EXP-CROSS-001).

---

## LEDGER-005: Rebate as Alpha

**Status:** **FAILED**

**Hypothesis:** Gate 70% maker rebate provides standalone edge.

**Result:** Rebate does not rescue wrong direction + inventory drag. Q8: zero-rebate does not flip winner on majors.

**Key evidence:** `outputs/ab_etf_vs_perp/AB_REPORT.md` Q7–Q8

---

## LEDGER-006: 3x PERP Unattended

**Status:** **FAILED**

**Hypothesis:** 3x isolated PERP grid is safe for long-run unattended operation.

**Result:** Liquidations on SOL, PENGU, PUMP. Q13: do not unattended-run 3x where liquidated.

**Key evidence:** `outputs/ab_etf_vs_perp/AB_REPORT.md` Q13

**Allowed use:** Stress test only.

---

## LEDGER-007: Regime Switching Alpha

**Status:** **UNTESTED**

**Hypothesis:** Alpha source is regime detection + state machine (grid/directional rotation), not pure static grid.

**Rationale:** Pure grid FAILs (LEDGER-001, LEDGER-003 sub-claims). FSM structure exists in code (`qtb/dual/tech_fsm.py`, `crypto_fsm.py`) but not validated at full rigor.

**Required before upgrade:** Walk-forward, OOS, Monte Carlo, negative controls.

---

## LEDGER-008: Grid Value Add

**Status:** **UNTESTED**

**Definition:** `GRID_VALUE_ADD = Total Equity(with Grid) - Total Equity(same exposure without Grid)`

**Required test:** Isolated grid study per asset (BTC, ETH, SOL, SOXL, SNXX) — geometric/arithmetic, ATR spacing sweep — **without** direction FSM mixed in.

**Blocker:** DATA_QUALITY_REPORT gate + formal comparison matrix (EXP-GRID-001).

---

## LEDGER-009: 0.40 ATR Plateau

**Status:** **WEAK EVIDENCE**

**Hypothesis:** 0.40 ATR grid step sits on a parameter plateau (0.35, 0.45, 0.50 also reasonable).

**Current basis:** Narrative in dual reports + prior demo sweeps — **not independently verified** on Binance ticks with plateau detector.

**Red-team flag:** Dual report Q9 text is template — do not treat as measured until sweep re-run logged.

**Required:** `src/analysis/parameter_plateau.py` full implementation + EXP-CRYPTO-004.

---

## LEDGER-010: Cross-Market Decoupling

**Status:** **UNTESTED**

**Hypothesis:** Tech down / Crypto up periods exist and independent books capture them, improving portfolio survivability.

**Seed template:** CRYPTO_C1 2024-09→11 — **STRUCTURAL_SEED_ONLY** (no execution backtest yet).

**Required:** EXP-CROSS-002 with real Binance data on both books.

---

## INVALIDATED Entries

*(None yet. When overturning, record here with reason.)*

| ID | Was | Now | Reason | Date |
|----|-----|-----|--------|------|
| — | — | — | — | — |

---

## Evidence Class Definitions

| Class | Meaning |
|-------|---------|
| **CONFIRMED** | Survives Base+Conservative, OOS or multi-venue replication, red-team pass |
| **STRONG EVIDENCE** | Consistent on real data; minor caveats documented |
| **WEAK EVIDENCE** | Directionally suggestive; single window or template text |
| **FAILED** | Hypothesis rejected on real data |
| **UNTESTED** | Designed but not executed with full pipeline |
| **INVALIDATED** | Prior conclusion overturned with documented evidence chain |

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2026-09-13 | Initial ledger from Phase 1 audit; migrated from `RESEARCH_HISTORY.md` | phase1-audit |
| 2026-09-13 | Added Binance 7d tick FAIL (LEDGER-003 reinforcement) | phase1-audit |

**Supersedes:** `docs/RESEARCH_HISTORY.md` (kept as redirect/reference, not primary SSOT)
