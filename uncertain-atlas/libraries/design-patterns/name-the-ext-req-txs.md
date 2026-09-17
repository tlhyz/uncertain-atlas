# 模式：把 ExtendVote 请求余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**例**：[ExtendVoteRequest.txs 是扩展要指的那份块的交易列表 ≠ 已经执行那些交易](../../tracks/implementation/worked-example-extreqtxs-vs-fintxs.md)。

## 三个名字

1. **ExtendVoteRequest.txs 是扩展要指的那份块的交易列表不是已经执行那些交易：** 看见填了 txs 不是已经交差。
2. **ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息不是已经交差 local_last_commit：** 看见填了 proposed_last_commit 不是已经跑过 Process。
3. **ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希不是已经是 Finalize 请求栏的 next_validators_hash：** 看见填了 next_validators_hash 不是已经换了人。

## 为什么要分开叫

官方把 `txs` 是扩展要指的那份块的交易列表、`proposed_last_commit` 是上一份拟议块的 last commit 信息、`next_validators_hash` 是下一份验证者集合的哈希写成三件事。把它们叫成一个「看见填了 ExtendVote 请求余栏就已经执行那些交易」，会把已经执行那些交易、已经交差 local_last_commit 和已经是 Finalize 请求栏的 next_validators_hash 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求余栏就已经执行那些交易」，先数清问的是 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表不是已经执行那些交易、ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息不是已经交差 local_last_commit，还是 ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希不是已经是 Finalize 请求栏的 next_validators_hash，再决定要不要同一次发布。
