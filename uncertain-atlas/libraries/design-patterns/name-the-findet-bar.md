# 模式：把 FinalizeBlock Usage determinism 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[executes txs deterministically ≠ 已经可以像 Prepare 那样](../../tracks/implementation/worked-example-findet-vs-replication.md)。

## 三个名字

1. **executes txs deterministically before returning control 不是已经可以像 Prepare 那样：** 看见确定执行 txs 不是已经 Prepare 没有确定性要求 interchangeable。
2. **app_hash MUST be deterministic / only params + previous state 不是已经印进本头 / next_block_delay 非确定就代表整门非确定：** 看见 app_hash 必须确定不是已经 next_block_delay 非确定就代表整门非确定。
3. **implementation MUST be deterministic for state machine replication 不是已经是 Req 11–12 / finfields bundled：** 看见 Usage 这句不是已经 Req 11–12 或 finfields bundled interchangeable。

## 为什么要分开叫

官方把 executes txs deterministically、app_hash MUST be deterministic、implementation MUST be deterministic for state machine replication 写成三个名字。把它们叫成一个「看见 Usage 写了必须确定就已经可以像 Prepare 那样、已经印进本头、已经 next_block_delay 非确定就代表整门非确定」，会把执行确定性、app_hash 必须确定和状态机复制必须确定三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Usage 写了必须确定」，先数清问的是 executes txs deterministically 是不是已经可以像 Prepare 那样、app_hash MUST be deterministic 是不是已经 next_block_delay 非确定就代表整门非确定，还是 implementation MUST be deterministic 是不是已经是 Req 11–12 / finfields bundled，再决定要不要同一次发布。
