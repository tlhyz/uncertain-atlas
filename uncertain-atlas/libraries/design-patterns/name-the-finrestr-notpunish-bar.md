# 模式：点名 finrestr-notpunish 杠

**层次**：实现 / FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（428 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finrestr-notpunish-vs-bundled.md`](../tracks/implementation/worked-example-finrestr-notpunish-vs-bundled.md)。

- **misbehavior 不是已经定奖惩：** 看见填了 misbehavior，不是已经定奖惩 interchangeable / 1062 finrestr-notpunish interchangeable。
- **看见有过错列表 不是已经是 ProcessProposalRequest.misbehavior：** 看见有过错列表，不是已经是 ProcessProposalRequest.misbehavior interchangeable。
- **看见能指过错 不是已经交差：** 看见能指过错，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 misbehavior 正式三事（428 余量），先数清问的是是不是已经定奖惩、是不是已经是 Process misbehavior、还是看见能指过错是不是已经交差，再决定要不要同一次发布。428 finreqrest vs procreq bundled unbundling 在本页 item 2 续。
