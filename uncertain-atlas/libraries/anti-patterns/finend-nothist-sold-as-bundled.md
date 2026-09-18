# 反模式：把 FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事（429 余量） 写成已经 已经有完整历史 / 已经是快照重放 / 已经切进共识

**层次**：实现 / FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事（429 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finend-nothist-vs-bundled.md`](../tracks/implementation/worked-example-finend-nothist-vs-bundled.md)。

把 FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事（429 余量） 写成已经 已经有完整历史 / 已经是快照重放 / 已经切进共识，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height 正式三事（429 余量），必须分开 not already full-history、not already snapshot-restore、not already consensus 三件事，不要和 429 / 382 / 1064 / 1065 糊成一句。

也不是：

- [finend-nothead-sold-as-bundled](finend-nothead-sold-as-bundled.md) 是 time 仍未对上拟议块头单句边界（1065 item 2），不是本页 syncing_to_height 仍未有完整历史边界。
- syncing_to_height 就已经有完整历史是不变量 382，不是本页在同步或重放仍未是快照重放边界。
