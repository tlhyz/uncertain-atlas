# 模式：点名 prepev-notret 杠

**层次**：实现 / PrepEv Prepare MAY produce events not already in PrepareProposalResponse / not already engine-received / not already 357-checked 正式三事（448 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应**：[`../tracks/implementation/worked-example-prepev-notret-vs-bundled.md`](../tracks/implementation/worked-example-prepev-notret-vs-bundled.md)。

- **Prepare MAY 产出事件不是已经在回包里交回 不是已经在 PrepareProposalResponse 里交回：看见Prepare MAY 产出事件不是已经在回包里交回，不是已经在 PrepareProposalResponse 里交回 interchangeable / 1368 prepev-notret interchangeable。**
- **Prepare MAY produce events is not already in the response 不是已经 Prepare 返回时引擎收到：看见Prepare MAY produce events is not already in the response，不是已经 Prepare 返回时引擎收到 interchangeable / 1368 prepev-notret interchangeable。**
- **Prepare MAY 产出事件不是已经在回包里交回 不是已经验过重复：看见Prepare MAY 产出事件不是已经在回包里交回，不是已经验过重复 interchangeable / 1368 prepev-notret interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（448 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
