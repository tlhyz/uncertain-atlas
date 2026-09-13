# Research North Star (总目标)

> **Mission:** Build a **ROBUST · REPRODUCIBLE · SURVIVABLE** dual-book regime-switching system — not the highest backtest return on one window.

## One sentence

Validate whether **Tech (SOXL/SNXX)** and **Crypto (BTC/ETH/SOL)** can run as **independent books** with **limit/maker-first** execution, using **real ticks where they exist**, and produce **honest live candidates** — or prove ideas **FAILED** and stop spending compute on them.

## Success looks like

| Criterion | Measure |
|-----------|---------|
| Survives | Max DD within configured hard limits; min liq buffer reported |
| Reproduces | Clone → download → manifest → same verdict on same config |
| Auditable | Every run has `outputs/review_logs/` entry + git commit |
| OOS | Train/val/OOS or walk-forward on BTC/ETH/SOL; Gate calibration on finalists |
| Honest | FAIL stays FAIL; no synthetic ticks; no grid-gross-only claims |

## Explicit non-goals

- Maximize one cherry-picked window
- Revive 3L ETF grid or 3x unattended PERP as default
- Merge Tech signal into Crypto book
- Touch `uncertain-atlas/` blockchain content

---

## Phase map (macro milestones)

| Phase | Goal | Exit criteria |
|-------|------|---------------|
| **P0** | Repo is SSOT | Docs + configs + tests green; PR merged |
| **P1** | Data pipeline | Binance manifests + tick validation for SOXL/SNXX/BTC/ETH/SOL |
| **P2** | Crypto structure | Q-crypto 1–7 answered on multi-year Binance ticks |
| **P3** | Tech FSM | Q-tech 1–10 answered on Binance ticks + Gate OOS |
| **P4** | Portfolio | 10k combined book; cross-market regimes A–F |
| **P5** | Robustness | MC 1000 paths + parameter plateau on finalists |
| **P6** | Live candidates | `LIVE_CANDIDATES.md` with MEDIUM+ confidence rows only |

**Current phase:** **P0 → P1** (framework delivered; data + tick re-run next)

---

## Book-level sub-missions

### Book A — Tech

Prove or falsify: *「先回调 → 筑底 → 暴涨」* can be traded without **Short destroying the account** when timing is wrong.

- If Short→Long **FAIL** vs Cash→Long → **remove Short from baseline**
- If Grid→Trend **wins** → document mix schedule with plateau evidence

### Book B — Crypto

Prove or falsify: *「Crypto 独立行情」* reduces Tech-book drawdown **without** hiding Tech losses behind Crypto leverage.

- Independent FSM must beat unified-signal control on **total portfolio** metrics

---

## Agent self-contract

Every session I will:

1. Read `docs/RESEARCH_BACKLOG.md` — pick **one** `pending` task minimum
2. Finish the task or mark `blocked` with explicit reason
3. Write review log + update backlog status
4. Commit + push if on a working branch
5. **Not end idle** while my phase has unblocked `pending` tasks and user has not said stop

See `docs/WORK_CADENCE.md` for timers and session rules.
