# Work Cadence — 定时提醒 & 会话规则

How agents and humans **keep working** without losing thread, burning compute blindly, or stopping mid-pipeline.

---

## Session start (every time)

```bash
pytest -q                                    # M-01
python scripts/check_backlog.py --next 3     # pick tasks
cat docs/RESEARCH_GOALS.md | head -40        # re-read north star
```

**Pick ≥1 backlog task.** Mark it `in_progress` in `docs/RESEARCH_BACKLOG.md` before coding.

---

## Session end (every time — do not skip)

1. Mark task `done` | `blocked` | `failed` with log path
2. Write `outputs/review_logs/YYYY-MM-DD_<id>_<verdict>.md`
3. Update `outputs/review_logs/INDEX.md`
4. Run M-05: add newly discovered sub-tasks to backlog
5. `git commit` + `git push` if on working branch
6. Update PR if open

**Stop condition:** all current-phase tasks `done`/`blocked`/`failed` AND review log written — not "I got tired."

---

## Timed reminders (Cloud Agent)

Recurring timer **`research-continue`** should fire and enqueue:

> Read `docs/RESEARCH_BACKLOG.md`. Execute the lowest-ID `pending` task in current phase (P0–P6). Write review log. Update backlog. Commit if changed. Do not idle while unblocked pending tasks remain.

| Timer | Schedule | Purpose |
|-------|----------|---------|
| `research-continue` | every **4 hours** | pick next backlog task |
| `research-daily-audit` | **09:00 UTC** daily | backlog hygiene + CURRENT_CONCLUSIONS check |
| `pr-ci-watch` | on push | subscribe_github_ci for working branch |

To list active timers: MCP `cursor-subscriptions` → `list_subscriptions`.

---

## Phase focus (what to work on now)

```
IF P0 has pending → only P0
ELIF P1 has pending → only P1 (data before sweeps)
ELIF user confirmed full sweeps → P2/P3 in parallel OK
ELSE → P4 → P5 → P6 in order
```

Never start P5 Monte Carlo before P1 data manifests exist.

---

## Anti-stall rules

| Situation | Action |
|-----------|--------|
| Download running | log progress; do not start duplicate download |
| Test failing | fix or mark task `blocked` with issue — do not skip |
| FAIL result | log it, update RESEARCH_HISTORY — **continue** to next task |
| Same FAIL twice | mark `failed`, move to `X-` section — stop retrying |
| User says stop | pause timers via `unsubscribe` |

---

## Progress tracking files

| File | Updates |
|------|---------|
| `docs/RESEARCH_BACKLOG.md` | every task state change |
| `docs/RESEARCH_GOALS.md` | phase transitions only |
| `docs/CURRENT_CONCLUSIONS.md` | evidence class changes |
| `outputs/review_logs/` | every experiment |

---

## Human-readable heartbeat

Optional: append one line to `outputs/review_logs/HEARTBEAT.md`:

```
2026-09-13T00:10Z | P1-02 in_progress | downloading SOXLUSDT day 2026-07-15
```

Lets any researcher see the agent is alive without reading full logs.
