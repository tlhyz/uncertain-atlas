# 模式：点名 procrestr-notts 杠

**层次**：实现 / ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事（420 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procrestr-notts-vs-bundled.md`](../tracks/implementation/worked-example-procrestr-notts-vs-bundled.md)。

- **time 不是已经验过票上时间：** 看见填了 time，不是已经验过票上时间 interchangeable / 1029 procrestr-notts interchangeable。
- **看见有拟议块时间戳 不是已经验过块头：** 看见有拟议块时间戳，不是已经验过块头 interchangeable。
- **看见能指时间 不是已经交差：** 看见能指时间，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 time 正式三事（420 余量），先数清问的是是不是已经验过票上时间、是不是已经验过块头、还是看见能指时间是不是已经交差，再决定要不要同一次发布。420 procreqrest vs extreq bundled unbundling 在本页 item 2 续。
