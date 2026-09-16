# Review Log — P1-14 SOXL listing-length tick manifest

## Meta

- **date_utc:** 2026-09-16T01:24Z
- **experiment_id:** P1-14
- **author:** cursor-agent
- **data_manifest:** `data/manifests/binance_SOXLUSDT_aggTrades_2026-05-15_2026-09-11.json`

## Data coverage

| | |
|--|--|
| Window | 2026-05-15 → 2026-09-11 |
| Days | **120 / 0 gaps** |
| Rows | **62,409,315** |
| Bytes | 3,265,883,206 |
| Git | manifest + sha256 only; CSVs stay in `cache/` |

Audited P7 window manifest `2026-07-15_2026-09-11` (59d / 31,190,286) **unchanged**.

## Verdict

- **verdict:** PASS
- **one_line_summary:** Listing-length SOXL ticks now have a checksummed manifest; raw CSVs still not in git.

## Do NOT retry

- P3-11 top-20 @ 60d horizon
