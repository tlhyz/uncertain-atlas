# 模式：点名 finrestr-nothash 杠

**层次**：实现 / FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事（428 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finrestr-nothash-vs-bundled.md`](../tracks/implementation/worked-example-finrestr-nothash-vs-bundled.md)。

- **hash 不是已经是 ProcessProposalRequest.hash：** 看见填了 hash，不是已经是 ProcessProposalRequest.hash interchangeable / 1061 finrestr-nothash interchangeable。
- **看见能指已决块 不是已经跑过 Process：** 看见能指已决块，不是已经跑过 Process interchangeable。
- **看见字段名对得上 不是已经交差：** 看见字段名对得上，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 hash 正式三事（428 余量），先数清问的是是不是已经是 Process hash、是不是已经跑过 Process、还是看见字段名对得上是不是已经交差，再决定要不要同一次发布。428 finreqrest vs procreq bundled unbundling 在本页 item 1 启动。
