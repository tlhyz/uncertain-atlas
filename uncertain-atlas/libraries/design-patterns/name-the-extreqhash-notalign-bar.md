# 模式：点名 extreqhash-notalign 杠

**层次**：实现 / ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事（410 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extreqhash-notalign-vs-bundled.md`](../tracks/implementation/worked-example-extreqhash-notalign-vs-bundled.md)。

- **ExtendVoteRequest.height 不是已经对上了拟议块：** 看见填了 height，不是已经对上了拟议块 interchangeable / 1023 extreqhash-notalign interchangeable。
- **看见能对一下 不是已经会调 ExtendVote：** 看见能对一下，不是已经会调 interchangeable。
- **看见有高度 不是已经是拍快照的高度：** 看见有高度，不是已经是拍快照的高度 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.height 正式三事（410 余量），先数清问的是是不是已经对上了拟议块、是不是已经会调、还是看见有高度是不是已经是拍快照的高度，再决定要不要同一次发布。410 extreqhash vs process bundled unbundling 在本页 item 2 续。
