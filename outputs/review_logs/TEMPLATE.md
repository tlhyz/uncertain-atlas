# Review Log — TEMPLATE

> Copy this file to `outputs/review_logs/YYYY-MM-DD_<experiment_id>_<verdict>.md` and fill every section.

## Meta

- **date_utc:**
- **experiment_id:**
- **git_commit:** `git rev-parse --short HEAD`
- **author:** human | cursor-agent
- **config_paths:**
- **data_manifest:**
- **fill_modes_verdict:** base, conservative (optimistic excluded)

## Data coverage

- **venue / symbols:**
- **start → end:**
- **bars / ticks:**
- **precision:** TICK | BAR | STRUCTURAL_SEED
- **known gaps:**

## Results (primary metrics only)

| Metric | Value |
|--------|------:|
| Total return | |
| Max DD | |
| Sharpe / Calmar | |
| Liquidations | |
| Min liq buffer | |
| Net funding | |

## Verdict

- **verdict:** PASS | FAIL | INCONCLUSIVE | DATA_GAP
- **evidence_class:** PROVEN | STRONG | WEAK | FAILED | UNTESTED
- **one_line_summary:**

## vs prior run

- **prior_log:** path or N/A
- **delta_return:**
- **delta_max_dd:**
- **what_changed:** config | code | data

## Review notes

- What worked:
- What failed:
- Surprises vs thesis:

## Optimization — next actions

1.
2.
3.

## Do NOT retry (dead ends)

-

## Doc updates required?

- [ ] `docs/CURRENT_CONCLUSIONS.md`
- [ ] `docs/RESEARCH_HISTORY.md`
- [ ] `outputs/LIVE_CANDIDATES.md`
