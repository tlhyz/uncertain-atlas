# 模式：点名 preprend-notts 杠

**层次**：实现 / FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（426 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-preprend-notts-vs-bundled.md`](../tracks/implementation/worked-example-preprend-notts-vs-bundled.md)。

- **time 不是已经对上了拟议块头：** 看见填了 time，不是已经对上了拟议块头 interchangeable / 1057 preprend-notts interchangeable。
- **看见有已决块时间戳 不是已经是 PrepareProposalRequest.time：** 看见有已决块时间戳，不是已经是 PrepareProposalRequest.time interchangeable。
- **看见能指已决时间 不是已经交差：** 看见能指已决时间，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.time 正式三事（426 余量），先数清问的是是不是已经对上了拟议块头、是不是已经是 PrepareProposalRequest.time、还是看见能指已决时间是不是已经交差，再决定要不要同一次发布。426 prepreqend vs finreq bundled unbundling 在本页 item 3 完成。
