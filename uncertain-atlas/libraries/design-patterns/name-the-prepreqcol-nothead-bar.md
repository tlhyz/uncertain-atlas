# 模式：点名 prepreqcol-nothead 杠

**层次**：实现 / PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事（423 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-prepreqcol-nothead-vs-bundled.md`](../tracks/implementation/worked-example-prepreqcol-nothead-vs-bundled.md)。

- **height 不是已经对上了拟议块头：** 看见填了 height，不是已经对上了拟议块头 interchangeable / 1048 prepreqcol-nothead interchangeable。
- **看见有将要提议的高度 不是已经知道本头哈希：** 看见有将要提议的高度，不是已经知道本头哈希 interchangeable。
- **看见能指高度 不是已经交差：** 看见能指高度，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 正式三事（423 余量），先数清问的是是不是已经对上了拟议块头、是不是已经知道本头哈希、还是看见能指高度是不是已经交差，再决定要不要同一次发布。423 prepreq vs return bundled unbundling 在本页 item 3 完成。
