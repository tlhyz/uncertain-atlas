# 模式：点名 valuse-notprep 杠

**层次**：实现 / ValUse Prepare ExtendedCommitInfo Validator not already Process-Finalize CommitInfo / not already interchangeable / not already 369-extract 正式三事（449 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage 句。  
**对应**：[`../tracks/implementation/worked-example-valuse-notprep-vs-bundled.md`](../tracks/implementation/worked-example-valuse-notprep-vs-bundled.md)。

- **Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo 不是已经是 Process/Finalize 的 CommitInfo：看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo，不是已经是 Process/Finalize 的 CommitInfo interchangeable / 1373 valuse-notprep interchangeable。**
- **Prepare ExtendedCommitInfo Validator is not already Process/Finalize CommitInfo 不是已经可以拿 CommitInfo 代替：看见Prepare ExtendedCommitInfo Validator is not already Process/Finalize CommitInfo，不是已经可以拿 CommitInfo 代替 interchangeable / 1373 valuse-notprep interchangeable。**
- **Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo 不是已经从块里抽出：看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo，不是已经从块里抽出 interchangeable / 1373 valuse-notprep interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（449 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
