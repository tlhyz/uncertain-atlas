# Cursor / AI Handoff

> **Model-agnostic** — any AI (Cursor, Grok, future) can continue from here.

---

## READ FIRST (in order)

1. `README.md` — 5-minute orientation
2. `docs/RESEARCH_LEDGER.md` — **SSOT for what failed vs proven** (supersedes RESEARCH_HISTORY)
3. `docs/CURRENT_CONCLUSIONS.md` — current best evidence with confidence
4. `ROADMAP.md` — LEVEL 0–12 progression
5. `TASKS.md` — what to do next
6. `GAP_ANALYSIS.md` — what's missing
7. `PHASE1_SELF_AUDIT.md` — red team findings
8. `NEXT_EXPERIMENTS.md` — information-gain priority
9. `docs/DATA_POLICY.md` — no synthetic ticks
10. `.cursor/rules/quant-research-permanent.mdc` — **永久规则 & 北星目标（alwaysApply）**

---

## DO NOT REPEAT

| Dead end | Evidence |
|----------|----------|
| Long-run 3L ETF grid as core strategy | LEDGER-001 FAILED |
| 3x PERP unattended default | LEDGER-006 FAILED |
| Rebate as primary alpha | LEDGER-005 FAILED |
| Tech signal driving Crypto book | Design rejected |
| Initial Short→Long without beating Cash→Long | LEDGER-003 FAILED (Gate + Binance 7d) |
| Mass parameter sweeps before infra gates | GAP_ANALYSIS §9 |
| Synthetic ticks | DATA_POLICY |
| Touch `uncertain-atlas/` | Separate branch |

---

## CURRENT TASK

**Phase 1.5 — Infrastructure blockers** (LEVEL 0 conditional pass complete)

Execute in order:
1. TASK-0008 — DATA_QUALITY_REPORT gate
2. TASK-0009 — ACCOUNTING_INVARIANTS
3. TASK-0010 — test_no_future_leak.py
4. TASK-0011 — Fix ETH/SOL aggTrades + manifest
5. TASK-0012 — Fix dual report static Q-answers

**Do NOT start EXP-TECH-001 until GAP_ANALYSIS §9 criteria met.**

---

## CURRENT BLOCKERS

| Blocker | Owner | Task |
|---------|-------|------|
| No DATA_QUALITY gate | agent | TASK-0008 |
| No accounting invariant tests | agent | TASK-0009 |
| No future-leak tests | agent | TASK-0010 |
| ETH/SOL aggTrades rows=0 | agent | TASK-0011 |
| Dual report template Q-answers | agent | TASK-0012 |
| PR #8 not merged | **human** | TASK-0014 |
| 65d tick backtest in progress | prior session | TASK-0013 |

---

## MOST IMPORTANT FILES

```
docs/RESEARCH_LEDGER.md      ← evidence SSOT
docs/CURRENT_CONCLUSIONS.md  ← honest current state
ROADMAP.md                   ← level progression
TASKS.md                     ← work queue
GAP_ANALYSIS.md              ← infra gaps
experiments/registry.yaml    ← experiment index
qtb/dual/portfolio.py        ← dual engine runtime
qtb/ab/fills.py              ← Base/Conservative fills
qtb/data/binance_futures.py   ← aggTrades downloader
configs/portfolio.yaml       ← 6500/2500/1000 capital
outputs/review_logs/         ← session audit trail
```

**Runtime code is in `qtb/`**, not `src/` (migration incomplete).

---

## NEXT ACTIONS

1. Pick lowest open task from `TASKS.md` TOP 10
2. Run `pytest -q` at session start
3. After any experiment: review log → ledger → registry → commit
4. Red team before advancing ROADMAP level
5. Respond to `research-continue` timer (**every 10 min**) — see `docs/WORK_CADENCE.md`
6. Obey `.cursor/rules/quant-research-permanent.mdc` (alwaysApply)

---

## Running Code Today

```bash
pip install -e ".[dev]"
pytest -q
python scripts/download_binance.py --detect-start --symbols SOXL SNXX BTC
python scripts/build_manifest.py
python -m qtb.cli ab -c configs/ab_etf_vs_perp.yaml
python -m qtb.cli dual -c configs/dual_engine_perp.yaml
```

---

## Agent Rules Summary

1. FAIL stays FAIL — evidence chain to overturn
2. Conclusions: Base + Conservative only
3. Crypto independent from Tech
4. Review → Red Team → Fix (max 3) → Re-run → Ledger
5. "NO EDGE FOUND" is valid
6. Complexity must earn its keep vs Cash→Long
