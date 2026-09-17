# 模式：把 Finalize 请求余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**例**：[FinalizeBlockRequest.hash 是已决块的哈希 ≠ 已经是 ProcessProposalRequest.hash](../../tracks/implementation/worked-example-finreqrest-vs-procreq.md)。

## 三个名字

1. **FinalizeBlockRequest.hash 是已决块的哈希不是已经是 ProcessProposalRequest.hash：** 看见填了 hash 不是已经跑过 Process。
2. **FinalizeBlockRequest.misbehavior 是过错验证者信息列表不是已经定奖惩：** 看见填了 misbehavior 不是已经是 ProcessProposalRequest.misbehavior。
3. **FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Process 请求末栏的 next_validators_hash：** 看见填了 next_validators_hash 不是已经是 Prepare 请求末栏的 next_validators_hash。

## 为什么要分开叫

官方把 FinalizeBlock Request 表上 `hash` 是已决块的哈希、`misbehavior` 是过错验证者信息列表、`next_validators_hash` 是下一验证者集合默克尔根写成三件事。把它们叫成一个「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash」，会把已经是 ProcessProposalRequest.hash、已经定奖惩和已经是 Process 请求末栏的 next_validators_hash 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash」，先数清问的是 FinalizeBlockRequest.hash 是已决块的哈希不是已经是 ProcessProposalRequest.hash、FinalizeBlockRequest.misbehavior 是过错验证者信息列表不是已经定奖惩，还是 FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Process 请求末栏的 next_validators_hash，再决定要不要同一次发布。
