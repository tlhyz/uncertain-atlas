# 反模式：把 ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事（410 余量） 写成已经 已经对上了拟议块 / 已经会调 ExtendVote / 已经是拍快照的高度

**层次**：实现 / ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事（410 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extreqhash-notalign-vs-bundled.md`](../tracks/implementation/worked-example-extreqhash-notalign-vs-bundled.md)。

把 ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事（410 余量） 写成已经 已经对上了拟议块 / 已经会调 ExtendVote / 已经是拍快照的高度，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.height 正式三事（410 余量），必须分开 not already aligned、not already will-call、not already snapshot-height 三件事，不要和 410 / 409 / 353 / 1022 / 1024 糊成一句。

也不是：

- [extreqhash-notproc-sold-as-bundled](extreqhash-notproc-sold-as-bundled.md) 是 hash 仍未 Process 单句边界（1022 item 1），不是本页 height 仍未对上拟议块边界。
- 请求内容对应即将发 Precommit 的拟议块就已经会调是不变量 409，不是本页能对一下仍未会调边界。
