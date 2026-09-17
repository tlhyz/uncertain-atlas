# 反模式：把 ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事（410 余量） 写成已经 已经验过票上时间 / 已经交差 / 已经是过错发生那一高已提交块的时间

**层次**：实现 / ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事（410 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extreqhash-notts-vs-bundled.md`](../tracks/implementation/worked-example-extreqhash-notts-vs-bundled.md)。

把 ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事（410 余量） 写成已经 已经验过票上时间 / 已经交差 / 已经是过错发生那一高已提交块的时间，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.time 正式三事（410 余量），必须分开 not already vote-ts-checked、not already settled、not already evidence-time 三件事，不要和 410 / 304 / 352 / 1022 / 1023 糊成一句。

也不是：

- [extreqhash-notalign-sold-as-bundled](extreqhash-notalign-sold-as-bundled.md) 是 height 仍未对上拟议块单句边界（1023 item 2），不是本页 time 仍未验过票上时间边界。
- 票上 Timestamp 就已经验过是不变量 304，不是本页能指时间仍未交差边界。
