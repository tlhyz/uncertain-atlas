# 反模式：看见 ExtendedVoteInfo 按投票权降序排就当成已经进了块 / 看见 CometBFT 保证顺序就当成已经由应用排过 / 看见从 store 装回就当成已经从拟议块或已决块抽出

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedCommitInfo Notes。  
**例**：[ExtendedCommitInfo.votes 里的 ExtendedVoteInfo 按投票权降序排 ≠ 已经进了块](../../tracks/implementation/worked-example-extcinotes-vs-order.md)。

## 塌法

1. 看见 The `ExtendedVoteInfo` in `votes` are ordered by the voting power of the validators (descending order) / 看见顺序在，就当成已经进了块，或当成已经交差。
2. 看见 CometBFT guarantees the `votes` ordering through its logic to update the validator set / 看见 ordering is also persisted when a validator set is saved in the store，就当成已经由应用排过，或当成已经是收到票时的顺序。
3. 看见 The validator set is loaded from the store when building the `ExtendedCommitInfo` / 看见 ensuring order is maintained from the persisted validator set，就当成已经从拟议块或已决块抽出，或当成已经是 CommitInfo Notes 那套话就已经是同一句。

## 为什么会出事

官方写：`ExtendedCommitInfo.votes` 里的 `ExtendedVoteInfo` 按投票权降序排。CometBFT 通过更新验证者集合的逻辑保证这个顺序，集合写入 store 时顺序也落盘。造 `ExtendedCommitInfo` 时从 store 再装集合，好保住这份顺序。这不是已经进了块，不是已经由应用排过，也不是已经从拟议块或已决块抽出。看见 ExtendedCommitInfo Notes 票序正式三事，不是已经交差，不是已经是收到票时的顺序，不是已经可以用不变量 365 代替。

## 和相邻反模式

- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 按投票权降序排就已经进了块，不是本页这种 ExtendedCommitInfo Notes 路径。
- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，不是本页这种从 store 再装不是已经从拟议块或已决块抽出。
- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 ExtendedCommitInfo.round 是提交轮不是已经按投票权排过，不是本页这种 votes Notes 票序。
