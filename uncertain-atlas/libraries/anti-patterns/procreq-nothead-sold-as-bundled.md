# 反模式：把 ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事（419 余量） 写成已经 已经对上了拟议块头 / 已经 ExtendVoteRequest.height 那种已经对上了拟议块 / 已经交差

**层次**：实现 / ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事（419 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procreq-nothead-vs-bundled.md`](../tracks/implementation/worked-example-procreq-nothead-vs-bundled.md)。

把 ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事（419 余量） 写成已经 已经对上了拟议块头 / 已经 ExtendVoteRequest.height 那种已经对上了拟议块 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.height 正式三事（419 余量），必须分开 not already header-aligned、not already ext-height、not already settled 三件事，不要和 419 / 417 / 410 / 1025 / 1026 糊成一句。

也不是：

- [procreq-notproc-sold-as-bundled](procreq-notproc-sold-as-bundled.md) 是 hash 仍未 Process 单句边界（1026 item 2），不是本页 height 仍未对上拟议块头边界。
- Process 的 height / time 对上拟议块头就已经验过块头是不变量 417，不是本页有高度仍未 ext-height 边界。
