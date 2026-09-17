# 例：看见本地不再振荡 is not already global same height interchangeable / not already same b interchangeable / not already settled interchangeable

**层次**：实现 / 本地不再振荡 not already global same height / not already same b / not already settled 正式三事（328 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「本地不再振荡 not already global same height / not already same b / not already settled 正式三事（328 余量）/ not 943 checktx-oscillate-notsameb interchangeable / not 328 checktx-oscillate-vs-stable bundled interchangeable」，不是振荡 bundled（328），也不是索引器已经保证不重放（313），也不是四门已经结算（33）。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 官方三件事

1. **看见本地 h_p,stable / 看见本节点不再振荡 这份本地 is not already 已经是全局同一高度 interchangeable，也不是已经振荡 bundled（328） interchangeable / 943 checktx-oscillate-notsameb interchangeable / 941 checktx-oscillate-notcode interchangeable / 328 checktx-oscillate item 1 不同码 interchangeable，也不是已经本地不再振荡 not already global same height / not already same b / not already settled 正式三事 bundled（328 item 3 余量） interchangeable / 328 checktx-oscillate item 3 interchangeable。**  
   官方写：Requirement 13 写的是全局 h_stable，实现者也可以把它看成只属于进程 p 的 h_p,stable，一般性不丢。看见本节点稳住了，不是已经全网同一高度 interchangeable——本页从 328 item 3 侧钉 not already global same height 单句。328 checktx-oscillate vs stable bundled unbundling 在本页 item 3 完成。

2. **看见本地不再振荡 / 看见本节点稳住了 / 这份本地 is not already 已经各节点同一份 b interchangeable，也不是已经振荡 bundled（328） interchangeable / 943 checktx-oscillate-notsameb interchangeable / 328 checktx-oscillate item 2 还在振荡 interchangeable / 942 checktx-oscillate-notstable interchangeable，也不是已经索引器已经保证不重放 interchangeable / 313 indexer interchangeable。**  
   官方把本地不再振荡和已经同一份 b 分开——相反，b 必须各正确进程相同。328 bundled 第三件事常与 313 / 33 混成「看见本地稳住就已经全网同一份或已经交差 interchangeable」，本页钉 not already same b 单句。

3. **看见本地不再振荡 / 看见本节点稳住了 / 这份本地 is not already 已经交差 interchangeable，也不是已经振荡 bundled（328） interchangeable / 943 checktx-oscillate-notsameb interchangeable / 941 checktx-oscillate-notcode interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把本地不再振荡和已经交差分开。看见本地不再振荡，不是已经交差 interchangeable。328 checktx-oscillate vs stable bundled unbundling 在本页 item 3 完成。

怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **本地不再振荡 not already global same height ≠ 已经是全局同一高度 interchangeable：** 官方把可以本地的稳定高度和必须全网同一份 b 分开。
- **看见本地不再振荡 not already same b ≠ 已经各节点同一份 b interchangeable：** 官方把本地稳住和 b 必须各正确进程相同分开。
- **看见本节点稳住了 not already settled ≠ 已经交差 interchangeable：** 官方把本节点稳住和已经交差分开；328 checktx-oscillate vs stable bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本地不再振荡 | 不是已经各节点同一份 b | 不是索引器已经保证不重放（313） |
| 看见本节点稳住了 | 不是已经是全局同一高度 | 不是四门已经结算（33） |
| 看见本地 h_p,stable | 不是已经交差 | 不是回了不同码就已经有了 CheckTxCode（941） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地不再振荡 not already global same height / not already same b / not already settled 正式三事（328 余量），必须分开是不是已经是全局同一高度、是不是已经各节点同一份 b、是不是已经交差。可以跳过「看见本地稳住就已经全网同一份」。不要另写怎样实现 CheckTx 或怎样挑稳定高度。328 checktx-oscillate vs stable bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔。
- 振荡 bundled。那是不变量 328。
- 回了不同码就已经有了 CheckTxCode。那是不变量 328 item 1 余量 / 941。
- 索引器已经保证不重放。那是不变量 313。
- 四门已经结算。那是不变量 33。
