# 反模式：看见 CommitInfo.votes 按投票权降序排就当成已经进了块 / 看见引擎保证并落盘就当成已经由应用排过 / 看见从 store 再装就当成已经从拟议块或已决块抽出

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Notes。  
**例**：[CommitInfo.votes 里的 VoteInfo 按投票权降序排 ≠ 已经进了块](../../tracks/implementation/worked-example-cinotes-vs-order.md)。

## 塌法

1. 看见 The `VoteInfo` in `votes` are ordered by the voting power of the validators descending order / 看见按投票权降序排，就当成已经进了块，或当成已经交差。
2. 看见 CometBFT guarantees the `votes` ordering through its logic to update the validator set / 看见 The ordering is also persisted when a validator set is saved in the store，就当成已经由应用排过，或当成已经是收到票时的顺序。
3. 看见 The validator set is loaded from the store when building the `CommitInfo` / 看见 ensuring order is maintained from the persisted validator set，就当成已经从拟议块或已决块抽出，或当成已经是 ExtendedCommitInfo Notes 那套话就已经是同一句。

## 为什么会出事

官方写：`CommitInfo.votes` 里的 `VoteInfo` 按投票权降序排。CometBFT 通过更新验证者集合的逻辑保证这个顺序，集合写入 store 时顺序也落盘。造 `CommitInfo` 时从 store 再装集合，好保住这份顺序。这不是已经进了块，不是已经由应用排过，也不是已经从拟议块或已决块抽出。看见 CommitInfo Notes 票序正式三事，不是已经交差，不是已经是 ExtendedCommitInfo Notes  interchangeable，不是已经可以用不变量 365 代替。

## 和相邻反模式

- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 能按到场定奖惩就已经罚没，不是本页这种 VoteInfo 按投票权降序排不是已经进了块。
- [extcinotes-sold-as-inblock](extcinotes-sold-as-inblock.md) 是 ExtendedCommitInfo Notes 路径，不是本页这种 CommitInfo Notes 从 store 再装不是已经从块里抽出。
- [validatorusage-sold-as-samegate](validatorusage-sold-as-samegate.md) 是四门 Validator 映射，不是本页这种 CommitInfo Notes 票序。
