# 例：看见 PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节不是已经能回超限列表；看见 PrepareProposalRequest.txs 是挑进拟议块的初步交易列表不是已经跑过 Process；看见 PrepareProposalRequest.height 是将要提议的那块的高度不是已经对上了拟议块头

**层次**：实现 / Prepare 请求栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节不是已经能回超限列表 / PrepareProposalRequest.txs 是挑进拟议块的初步交易列表不是已经跑过 Process / PrepareProposalRequest.height 是将要提议的那块的高度不是已经对上了拟议块头」，不是聚合体积可以超过 max_tx_bytes 就已经能回超限列表，也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。不要另写怎样写 Prepare 请求栏。

## 官方三件事

规范把 PrepareProposal Request 表上 `max_tx_bytes` 是当前配置的、改过的交易占的最大字节、`txs` 是挑进拟议块的初步交易列表、`height` 是将要提议的那块的高度写成三件独立的实现事，不是「看见填了 Prepare 请求栏就已经能回超限列表、已经跑过 Process、已经对上了拟议块头」一件事：

1. **看见 `PrepareProposalRequest.max_tx_bytes` 是当前配置的、改过的交易占的最大字节 / 看见填了 max_tx_bytes 不是已经能回超限列表，也不是已经是引擎会帮你裁。**  
   官方写：`max_tx_bytes` 是当前配置的、改过的交易占的最大字节。看见填了 max_tx_bytes，不是已经聚合体积可以超过 `PrepareProposalRequest.max_tx_bytes` 那种已经能回超限列表。看见有当前配置上限，不是已经 Requirement 2 保证回的列表不让块超字节上限那种已经是引擎会帮你裁。看见能指上限，不是已经交差。
2. **看见 `PrepareProposalRequest.txs` 是挑进拟议块的初步交易列表 / 看见填了 txs 不是已经跑过 Process，也不是已经是 ProcessProposalRequest.txs。**  
   官方写：`txs` 是挑进拟议块的初步交易列表。看见填了 txs，不是已经 Prepare 和 Process / Finalize 同一套字段那种已经跑过 Process。看见是初步列表，不是已经 `ProcessProposalRequest.txs` 是拟议块的交易列表那种已经执行那些交易。看见能指初步交易，不是已经交差。
3. **看见 `PrepareProposalRequest.height` 是将要提议的那块的高度 / 看见填了 height 不是已经对上了拟议块头，也不是已经是 ProcessProposalRequest.height。**  
   官方写：`height` 是将要提议的那块的高度。看见填了 height，不是已经 `ProcessProposalRequest.height` 是拟议块的高度那种已经对上了拟议块头。看见有将要提议的高度，不是已经 Prepare 的 `height` / `time` / `proposer_address` 对上拟议头那种已经知道本头哈希。看见能指高度，不是已经交差。

怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs 是规范里的做法，本页不抄。聚合体积可以超过 max_tx_bytes 就已经能回超限列表是不变量 345，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节 ≠ 已经能回超限列表：** 官方把 Prepare 请求表上这份当前配置的、改过的交易占的最大字节和 Requirements 里那份聚合体积可以超过 max_tx_bytes 分开。
- **PrepareProposalRequest.txs 是挑进拟议块的初步交易列表 ≠ 已经跑过 Process：** 官方把 Prepare 请求表上这份挑进拟议块的初步交易列表和 Usage 里那份与 Process / Finalize 同一套字段分开。
- **PrepareProposalRequest.height 是将要提议的那块的高度 ≠ 已经对上了拟议块头：** 官方把 Prepare 请求表上这份将要提议的那块的高度和 Process 请求表上那份拟议块高度分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节 | 不是已经能回超限列表 | 不是聚合体积可以超过 max_tx_bytes 就已经能回超限列表（345） |
| PrepareProposalRequest.txs 是挑进拟议块的初步交易列表 | 不是已经跑过 Process | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| PrepareProposalRequest.height 是将要提议的那块的高度 | 不是已经对上了拟议块头 | 不是 ProcessProposalRequest.height 是拟议块的高度就已经对上了拟议块头（419） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Prepare 请求栏就已经能回超限列表、已经跑过 Process、已经对上了拟议块头」，必须分开 PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节是不是已经能回超限列表、PrepareProposalRequest.txs 是挑进拟议块的初步交易列表是不是已经跑过 Process、PrepareProposalRequest.height 是将要提议的那块的高度是不是已经对上了拟议块头。可以跳过「看见填了 Prepare 请求栏就已经能回超限列表」。不要另写怎样写 Prepare 请求栏。

## 本页不抄

- 怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs。
- 聚合体积可以超过 max_tx_bytes 就已经能回超限列表。那是不变量 345。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- ProcessProposalRequest.height 是拟议块的高度就已经对上了拟议块头。那是不变量 419。
