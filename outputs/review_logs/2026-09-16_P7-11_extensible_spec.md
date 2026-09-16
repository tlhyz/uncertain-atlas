# Review Log — P7-11 extensible grid spec

## Meta

- **date_utc:** 2026-09-16T00:55Z
- **experiment_id:** P7-11
- **author:** cursor-agent
- **config_paths:** `soxl-lab/params/run.yaml`

## Verdict

- **verdict:** PASS
- **one_line_summary:** Defaults unchanged; YAML/CLI now expose grid_kind, fee_bps, reanchor, mmr; hedge registry; unknown keys warned.

## What changed

- Engine: geometric levels, fee_bps, apply_reanchor, IsolatedDirBook.mmr_frac
- CLI: extras + `--check` unknown keys; `register_hedge`
- Docs: 使用注意事项 §8
- 29 unit tests; default folder names unchanged when knobs stay default

## Do NOT retry

- Do not treat this as a new strategy verdict
