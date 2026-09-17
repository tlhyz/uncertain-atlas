# 模式：点名 finreqcol-notlocal 杠

**层次**：实现 / FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事（422 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finreqcol-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-finreqcol-notlocal-vs-bundled.md)。

- **decided_last_commit 不是已经交差 local_last_commit：** 看见填了 decided_last_commit，不是已经交差 local_last_commit interchangeable / 1040 finreqcol-notlocal interchangeable。
- **看见从刚决定那块拿到 不是已经定奖惩：** 看见从刚决定那块拿到，不是已经定奖惩 interchangeable。
- **看见能指上一份提交 不是已经交差：** 看见能指上一份提交，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 decided_last_commit 正式三事（422 余量），先数清问的是是不是已经交差 local_last_commit、是不是已经定奖惩、还是看见能指上一份提交是不是已经交差，再决定要不要同一次发布。422 finreq vs procreq bundled unbundling 在本页 item 1 启动。
