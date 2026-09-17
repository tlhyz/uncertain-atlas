# 模式：点名 procreq-notproc 杠

**层次**：实现 / ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事（419 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procreq-notproc-vs-bundled.md`](../tracks/implementation/worked-example-procreq-notproc-vs-bundled.md)。

- **ProcessProposalRequest.hash 不是已经跑过 Process：** 看见填了 hash，不是已经跑过 Process interchangeable / 1026 procreq-notproc interchangeable。
- **看见有拟议块哈希 不是已经请求里的 hash 那种不保证已经对该块跑过 Process：** 看见有拟议块哈希，不是已经请求里的 hash 那种不保证已经对该块跑过 Process interchangeable。
- **看见能指 不是已经交差：** 看见能指，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.hash 正式三事（419 余量），先数清问的是是不是已经跑过 Process、是不是已经请求里的 hash 那种不保证已经对该块跑过 Process、还是看见能指是不是已经交差，再决定要不要同一次发布。419 procreq vs extreq bundled unbundling 在本页 item 2 续。
