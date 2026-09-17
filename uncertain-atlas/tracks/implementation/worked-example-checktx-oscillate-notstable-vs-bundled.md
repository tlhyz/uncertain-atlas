# 例：看见还在振荡 is not already past h_stable interchangeable / not already left the pool interchangeable / not already settled interchangeable

**层次**：实现 / 还在振荡 not already past h_stable / not already left the pool / not already settled 正式三事（328 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「还在振荡 not already past h_stable / not already left the pool / not already settled 正式三事（328 余量）/ not 942 checktx-oscillate-notstable interchangeable / not 328 checktx-oscillate-vs-stable bundled interchangeable」，不是振荡 bundled（328），也不是提案收了已经从池里删掉（301），也不是四门已经结算（33）。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 官方三件事

1. **看见还在振荡 / 看见还在池里 这份待法 is not already 已经过了 h_stable interchangeable，也不是已经振荡 bundled（328） interchangeable / 942 checktx-oscillate-notstable interchangeable / 941 checktx-oscillate-notcode interchangeable / 328 checktx-oscillate item 1 不同码 interchangeable，也不是已经还在振荡 not already past h_stable / not already left the pool / not already settled 正式三事 bundled（328 item 2 余量） interchangeable / 328 checktx-oscillate item 2 interchangeable。**  
   官方写：对任意 tx，存在布尔 b 和高度 h_stable，使得任意正确进程在 h ≥ h_stable 上都有定义好的 CheckTxCode，且 OK = b。Requirement 13 保证：这笔若在本节点池里待得够久，会最终不再在成功和失败之间来回。看见还在振荡，不是已经过了 h_stable interchangeable——本页从 328 item 2 侧钉 not already past h_stable 单句。328 checktx-oscillate vs stable bundled unbundling 在本页 item 2 续。

2. **看见还在池里 / 看见最终不再振荡 / 这份待法 is not already 已经离池 interchangeable，也不是已经振荡 bundled（328） interchangeable / 942 checktx-oscillate-notstable interchangeable / 328 checktx-oscillate item 3 本地不再振荡 interchangeable / 943 checktx-oscillate-notsameb interchangeable，也不是已经提案收了已经从池里删掉 interchangeable / 301 pool-remove interchangeable。**  
   官方把还在池里和已经离池分开——328 bundled 第二件事常与 301 混成「看见还在振荡就已经过了 h_stable 或已经从池里删掉 interchangeable」，本页钉 not already left the pool 单句。

3. **看见最终不再振荡 / 看见还在池里 / 这份待法 is not already 已经交差 interchangeable，也不是已经振荡 bundled（328） interchangeable / 942 checktx-oscillate-notstable interchangeable / 941 checktx-oscillate-notcode interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把最终不再振荡和已经进了块 / 已经交差分开。看见最终不再振荡，不是已经交差 interchangeable。328 checktx-oscillate vs stable bundled unbundling 在本页 item 2 续。

怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **还在振荡 not already past h_stable ≠ 已经过了 h_stable interchangeable：** 官方把「最终不再振荡」写成存在以后的高度，不是看见此刻来回就已经齐。
- **看见还在池里 not already left the pool ≠ 已经离池 interchangeable：** 官方把还在池里和已经离池分开。
- **看见最终不再振荡 not already settled ≠ 已经交差 interchangeable：** 官方把最终不再振荡和已经进了块分开；328 checktx-oscillate vs stable bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 还在振荡 | 不是已经过了 h_stable | 不是提案收了已经从池里删掉（301） |
| 看见还在池里 | 不是已经离池 | 不是四门已经结算（33） |
| 看见最终不再振荡 | 不是已经交差 | 不是回了不同码就已经有了 CheckTxCode（941） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看还在振荡 not already past h_stable / not already left the pool / not already settled 正式三事（328 余量），必须分开是不是已经过了 h_stable、是不是已经离池、是不是已经交差。可以跳过「看见还在振荡就已经过了稳定高度」。不要另写怎样实现 CheckTx 或怎样挑稳定高度。328 checktx-oscillate vs stable bundled unbundling 在本页 item 2 续；续 [`worked-example-checktx-oscillate-notsameb-vs-bundled.md`](worked-example-checktx-oscillate-notsameb-vs-bundled.md)（不变量 943 item 3）。

## 本页不抄

- 怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔。
- 振荡 bundled。那是不变量 328。
- 回了不同码就已经有了 CheckTxCode。那是不变量 328 item 1 余量 / 941。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
