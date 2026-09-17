# 反模式：看见 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息就当成已经交差 proposed_last_commit / 看见 PrepareProposalRequest.time 是将要提议那块的时间戳就当成已经对上了拟议块头 / 看见 PrepareProposalRequest.misbehavior 是过错验证者信息列表就当成已经定奖惩

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**例**：[PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息 ≠ 已经交差 proposed_last_commit](../../tracks/implementation/worked-example-prepreqrest-vs-procreq.md)。

## 塌法

1. 看见 `PrepareProposalRequest.local_last_commit` 是从本进程 CometBFT 数据结构拿到的上一份提交信息 / 看见填了 local_last_commit，就当成已经交差 proposed_last_commit，或当成已经是上一高度的预提交带扩展。
2. 看见 `PrepareProposalRequest.time` 是将要提议那块的时间戳 / 看见填了 time，就当成已经对上了拟议块头，或当成已经是 ProcessProposalRequest.time。
3. 看见 `PrepareProposalRequest.misbehavior` 是过错验证者信息列表 / 看见填了 misbehavior，就当成已经定奖惩，或当成已经是 ProcessProposalRequest.misbehavior。

## 为什么会出事

官方写：`local_last_commit` 是上一份提交信息，从本进程 CometBFT 数据结构拿到。`time` 是将要提议那块的时间戳。`misbehavior` 是过错验证者信息列表。看见填了栏，不是已经交差 proposed_last_commit，也不是已经对上了拟议块头，也不是已经定奖惩。

## 和相邻反模式

- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展，不是本页这种 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息不是已经交差 proposed_last_commit。
- [procreqrest-sold-as-extreq](procreqrest-sold-as-extreq.md) 是 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit，不是本页这种 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息不是已经交差 proposed_last_commit。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就已经定奖惩，不是本页这种 PrepareProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩。
