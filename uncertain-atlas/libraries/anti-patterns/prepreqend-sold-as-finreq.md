# 反模式：看见 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根就当成已经是 Finalize 请求栏的 next_validators_hash / 看见 PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址就当成已经造了这份提案 / 看见 FinalizeBlockRequest.time 是已决块的时间戳就当成已经对上了拟议块头

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**例**：[PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是 Finalize 请求栏的 next_validators_hash](../../tracks/implementation/worked-example-prepreqend-vs-finreq.md)。

## 塌法

1. 看见 `PrepareProposalRequest.next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash，就当成已经是 Finalize 请求栏的 next_validators_hash，或当成已经换了人。
2. 看见 `PrepareProposalRequest.proposer_address` 是正在造这份提案的验证者地址 / 看见填了 proposer_address，就当成已经造了这份提案，或当成已经知道本头哈希。
3. 看见 `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 time，就当成已经对上了拟议块头，或当成已经是 PrepareProposalRequest.time。

## 为什么会出事

官方写：`next_validators_hash` 是下一验证者集合的默克尔根。`proposer_address` 是正在造这份提案的验证者地址。Finalize 请求 `time` 是已决块的时间戳。看见填了栏，不是已经是 Finalize 请求栏的 next_validators_hash，也不是已经造了这份提案，也不是已经对上了拟议块头。

## 和相邻反模式

- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根就已经是同一套字段，不是本页这种 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Finalize 请求栏的 next_validators_hash。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希，不是本页这种 PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址不是已经造了这份提案。
- [prepreqrest-sold-as-procreq](prepreqrest-sold-as-procreq.md) 是 PrepareProposalRequest.time 是将要提议那块的时间戳就已经对上了拟议块头，不是本页这种 FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头。
