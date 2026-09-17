# 模式：把 Process 请求栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**例**：[ProcessProposalRequest.txs 是拟议块的交易列表 ≠ 已经执行那些交易](../../tracks/implementation/worked-example-procreq-vs-extreq.md)。

## 三个名字

1. **ProcessProposalRequest.txs 是拟议块的交易列表不是已经执行那些交易：** 看见填了 txs 不是已经是 ExtendVoteRequest.txs。
2. **ProcessProposalRequest.hash 是拟议块的哈希不是已经跑过 Process：** 看见填了 hash 不是已经是 ExtendVoteRequest.hash。
3. **ProcessProposalRequest.height 是拟议块的高度不是已经对上了拟议块头：** 看见填了 height 不是已经是 ExtendVoteRequest.height。

## 为什么要分开叫

官方把 ProcessProposal Request 表上 `txs` 是拟议块的交易列表、`hash` 是拟议块的哈希、`height` 是拟议块的高度写成三件事。把它们叫成一个「看见填了 Process 请求栏就已经执行那些交易」，会把已经执行那些交易、已经跑过 Process 和已经对上了拟议块头一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Process 请求栏就已经执行那些交易」，先数清问的是 ProcessProposalRequest.txs 是拟议块的交易列表不是已经执行那些交易、ProcessProposalRequest.hash 是拟议块的哈希不是已经跑过 Process，还是 ProcessProposalRequest.height 是拟议块的高度不是已经对上了拟议块头，再决定要不要同一次发布。
