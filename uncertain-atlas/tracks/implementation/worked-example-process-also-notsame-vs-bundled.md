# 例：看见通常紧跟 Prepare、列表对得上 is not already guaranteed this Prepare interchangeable / not already must match interchangeable / not already settled interchangeable

**层次**：实现 / 通常紧跟 Prepare、列表对得上 not already guaranteed this Prepare / not already must match / not already settled 正式三事（351 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「通常紧跟 Prepare、列表对得上 not already guaranteed this Prepare / not already must match / not already settled 正式三事（351 余量）/ not 861 process-also-notsame interchangeable / not 351 process-also-vs-prepare bundled interchangeable」，不是 Process 也会在提议者那边叫 bundled（351），也不是正确提议者的准备提案必须被正确接收者 Accept（347），也不是候选已经是 ExecuteTxState（311）。不要另写怎样写 Process。

## 官方三件事

1. **看见通常紧跟 Prepare、`ProcessProposalRequest.txs` 等于 `PrepareProposalResponse.txs` / 看见列表对得上 这份通常 is not already 已经保证是这一次 Prepare 的回包 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 861 process-also-notsame interchangeable / 860 process-also-notskip interchangeable / 351 process-also item 1 提议者 interchangeable，也不是已经通常紧跟 Prepare、列表对得上 not already guaranteed this Prepare / not already must match / not already settled 正式三事 bundled（351 item 2 余量） interchangeable / 351 process-also item 2 interchangeable。**  
   官方写：通常这次 Process 紧跟 Prepare，而且请求对得上刚回的那块。看见通常对得上，不是已经保证是这一次 interchangeable——本页从 351 item 2 侧钉 not already guaranteed this Prepare 单句。351 process-also vs prepare bundled unbundling 在本页 item 2 续。

2. **看见列表对得上 / 看见 txs 一样 / 这份通常 is not already 已经必须对上 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 861 process-also-notsame interchangeable / 351 process-also item 3 失败 interchangeable / 862 process-also-notevery interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept interchangeable / 347 req3 interchangeable。**  
   官方把 txs 一样和已经必须对上分开——351 bundled 第二件事常与 347 混成「看见列表对得上就已经保证是这一次或已经必须对上 interchangeable」，本页钉 not already must match 单句。

3. **看见列表对得上 / 看见刚 Prepare 完 / 这份通常 is not already 已经交差 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 861 process-also-notsame interchangeable / 860 process-also-notskip interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把刚 Prepare 完和已经交差分开。看见刚 Prepare 完，不是已经交差 interchangeable。351 process-also vs prepare bundled unbundling 在本页 item 2 续。

怎样写 Process、怎样缓存候选、怎样测失败路径是规范里的做法，本页不抄。

## 官方为什么这样拆

- **通常紧跟 Prepare、列表对得上 not already guaranteed this Prepare ≠ 已经保证是这一次 interchangeable：** 官方把通常对得上和保证是这一次分开。
- **看见 txs 一样 not already must match ≠ 已经必须对上 interchangeable：** 官方把 txs 一样和已经必须对上分开。
- **看见刚 Prepare 完 not already settled ≠ 已经交差 interchangeable：** 官方把刚 Prepare 完和已经交差分开；351 process-also vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 通常紧跟 Prepare、列表对得上 | 不是已经保证是这一次 | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |
| 看见 txs 一样 | 不是已经必须对上 | 不是候选已经是 ExecuteTxState（311） |
| 看见刚 Prepare 完 | 不是已经交差 | 不是提议者就已经不用再 Process（860） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常紧跟 Prepare、列表对得上 not already guaranteed this Prepare / not already must match / not already settled 正式三事（351 余量），必须分开是不是已经保证是这一次、是不是已经必须对上、是不是已经交差。可以跳过「看见列表对得上就已经保证是这一次」。不要另写怎样写 Process。351 process-also vs prepare bundled unbundling 在本页 item 2 续；续 [`worked-example-process-also-notevery-vs-bundled.md`](worked-example-process-also-notevery-vs-bundled.md)（不变量 862 item 3）。

## 本页不抄

- 怎样写 Process、怎样缓存候选、怎样测失败路径。
- Process 也会在提议者那边叫 bundled。那是不变量 351。
- Process 也会在提议者那边叫。那是不变量 351 item 1 余量 / 860。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- 候选已经是 ExecuteTxState。那是不变量 311。
