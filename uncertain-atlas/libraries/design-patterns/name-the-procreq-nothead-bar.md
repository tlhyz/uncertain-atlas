# 模式：点名 procreq-nothead 杠

**层次**：实现 / ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事（419 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procreq-nothead-vs-bundled.md`](../tracks/implementation/worked-example-procreq-nothead-vs-bundled.md)。

- **ProcessProposalRequest.height 不是已经对上了拟议块头：** 看见填了 height，不是已经对上了拟议块头 interchangeable / 1027 procreq-nothead interchangeable。
- **看见有高度 不是已经 ExtendVoteRequest.height 那种已经对上了拟议块：** 看见有高度，不是已经 ExtendVoteRequest.height 那种已经对上了拟议块 interchangeable。
- **看见能指 不是已经交差：** 看见能指，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.height 正式三事（419 余量），先数清问的是是不是已经对上了拟议块头、是不是已经 ExtendVoteRequest.height 那种已经对上了拟议块、还是看见能指是不是已经交差，再决定要不要同一次发布。419 procreq vs extreq bundled unbundling 在本页 item 3 完成。
