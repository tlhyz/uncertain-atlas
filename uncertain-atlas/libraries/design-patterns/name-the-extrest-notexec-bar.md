# 模式：点名 extrest-notexec 杠

**层次**：实现 / ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事（411 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extrest-notexec-vs-bundled.md`](../tracks/implementation/worked-example-extrest-notexec-vs-bundled.md)。

- **txs 不是已经执行那些交易：** 看见填了 txs，不是已经执行那些交易 interchangeable / 1034 extrest-notexec interchangeable。
- **看见有交易列表 不是已经交差：** 看见有交易列表，不是已经交差 interchangeable。
- **看见能指 不是已经整块跑了：** 看见能指，不是已经整块跑了 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 txs 正式三事（411 余量），先数清问的是是不是已经执行那些交易、是不是已经交差、还是看见能指是不是已经整块跑了，再决定要不要同一次发布。411 extreqtxs vs fintxs bundled unbundling 在本页 item 1 启动。
