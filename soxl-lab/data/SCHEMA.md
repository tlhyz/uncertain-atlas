# SOXL tick schema (Binance UM aggTrades, local cache)

Venue file: `cache/binance_futures_SOXLUSDT_aggTrades_YYYY-MM-DD.csv`

| Column | Type | Meaning |
|--------|------|---------|
| `ts_ms` | int | Event time, milliseconds |
| `price` | float | Print price (USDT) |
| `qty` | float | Base quantity |
| `quote_qty` | float | Quote notional |
| `is_buyer_maker` | bool | Maker-is-buyer flag |
| `agg_id` | int | Aggregate trade id |

Independently measured on this VM (2026-09-15):

- Days: **59** contiguous `2026-07-15` → `2026-09-11` (0 gaps)
- Rows: **31,190,286**
- Bytes: **1,646,097,593**
- Price: **min 85.94 / max 191.10**; daily-median range 101.96–165.41
- 1h bars on overlap window: **1392** (`2026-07-16 00:00Z` → `2026-09-11 23:00Z`)
- Tick vs 1h coverage: **1392/1392**, missing trades **0**

Do not commit the CSVs. Rebuild from Binance Vision via the parent download script.
