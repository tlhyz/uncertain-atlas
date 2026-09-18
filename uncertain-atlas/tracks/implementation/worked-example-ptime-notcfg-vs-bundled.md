# 例：看见 ProposeTimeout set-on-enter is not already timeout-propose interchangeable / not already left-critical interchangeable / not already will-call interchangeable

**层次**：实现 / ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事（416 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事（416 余量）/ not 1094 ptime-notcfg interchangeable / not 416 proposetimeout-vs-process bundled interchangeable」，不是 Process 何时调用余量 bundled（416），也不是立刻整块执行就已经离开关键路径（327），也不是 Process 调用是同步的就已经能稍后改裁决（354）。不要另写怎样写 Process 何时调用余量。

## 官方三件事

1. **看见进了这一轮会先设 ProposeTimeout / 看见设了定时 这份栏 is not already 已经填了 TimeoutPropose interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1094 ptime-notcfg interchangeable / 1095 ptime-notproc interchangeable / 416 proposetimeout item 2 header interchangeable，也不是已经 ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事 bundled（416 item 1 余量） interchangeable / 416 proposetimeout item 1 interchangeable。**  
   官方写：节点 p 进了高度 h、一轮 r，先设定时器 ProposeTimeout。看见设了定时，不是已经填了 TimeoutPropose interchangeable——本页从 416 item 1 侧钉 not already timeout-propose 单句。416 proposetimeout vs process bundled unbundling 在本页 item 1 启动。

2. **看见进了这一轮 / 看见设了定时 / 这份栏 is not already 已经离开关键路径 interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1094 ptime-notcfg interchangeable / 416 proposetimeout item 3 prevote interchangeable / 1096 ptime-notcall interchangeable，也不是已经立刻整块执行就已经离开关键路径 interchangeable / 327 prepare-timeout interchangeable。**  
   官方把进了这一轮和已经离开关键路径分开。看见进了这一轮，不是已经离开关键路径 interchangeable。本页钉 not already left-critical 单句。

3. **看见有定时器 / 看见设了定时 / 这份栏 is not already 已经会调 Process interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1094 ptime-notcfg interchangeable / 1095 ptime-notproc interchangeable，也不是已经 Process 调用是同步的就已经能稍后改裁决 interchangeable / 354 process-when interchangeable。**  
   官方把有定时器和已经会调 Process 分开。看见有定时器，不是已经会调 Process interchangeable。416 proposetimeout vs process bundled unbundling 在本页 item 1 启动。

怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProposeTimeout set-on-enter not already timeout-propose ≠ 已经填了 TimeoutPropose interchangeable：** 官方把算法里这份定时器和配置里那份 TimeoutPropose 分开。
- **看见进了这一轮 not already left-critical ≠ 已经离开关键路径 interchangeable：** 官方把进了这一轮和已经离开关键路径分开。
- **看见有定时器 not already will-call ≠ 已经会调 Process interchangeable：** 官方把有定时器和已经会调 Process 分开；416 proposetimeout vs process bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 进了这一轮会先设 ProposeTimeout | 不是已经填了 TimeoutPropose | 不是立刻整块执行就已经离开关键路径（327） |
| 看见进了这一轮 | 不是已经离开关键路径 | 不是 Process 调用是同步的就已经能稍后改裁决（354） |
| 看见有定时器 | 不是已经会调 Process | 不是先验块头就已经跑过 Process（1095） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事（416 余量），必须分开是不是已经填了 TimeoutPropose、是不是已经离开关键路径、是不是已经会调 Process。可以跳过「看见到了 Process 何时调用就已经填了 TimeoutPropose」。不要另写怎样写 Process 何时调用余量。416 proposetimeout vs process bundled unbundling 在本页 item 1 启动；续 [`worked-example-ptime-notproc-vs-bundled.md`](worked-example-ptime-notproc-vs-bundled.md)（不变量 1095 item 2）。

## 本页不抄

- 怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头。
- Process 何时调用余量 bundled。那是不变量 416。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
