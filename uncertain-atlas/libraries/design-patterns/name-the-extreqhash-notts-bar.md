# 模式：点名 extreqhash-notts 杠

**层次**：实现 / ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事（410 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extreqhash-notts-vs-bundled.md`](../tracks/implementation/worked-example-extreqhash-notts-vs-bundled.md)。

- **ExtendVoteRequest.time 不是已经验过票上时间：** 看见填了 time，不是已经验过票上时间 interchangeable / 1024 extreqhash-notts interchangeable。
- **看见能指时间 不是已经交差：** 看见能指时间，不是已经交差 interchangeable。
- **看见有时间戳 不是已经是过错发生那一高已提交块的时间：** 看见有时间戳，不是已经是过错发生那一高已提交块的时间 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.time 正式三事（410 余量），先数清问的是是不是已经验过票上时间、是不是已经交差、还是看见有时间戳是不是已经是过错发生那一高已提交块的时间，再决定要不要同一次发布。410 extreqhash vs process bundled unbundling 在本页 item 3 完成。
