# 模式：把 Prepare 请求栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**例**：[PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节 ≠ 已经能回超限列表](../../tracks/implementation/worked-example-prepreq-vs-return.md)。

## 三个名字

1. **PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节不是已经能回超限列表：** 看见填了 max_tx_bytes 不是已经是引擎会帮你裁。
2. **PrepareProposalRequest.txs 是挑进拟议块的初步交易列表不是已经跑过 Process：** 看见填了 txs 不是已经是 ProcessProposalRequest.txs。
3. **PrepareProposalRequest.height 是将要提议的那块的高度不是已经对上了拟议块头：** 看见填了 height 不是已经是 ProcessProposalRequest.height。

## 为什么要分开叫

官方把 PrepareProposal Request 表上 `max_tx_bytes` 是当前配置的、改过的交易占的最大字节、`txs` 是挑进拟议块的初步交易列表、`height` 是将要提议的那块的高度写成三件事。把它们叫成一个「看见填了 Prepare 请求栏就已经能回超限列表」，会把已经能回超限列表、已经跑过 Process 和已经对上了拟议块头一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Prepare 请求栏就已经能回超限列表」，先数清问的是 PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节不是已经能回超限列表、PrepareProposalRequest.txs 是挑进拟议块的初步交易列表不是已经跑过 Process，还是 PrepareProposalRequest.height 是将要提议的那块的高度不是已经对上了拟议块头，再决定要不要同一次发布。
