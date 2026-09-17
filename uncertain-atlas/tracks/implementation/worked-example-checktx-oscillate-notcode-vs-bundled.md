# 例：看见同一高度回了不同码 is not already CheckTxCode interchangeable / not already OK interchangeable / not already settled interchangeable

**层次**：实现 / 同一高度回了不同码 not already CheckTxCode / not already OK / not already settled 正式三事（328 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「同一高度回了不同码 not already CheckTxCode / not already OK / not already settled 正式三事（328 余量）/ not 941 checktx-oscillate-notcode interchangeable / not 328 checktx-oscillate-vs-stable bundled interchangeable」，不是振荡 bundled（328），也不是 CheckTxState 已经是 ExecuteTxState（312），也不是弱过滤器就已经是 Process（339）。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 官方三件事

1. **看见同一高度 CheckTx 回了不同码 / 看见 CheckTxCodes 是集合 这份集合 is not already 已经有了 CheckTxCode interchangeable，也不是已经振荡 bundled（328） interchangeable / 941 checktx-oscillate-notcode interchangeable / 942 checktx-oscillate-notstable interchangeable / 328 checktx-oscillate item 2 还在振荡 interchangeable，也不是已经同一高度回了不同码 not already CheckTxCode / not already OK / not already settled 正式三事 bundled（328 item 1 余量） interchangeable / 328 checktx-oscillate item 1 interchangeable。**  
   官方写：高度 h 上对同一笔 tx 的 CheckTxResponse 码收成集合 CheckTxCodes。集合可以有多个码。只有它是单元素时，才定义 CheckTxCode。不是单元素，CheckTxCode 没有定义。看见回了两次，不是已经有这个码 interchangeable——本页从 328 item 1 侧钉 not already CheckTxCode 单句。328 checktx-oscillate vs stable bundled unbundling 在本页 item 1 启动。

2. **看见集合在 / 看见回了两次 / 这份集合 is not already 已经能说 OK interchangeable，也不是已经振荡 bundled（328） interchangeable / 941 checktx-oscillate-notcode interchangeable / 328 checktx-oscillate item 3 本地不再振荡 interchangeable / 943 checktx-oscillate-notsameb interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把集合在和 OK(CheckTxCode) 已经有定义分开——328 bundled 第一件事常与 312 混成「看见回了不同码就已经有了 CheckTxCode 或已经按 ExecuteTxState 交差 interchangeable」，本页钉 not already OK 单句。

3. **看见集合在 / 看见回了两次 / 这份集合 is not already 已经交差 interchangeable，也不是已经振荡 bundled（328） interchangeable / 941 checktx-oscillate-notcode interchangeable / 942 checktx-oscillate-notstable interchangeable，也不是已经弱过滤器就已经是 Process interchangeable / 339/931 checktx-weak-notproc interchangeable。**  
   官方把集合在和已经交差分开。看见集合在，不是已经交差 interchangeable。328 checktx-oscillate vs stable bundled unbundling 在本页 item 1 启动。

怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **同一高度回了不同码 not already CheckTxCode ≠ 已经有了 CheckTxCode interchangeable：** 官方把集合和单元素才定义的那个码分开。
- **看见集合在 not already OK ≠ 已经能说 OK interchangeable：** 官方把集合在和 OK(CheckTxCode) 已经有定义分开。
- **看见集合在 not already settled ≠ 已经交差 interchangeable：** 官方把集合在和已经交差分开；328 checktx-oscillate vs stable bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一高度回了不同码 | 不是已经有了 CheckTxCode | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 看见集合在 | 不是已经能说 OK | 不是弱过滤器就已经是 Process（339） |
| 看见回了两次 | 不是已经交差 | 不是还在振荡就已经过了 h_stable（942） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度回了不同码 not already CheckTxCode / not already OK / not already settled 正式三事（328 余量），必须分开是不是已经有了 CheckTxCode、是不是已经能说 OK、是不是已经交差。可以跳过「看见过了就已经稳定」。不要另写怎样实现 CheckTx 或怎样挑稳定高度。328 checktx-oscillate vs stable bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktx-oscillate-notstable-vs-bundled.md`](worked-example-checktx-oscillate-notstable-vs-bundled.md)（不变量 942 item 2）。

## 本页不抄

- 怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔。
- 振荡 bundled。那是不变量 328。
- 还在振荡就已经过了 h_stable。那是不变量 328 item 2 余量 / 942。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
