# 模式：把 FinalizeBlock misbehavior not VoteInfo availability 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock misbehavior not VoteInfo availability ≠ bundled](../../tracks/implementation/worked-example-finmisbeh-notvoteinfo-vs-bundled.md)。

## 三个名字

1. **misbehavior fault list not VoteInfo availability rewards 不是 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled：** 看见 misbehavior 过错列表不是已经 VoteInfo block_id_flag 按到场定奖惩，不是 463 bundled interchangeable / 365 VoteInfo 按到场定奖惩 interchangeable / 440 ExtendedVoteInfo 暴露签 interchangeable。
2. **misbehavior fault list not ProcessProposal misbehavior already定奖惩 不是 420 Process 请求余栏：** 看见 Finalize misbehavior 不是已经 ProcessProposalRequest.misbehavior 已经定奖惩，不是 463 bundled interchangeable / 420 Process 请求余栏 interchangeable / 428 Finalize 请求余栏 interchangeable。
3. **misbehavior fault list not Misbehavior.type already slashed 不是 372 / 447 枚举：** 看见 misbehavior 过错列表不是已经 Misbehavior.type 就已经 slashed，不是 463 bundled interchangeable / 372 枚举 interchangeable / 21 证据上链 interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock misbehavior not VoteInfo availability 写成三个名字。把它们叫成一个「看见 misbehavior 过错列表 就已经 VoteInfo 按到场定奖惩 / 已经定奖惩 / 已经 slashed」，会把 misbehavior vs VoteInfo 按到场定奖惩、misbehavior vs Process misbehavior already定奖惩、misbehavior vs Misbehavior.type slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock misbehavior not VoteInfo availability 正式三事，先数清问的是 misbehavior fault list 是不是 VoteInfo availability rewards、misbehavior fault list 是不是 ProcessProposal misbehavior already定奖惩、misbehavior fault list 是不是 Misbehavior.type already slashed，再决定要不要同一次发布。
