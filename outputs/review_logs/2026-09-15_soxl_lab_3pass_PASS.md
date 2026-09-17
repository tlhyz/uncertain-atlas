# Review Log — SOXL personal lab classify + 3-pass audit

## Meta

- **date_utc:** 2026-09-15T23:55Z
- **task:** user request — classify SOXL ticks / params / results, review three times, open a SOXL-only personal private lab
- **folder:** `soxl-lab/` (extractable; this environment cannot create a private GitHub remote)

## Classification

1. **Data** — local TICK 59d 2026-07-15→09-11, 31,190,286 prints, 1,646,097,593 bytes, 0 gaps; 1h 1392/1392; manifests + schema only in git.
2. **Params** — personal 5x / ±20U / ±20% / 200 / 5k+5k locked to `USER_*`; ATR 0.40/±5 kept as research template, labeled not-user.
3. **Results** — P7-01 PASS coverage; P7-03 BAR overturned; P7-04 TICK FAIL pair; P7-05 both modes FAIL (long liquidated).

## Triple review

`python3 soxl-lab/scripts/verify_three_passes.py --times 3` → three consecutive `ok: true` with empty error lists. Independent recount of rows, bytes, sha256 sample, daily CSVs agreed before the script was trusted.

## Private repo

`soxl-lab/EXTRACT_PRIVATE_REPO.md` + `scripts/extract_private_repo.sh`. `gh` is read-only here — you create the empty private remote.

## Verdict

- **task_verdict:** **DONE**
- **data_verdict:** **PASS** (local window)
- **user-grid live:** **NO**
