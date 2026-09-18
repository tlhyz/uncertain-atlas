# 模式：点名 prepreqcol-notproc 杠

**层次**：实现 / PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事（423 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-prepreqcol-notproc-vs-bundled.md`](../tracks/implementation/worked-example-prepreqcol-notproc-vs-bundled.md)。

- **txs 不是已经跑过 Process：** 看见填了 txs，不是已经跑过 Process interchangeable / 1047 prepreqcol-notproc interchangeable。
- **看见是初步列表 不是已经执行那些交易：** 看见是初步列表，不是已经执行那些交易 interchangeable。
- **看见能指初步交易 不是已经交差：** 看见能指初步交易，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 txs 正式三事（423 余量），先数清问的是是不是已经跑过 Process、是不是已经执行那些交易、还是看见能指初步交易是不是已经交差，再决定要不要同一次发布。423 prepreq vs return bundled unbundling 在本页 item 2 续。
