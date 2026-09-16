# 模式：把 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed ≠ bundled](../../tracks/implementation/worked-example-finreward-notslashed-vs-bundled.md)。

## 三个名字

1. **can use decided_last_commit + misbehavior to determine rewards not already slashed 不是 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled：** 看见 can use 定奖惩不是已经 slashed，不是 463 bundled interchangeable / 363 回包义务 interchangeable / 21 证据上链 interchangeable。
2. **can use not VoteInfo availability rewards 不是 365 VoteInfo 按到场定奖惩：** 看见 rewards and punishments 不是已经 VoteInfo block_id_flag 按到场定奖惩，不是 463 bundled interchangeable / 365 VoteInfo 按到场定奖惩 interchangeable / 440 ExtendedVoteInfo 暴露签 interchangeable。
3. **can use not already committed 不是 Finalize + Commit 交差：** 看见 determine rewards and punishments 不是已经四门已经结算 / 已经交差，不是 463 bundled interchangeable / 586 ABCI 1.0 equiv interchangeable / 555 Contains newly decided not settled interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed 写成三个名字。把它们叫成一个「看见 can use 定奖惩就已经 slashed」，会把 can use vs slashed、can use vs VoteInfo 按到场定奖惩、can use vs 已经交差 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed 正式三事，先数清问的是 can use 定奖惩 是不是 already slashed、can use 定奖惩 是不是 VoteInfo availability rewards、can use 定奖惩 是不是 already committed，再决定要不要同一次发布。
