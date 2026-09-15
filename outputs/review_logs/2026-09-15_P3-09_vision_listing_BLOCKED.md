# Review Log — P3-09/P3-10 Vision listing probe

## Meta

- **date_utc:** 2026-09-15T23:55Z
- **task:** P3-09 (also closes the “just download 2025 ticks” interpretation of P3-10)
- **method:** HTTP Range-GET against `data.binance.vision` UM daily aggTrades / 1h klines
- **do not invent files:** 404 means the day does not exist

## Probe (SOXLUSDT)

| Day | aggTrades | Note |
|-----|-----------|------|
| 2024-09-01 | **404** | FAIL_F2 start |
| 2025-05-01 | **404** | old DATA_POLICY guess |
| 2025-09-01 | **404** | FAIL_F1 start |
| 2025-10-31 | **404** | FAIL_F1 end |
| 2025-12-01 | **404** | |
| 2026-05-01 | **404** | |
| 2026-05-14 | **404** | day before listing |
| **2026-05-15** | **206** | **first Vision day** |
| 2026-06-01 | 206 | |
| 2026-06-22 | 206 (klines too) | TECH_T3 start |
| 2026-07-08 / 09 / 14 | 206 | local gap is cache, not venue |

Binary search 2026-05-01→06-01 landed on **2026-05-15**.

## Implications

- P3-09 FAIL_F1 (2025-09→10) and P3-10 FAIL_F2 (2024-09→11) **cannot** be TICK-tested on Binance UM Vision. Stay **STRUCTURAL_SEED_ONLY**.
- DATA_POLICY “SOXLUSDT ~2025-05+” was wrong; corrected to **2026-05-15+**.
- Unblocked work: pull 2026-05-15→07-14 (P1-12) so TECH_T3 / P3-11 have more than the 07-15 cache.

## Red team

1. Range-GET 206 is not a full-file checksum — first download day will confirm rows.
2. REST fallback might have pre-listing prints; we do not use REST to invent Vision history.
3. Gate perp could still have a different listing; not probed this tick.
4. SNXX earliest not re-probed.
5. `detect_earliest_available()` walks back from *today* and is the wrong tool for 2025 seeds.

## Verdict

- **P3-09 / P3-10:** **BLOCKED** (venue has no files, not a retry)
- **P1-12:** **in_progress** — `scripts/download_soxl_listing_prefix.py`
- **live:** n/a
