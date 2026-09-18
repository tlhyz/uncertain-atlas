# 例：看见 prevote-or-nil look is not already will-call interchangeable / not already still-reject interchangeable / not already settled interchangeable

**层次**：实现 / prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事（416 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事（416 余量）/ not 1096 ptime-notcall interchangeable / not 416 proposetimeout-vs-process bundled interchangeable」，不是 Process 何时调用余量 bundled（416），也不是 Process 调用是同步的就已经能稍后改裁决（354），也不是 Process 也会在提议者那边叫就已经不用再 Process（351）。不要另写怎样写 Process 何时调用余量。

## 官方三件事

1. **看见收齐块片才按验证者算法看该不该 prevote 这块或 nil / 看见在看 这份栏 is not already 已经会调 Process interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1096 ptime-notcall interchangeable / 1094 ptime-notcfg interchangeable / 416 proposetimeout item 1 timeout interchangeable，也不是已经 prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事 bundled（416 item 3 余量） interchangeable / 416 proposetimeout item 3 interchangeable。**  
   官方写：收到提案和全部块片之后，p 按验证者算法看该不该 prevote 这块，还是 prevote nil。看见在看，不是已经会调 Process interchangeable——本页从 416 item 3 侧钉 not already will-call 单句。416 proposetimeout vs process bundled unbundling 在本页 item 3 完成。

2. **看见还没调 / 看见在看 / 这份栏 is not already 已经还能再 Reject interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1096 ptime-notcall interchangeable / 416 proposetimeout item 2 header interchangeable / 1095 ptime-notproc interchangeable，也不是已经 Process 调用是同步的就已经能稍后改裁决 interchangeable / 354 process-when interchangeable。**  
   官方把还没调和已经还能再 Reject 分开。看见还没调，不是已经还能再 Reject interchangeable。本页钉 not already still-reject 单句。

3. **看见有算法 / 看见在看 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1096 ptime-notcall interchangeable / 1094 ptime-notcfg interchangeable，也不是已经 Process 也会在提议者那边叫就已经不用再 Process interchangeable / 351 process-proposer interchangeable。**  
   官方把有算法和已经交差分开。看见有算法，不是已经交差 interchangeable。416 proposetimeout vs process bundled unbundling 在本页 item 3 完成。

怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **prevote-or-nil look not already will-call ≠ 已经会调 Process interchangeable：** 官方把还在看该不该 prevote 和已经调 Process 分开。
- **看见还没调 not already still-reject ≠ 已经还能再 Reject interchangeable：** 官方把还没调和已经还能再 Reject 分开。
- **看见有算法 not already settled ≠ 已经交差 interchangeable：** 官方把有算法和已经交差分开；416 proposetimeout vs process bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收齐块片才按验证者算法看该不该 prevote 这块或 nil | 不是已经会调 Process | 不是 Process 调用是同步的就已经能稍后改裁决（354） |
| 看见还没调 | 不是已经还能再 Reject | 不是 Process 也会在提议者那边叫就已经不用再 Process（351） |
| 看见有算法 | 不是已经交差 | 不是设了 ProposeTimeout 就已经填了 TimeoutPropose（1094） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事（416 余量），必须分开是不是已经会调 Process、是不是已经还能再 Reject、是不是已经交差。可以跳过「看见到了 Process 何时调用就已经填了 TimeoutPropose」。不要另写怎样写 Process 何时调用余量。416 proposetimeout vs process bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头。
- Process 何时调用余量 bundled。那是不变量 416。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
