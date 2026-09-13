# 反模式：看见 availability 同句就当成已经奖罚完 / 看见 VoteInfo typically from block 就当成已经从本进程抽出 / 看见 ExtendedVoteInfo from local process 就当成已经和 CommitInfo 同一路

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo Usage / ExtendedVoteInfo Usage。  
**例**：[VoteInfo 与 ExtendedVoteInfo Usage 都写 allowing for rewards based on validator availability ≠ 已经奖罚完](../../tracks/implementation/worked-example-viusageavail-vs-extractpath.md)。

## 塌法

1. 看见 Indicates whether a validator signed the last block, allowing for rewards based on validator availability / 看见同一句，就当成已经奖罚完，或当成已经交差。
2. 看见 This information is typically extracted from a proposed or decided block / 看见 typically extracted，就当成已经从本进程 CometBFT 数据结构抽出，或当成已经是 Prepare 里的 ExtendedVoteInfo。
3. 看见 This information is extracted from CometBFT's data structures in the local process / 看见 extracted from local process，就当成已经 typically extracted from proposed or decided block，或当成已经是 Process/Finalize 里的 CommitInfo 同一路。

## 为什么会出事

官方写：VoteInfo 与 ExtendedVoteInfo Usage 都写 allowing for rewards based on validator availability。VoteInfo 通常从拟议块或已决块抽出。ExtendedVoteInfo 从本进程 CometBFT 数据结构抽出。这不是已经奖罚完，不是已经从本进程抽出（对 VoteInfo 路径），也不是已经和 CommitInfo 同一路（对 ExtendedVoteInfo 路径）。看见 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事，不是已经交差，不是已经 Prepare 和 Process 同一路，不是已经 interchangeable。

## 和相邻反模式

- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 能按到场定奖惩就已经罚没，不是本页这种 availability 同句不是已经奖罚完。
- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，不是本页这种 from local process 不是已经 typically from block。
- [extvirest-sold-as-voteinfo](extvirest-sold-as-voteinfo.md) 是 ExtendedVoteInfo.block_id_flag 表栏就已经罚没，不是本页这种 availability 同句不是已经奖罚完。
