# 反模式：把 FinalizeBlock misbehavior not VoteInfo availability 正式三事卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled / 已经 VoteInfo 按到场定奖惩 / 已经 Misbehavior.type 就已经罚没

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock misbehavior not VoteInfo availability ≠ bundled](../../tracks/implementation/worked-example-finmisbeh-notvoteinfo-vs-bundled.md)。

## 卖法

- 「看见 FinalizeBlockRequest.misbehavior 是过错验证者信息列表 / 看见 misbehavior 过错列表 就已经 VoteInfo block_id_flag 按到场定奖惩 interchangeable / 已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable。」
- 「看见 misbehavior 过错列表 就已经 ProcessProposalRequest.misbehavior 已经定奖惩 interchangeable / 已经 Process 请求余栏 interchangeable。」
- 「看见 misbehavior 过错列表 就已经 Misbehavior.type 就已经 slashed interchangeable / 已经过错枚举 interchangeable / 已经罚没 interchangeable。」

## 为什么错

官方把 Finalize 请求表上 misbehavior 过错列表、VoteInfo / ExtendedVoteInfo Usage 按到场定奖惩、Process 请求表上 misbehavior、Misbehavior.type 只是过错枚举写成三件独立的实现事。把它们卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled、已经 VoteInfo 按到场定奖惩、已经 Misbehavior.type 就已经罚没，会把 misbehavior not VoteInfo availability rewards、misbehavior not ProcessProposal misbehavior already定奖惩、misbehavior not Misbehavior.type already slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock misbehavior not VoteInfo availability 正式三事，必须分开 misbehavior not VoteInfo availability rewards、misbehavior not ProcessProposal misbehavior already定奖惩、misbehavior not Misbehavior.type already slashed 三个名字，不要把它们卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled / 已经 VoteInfo 按到场定奖惩 / 已经 Misbehavior.type 就已经罚没。

## 和相邻反模式

- [finreward-sold-as-slashed](finreward-sold-as-slashed.md) 是 463 bundled 三事专用，不是本页 misbehavior vs VoteInfo 按到场定奖惩 单句边界。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 按到场定奖惩，不是本页 misbehavior vs VoteInfo availability 边界。
- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 Misbehavior.type 枚举，不是本页 misbehavior 过错列表 vs 已经 slashed 边界。
