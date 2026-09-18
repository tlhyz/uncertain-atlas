# 反模式：把 ExtCiNotes ext votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（441 余量） 写成已经 已经进了块 / 已经交差 / 已经写进 last_commit

**层次**：实现 / ExtCiNotes ext votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（441 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedCommitInfo Notes 句。  
**对应**：[`../tracks/implementation/worked-example-extcnotes-notord-vs-bundled.md`](../tracks/implementation/worked-example-extcnotes-notord-vs-bundled.md)。

把 ExtCiNotes ext votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（441 余量） 写成已经 已经进了块 / 已经交差 / 已经写进 last_commit，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（441 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 441 / 365 / 444 / 1357 / 1358 糊成一句。

也不是：

- [extcnotes-noteng-sold-as-bundled](extcnotes-noteng-sold-as-bundled.md) 是 noteng 单句边界（1357），不是本页边界。
- [extcnotes-notload-sold-as-bundled](extcnotes-notload-sold-as-bundled.md) 是 notload 单句边界（1358），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
