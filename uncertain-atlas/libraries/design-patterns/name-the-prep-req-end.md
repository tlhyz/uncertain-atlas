# 模式：把 Prepare 请求末栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**例**：[PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是 Finalize 请求栏的 next_validators_hash](../../tracks/implementation/worked-example-prepreqend-vs-finreq.md)。

## 三个名字

1. **PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Finalize 请求栏的 next_validators_hash：** 看见填了 next_validators_hash 不是已经换了人。
2. **PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址不是已经造了这份提案：** 看见填了 proposer_address 不是已经知道本头哈希。
3. **FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头：** 看见填了 time 不是已经是 PrepareProposalRequest.time。

## 为什么要分开叫

官方把 PrepareProposal Request 表上 `next_validators_hash` 是下一验证者集合默克尔根、`proposer_address` 是正在造这份提案的验证者地址、FinalizeBlock Request 表上 `time` 是已决块的时间戳写成三件事。把它们叫成一个「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash」，会把已经是 Finalize 请求栏的 next_validators_hash、已经造了这份提案和已经对上了拟议块头一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash」，先数清问的是 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Finalize 请求栏的 next_validators_hash、PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址不是已经造了这份提案，还是 FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头，再决定要不要同一次发布。
