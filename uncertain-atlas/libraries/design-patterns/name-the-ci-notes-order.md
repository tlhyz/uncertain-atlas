# 模式：把 CommitInfo Notes 票序正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Notes。  
**例**：[CommitInfo.votes 里的 VoteInfo 按投票权降序排 ≠ 已经进了块](../../tracks/implementation/worked-example-cinotes-vs-order.md)。

## 三个名字

1. **VoteInfo 按投票权降序排不是已经进了块 / 已经交差：** 看见顺序在不是已经写进 last_commit。
2. **引擎保证并落盘不是已经由应用排过 / 已经是收到票时的顺序：** 看见 CometBFT 保证不是应用自己排。
3. **从 store 再装不是已经从拟议块或已决块抽出 / 已经是 ExtendedCommitInfo Notes 同一句：** 看见 building CommitInfo 不是 interchangeable。

## 为什么要分开叫

官方把 CommitInfo Notes 里 votes 按投票权降序排、引擎保证并落盘、造 CommitInfo 时从 store 再装写成三个名字。把它们叫成一个「看见 Process / Finalize 里有 CommitInfo 就已经按投票权排好、已经从块里抽出」，会把 CommitInfo Notes 和 ExtendedCommitInfo Notes 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process / Finalize 里有 CommitInfo 就已经按投票权排好」，先数清问的是 VoteInfo 按投票权降序排不是已经进了块 / 已经交差、引擎保证并落盘不是已经由应用排过 / 已经是收到票时的顺序，还是造 CommitInfo 时从 store 再装不是已经从拟议块或已决块抽出 / 已经是 ExtendedCommitInfo Notes 同一句，再决定要不要同一次发布。
