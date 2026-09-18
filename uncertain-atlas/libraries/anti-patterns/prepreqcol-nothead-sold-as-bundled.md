# 反模式：把 PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事（423 余量） 写成已经 已经对上了拟议块头 / 已经知道本头哈希 / 已经交差

**层次**：实现 / PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事（423 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-prepreqcol-nothead-vs-bundled.md`](../tracks/implementation/worked-example-prepreqcol-nothead-vs-bundled.md)。

把 PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事（423 余量） 写成已经 已经对上了拟议块头 / 已经知道本头哈希 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 正式三事（423 余量），必须分开 not already header-aligned、not already header-known、not already settled 三件事，不要和 423 / 419 / 359 / 422 / 1046 / 1047 糊成一句。

也不是：

- [prepreqcol-notproc-sold-as-bundled](prepreqcol-notproc-sold-as-bundled.md) 是 txs 仍未跑过 Process 单句边界（1047 item 2），不是本页 height 仍未对上拟议块头边界。
- ProcessProposalRequest.height 就已经对上了拟议块头是不变量 419，不是本页有将要提议的高度仍未知道本头哈希边界。
