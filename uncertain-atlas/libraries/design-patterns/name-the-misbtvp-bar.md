# 模式：把 Misbehavior total_voting_power 栏正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**例**：[Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权 ≠ 已经 VoteInfo.validator.power](../../tracks/implementation/worked-example-misbtvp-vs-attendance.md)。

## 三个名字

1. **Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权不是已经 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权：** 看见集合总权不是已经单个验证者 power interchangeable。
2. **Misbehavior.total_voting_power 是 offense height 那一高的集合总权不是已经按到场定奖惩：** 看见集合总权不是已经 block_id_flag 奖罚完。
3. **Misbehavior.total_voting_power 不是已经定了奖惩：** 看见填了 total_voting_power 不是已经 slashed。

## 为什么要分开叫

官方把 Misbehavior 里 `total_voting_power` 栏写成三个名字。把它们叫成一个「看见 Misbehavior 里填了 total_voting_power 就已经按到场定奖惩」，会把集合总权、单个验证者 power、到场定奖惩一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior 里填了 total_voting_power 就已经按到场定奖惩」，先数清问的是 Misbehavior.total_voting_power 是不是已经 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权、Misbehavior.total_voting_power 是不是已经按到场定奖惩，还是 Misbehavior.total_voting_power 是不是已经定了奖惩，再决定要不要同一次发布。
