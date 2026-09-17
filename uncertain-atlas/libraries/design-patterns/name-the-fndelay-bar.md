# 模式：把 FinalizeBlockResponse next_block_delay 非确定正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage `next_block_delay`。  
**例**：[next_block_delay Deterministic = No ≠ 已经是槽位](../../tracks/implementation/worked-example-fndelay-vs-deterministic.md)。

## 三个名字

1. **next_block_delay Deterministic = No 不是已经是槽位 / finality / timeout_commit：** 看见 Response 表非确定列，不是已经块间隔或已经 finality。
2. **each node MAY / wallclock / NTP 不是已经 app_hash MUST be deterministic / 整门非确定：** 看见各节点可以回不同值，不是已经 Finalize 回包整门非确定。
3. **Set to 0 when all precommits and block processed 不是已经决定 / finality / 块间隔：** 看见 set to 0 立刻开下一高，不是已经决定或已经槽位。

## 为什么要分开叫

官方把 `next_block_delay` Response 表 **Deterministic = No**、Usage 里 each node MAY 回不同值 / wallclock、Set to 0 when all precommits and block processed 写成三个名字。把它们叫成一个「看见非确定就已经是槽位 / 已经 finality」，会把槽位、整门非确定、set to 0 语义三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见非确定就已经是槽位」，先数清问的是 next_block_delay Deterministic = No 是不是已经是槽位 / finality / timeout_commit、each node MAY / wallclock 是不是已经 app_hash MUST be deterministic / 整门非确定，还是 Set to 0 when all precommits and block processed 是不是已经决定 / finality / 块间隔，再决定要不要同一次发布。
