# 模式：把 ExtendedCommitInfo Notes 票序正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedCommitInfo Notes。  
**例**：[ExtendedCommitInfo.votes 里的 ExtendedVoteInfo 按投票权降序排 ≠ 已经进了块](../../tracks/implementation/worked-example-extcinotes-vs-order.md)。

## 三个名字

1. **ExtendedVoteInfo 按投票权降序排不是已经进了块 / 已经交差：** 看见顺序在不是已经写进 last_commit。
2. **CometBFT 通过更新验证者集合的逻辑保证这个顺序、集合写入 store 时顺序也落盘不是已经由应用排过 / 已经是收到票时的顺序：** 看见引擎保证并落盘不是已经由 Prepare 回包决定。
3. **造 ExtendedCommitInfo 时从 store 再装集合不是已经从拟议块或已决块抽出 / 已经是 CommitInfo Notes 那套话就已经是同一句：** 看见从 store 装回不是已经是 VoteInfo 从块里抽出那种路径。

## 为什么要分开叫

官方把 ExtendedCommitInfo Notes 里 votes 按投票权降序排、引擎保证并落盘、从 store 再装写成三个名字。把它们叫成一个「看见 Prepare 里有 ExtendedCommitInfo 就已经按投票权排好、已经进了块、已经从块里抽出」，会把已经由应用排过、已经从拟议块或已决块抽出和已经可以用不变量 365 代替一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare 里有 ExtendedCommitInfo 就已经按投票权排好」，先数清问的是 ExtendedVoteInfo 按投票权降序排不是已经进了块 / 已经交差、CometBFT 通过更新验证者集合的逻辑保证这个顺序、集合写入 store 时顺序也落盘不是已经由应用排过 / 已经是收到票时的顺序，还是造 ExtendedCommitInfo 时从 store 再装集合不是已经从拟议块或已决块抽出 / 已经是 CommitInfo Notes 那套话就已经是同一句，再决定要不要同一次发布。
