# 反模式：把 PrepEv Prepare MAY produce events not already in PrepareProposalResponse / not already engine-received / not already 357-checked 正式三事（448 余量） 写成已经 已经在 PrepareProposalResponse 里交回 / 已经 Prepare 返回时引擎收到 / 已经验过重复

**层次**：实现 / PrepEv Prepare MAY produce events not already in PrepareProposalResponse / not already engine-received / not already 357-checked 正式三事（448 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应**：[`../tracks/implementation/worked-example-prepev-notret-vs-bundled.md`](../tracks/implementation/worked-example-prepev-notret-vs-bundled.md)。

把 PrepEv Prepare MAY produce events not already in PrepareProposalResponse / not already engine-received / not already 357-checked 正式三事（448 余量） 写成已经 已经在 PrepareProposalResponse 里交回 / 已经 Prepare 返回时引擎收到 / 已经验过重复，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（448 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 448 / 357 / 503 / 1369 / 1370 糊成一句。

也不是：

- [prepev-notkeep-sold-as-bundled](prepev-notkeep-sold-as-bundled.md) 是 notkeep 单句边界（1369），不是本页边界。
- [prepev-notfin-sold-as-bundled](prepev-notfin-sold-as-bundled.md) 是 notfin 单句边界（1370），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
