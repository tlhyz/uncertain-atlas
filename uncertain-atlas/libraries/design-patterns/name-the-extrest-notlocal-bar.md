# 模式：点名 extrest-notlocal 杠

**层次**：实现 / ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事（411 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extrest-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-extrest-notlocal-vs-bundled.md)。

- **proposed_last_commit 不是已经交差 local_last_commit：** 看见填了 proposed_last_commit，不是已经交差 local_last_commit interchangeable / 1035 extrest-notlocal interchangeable。
- **看见有上一份拟议块的 last commit 不是已经字段名对上就已经跑过 Process：** 看见有上一份拟议块的 last commit，不是已经字段名对上就已经跑过 Process interchangeable。
- **看见能指 不是已经是本头 LastCommit：** 看见能指，不是已经是本头 LastCommit interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposed_last_commit 正式三事（411 余量），先数清问的是是不是已经交差 local_last_commit、是不是已经字段名对上就已经跑过 Process、还是看见能指是不是已经是本头 LastCommit，再决定要不要同一次发布。411 extreqtxs vs fintxs bundled unbundling 在本页 item 2 续。
