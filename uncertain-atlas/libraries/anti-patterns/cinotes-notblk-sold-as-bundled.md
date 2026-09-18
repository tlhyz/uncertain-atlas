# 反模式：把 CiNotes votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（444 余量） 写成已经 已经进了块 / 已经交差 / 已经写进 last_commit

**层次**：实现 / CiNotes votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（444 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Notes 句。  
**对应**：[`../tracks/implementation/worked-example-cinotes-notblk-vs-bundled.md`](../tracks/implementation/worked-example-cinotes-notblk-vs-bundled.md)。

把 CiNotes votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（444 余量） 写成已经 已经进了块 / 已经交差 / 已经写进 last_commit，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（444 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 444 / 365 / 392 / 1354 / 1355 糊成一句。

也不是：

- [cinotes-notapp-sold-as-bundled](cinotes-notapp-sold-as-bundled.md) 是 notapp 单句边界（1354），不是本页边界。
- [cinotes-notstore-sold-as-bundled](cinotes-notstore-sold-as-bundled.md) 是 notstore 单句边界（1355），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
