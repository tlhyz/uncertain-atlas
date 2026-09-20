# 反模式：看见 Process 里的 CommitInfo 就当成已经是 Prepare 里的 ExtendedCommitInfo / 看见 Finalize 里的 decided_last_commit 就当成已经是 Process 里的 proposed_last_commit / 看见 Prepare 里的 ExtendedCommitInfo 就当成已经和 CommitInfo 同一路

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage。  
**例**：[Validator 装在 CommitInfo 里用于 ProcessProposal ≠ 已经 PrepareProposal 里的 ExtendedCommitInfo](../../tracks/implementation/worked-example-validatorusage-vs-gates.md)。

## 塌法

1. 看见 Used as part of `VoteInfo` within `CommitInfo` (used in `ProcessProposal` / 看见 Process 路径，就当成已经是 `PrepareProposal` 里的 `ExtendedCommitInfo`，或当成已经是 `local_last_commit` 同一份。
2. 看见 `CommitInfo` also used in `FinalizeBlock` / 看见 `decided_last_commit`，就当成已经是 Process 里的 `proposed_last_commit` 同一路，或当成已经是 decided 就已经交差。
3. 看见 Used as part of `ExtendedCommitInfo` (used in `PrepareProposal` / 看见 Prepare 路径，就当成已经是 Process/Finalize 里的 `CommitInfo` 同一路，或当成已经可以拿 `CommitInfo` 代替 `ExtendedCommitInfo`。

## 为什么会出事

官方写：`Validator` 装在 `VoteInfo`/`CommitInfo` 给 Process 和 Finalize。装在 `ExtendedCommitInfo` 给 Prepare。Process 走 `proposed_last_commit`，Finalize 走 `decided_last_commit`，Prepare 走 `local_last_commit`。这不是已经同一门，不是已经同一路，不是已经 interchangeable。看见 Validator Usage 四门映射正式三事，不是已经带了公钥，不是已经从块里抽出，不是已经可以用不变量 364 代替本页。

## 和相邻反模式

- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 用 address 认人就已经带了公钥，不是本页这种 Process 的 CommitInfo 不是已经 Prepare 的 ExtendedCommitInfo。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 能按到场定奖惩就已经罚没，不是本页这种 Finalize 的 decided_last_commit 不是已经 Process 的 proposed_last_commit。
- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，不是本页这种 Prepare 的 ExtendedCommitInfo 不是已经 Process/Finalize 的 CommitInfo。
