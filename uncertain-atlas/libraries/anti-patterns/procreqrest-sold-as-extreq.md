# 反模式：看见 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就当成已经交差 local_last_commit / 看见 ProcessProposalRequest.time 是拟议块的时间戳就当成已经验过票上时间 / 看见 ProcessProposalRequest.misbehavior 是过错验证者信息列表就当成已经定奖惩

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**例**：[ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 ≠ 已经交差 local_last_commit](../../tracks/implementation/worked-example-procreqrest-vs-extreq.md)。

## 塌法

1. 看见 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息 / 看见填了 proposed_last_commit，就当成已经交差 local_last_commit，或当成已经是 ExtendVoteRequest.proposed_last_commit。
2. 看见 `ProcessProposalRequest.time` 是拟议块的时间戳 / 看见填了 time，就当成已经验过票上时间，或当成已经是 ExtendVoteRequest.time。
3. 看见 `ProcessProposalRequest.misbehavior` 是过错验证者信息列表 / 看见填了 misbehavior，就当成已经定奖惩，或当成已经是 ExtendVoteRequest.misbehavior。

## 为什么会出事

官方写：`proposed_last_commit` 是上一份提交信息，从拟议块里的信息拿到。`time` 是拟议块的时间戳。`misbehavior` 是过错验证者信息列表。看见填了栏，不是已经交差 local_last_commit，也不是已经验过票上时间，也不是已经定奖惩。

## 和相邻反模式

- [extreqtxs-sold-as-fintxs](extreqtxs-sold-as-fintxs.md) 是 ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息就已经交差 local_last_commit，不是本页这种 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息不是已经交差 local_last_commit。
- [extreqhash-sold-as-process](extreqhash-sold-as-process.md) 是 ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳就已经验过票上时间，不是本页这种 ProcessProposalRequest.time 是拟议块的时间戳不是已经验过票上时间。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就已经定奖惩，不是本页这种 ProcessProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩。
