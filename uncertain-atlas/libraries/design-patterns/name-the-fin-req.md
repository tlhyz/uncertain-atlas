# 模式：把 Finalize 请求栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**例**：[FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 ≠ 已经交差 local_last_commit](../../tracks/implementation/worked-example-finreq-vs-procreq.md)。

## 三个名字

1. **FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息不是已经交差 local_last_commit：** 看见填了 decided_last_commit 不是已经是 ProcessProposalRequest.proposed_last_commit。
2. **FinalizeBlockRequest.height 是已决块的高度不是已经对上了拟议块头：** 看见填了 height 不是已经是 ProcessProposalRequest.height。
3. **FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表不是已经执行那些交易：** 看见填了 txs 不是已经是 ProcessProposalRequest.txs。

## 为什么要分开叫

官方把 FinalizeBlock Request 表上 `decided_last_commit` 是从刚决定那块拿到的上一份提交信息、`height` 是已决块的高度、`txs` 是作为这块一部分提交的交易列表写成三件事。把它们叫成一个「看见填了 Finalize 请求栏就已经交差 local_last_commit」，会把已经交差 local_last_commit、已经对上了拟议块头和已经执行那些交易一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 请求栏就已经交差 local_last_commit」，先数清问的是 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息不是已经交差 local_last_commit、FinalizeBlockRequest.height 是已决块的高度不是已经对上了拟议块头，还是 FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表不是已经执行那些交易，再决定要不要同一次发布。
