# Review Log — P3-11 listing-length retry

## Meta

- **date_utc:** 2026-09-16T00:47Z
- **experiment_id:** P3-11
- **git_commit:** (this commit)
- **author:** cursor-agent
- **config_paths:** `configs/experiments/dual_binance_tick_similar_windows.yaml`
- **data_manifest:** Vision 1h klines SOXLUSDT 2026-05-15→09-11 (2866 bars); ticks not required
- **fill_modes_verdict:** n/a (shape search only)

## Data coverage

- **venue / symbols:** Binance UM SOXLUSDT only (not SNXX-aligned)
- **start → end:** 2026-05-15 → 2026-09-11
- **bars:** 2866 @ 1h (`binance_vision_klines_range`)
- **precision:** STRUCTURAL_SEED (no execution claim)
- **seed:** TECH_T3 (2026-06-22→08-31) — now inside listing

## Results

| Metric | Value |
|--------|------:|
| Slides @ 1440h / step 168h | **9** |
| Hits returned | 9 |
| Bars needed for top-20 | 4632 (~193d) |
| Top-20 possible | **false** |
| Best composite | 0.4928 (2026-06-19→08-18) |

Prior 65d scan: 0–1 window. Listing prefix unblocked the template and grew slides 1→9. Still far from 20 independent 60d windows. Vision listing is 120d; cannot extend further.

## Verdict

- **verdict:** BLOCKED
- **evidence_class:** STRONG (arithmetic, not a download miss)
- **one_line_summary:** 120d listing yields 9 slides; top-20 @ 60d horizon needs ~193d that do not exist.

## vs prior run

- **prior_log:** `outputs/review_logs/2026-09-14_P3-11_similar_windows_BLOCKED.md`
- **what_changed:** SOXL-only 05-15 start; TECH_T3 seed; runner knobs in `run.py`

## Review notes

- Dual-dataset align to SNXX would shrink back to ~July — this scan correctly used SOXL-only bars.
- Best composite 0.49 is a sliding self-overlap with TECH_T3, not an OOS twin.
- Wired `similar_search_seed` / horizon / step in `qtb/dual/run.py`.

## Optimization — next actions

1. Do **not** retry top-20 at 60d horizon.
2. If needed later: shrink horizon (changes the question) or drop the top-20 requirement.

## Do NOT retry

- P3-11 top-20 with 1440-bar horizon on SOXL Vision history
- TECH_T2 / 2025 seeds (STRUCTURAL_SEED_ONLY, no SOXL)

## Doc updates required?

- [x] `docs/RESEARCH_BACKLOG.md` P3-11 blocked
- [ ] `docs/CURRENT_CONCLUSIONS.md` (no live-candidate change)
