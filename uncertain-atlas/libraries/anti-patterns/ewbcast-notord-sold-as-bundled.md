# 反模式：把 ExtWhenBcast step7-after-step6 not already construct-CanonicalVote / not already fill / not already Verify 正式三事（513 余量） 写成已经 已经 construct CanonicalVote bundled / 已经 fill CanonicalVoteExtension bundled / 已经 Verify 过扩展

**层次**：实现 / ExtWhenBcast step7-after-step6 not already construct-CanonicalVote / not already fill / not already Verify 正式三事（513 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7 broadcasts the Precommit message 句。  
**对应**：[`../tracks/implementation/worked-example-ewbcast-notord-vs-bundled.md`](../tracks/implementation/worked-example-ewbcast-notord-vs-bundled.md)。

把 ExtWhenBcast step7-after-step6 not already construct-CanonicalVote / not already fill / not already Verify 正式三事（513 余量） 写成已经 已经 construct CanonicalVote bundled / 已经 fill CanonicalVoteExtension bundled / 已经 Verify 过扩展，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（513 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 513 / 511 / 510 / 1343 / 1345 糊成一句。

也不是：

- [ewbcast-notpre-sold-as-bundled](ewbcast-notpre-sold-as-bundled.md) 是 notpre 单句边界（1343），不是本页边界。
- [ewbcast-notlc-sold-as-bundled](ewbcast-notlc-sold-as-bundled.md) 是 notlc 单句边界（1345），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
