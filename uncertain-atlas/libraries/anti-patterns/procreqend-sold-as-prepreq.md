# 反模式：看见 ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根就当成已经是 Prepare 请求末栏的 next_validators_hash / 看见 ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址就当成已经正在造这份提案 / 看见 PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表就当成已经是初步交易列表

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**例**：[ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是 Prepare 请求末栏的 next_validators_hash](../../tracks/implementation/worked-example-procreqend-vs-prepreq.md)。

## 塌法

1. 看见 `ProcessProposalRequest.next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash，就当成已经是 Prepare 请求末栏的 next_validators_hash，或当成已经是 Finalize 请求栏的 next_validators_hash。
2. 看见 `ProcessProposalRequest.proposer_address` 是造了这份提案的验证者地址 / 看见填了 proposer_address，就当成已经正在造这份提案，或当成已经知道本头哈希。
3. 看见 `PrepareProposalResponse.txs` 是可能改过的、挑进拟议块的交易列表 / 看见回了 txs，就当成已经是初步交易列表，或当成已经保证是这一次。

## 为什么会出事

官方写：`next_validators_hash` 是下一验证者集合的默克尔根。`proposer_address` 是造了这份提案的验证者地址。Prepare 回包 `txs` 是可能改过的、挑进拟议块的交易列表。看见填了栏，不是已经是 Prepare 请求末栏的 next_validators_hash，也不是已经正在造这份提案，也不是已经是初步交易列表。

## 和相邻反模式

- [prepreqend-sold-as-finreq](prepreqend-sold-as-finreq.md) 是 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根就已经是 Finalize 请求栏的 next_validators_hash，不是本页这种 ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Prepare 请求末栏的 next_validators_hash。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希，不是本页这种 ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案。
- [prepreq-sold-as-return](prepreq-sold-as-return.md) 是 PrepareProposalRequest.txs 是挑进拟议块的初步交易列表就已经跑过 Process，不是本页这种 PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表不是已经是初步交易列表。
