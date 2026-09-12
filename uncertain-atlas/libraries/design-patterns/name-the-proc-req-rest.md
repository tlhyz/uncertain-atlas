# 模式：把 Process 请求余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**例**：[ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 ≠ 已经交差 local_last_commit](../../tracks/implementation/worked-example-procreqrest-vs-extreq.md)。

## 三个名字

1. **ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息不是已经交差 local_last_commit：** 看见填了 proposed_last_commit 不是已经是 ExtendVoteRequest.proposed_last_commit。
2. **ProcessProposalRequest.time 是拟议块的时间戳不是已经验过票上时间：** 看见填了 time 不是已经是 ExtendVoteRequest.time。
3. **ProcessProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩：** 看见填了 misbehavior 不是已经是 ExtendVoteRequest.misbehavior。

## 为什么要分开叫

官方把 ProcessProposal Request 表上 `proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息、`time` 是拟议块的时间戳、`misbehavior` 是过错验证者信息列表写成三件事。把它们叫成一个「看见填了 Process 请求余栏就已经交差 local_last_commit」，会把已经交差 local_last_commit、已经验过票上时间和已经定奖惩一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Process 请求余栏就已经交差 local_last_commit」，先数清问的是 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息不是已经交差 local_last_commit、ProcessProposalRequest.time 是拟议块的时间戳不是已经验过票上时间，还是 ProcessProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩，再决定要不要同一次发布。
