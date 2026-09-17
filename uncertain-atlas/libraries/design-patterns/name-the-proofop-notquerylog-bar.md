# 模式：把 CheckTx 回包 log not Query log / not CheckTx Data used / not already settled 正式三事（390 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**例**：[CheckTx ≠ bundled（390）](../../tracks/implementation/worked-example-proofop-notquerylog-vs-bundled.md)。

## 三个名字

1. **log 不是已经是 Query 日志：** 看见回了日志，不是已经 384 interchangeable / 745 proofop-notquerylog interchangeable。
2. **看见回了日志 不是已经 Data 被引擎用了：** 看见有日志，不是已经 Data interchangeable。
3. **看见能回 不是已经交差：** 看见 log，不是已经交差 interchangeable。

官方把 ProofOp.key / ProofOp.data / CheckTx 回包 log 三条核心句拆成三个名字。把它们叫成一个「看见填了 ProofOp 键就已经是 Query 回包键」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 log 正式三事（390 余量），先数清问的是 log 是不是已经是 Query 日志 / 384、是不是已经 Data 被引擎用了、还是看见能回是不是已经交差，再决定要不要同一次发布。390 proofop vs key bundled unbundling 在本页 item 3 完成。
