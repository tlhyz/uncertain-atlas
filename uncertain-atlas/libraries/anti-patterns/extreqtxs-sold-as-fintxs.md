# 反模式：看见 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表就当成已经执行那些交易 / 看见 ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息就当成已经交差 local_last_commit / 看见 ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希就当成已经是 Finalize 请求栏的 next_validators_hash

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**例**：[ExtendVoteRequest.txs 是扩展要指的那份块的交易列表 ≠ 已经执行那些交易](../../tracks/implementation/worked-example-extreqtxs-vs-fintxs.md)。

## 塌法

1. 看见 `ExtendVoteRequest.txs` 是扩展要指的那份块的交易列表 / 看见填了 txs，就当成已经执行那些交易，或当成已经交差。
2. 看见 `ExtendVoteRequest.proposed_last_commit` 是上一份拟议块的 last commit 信息 / 看见填了 proposed_last_commit，就当成已经交差 local_last_commit，或当成已经跑过 Process。
3. 看见 `ExtendVoteRequest.next_validators_hash` 是下一份验证者集合的哈希 / 看见填了 next_validators_hash，就当成已经是 Finalize 请求栏的 next_validators_hash，或当成已经换了人。

## 为什么会出事

官方写：`txs` 是扩展要指的那份块的交易列表。`proposed_last_commit` 是上一份拟议块的 last commit 信息。`next_validators_hash` 是下一份验证者集合的哈希。看见填了栏，不是已经执行那些交易，也不是已经交差 local_last_commit，也不是已经是 Finalize 请求栏的 next_validators_hash。

## 和相邻反模式

- [fintxs-sold-as-control](fintxs-sold-as-control.md) 是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差，不是本页这种 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表不是已经执行那些交易。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process，不是本页这种 ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息不是已经交差 local_last_commit。
- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 Finalize 请求 next_validators_hash 就已经是同一套字段，不是本页这种 ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希不是已经是 Finalize 请求栏的 next_validators_hash。
