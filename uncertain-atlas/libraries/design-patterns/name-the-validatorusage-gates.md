# 模式：把 Validator Usage 四门映射正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage。  
**例**：[Validator 装在 CommitInfo 里用于 ProcessProposal ≠ 已经 PrepareProposal 里的 ExtendedCommitInfo](../../tracks/implementation/worked-example-validatorusage-vs-gates.md)。

## 三个名字

1. **Process 的 CommitInfo 不是已经 Prepare 的 ExtendedCommitInfo / 已经是 local_last_commit 同一份：** 看见 Process 路径不是 Prepare 路径。
2. **Finalize 的 decided_last_commit 不是已经 Process 的 proposed_last_commit / 已经是 decided 就已经交差：** 看见已决路径不是拟议路径。
3. **Prepare 的 ExtendedCommitInfo 不是已经 Process/Finalize 的 CommitInfo / 已经可以 interchangeable：** 看见 Extended 结构不是 VoteInfo/CommitInfo 同一路。

## 为什么要分开叫

官方把 `Validator` 装进 `VoteInfo`/`CommitInfo` 给 Process 和 Finalize、装进 `ExtendedCommitInfo` 给 Prepare，写成三个名字。把它们叫成一个「看见四门里都有 Validator 就已经同一门」，会把 Process 的 `CommitInfo` 和 Prepare 的 `ExtendedCommitInfo` 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare / Process / Finalize 里都有验证者就已经同一门」，先数清问的是 Process 的 CommitInfo 不是已经 Prepare 的 ExtendedCommitInfo / 已经是 local_last_commit 同一份，还是 Finalize 的 decided_last_commit 不是已经 Process 的 proposed_last_commit / 已经是 decided 就已经交差，还是 Prepare 的 ExtendedCommitInfo 不是已经 Process/Finalize 的 CommitInfo / 已经可以 interchangeable，再决定要不要同一次发布。
