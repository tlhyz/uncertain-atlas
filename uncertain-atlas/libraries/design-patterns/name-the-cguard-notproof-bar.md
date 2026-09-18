# 模式：点名 cguard-notproof 杠

**层次**：实现 / Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事（405 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-cguard-notproof-vs-bundled.md`](../tracks/implementation/worked-example-cguard-notproof-vs-bundled.md)。

- **自描述 type 不是已经是 ProofOp 类型：** 看见写了 type，不是已经是 ProofOp 类型 interchangeable / 1105 cguard-notproof interchangeable。
- **看见能支持多种树 不是已经对上 AppHash：** 看见能支持多种树，不是已经对上 AppHash interchangeable。
- **看见能回证明 不是已经交差：** 看见能回证明，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自描述 type 正式三事（405 余量），先数清问的是是不是已经是 ProofOp 类型、是不是已经对上 AppHash、还是看见能回证明是不是已经交差，再决定要不要同一次发布。405 checktxguard vs optional bundled unbundling 在本页 item 3 完成。
