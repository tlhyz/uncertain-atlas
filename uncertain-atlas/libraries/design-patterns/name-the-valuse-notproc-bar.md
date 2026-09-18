# 模式：点名 valuse-notproc 杠

**层次**：实现 / ValUse Process CommitInfo Validator not already Prepare ExtendedCommitInfo / not already local_last_commit / not already 364-pubkey 正式三事（449 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage 句。  
**对应**：[`../tracks/implementation/worked-example-valuse-notproc-vs-bundled.md`](../tracks/implementation/worked-example-valuse-notproc-vs-bundled.md)。

- **Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo 不是已经是 Prepare 的 ExtendedCommitInfo：看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo，不是已经是 Prepare 的 ExtendedCommitInfo interchangeable / 1371 valuse-notproc interchangeable。**
- **Process CommitInfo Validator is not already Prepare ExtendedCommitInfo 不是已经是 local_last_commit 同一份：看见Process CommitInfo Validator is not already Prepare ExtendedCommitInfo，不是已经是 local_last_commit 同一份 interchangeable / 1371 valuse-notproc interchangeable。**
- **Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo 不是已经带了公钥：看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo，不是已经带了公钥 interchangeable / 1371 valuse-notproc interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（449 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
