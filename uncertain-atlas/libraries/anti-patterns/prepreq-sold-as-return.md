# 反模式：看见 PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节就当成已经能回超限列表 / 看见 PrepareProposalRequest.txs 是挑进拟议块的初步交易列表就当成已经跑过 Process / 看见 PrepareProposalRequest.height 是将要提议的那块的高度就当成已经对上了拟议块头

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**例**：[PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节 ≠ 已经能回超限列表](../../tracks/implementation/worked-example-prepreq-vs-return.md)。

## 塌法

1. 看见 `PrepareProposalRequest.max_tx_bytes` 是当前配置的、改过的交易占的最大字节 / 看见填了 max_tx_bytes，就当成已经能回超限列表，或当成已经是引擎会帮你裁。
2. 看见 `PrepareProposalRequest.txs` 是挑进拟议块的初步交易列表 / 看见填了 txs，就当成已经跑过 Process，或当成已经是 ProcessProposalRequest.txs。
3. 看见 `PrepareProposalRequest.height` 是将要提议的那块的高度 / 看见填了 height，就当成已经对上了拟议块头，或当成已经是 ProcessProposalRequest.height。

## 为什么会出事

官方写：`max_tx_bytes` 是当前配置的、改过的交易占的最大字节。`txs` 是挑进拟议块的初步交易列表。`height` 是将要提议的那块的高度。看见填了栏，不是已经能回超限列表，也不是已经跑过 Process，也不是已经对上了拟议块头。

## 和相邻反模式

- [preparereturn-sold-as-trimmed](preparereturn-sold-as-trimmed.md) 是聚合体积可以超过 max_tx_bytes 就已经能回超限列表，不是本页这种 PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节不是已经能回超限列表。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process，不是本页这种 PrepareProposalRequest.txs 是挑进拟议块的初步交易列表不是已经跑过 Process。
- [procreq-sold-as-extreq](procreq-sold-as-extreq.md) 是 ProcessProposalRequest.height 是拟议块的高度就已经对上了拟议块头，不是本页这种 PrepareProposalRequest.height 是将要提议的那块的高度不是已经对上了拟议块头。
