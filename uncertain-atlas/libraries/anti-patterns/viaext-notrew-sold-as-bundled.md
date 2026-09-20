# 反模式：把 ViAvail availability same-sentence not already rewarded / not already settled / not already Finalize-computed 正式三事（442 余量） 写成已经 已经奖罚完 / 已经交差 / 已经 Finalize 算完奖惩

**层次**：实现 / ViAvail availability same-sentence not already rewarded / not already settled / not already Finalize-computed 正式三事（442 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo Usage / ExtendedVoteInfo Usage 句。  
**对应**：[`../tracks/implementation/worked-example-viaext-notrew-vs-bundled.md`](../tracks/implementation/worked-example-viaext-notrew-vs-bundled.md)。

把 ViAvail availability same-sentence not already rewarded / not already settled / not already Finalize-computed 正式三事（442 余量） 写成已经 已经奖罚完 / 已经交差 / 已经 Finalize 算完奖惩，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（442 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 442 / 365 / 425 / 1375 / 1376 糊成一句。

也不是：

- [viaext-notblk-sold-as-bundled](viaext-notblk-sold-as-bundled.md) 是 notblk 单句边界（1375），不是本页边界。
- [viaext-notloc-sold-as-bundled](viaext-notloc-sold-as-bundled.md) 是 notloc 单句边界（1376），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
