# 模式：点名 valuse-notfin 杠

**层次**：实现 / ValUse Finalize decided_last_commit Validator not already Process proposed / not already settled / not already Prepare-ext 正式三事（449 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage 句。  
**对应**：[`../tracks/implementation/worked-example-valuse-notfin-vs-bundled.md`](../tracks/implementation/worked-example-valuse-notfin-vs-bundled.md)。

- **Finalize decided_last_commit 不是已经 Process proposed_last_commit 不是已经是 Process proposed_last_commit：看见Finalize decided_last_commit 不是已经 Process proposed_last_commit，不是已经是 Process proposed_last_commit interchangeable / 1372 valuse-notfin interchangeable。**
- **Finalize decided_last_commit is not already Process proposed_last_commit 不是已经交差：看见Finalize decided_last_commit is not already Process proposed_last_commit，不是已经交差 interchangeable / 1372 valuse-notfin interchangeable。**
- **Finalize decided_last_commit 不是已经 Process proposed_last_commit 不是已经可以拿 Prepare Extended 代替：看见Finalize decided_last_commit 不是已经 Process proposed_last_commit，不是已经可以拿 Prepare Extended 代替 interchangeable / 1372 valuse-notfin interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（449 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
