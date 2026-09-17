# 模式：点名 finreqcol-nothead 杠

**层次**：实现 / FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事（422 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finreqcol-nothead-vs-bundled.md`](../tracks/implementation/worked-example-finreqcol-nothead-vs-bundled.md)。

- **height 不是已经对上了拟议块头：** 看见填了 height，不是已经对上了拟议块头 interchangeable / 1041 finreqcol-nothead interchangeable。
- **看见有已决块高度 不是已经字段名对上就已经跑过 Process：** 看见有已决块高度，不是已经字段名对上就已经跑过 Process interchangeable。
- **看见能指高度 不是已经交差：** 看见能指高度，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 正式三事（422 余量），先数清问的是是不是已经对上了拟议块头、是不是已经字段名对上就已经跑过 Process、还是看见能指高度是不是已经交差，再决定要不要同一次发布。422 finreq vs procreq bundled unbundling 在本页 item 2 续。
