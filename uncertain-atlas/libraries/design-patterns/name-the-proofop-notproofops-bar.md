# 模式：把 ProofOp.data not proof_ops / not already AppHash matched / not already settled 正式三事（390 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**例**：[ProofOp.data ≠ bundled（390）](../../tracks/implementation/worked-example-proofop-notproofops-vs-bundled.md)。

## 三个名字

1. **data 不是已经是 proof_ops：** 看见填了 data，不是已经 325 interchangeable / 744 proofop-notproofops interchangeable。
2. **看见填了 data 不是已经对上 AppHash：** 看见有编码证明，不是已经 325 interchangeable。
3. **看见能回 不是已经交差：** 看见 data，不是已经交差 interchangeable。

官方把 ProofOp.key / ProofOp.data / CheckTx 回包 log 三条核心句拆成三个名字。把它们叫成一个「看见填了 ProofOp 键就已经是 Query 回包键」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProofOp.data 正式三事（390 余量），先数清问的是 data 是不是已经是 proof_ops / 325、是不是已经对上 AppHash / 325、还是看见能回是不是已经交差，再决定要不要同一次发布。390 proofop vs key bundled unbundling 在本页 item 2 续。
