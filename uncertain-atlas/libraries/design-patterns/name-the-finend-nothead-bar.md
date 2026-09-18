# 模式：点名 finend-nothead 杠

**层次**：实现 / FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（429 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finend-nothead-vs-bundled.md`](../tracks/implementation/worked-example-finend-nothead-vs-bundled.md)。

- **time 不是已经对上了拟议块头：** 看见填了 time，不是已经对上了拟议块头 interchangeable / 1065 finend-nothead interchangeable。
- **看见有已决块时间戳 不是已经是 PrepareProposalRequest.time：** 看见有已决块时间戳，不是已经是 PrepareProposalRequest.time interchangeable。
- **看见能指时间戳 不是已经交差：** 看见能指时间戳，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 time 正式三事（429 余量），先数清问的是是不是已经对上了拟议块头、是不是已经是 Prepare time、还是看见能指时间戳是不是已经交差，再决定要不要同一次发布。429 finreqend vs procreq bundled unbundling 在本页 item 2 续。
