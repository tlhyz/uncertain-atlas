# 例：看见只做基本检查再异步 Process is not already can still Reject interchangeable / not already can force nil interchangeable / not already settled interchangeable

**层次**：实现 / 只做基本检查再异步 Process not already can still Reject / not already can force nil / not already settled 正式三事（354 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「只做基本检查再异步 Process not already can still Reject / not already can force nil / not already settled 正式三事（354 余量）/ not 858 process-when-notreject interchangeable / not 354 process-when-vs-later bundled interchangeable」，不是 Process 何时调用 bundled（354），也不是四门已经结算（33），也不是立刻整块执行就已经离开关键路径（327）。不要另写怎样写 Process 何时调用。

## 官方三件事

1. **看见只做基本检查再异步 Process / 看见已经回了 `ACCEPT` 这份异步 is not already 已经还能再 Reject interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 858 process-when-notreject interchangeable / 857 process-when-notlater interchangeable / 354 process-when item 1 同步 interchangeable，也不是已经只做基本检查再异步 Process not already can still Reject / not already can force nil / not already settled 正式三事 bundled（354 item 2 余量） interchangeable / 354 process-when item 2 interchangeable。**  
   官方写：应用可以先做基本检查再异步处理这块；这时不能再 Reject。看见已经回了 `ACCEPT`，不是已经还能再 Reject interchangeable——本页从 354 item 2 侧钉 not already can still Reject 单句。354 process-when vs later bundled unbundling 在本页 item 2 续。

2. **看见已经回了 `ACCEPT` / 看见还在跑 / 这份异步 is not already 已经还能强迫 prevote/precommit `nil` interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 858 process-when-notreject interchangeable / 354 process-when item 3 立刻 ACCEPT interchangeable / 859 process-when-notverified interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把还在跑和已经还能强迫 `nil` 分开——354 bundled 第二件事常与 33 混成「看见已经回了就已经还能再 Reject 或已经还能强迫 nil interchangeable」，本页钉 not already can force nil 单句。

3. **看见已经回了 `ACCEPT` / 看见异步了 / 这份异步 is not already 已经交差 interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 858 process-when-notreject interchangeable / 857 process-when-notlater interchangeable，也不是已经立刻整块执行就已经离开关键路径 interchangeable / 327 immediate interchangeable。**  
   官方把异步了和已经交差分开。看见异步了，不是已经交差 interchangeable。354 process-when vs later bundled unbundling 在本页 item 2 续。

怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **只做基本检查再异步 Process not already can still Reject ≠ 已经还能再 Reject interchangeable：** 官方把异步处理和还能改票分开。
- **看见还在跑 not already can force nil ≠ 已经还能强迫 nil interchangeable：** 官方把还在跑和已经还能强迫 nil 分开。
- **看见异步了 not already settled ≠ 已经交差 interchangeable：** 官方把异步了和已经交差分开；354 process-when vs later bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 只做基本检查再异步 Process | 不是已经还能再 Reject | 不是四门已经结算（33） |
| 看见还在跑 | 不是已经还能强迫 prevote/precommit nil | 不是立刻整块执行就已经离开关键路径（327） |
| 看见异步了 | 不是已经交差 | 不是同步就已经能稍后改裁决（857） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只做基本检查再异步 Process not already can still Reject / not already can force nil / not already settled 正式三事（354 余量），必须分开是不是已经还能再 Reject、是不是已经还能强迫 nil、是不是已经交差。可以跳过「看见已经回了就已经还能再 Reject」。不要另写怎样写 Process 何时调用。354 process-when vs later bundled unbundling 在本页 item 2 续；续 [`worked-example-process-when-notverified-vs-bundled.md`](worked-example-process-when-notverified-vs-bundled.md)（不变量 859 item 3）。

## 本页不抄

- 怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT。
- Process 何时调用 bundled。那是不变量 354。
- Process 调用是同步的。那是不变量 354 item 1 余量 / 857。
- 四门已经结算。那是不变量 33。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
