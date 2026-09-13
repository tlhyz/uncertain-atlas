# 模式：把 FinalizeBlock decided_last_commit + misbehavior 定奖惩正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[can use decided_last_commit + misbehavior 定奖惩 ≠ 已经罚没](../../tracks/implementation/worked-example-finreward-vs-slashed.md)。

## 三个名字

1. **can use decided_last_commit 和 misbehavior 定奖惩不是已经罚没：** 看见 can use 不是已经交差。
2. **decided_last_commit 从刚决定那块拿到不是已经 proposed_last_commit：** 看见 decided block commit 不是已经交差 local_last_commit。
3. **misbehavior 过错列表不是已经 VoteInfo 按到场定奖惩：** 看见 misbehavior 不是已经 Misbehavior.type 就已经 slashed。

## 为什么要分开叫

官方把 can use decided_last_commit and misbehavior to determine rewards and punishments、decided_last_commit from decided block、misbehavior 过错验证者信息列表写成三个名字。把它们叫成一个「看见 Finalize 里有 decided_last_commit 和 misbehavior 就已经罚没」，会把能定奖惩、decided vs proposed commit 和 VoteInfo 到场三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有 misbehavior 就已经罚没」，先数清问的是 can use decided_last_commit 和 misbehavior 定奖惩是不是已经罚没、decided_last_commit 从刚决定那块拿到是不是已经 proposed_last_commit，还是 misbehavior 过错列表是不是已经 VoteInfo 按到场定奖惩，再决定要不要同一次发布。
