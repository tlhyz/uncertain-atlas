# 反模式：把 FinalizeBlock Usage determinism 正式三事说成已经可以像 Prepare 那样

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[executes txs deterministically ≠ 已经可以像 Prepare 那样](../../tracks/implementation/worked-example-findet-vs-replication.md)。

## 错在哪里

把 Application executes txs deterministically before returning control 写成已经可以像 Prepare 那样依赖非确定值，或已经套用 candidate 就不需要再在 Finalize 执行；把 app_hash MUST be deterministic / only params + previous state 写成已经印进本头，或已经 next_block_delay 非确定就代表 Finalize 回包整门都可以非确定；把 implementation MUST be deterministic for state machine replication 写成已经是 Req 11–12 那种 s_h / T_h 只依赖两份 interchangeable，或已经和 407 finfields bundled / 342 / 460 / 404 / 469 糊成一句。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Usage determinism 正式三事，必须分开 executes txs deterministically、app_hash MUST be deterministic、implementation MUST be deterministic for state machine replication 三件事，不要和 338 / 342 / 404 / 407 / 460 / 469 糊成一句。
