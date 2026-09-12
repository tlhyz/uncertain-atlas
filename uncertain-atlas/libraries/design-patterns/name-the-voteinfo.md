# 模式：把 VoteInfo 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**例**：[VoteInfo 能按到场定奖惩 ≠ 已经罚没](../../tracks/implementation/worked-example-voteinfo-vs-reward.md)。

## 三个名字

1. **VoteInfo 能按到场定奖惩不是已经罚没：** 看见有 `block_id_flag` 不是已经交差。
2. **从拟议块或已决块抽出不是已经带了公钥：** 看见有 `VoteInfo.validator` 不是已经是 ValidatorUpdate。
3. **按投票权降序排不是已经进了块：** 看见从 store 再装不是已经交差。

## 为什么要分开叫

官方把 `VoteInfo` 标明上一块有没有签、从拟议块或已决块抽出、`votes` 按投票权降序排并从 store 再装写成三件事。把它们叫成一个「看见 CommitInfo 里有票就已经罚没」，会把回包义务、Validator 类型和本地 State 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 CommitInfo 里有票就已经罚没」，先数清问的是 VoteInfo 能按到场定奖惩不是已经罚没、从拟议块或已决块抽出不是已经带了公钥，还是按投票权降序排不是已经进了块，再决定要不要同一次发布。
