# 反模式：把 FinalizeBlock decided_last_commit + misbehavior 定奖惩正式三事说成已经罚没

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[can use decided_last_commit + misbehavior 定奖惩 ≠ 已经罚没](../../tracks/implementation/worked-example-finreward-vs-slashed.md)。

## 错在哪里

把 The Application can use decided_last_commit and misbehavior to determine rewards and punishments 写成已经罚没，或已经定奖惩完；把 decided_last_commit from decided block 写成已经 ProcessProposalRequest.proposed_last_commit，或已经交差 local_last_commit；把 FinalizeBlockRequest.misbehavior 写成已经 VoteInfo 按到场定奖惩，或已经 Misbehavior.type 就已经 slashed，或已经和 363 / 422 / 365 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock decided_last_commit + misbehavior 定奖惩正式三事，必须分开 can use 定奖惩、decided_last_commit 从刚决定那块拿到、misbehavior 过错列表三件事，不要和 363 / 422 / 365 / 372 / 21 糊成一句。
