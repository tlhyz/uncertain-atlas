# 反模式：把 CiFields round is commit-round not already voting-power-ordered / not already slashed / not already 394-ext-round 正式三事（445 余量） 写成已经 已经按投票权排过 / 已经罚没 / 已经是 ExtendedCommitInfo.round

**层次**：实现 / CiFields round is commit-round not already voting-power-ordered / not already slashed / not already 394-ext-round 正式三事（445 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields 句。  
**对应**：[`../tracks/implementation/worked-example-cifields-notrnd-vs-bundled.md`](../tracks/implementation/worked-example-cifields-notrnd-vs-bundled.md)。

把 CiFields round is commit-round not already voting-power-ordered / not already slashed / not already 394-ext-round 正式三事（445 余量） 写成已经 已经按投票权排过 / 已经罚没 / 已经是 ExtendedCommitInfo.round，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（445 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 445 / 392 / 394 / 1360 / 1361 糊成一句。

也不是：

- [cifields-notlst-sold-as-bundled](cifields-notlst-sold-as-bundled.md) 是 notlst 单句边界（1360），不是本页边界。
- [cifields-notnts-sold-as-bundled](cifields-notnts-sold-as-bundled.md) 是 notnts 单句边界（1361），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
