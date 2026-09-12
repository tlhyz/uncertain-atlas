# 反模式：看见 FinalizeBlockRequest.hash 是已决块的哈希就当成已经是 ProcessProposalRequest.hash / 看见 FinalizeBlockRequest.misbehavior 是过错验证者信息列表就当成已经定奖惩 / 看见 FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根就当成已经是 Process 请求末栏的 next_validators_hash

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**例**：[FinalizeBlockRequest.hash 是已决块的哈希 ≠ 已经是 ProcessProposalRequest.hash](../../tracks/implementation/worked-example-finreqrest-vs-procreq.md)。

## 塌法

1. 看见 `FinalizeBlockRequest.hash` 是已决块的哈希 / 看见填了 hash，就当成已经是 ProcessProposalRequest.hash，或当成已经跑过 Process。
2. 看见 `FinalizeBlockRequest.misbehavior` 是过错验证者信息列表 / 看见填了 misbehavior，就当成已经定奖惩，或当成已经是 ProcessProposalRequest.misbehavior。
3. 看见 `FinalizeBlockRequest.next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash，就当成已经是 Process 请求末栏的 next_validators_hash，或当成已经是 Prepare 请求末栏的 next_validators_hash。

## 为什么会出事

官方写：`hash` 是已决块的哈希。`misbehavior` 是过错验证者信息列表。`next_validators_hash` 是下一验证者集合的默克尔根。看见填了栏，不是已经是 ProcessProposalRequest.hash，也不是已经定奖惩，也不是已经是 Process 请求末栏的 next_validators_hash。

## 和相邻反模式

- [procreq-sold-as-extreq](procreq-sold-as-extreq.md) 是 ProcessProposalRequest.hash 是拟议块的哈希就已经跑过 Process，不是本页这种 FinalizeBlockRequest.hash 是已决块的哈希不是已经是 ProcessProposalRequest.hash。
- [procreqrest-sold-as-extreq](procreqrest-sold-as-extreq.md) 是 ProcessProposalRequest.misbehavior 是过错验证者信息列表就已经定奖惩，不是本页这种 FinalizeBlockRequest.misbehavior 是过错验证者信息列表不是已经定奖惩。
- [procreqend-sold-as-prepreq](procreqend-sold-as-prepreq.md) 是 ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Prepare 请求末栏的 next_validators_hash，不是本页这种 FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Process 请求末栏的 next_validators_hash。
