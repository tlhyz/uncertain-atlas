# Cursor / AI Handoff

## Read first (in order)

1. `README.md`
2. `docs/THESIS.md` — market view & two books
3. `docs/RESEARCH_HISTORY.md` — what failed vs untested
4. `docs/DATA_POLICY.md` — no synthetic ticks
5. `docs/CURRENT_CONCLUSIONS.md`
6. `docs/REVIEW_AND_OPTIMIZATION.md` — **review / optimize / log rules (mandatory)**
7. `docs/RESEARCH_GOALS.md` — **总目标 (north star)**
8. `docs/RESEARCH_BACKLOG.md` — **小目标队列 (pick pending each session)**
9. `docs/WORK_CADENCE.md` — **定时提醒 & 会话规则**
10. `REPO_REFACTOR_REPORT.md`

## Out of scope — DO NOT MODIFY

### `uncertain-atlas/` (blockchain / consensus research)

This quantitative trading refactor **does not touch** the Uncertain blockchain knowledge base.

- Lives on branch: `cursor/uncertain-architecture-atlas-11a5`
- **Not present** on `cursor/unified-tech-crypto-framework-cbaf`
- **Never** merge, move, rewrite, or delete `uncertain-atlas/` as part of grid/perp work
- If both tracks need coexistence in `main`, use **separate top-level dirs** with zero cross-imports

## In scope

| Path | Purpose |
|------|---------|
| `src/` | Target package (wraps `qtb/` during migration) |
| `qtb/` | Legacy engine — still runs all tests |
| `configs/` | All capital, fees, risk, experiments |
| `scripts/` | Download + run entry points |
| `outputs/` | Tracked research artifacts |
| `docs/` | Single source of truth for humans & AI |

## Running code today

```bash
pip install -e ".[dev]"
pytest -q
python scripts/download_binance.py --detect-start --symbols SOXL SNXX BTC
python -m qtb.cli ab -c configs/ab_etf_vs_perp.yaml
python -m qtb.cli dual -c configs/dual_engine_perp.yaml
```

## Rules for next agent

1. **FAIL stays FAIL** in docs and reports
2. **No synthetic ticks** — see DATA_POLICY
3. **Crypto independent** from Tech signals
4. **Primary metrics:** total equity, max DD, liq buffer — not grid gross
5. **Conclusions:** Base + Conservative fills only
6. **Do not** start full parameter sweeps until user confirms after refactor report
7. **Review → Optimize → Log (mandatory):** after every experiment or backtest-related change, write `outputs/review_logs/YYYY-MM-DD_<id>_<verdict>.md`, update `INDEX.md`, commit with code — see `docs/REVIEW_AND_OPTIMIZATION.md`
8. **Continuous review:** compare each run to prior logs; state `vs_prior` delta and `optimization_next`; never delete FAIL logs
9. **Never stop idle:** each session complete ≥1 backlog task (`docs/RESEARCH_BACKLOG.md`); session end checklist in `docs/WORK_CADENCE.md`
10. **Respond to timer `research-continue`:** pick next pending task, execute, log, commit — see `docs/WORK_CADENCE.md`

## Next experiments (after user OK)

1. Binance SOXL/SNXX full aggTrades manifest + tick validation every bar
2. Re-run Tech FSM Q1–Q10 on Binance ticks
3. BTC/ETH/SOL 2019+ grid leverage scan
4. Gate OOS calibration pass
5. Update `outputs/LIVE_CANDIDATES.md`
