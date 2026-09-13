# Review Log — TASK-0009 ACCOUNTING_INVARIANTS

## Meta

- **date_utc:** 2026-09-13T00:52Z
- **experiment_id:** TASK-0009
- **author:** cursor-agent

## Action

1. `docs/ACCOUNTING_INVARIANTS.md` — spot/perp/funding/fee formulas
2. `qtb/ab/accounting_check.py` — verify_engine_result + AccountingInvariantError
3. `tests/test_accounting_invariants.py` — 9 tests (flat cash, spot conservation, perp identity, deterministic replay)

## Verdict

- **verdict:** PASS
- **tests:** 97 total pass

## Next

TASK-0010 test_no_future_leak.py
