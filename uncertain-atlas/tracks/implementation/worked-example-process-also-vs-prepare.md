# 例：看见 Process 也会在提议者那边叫不是已经不用再 Process；看见通常紧跟 Prepare、列表对得上不是已经保证是这一次；看见失败时可能对上更早一次或根本不调不是已经每轮都会叫

**层次**：实现 / Process 也会在提议者那边叫。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Process 也会在提议者那边叫不是已经不用再 Process / 通常紧跟 Prepare、列表对得上不是已经保证是这一次 / 失败时可能对上更早一次或根本不调不是已经每轮都会叫」，不是四门已经结算，也不是正确提议者的准备提案必须被正确接收者 Accept。不要另写怎样写 Process。351 processalso vs prepare bundled unbundling 续（806+807）；精读 [`worked-example-process-notskip-vs-bundled.md`](worked-example-process-notskip-vs-bundled.md)（不变量 806 item 1）；精读 [`worked-example-process-notguaranteed-vs-bundled.md`](worked-example-process-notguaranteed-vs-bundled.md)（不变量 807 item 2）。

## 官方三件事

规范把提议者这边也会叫 Process、通常对得上、失败时不保证写成三件独立的实现事，不是「看见自己刚 Prepare 过就已经不用再 Process、已经保证是这一次、已经每轮都会叫」一件事：

1. **看见 `ProcessProposal` 也会在这一轮的提议者那边叫 / 看见自己刚 Prepare 过 不是已经不用再 Process，也不是已经交差。**  
   官方写：`ProcessProposal` 也会在这一轮的提议者那边叫。看见自己刚回了 Prepare，不是已经不用再叫 Process。看见是提议者，不是已经交差。看见列表自己编的，不是已经过了 Process。
2. **看见通常紧跟 Prepare、`ProcessProposalRequest.txs` 等于 `PrepareProposalResponse.txs` / 看见列表对得上 不是已经保证是这一次 Prepare 的回包，也不是已经必须对上。**  
   官方写：通常这次 Process 紧跟 Prepare，而且请求对得上刚回的那块。看见通常对得上，不是已经保证。看见 txs 一样，不是已经必须一样。看见刚 Prepare 完，不是已经是同一份调用。
3. **看见失败时可能对上更早一次 Prepare / 看见根本不调 Process 不是已经是这一次 Prepare，也不是已经每轮都会叫 Process。**  
   官方写：失败时不保证。`ProcessProposalRequest` 可能对上更早一次 Prepare 的回包，或者根本不调 Process。看见叫了 Process，不是已经是这一次刚回的那份。看见进了这一轮，不是已经会叫。看见失败了，不是已经交差。

怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径是规范里的做法，本页不抄。四门已经结算是不变量 33，本页不抄。

## 官方为什么这样拆

- **Process 也会在提议者那边叫 ≠ 已经不用再 Process：** 官方把提议者也会叫 Process 和刚 Prepare 过分开。
- **通常紧跟 Prepare、列表对得上 ≠ 已经保证是这一次：** 官方把通常对得上和保证是这一次分开。
- **失败时可能对上更早一次或根本不调 ≠ 已经每轮都会叫：** 官方把失败时的两种情况和每轮都会叫分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 也会在提议者那边叫 | 不是已经不用再 Process | 不是四门已经结算（33） |
| 通常紧跟 Prepare、列表对得上 | 不是已经保证是这一次 | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |
| 失败时可能对上更早一次或根本不调 | 不是已经每轮都会叫 | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见自己刚 Prepare 过就已经不用再 Process、已经保证是这一次、已经每轮都会叫」，必须分开 Process 也会在提议者那边叫是不是已经不用再 Process、通常紧跟 Prepare、列表对得上是不是已经保证是这一次、失败时可能对上更早一次或根本不调是不是已经每轮都会叫。可以跳过「看见自己刚 Prepare 过就已经不用再 Process」。不要另写怎样写 Process。351 processalso vs prepare bundled unbundling 续（806+807）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- 候选已经是 ExecuteTxState。那是不变量 311。
