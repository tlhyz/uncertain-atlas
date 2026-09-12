# 模式：把 Process 请求末栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**例**：[ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是 Prepare 请求末栏的 next_validators_hash](../../tracks/implementation/worked-example-procreqend-vs-prepreq.md)。

## 三个名字

1. **ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Prepare 请求末栏的 next_validators_hash：** 看见填了 next_validators_hash 不是已经是 Finalize 请求栏的 next_validators_hash。
2. **ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案：** 看见填了 proposer_address 不是已经知道本头哈希。
3. **PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表不是已经是初步交易列表：** 看见回了 txs 不是已经保证是这一次。

## 为什么要分开叫

官方把 ProcessProposal Request 表上 `next_validators_hash` 是下一验证者集合默克尔根、`proposer_address` 是造了这份提案的验证者地址、PrepareProposal Response 表上 `txs` 是可能改过的、挑进拟议块的交易列表写成三件事。把它们叫成一个「看见填了 Process 请求末栏就已经是 Prepare 请求末栏的 next_validators_hash」，会把已经是 Prepare 请求末栏的 next_validators_hash、已经正在造这份提案和已经是初步交易列表一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Process 请求末栏就已经是 Prepare 请求末栏的 next_validators_hash」，先数清问的是 ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Prepare 请求末栏的 next_validators_hash、ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案，还是 PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表不是已经是初步交易列表，再决定要不要同一次发布。
