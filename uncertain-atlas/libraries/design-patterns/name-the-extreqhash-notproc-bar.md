# 模式：点名 extreqhash-notproc 杠

**层次**：实现 / ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事（410 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extreqhash-notproc-vs-bundled.md`](../tracks/implementation/worked-example-extreqhash-notproc-vs-bundled.md)。

- **ExtendVoteRequest.hash 不是已经跑过 Process：** 看见填了 hash，不是已经跑过 Process interchangeable / 1022 extreqhash-notproc interchangeable。
- **看见有头哈希 不是已经交差：** 看见有头哈希，不是已经交差 interchangeable。
- **看见能指 不是已经签了：** 看见能指，不是已经签了 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.hash 正式三事（410 余量），先数清问的是是不是已经跑过 Process、是不是已经交差、还是看见能指是不是已经签了，再决定要不要同一次发布。410 extreqhash vs process bundled unbundling 在本页 item 1 启动。
