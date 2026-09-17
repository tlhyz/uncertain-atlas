# 反模式：看见 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息就当成已经交差 local_last_commit / 看见 FinalizeBlockRequest.height 是已决块的高度就当成已经对上了拟议块头 / 看见 FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表就当成已经执行那些交易

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**例**：[FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 ≠ 已经交差 local_last_commit](../../tracks/implementation/worked-example-finreq-vs-procreq.md)。

## 塌法

1. 看见 `FinalizeBlockRequest.decided_last_commit` 是从刚决定那块拿到的上一份提交信息 / 看见填了 decided_last_commit，就当成已经交差 local_last_commit，或当成已经是 ProcessProposalRequest.proposed_last_commit。
2. 看见 `FinalizeBlockRequest.height` 是已决块的高度 / 看见填了 height，就当成已经对上了拟议块头，或当成已经是 ProcessProposalRequest.height。
3. 看见 `FinalizeBlockRequest.txs` 是作为这块一部分提交的交易列表 / 看见填了 txs，就当成已经执行那些交易，或当成已经是 ProcessProposalRequest.txs。

## 为什么会出事

官方写：`decided_last_commit` 是上一份提交信息，从刚决定那块拿到。`height` 是已决块的高度。`txs` 是作为这块一部分提交的交易列表。看见填了栏，不是已经交差 local_last_commit，也不是已经对上了拟议块头，也不是已经执行那些交易。

## 和相邻反模式

- [procreqrest-sold-as-extreq](procreqrest-sold-as-extreq.md) 是 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit，不是本页这种 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息不是已经交差 local_last_commit。
- [procreq-sold-as-extreq](procreq-sold-as-extreq.md) 是 ProcessProposalRequest.height 是拟议块的高度就已经对上了拟议块头，不是本页这种 FinalizeBlockRequest.height 是已决块的高度不是已经对上了拟议块头。
- [fintxs-sold-as-control](fintxs-sold-as-control.md) 是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差，不是本页这种 FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表不是已经执行那些交易。
