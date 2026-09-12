# 模式：把 Misbehavior 类型三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**例**：[Misbehavior.type 只是过错枚举 ≠ 已经罚没](../../tracks/implementation/worked-example-misbehavior-vs-enum.md)。

## 三个名字

1. **Misbehavior.type 只是过错枚举不是已经罚没：** 看见有类型不是已经定了奖惩。
2. **height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间：** 看见有时间不是已经交差。
3. **total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩：** 看见有总权不是已经改了集合。

## 为什么要分开叫

官方把 `Misbehavior.type` 只是过错枚举、`height` 是过错发生的高度、`time` 是那一高已提交块的时间、`total_voting_power` 是那一高验证者集合的总权写成三件事。把它们叫成一个「看见有 Misbehavior 就已经罚没」，会把证据上链、票上时间和 VoteInfo 到场一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有 Misbehavior 就已经罚没」，先数清问的是 Misbehavior.type 只是过错枚举不是已经罚没、height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间，还是 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩，再决定要不要同一次发布。
