# 例：看见 Process 调用是同步的 is not already can change verdict later interchangeable / not already left critical path interchangeable / not already settled interchangeable

**层次**：实现 / Process 调用是同步的 not already can change verdict later / not already left critical path / not already settled 正式三事（354 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 调用是同步的 not already can change verdict later / not already left critical path / not already settled 正式三事（354 余量）/ not 857 process-when-notlater interchangeable / not 354 process-when-vs-later bundled interchangeable」，不是 Process 何时调用 bundled（354），也不是立刻整块执行就已经离开关键路径（327），也不是 ExtendVote 同步就已经能稍后改（361/843）。不要另写怎样写 Process 何时调用。

## 官方三件事

1. **看见 Process 调用是同步的 / 看见引擎在等回包 这份同步 is not already 已经能在返回之后再改裁决 interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 857 process-when-notlater interchangeable / 858 process-when-notreject interchangeable / 354 process-when item 2 异步 interchangeable，也不是已经 Process 调用是同步的 not already can change verdict later / not already left critical path / not already settled 正式三事 bundled（354 item 1 余量） interchangeable / 354 process-when item 1 interchangeable。**  
   官方写：CometBFT 调 `ProcessProposal` 是同步的。看见是同步的，不是已经能稍后改裁决 interchangeable——本页从 354 item 1 侧钉 not already can change verdict later 单句。354 process-when vs later bundled unbundling 在本页 item 1 启动。

2. **看见引擎在等回包 / 看见规范写了同步 / 这份同步 is not already 已经离开关键路径 interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 857 process-when-notlater interchangeable / 354 process-when item 3 立刻 ACCEPT interchangeable / 859 process-when-notverified interchangeable，也不是已经立刻整块执行就已经离开关键路径 interchangeable / 327 immediate interchangeable。**  
   官方把引擎在等和已经离开关键路径分开——354 bundled 第一件事常与 327 混成「看见已经回了就已经能稍后改裁决或已经离开关键路径 interchangeable」，本页钉 not already left critical path 单句。

3. **看见引擎在等回包 / 看见立刻执行 / 这份同步 is not already 已经交差 interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 857 process-when-notlater interchangeable / 858 process-when-notreject interchangeable，也不是已经 ExtendVote 同步就已经能稍后改 interchangeable / 361 extend-when / 843 extend-when-notlater interchangeable。**  
   官方把立刻执行和已经交差分开。看见立刻执行，不是已经交差 interchangeable。354 process-when vs later bundled unbundling 在本页 item 1 启动。

怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process 调用是同步的 not already can change verdict later ≠ 已经能稍后改裁决 interchangeable：** 官方把同步调用和稍后改裁决分开。
- **看见引擎在等 not already left critical path ≠ 已经离开关键路径 interchangeable：** 官方把引擎在等和已经离开关键路径分开。
- **看见立刻执行 not already settled ≠ 已经交差 interchangeable：** 官方把立刻执行和已经交差分开；354 process-when vs later bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 调用是同步的 | 不是已经能在返回之后再改裁决 | 不是立刻整块执行就已经离开关键路径（327） |
| 看见引擎在等回包 | 不是已经离开关键路径 | 不是 ExtendVote 同步就已经能稍后改（361/843） |
| 看见立刻执行 | 不是已经交差 | 不是四门已经结算（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 调用是同步的 not already can change verdict later / not already left critical path / not already settled 正式三事（354 余量），必须分开是不是已经能稍后改裁决、是不是已经离开关键路径、是不是已经交差。可以跳过「看见已经回了就已经能稍后改裁决」。不要另写怎样写 Process 何时调用。354 process-when vs later bundled unbundling 在本页 item 1 启动；续 [`worked-example-process-when-notreject-vs-bundled.md`](worked-example-process-when-notreject-vs-bundled.md)（不变量 858 item 2）。

## 本页不抄

- 怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT。
- Process 何时调用 bundled。那是不变量 354。
- 只做基本检查再异步 Process。那是不变量 354 item 2 余量 / 858。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
- ExtendVote 同步就已经能稍后改。那是不变量 361 / 843。
