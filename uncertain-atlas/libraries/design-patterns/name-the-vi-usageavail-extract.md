# 模式：把 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo Usage / ExtendedVoteInfo Usage。  
**例**：[VoteInfo 与 ExtendedVoteInfo Usage 都写 allowing for rewards based on validator availability ≠ 已经奖罚完](../../tracks/implementation/worked-example-viusageavail-vs-extractpath.md)。

## 三个名字

1. **availability 同句不是已经奖罚完 / 已经交差：** 看见能按到场定奖惩不是已经算完。
2. **VoteInfo typically from proposed or decided block 不是已经从本进程抽出 / 已经是 Prepare 里的 ExtendedVoteInfo：** 看见 Process/Finalize 路径不是 Prepare 路径。
3. **ExtendedVoteInfo from local process 不是已经 typically from block / 已经是 CommitInfo 同一路：** 看见 extracted from local process 不是 interchangeable。

## 为什么要分开叫

官方把 VoteInfo 与 ExtendedVoteInfo Usage 里同一句 availability 和两条不同抽取路径写成三个名字。把它们叫成一个「看见 block_id_flag 就已经奖罚完、Prepare 和 Process 是同一路」，会把 VoteInfo typically from block 和 ExtendedVoteInfo from local process 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 block_id_flag 就已经奖罚完」，先数清问的是 availability 同句不是已经奖罚完 / 已经交差、VoteInfo 通常从拟议块或已决块抽出不是已经从本进程抽出 / 已经是 Prepare 里的 ExtendedVoteInfo，还是 ExtendedVoteInfo 从本进程 CometBFT 数据结构抽出不是已经 typically extracted from proposed or decided block / 已经是 Process/Finalize 里的 CommitInfo 同一路，再决定要不要同一次发布。
