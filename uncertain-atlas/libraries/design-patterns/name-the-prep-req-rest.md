# 模式：把 Prepare 请求余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**例**：[PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息 ≠ 已经交差 proposed_last_commit](../../tracks/implementation/worked-example-prepreqrest-vs-procreq.md)。

## 三个名字

1. **PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息不是已经交差 proposed_last_commit：** 看见填了 local_last_commit 不是已经是上一高度的预提交带扩展。
2. **PrepareProposalRequest.time 是将要提议那块的时间戳不是已经对上了拟议块头：** 看见填了 time 不是已经是 ProcessProposalRequest.time。
3. **PrepareProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩：** 看见填了 misbehavior 不是已经是 ProcessProposalRequest.misbehavior。

## 为什么要分开叫

官方把 PrepareProposal Request 表上 `local_last_commit` 是从本进程 CometBFT 数据结构拿到的上一份提交信息、`time` 是将要提议那块的时间戳、`misbehavior` 是过错验证者信息列表写成三件事。把它们叫成一个「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit」，会把已经交差 proposed_last_commit、已经对上了拟议块头和已经定奖惩一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit」，先数清问的是 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息不是已经交差 proposed_last_commit、PrepareProposalRequest.time 是将要提议那块的时间戳不是已经对上了拟议块头，还是 PrepareProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩，再决定要不要同一次发布。
