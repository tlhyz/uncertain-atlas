# 模式：点名 finreqcol-notexec 杠

**层次**：实现 / FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事（422 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finreqcol-notexec-vs-bundled.md`](../tracks/implementation/worked-example-finreqcol-notexec-vs-bundled.md)。

- **txs 不是已经执行那些交易：** 看见填了 txs，不是已经执行那些交易 interchangeable / 1042 finreqcol-notexec interchangeable。
- **看见有交易列表 不是已经是 ProcessProposalRequest.txs：** 看见有交易列表，不是已经是 ProcessProposalRequest.txs interchangeable。
- **看见能指交易 不是已经交差：** 看见能指交易，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 txs 正式三事（422 余量），先数清问的是是不是已经执行那些交易、是不是已经是 ProcessProposalRequest.txs、还是看见能指交易是不是已经交差，再决定要不要同一次发布。422 finreq vs procreq bundled unbundling 在本页 item 3 完成。
