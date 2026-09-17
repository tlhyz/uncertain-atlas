# Review, Optimize & Log Policy

Every researcher (human or AI) working in this repo must **continuously review**, **iteratively optimize**, and **persist logs** so later runs can learn from prior evidence — without rewriting history.

---

## Core rule

> **Review → Record → Optimize → Re-run → Review again**

No experiment is "done" when the script exits. It is done when:

1. Results were **reviewed** against thesis, benchmarks, and prior logs
2. A **review log entry** was written (even if verdict is FAIL)
3. **Next optimization actions** are explicit (what to change, what NOT to change)
4. Artifacts are saved under `outputs/` with reproducible config + data manifest

---

## When to write a review log

| Trigger | Required log? |
|---------|----------------|
| Any backtest / sweep / experiment run | **Yes** |
| Data download or manifest change | **Yes** |
| Config or strategy logic change | **Yes** before merge |
| Bug fix in fill engine / accounting | **Yes** + rerun affected experiment |
| Doc-only change | Optional short note if conclusion shifts |

---

## Log location & naming

```
outputs/review_logs/
  YYYY-MM-DD_<experiment_id>_<short-verdict>.md
  YYYY-MM-DD_<experiment_id>_summary.json   # optional machine-readable
```

Examples:

- `outputs/review_logs/2026-09-13_dual_engine_perp_FAIL.md`
- `outputs/review_logs/2026-09-13_binance_soxl_tick_validation_PASS.json`

**Do not delete FAIL logs.** Rename or supersede with newer dated entries only.

Also acceptable: append a section to the experiment's own `outputs/<experiment>/report.md` **and** mirror a one-line index entry in `outputs/review_logs/INDEX.md`.

---

## Required fields (every review log)

Copy [`outputs/review_logs/TEMPLATE.md`](../outputs/review_logs/TEMPLATE.md) or include:

| Field | Description |
|-------|-------------|
| `date_utc` | ISO timestamp |
| `experiment_id` | e.g. `dual_engine_perp`, `ab_etf_vs_perp` |
| `git_commit` | `git rev-parse --short HEAD` |
| `config_paths` | All YAML/TOML used |
| `data_manifest` | Path or "inline" provenance summary |
| `fill_modes` | Which modes matter (Base/Conservative for verdict) |
| `metrics` | total return, max DD, liq count, key Q answers |
| `verdict` | PASS / FAIL / INCONCLUSIVE / DATA_GAP |
| `evidence_class` | PROVEN / STRONG / WEAK / FAILED / UNTESTED |
| `vs_prior` | Delta vs last logged run for same experiment |
| `optimization_next` | Concrete next params/code/data actions |
| `do_not_retry` | Dead ends (avoid repeating disproven paths) |

---

## Review checklist (before claiming improvement)

1. **Data:** coverage, missing periods, TICK vs BAR label correct?
2. **Execution:** Base + Conservative agree directionally?
3. **Economics:** total equity, not grid gross alone?
4. **Risk:** funding, liquidation buffer, leverage caps?
5. **OOS:** same window not used for tune + validate?
6. **Thesis:** does result support or falsify Book A / Book B claim?
7. **History:** update `docs/CURRENT_CONCLUSIONS.md` if evidence class changes
8. **Live:** update `outputs/LIVE_CANDIDATES.md` only with honest confidence

---

## Optimization rules

- Optimize from **logged evidence**, not intuition.
- One major knob per iteration when diagnosing (grid step OR leverage OR short % — not all at once).
- If only one parameter works → mark **OVERFIT** (`src/analysis/parameter_plateau.py`).
- If FAIL persists across ≥2 disciplined iterations → update `docs/RESEARCH_HISTORY.md`, stop burning compute.
- Never optimize away a FAIL by switching to Optimistic fills or synthetic ticks.

---

## AI / Cursor agents (mandatory)

At end of any session that runs code or changes strategy:

1. Append or create a file under `outputs/review_logs/`
2. Update `outputs/review_logs/INDEX.md` one-line summary
3. If conclusions changed → patch `docs/CURRENT_CONCLUSIONS.md`
4. Commit logs with code/config changes (same PR or follow-up commit)
5. State in PR/commit body: **what was reviewed, what was optimized, what log was added**

See also: [`docs/CURSOR_HANDOFF.md`](CURSOR_HANDOFF.md)

---

## Human researchers

Same rules. PRs that change backtest behavior without a review log entry should be rejected in review.

---

## Related paths

| Path | Role |
|------|------|
| `outputs/review_logs/` | Dated review + optimization trail |
| `docs/RESEARCH_HISTORY.md` | Long-lived verdict archive |
| `docs/CURRENT_CONCLUSIONS.md` | Latest evidence snapshot |
| `data/manifests/` | Data reproducibility audit |
