# 例：看见不该验排序相关有效性 is not already should-check-in-CheckTx interchangeable / not already execute-state-checked interchangeable / not already settled interchangeable

**层次**：实现 / 不该验排序相关有效性 not already should-check-in-CheckTx / not already execute-state-checked / not already settled 正式三事（339 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「不该验排序相关有效性 not already should-check-in-CheckTx / not already execute-state-checked / not already settled 正式三事（339 余量）/ not 929 checktx-weak-notsort interchangeable / not 339 checktx-weak-vs-process bundled interchangeable」，不是弱过滤器 bundled（339），也不是 CheckTxState 已经是 ExecuteTxState（312），也不是四门已经结算（33）。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。

## 官方三件事

1. **看见 CheckTx 不该验所有有效性 / 看见有效性依赖排序 这份过滤器 is not already 已经该在 CheckTx 里验排序 interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 929 checktx-weak-notsort interchangeable / 930 checktx-weak-notpool interchangeable / 339 checktx-weak item 2 拜占庭 interchangeable，也不是已经不该验排序相关有效性 not already should-check-in-CheckTx / not already execute-state-checked / not already settled 正式三事 bundled（339 item 1 余量） interchangeable / 339 checktx-weak item 1 interchangeable。**  
   官方写：CheckTx 只是弱过滤器，用来把无效交易挡在内存池外，最终也挡在链外。交易不能保证按以后作为（可能的）决定块去执行时那一份状态来验，因此 CheckTx 不该把影响有效性的每件事都验完，尤其是那些有效性可能依赖交易排序的检查。看见不该验所有，不是已经该把排序相关的那部分写进 CheckTx interchangeable——本页从 339 item 1 侧钉 not already should-check-in-CheckTx 单句。339 checktx-weak vs process bundled unbundling 在本页 item 1 启动。

2. **看见排序会改有效性 / 看见过了 CheckTx / 这份过滤器 is not already 已经按将要执行的那份验过 interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 929 checktx-weak-notsort interchangeable / 339 checktx-weak item 3 ProcessProposal interchangeable / 931 checktx-weak-notproc interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把排序会改有效性和已经按将要执行的那份验过分开——339 bundled 第一件事常与 312 混成「看见不该验排序就已经该在 CheckTx 里验或已经按 ExecuteTxState 验过 interchangeable」，本页钉 not already execute-state-checked 单句。

3. **看见过了 CheckTx / 看见不该验所有 / 这份过滤器 is not already 已经交差 interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 929 checktx-weak-notsort interchangeable / 930 checktx-weak-notpool interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把过了 CheckTx 和已经交差分开。看见过了 CheckTx，不是已经交差 interchangeable。339 checktx-weak vs process bundled unbundling 在本页 item 1 启动。

怎样写 CheckTx、怎样挑哪些检查留给 Process、怎样写 ProcessProposal 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **不该验排序相关有效性 not already should-check-in-CheckTx ≠ 已经该在 CheckTx 里验 interchangeable：** 官方把「不该验所有、尤其是排序相关」和「按将要执行的那份验过」分开。
- **看见排序会改有效性 not already execute-state-checked ≠ 已经按将要执行的那份验过 interchangeable：** 官方把排序会改有效性和已经按 ExecuteTxState 验过分开。
- **看见过了 CheckTx not already settled ≠ 已经交差 interchangeable：** 官方把过了 CheckTx 和已经交差分开；339 checktx-weak vs process bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 不该验排序相关有效性 | 不是已经该在 CheckTx 里验 | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 看见排序会改有效性 | 不是已经按将要执行的那份验过 | 不是四门已经结算（33） |
| 看见过了 CheckTx | 不是已经交差 | 不是拜占庭就已经被池子挡住（930） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不该验排序相关有效性 not already should-check-in-CheckTx / not already execute-state-checked / not already settled 正式三事（339 余量），必须分开是不是已经该在 CheckTx 里验、是不是已经按将要执行的那份验过、是不是已经交差。可以跳过「看见过了 CheckTx 就已经验完」。不要把「不验排序」当不确定已经验完。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。339 checktx-weak vs process bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktx-weak-notpool-vs-bundled.md`](worked-example-checktx-weak-notpool-vs-bundled.md)（不变量 930 item 2）。

## 本页不抄

- 怎样写 CheckTx、怎样挑哪些检查留给 Process、怎样写 ProcessProposal。
- 弱过滤器 bundled。那是不变量 339。
- 拜占庭就已经被池子挡住。那是不变量 339 item 2 余量 / 930。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
