# 反模式：把 ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事（410 余量） 写成已经 已经跑过 Process / 已经交差 / 已经签了

**层次**：实现 / ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事（410 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extreqhash-notproc-vs-bundled.md`](../tracks/implementation/worked-example-extreqhash-notproc-vs-bundled.md)。

把 ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事（410 余量） 写成已经 已经跑过 Process / 已经交差 / 已经签了，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.hash 正式三事（410 余量），必须分开 not already processed、not already settled、not already signed 三件事，不要和 410 / 353 / 304 / 1023 / 1024 糊成一句。

也不是：

- [crashrec-notskip-sold-as-bundled](crashrec-notskip-sold-as-bundled.md) 是启动 Info 对上仍未能跳步边界（320/1021），不是本页 hash 仍未 Process 边界。
- 请求里的 hash 不是已经对该块跑过 Process 是不变量 353，不是本页有头哈希仍未交差边界。
