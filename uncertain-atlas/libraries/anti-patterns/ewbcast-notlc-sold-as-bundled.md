# 反模式：把 ExtWhenBcast broadcast not already last_commit / not already late-Verify / not already 438-bundled 正式三事（513 余量） 写成已经 已经写进 last_commit / 已经 Verify 过迟到扩展 / 已经 ExtendVote When 正式流程 bundled

**层次**：实现 / ExtWhenBcast broadcast not already last_commit / not already late-Verify / not already 438-bundled 正式三事（513 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7 broadcasts the Precommit message 句。  
**对应**：[`../tracks/implementation/worked-example-ewbcast-notlc-vs-bundled.md`](../tracks/implementation/worked-example-ewbcast-notlc-vs-bundled.md)。

把 ExtWhenBcast broadcast not already last_commit / not already late-Verify / not already 438-bundled 正式三事（513 余量） 写成已经 已经写进 last_commit / 已经 Verify 过迟到扩展 / 已经 ExtendVote When 正式流程 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（513 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 513 / 438 / 435 / 1343 / 1344 糊成一句。

也不是：

- [ewbcast-notpre-sold-as-bundled](ewbcast-notpre-sold-as-bundled.md) 是 notpre 单句边界（1343），不是本页边界。
- [ewbcast-notord-sold-as-bundled](ewbcast-notord-sold-as-bundled.md) 是 notord 单句边界（1344），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
