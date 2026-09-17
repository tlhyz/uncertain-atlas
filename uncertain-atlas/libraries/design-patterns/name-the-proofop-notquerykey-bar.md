# 模式：把 ProofOp.key not Query response key / not ProofOp type / not already settled 正式三事（390 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**例**：[ProofOp.key ≠ bundled（390）](../../tracks/implementation/worked-example-proofop-notquerykey-vs-bundled.md)。

## 三个名字

1. **key 不是已经是 Query 回包键：** 看见填了 key，不是已经 380 interchangeable / 743 proofop-notquerykey interchangeable。
2. **看见填了 key 不是已经是 ProofOp 类型：** 看见有键，不是已经是 type interchangeable。
3. **看见能填 不是已经交差：** 看见 key，不是已经交差 interchangeable。

官方把 ProofOp.key / ProofOp.data / CheckTx 回包 log 三条核心句拆成三个名字。把它们叫成一个「看见填了 ProofOp 键就已经是 Query 回包键」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProofOp.key 正式三事（390 余量），先数清问的是 key 是不是已经是 Query 回包键 / 380、是不是已经是 ProofOp 类型、还是看见能填是不是已经交差，再决定要不要同一次发布。390 proofop vs key bundled unbundling 在本页 item 1 启动。
