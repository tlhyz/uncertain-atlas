# Accounting Invariants — gate-grid-martingale

> Every backtest bar must conserve equity. Violations → experiment **FAIL**.

## Spot (ETF / cash market)

```
Total Equity = Cash + Position Qty × Mark Price
```

- `Cash` decreases on buy (cost + fee); increases on sell (proceeds − fee)
- Realized PnL flows into cash on sells
- No external top-ups after `initial`

**Implementation:** `qtb/ab/engine.py` → `_spot_equity()`, `run_spot_grid()`

## Perpetual (cross margin default in dual engine)

```
Total Equity = Wallet + Locked IM + Unrealized PnL + Reserve
```

Where:
- `Unrealized PnL = qty × (mark − avg)` (signed qty)
- `Wallet` = free collateral (fees, funding, realized PnL net of margin moves)
- `Locked IM` = initial margin for open positions
- `Reserve` = non-traded buffer (P2=30%, P3=50% plans)

**Isolated liquidation equity** uses `locked + uPnL` only (reserve not at risk until moved).

**Implementation:** `_perp_equity()`, `run_perp_grid()`, `qtb/dual/tick_exec.py`

## Funding

```
net_funding = funding_received − funding_paid
```

Applied to wallet each bar with non-zero `funding_rate`. Missing funding → 0 (documented), not invented.

## Fees & Rebate

```
fee_paid, rebate = FeeSpec.fee_and_rebate(notional, maker)
wallet -= fee_paid  (opens/closes)
rebate tracked in st.rebates (reduces effective fee)
```

## Liquidation

Terminal event: position flattened, locked/wallet zeroed per mode, `liquidated=True`. Equity ≥ 0.

## EngineResult cross-checks (automated)

| Market | Per-bar identity |
|--------|------------------|
| spot / cash | `equity[i] ≈ cash[i] + qty[i] × close[i]` |
| perp | `equity[i] ≈ cash[i] + inventory_value[i] − locked_im[i]` where `locked_im = cash + inv − equity` |

See `qtb/ab/accounting_check.py` → `verify_engine_result()`.

## Property invariants (tests)

1. **No trades, flat price, zero fees** → equity unchanged
2. **Cash benchmark** → equity = initial always
3. **Deterministic replay** → identical inputs → identical equity series
4. **No negative equity** without liquidation flag (within float tolerance)

## On violation

- Tests fail immediately (`AccountingInvariantError`)
- Production runs should call `verify_engine_result()` before writing reports (future hook)
