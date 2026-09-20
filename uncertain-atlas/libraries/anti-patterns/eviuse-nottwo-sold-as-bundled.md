# 反模式：把 ExtViUse two sigs when enabled empty-slice if no non_rp not already one-sig / not already no-second / not already 358-replay 正式三事（447 余量） 写成已经 已经只有一份签 / 已经没 non_rp 就没有第二份签 / 已经 optional 就跳过 Verify

**层次**：实现 / ExtViUse two sigs when enabled empty-slice if no non_rp not already one-sig / not already no-second / not already 358-replay 正式三事（447 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage 句。  
**对应**：[`../tracks/implementation/worked-example-eviuse-nottwo-vs-bundled.md`](../tracks/implementation/worked-example-eviuse-nottwo-vs-bundled.md)。

把 ExtViUse two sigs when enabled empty-slice if no non_rp not already one-sig / not already no-second / not already 358-replay 正式三事（447 余量） 写成已经 已经只有一份签 / 已经没 non_rp 就没有第二份签 / 已经 optional 就跳过 Verify，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（447 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 447 / 358 / 418 / 1365 / 1366 糊成一句。

也不是：

- [eviuse-notapp-sold-as-bundled](eviuse-notapp-sold-as-bundled.md) 是 notapp 单句边界（1365），不是本页边界。
- [eviuse-notexp-sold-as-bundled](eviuse-notexp-sold-as-bundled.md) 是 notexp 单句边界（1366），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
