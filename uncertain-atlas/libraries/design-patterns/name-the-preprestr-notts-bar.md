# 模式：点名 preprestr-notts 杠

**层次**：实现 / PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事（424 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-preprestr-notts-vs-bundled.md`](../tracks/implementation/worked-example-preprestr-notts-vs-bundled.md)。

- **time 不是已经对上了拟议块头：** 看见填了 time，不是已经对上了拟议块头 interchangeable / 1050 preprestr-notts interchangeable。
- **看见有将要提议的时间戳 不是已经验过票上时间：** 看见有将要提议的时间戳，不是已经验过票上时间 interchangeable。
- **看见能指时间 不是已经交差：** 看见能指时间，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 time 正式三事（424 余量），先数清问的是是不是已经对上了拟议块头、是不是已经验过票上时间、还是看见能指时间是不是已经交差，再决定要不要同一次发布。424 prepreqrest vs procreq bundled unbundling 在本页 item 2 续。
