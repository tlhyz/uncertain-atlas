# 反模式：把 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed 正式三事卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled / 已经罚没 / 已经定奖惩完

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed ≠ bundled](../../tracks/implementation/worked-example-finreward-notslashed-vs-bundled.md)。

## 卖法

- 「看见应用可以用 FinalizeBlockRequest.decided_last_commit 和 misbehavior 定验证者奖惩 / 看见 can use 定奖惩 就已经 slashed interchangeable / 已经 determine rewards and punishments interchangeable / 已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable。」
- 「看见 rewards and punishments 就已经 VoteInfo block_id_flag 按到场定奖惩 interchangeable / 已经 365 VoteInfo 按到场定奖惩 interchangeable。」
- 「看见 can use 定奖惩 就已经 Finalize + Commit 交差 interchangeable / 已经四门已经结算 interchangeable / 已经定奖惩完 interchangeable。」

## 为什么错

官方把 can use decided_last_commit and misbehavior to determine rewards and punishments、VoteInfo 按到场定奖惩、Finalize + Commit 已经交差写成三件独立的实现事。把它们卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled、已经罚没、已经定奖惩完，会把 can use not slashed、can use not VoteInfo availability rewards、can use not already committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed 正式三事，必须分开 can use not already slashed、can use not VoteInfo availability rewards、can use not already committed 三个名字，不要把它们卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled / 已经罚没 / 已经定奖惩完。

## 和相邻反模式

- [finreward-sold-as-slashed](finreward-sold-as-slashed.md) 是 463 bundled 三事专用，不是本页 can use not already slashed 单句边界。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 按到场定奖惩，不是本页 can use vs VoteInfo availability 边界。
- [evidence-equals-slash](evidence-equals-slash.md) 是证据上链就已经罚没，不是本页 can use 定奖惩 边界。
