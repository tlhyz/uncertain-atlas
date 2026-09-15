# SOXL data inventory (this VM)

Classified. Tick CSVs stay on disk. Only manifests and coverage live in git.

| Class | What | Location | Git? | Independent recount 2026-09-15 |
|-------|------|----------|------|--------------------------------|
| TICK raw | 59 daily aggTrades CSV | `../../cache/binance_futures_SOXLUSDT_aggTrades_YYYY-MM-DD.csv` | **no** | 59 files, 0 gaps, 31,190,286 rows, 1,646,097,593 bytes |
| TICK schema | columns + price span | `SCHEMA.md` | yes | min 85.94 / max 191.10 |
| TICK manifest (local) | sha256 + bytes | `manifests/binance_SOXLUSDT_aggTrades_2026-07-15_2026-09-11.json` | yes | 59 records; first/mid/last sha256 match |
| TICK manifest (historical) | 2026-07-09 listing | `manifests/binance_SOXLUSDT_aggTrades_2026-07-09_2026-09-11.json` | yes | 07-09→07-14 **absent** on this VM |
| BAR 1h | Vision klines | `../../cache/binance_futures_SOXLUSDT_1h_2026-07-16_2026-09-11_klines.csv` | no | 1392 bars |
| Coverage | TICK vs 1h | `../results/p7_tick_coverage.soxl.json` | yes | 1392/1392, miss 0 |

**Do not commit tick CSVs.** Rebuild with `../../scripts/download_soxl_overlap_ticks.py`.
