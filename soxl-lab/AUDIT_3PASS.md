# Triple review — SOXL lab

Script: `python3 scripts/verify_three_passes.py --times 3`

Each run re-reads disk (manifest, cache sample sha256, yaml, engine constants, result JSON, daily CSVs, P7-04 review log). No cached verdicts.

| Run | Pass 1 data | Pass 2 params | Pass 3 results | OK |
|-----|-------------|---------------|----------------|----|
| 1 | 59 files / 0 gaps / 1,646,097,593 bytes / first-mid-last sha256 / 1392/1392 | yaml `USER_*` / runner usdt+pct / windows.yaml rows | P7-04 exact floats + P7-05 ±20U and ±20% CSV | yes |
| 2 | same, fresh process | same | same | yes |
| 3 | same, fresh process | same | same | yes |

Machine logs: `results/audit/run_1.json`, `run_2.json`, `run_3.json`, `three_passes.json`.

## Independent recount (outside the script)

Recounted before trusting the script:

- `wc`-equivalent row sum across 59 CSVs = **31,190,286** (matches manifest `rows`)
- Price min/max over all prints = **85.94 / 191.10**
- 1h kline file = **1392** bars, 2026-07-16 00:00Z → 2026-09-11 23:00Z
- P7-05 daily CSVs: 58 UTC days each; last equity / cum_ret / win-days match `summary.json`
- Combined start capital implied by last equity / (1+cum_ret) = **10,000** both modes

## Caveats that are true, not errors

- Historical manifest `2026-07-09_2026-09-11` lists six days that are **not** on this VM.
- P7-04 same-symbol short leg is BAR; only the long grid is TICK. Documented, not hidden.
- P7-05 moving-grid reanchor clears the lot map without flattening qty (TP grid forgets open lots). Numbers are path-exact given that rule.
- This environment cannot create the private GitHub remote.
