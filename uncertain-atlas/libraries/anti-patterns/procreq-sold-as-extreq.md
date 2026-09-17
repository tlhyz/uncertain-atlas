# 反模式：看见 ProcessProposalRequest.txs 是拟议块的交易列表就当成已经执行那些交易 / 看见 ProcessProposalRequest.hash 是拟议块的哈希就当成已经跑过 Process / 看见 ProcessProposalRequest.height 是拟议块的高度就当成已经对上了拟议块头

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**例**：[ProcessProposalRequest.txs 是拟议块的交易列表 ≠ 已经执行那些交易](../../tracks/implementation/worked-example-procreq-vs-extreq.md)。

## 塌法

1. 看见 `ProcessProposalRequest.txs` 是拟议块的交易列表 / 看见填了 txs，就当成已经执行那些交易，或当成已经是 ExtendVoteRequest.txs。
2. 看见 `ProcessProposalRequest.hash` 是拟议块的哈希 / 看见填了 hash，就当成已经跑过 Process，或当成已经是 ExtendVoteRequest.hash。
3. 看见 `ProcessProposalRequest.height` 是拟议块的高度 / 看见填了 height，就当成已经对上了拟议块头，或当成已经是 ExtendVoteRequest.height。

## 为什么会出事

官方写：`txs` 是拟议块的交易列表。`hash` 是拟议块的哈希。`height` 是拟议块的高度。看见填了栏，不是已经执行那些交易，也不是已经跑过 Process，也不是已经对上了拟议块头。

## 和相邻反模式

- [extreqtxs-sold-as-fintxs](extreqtxs-sold-as-fintxs.md) 是 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表就已经执行那些交易，不是本页这种 ProcessProposalRequest.txs 是拟议块的交易列表不是已经执行那些交易。
- [extreqhash-sold-as-process](extreqhash-sold-as-process.md) 是 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希就已经跑过 Process，不是本页这种 ProcessProposalRequest.hash 是拟议块的哈希不是已经跑过 Process。
- [htmatch-sold-as-header](htmatch-sold-as-header.md) 是 Process 的 height / time 对上拟议块头就已经验过块头，不是本页这种 ProcessProposalRequest.height 是拟议块的高度不是已经对上了拟议块头。
