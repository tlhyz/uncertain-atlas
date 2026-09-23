# 例：看见 Process 调用是同步的不是已经能在返回之后再改裁决；看见只做基本检查再异步 Process 不是已经还能再 Reject；看见非验证者可以立刻回 ACCEPT 不是已经验过这块

**层次**：实现 / Process 何时调用。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Process 调用是同步的不是已经能在返回之后再改裁决 / 只做基本检查再异步 Process 不是已经还能再 Reject / 非验证者可以立刻回 ACCEPT 不是已经验过这块」，不是立刻整块执行就已经离开关键路径，也不是四门已经结算。不要另写怎样写 Process 何时调用。354 processwhen vs later bundled unbundling 续（815+816）；精读 [`worked-example-sync-notlater-vs-bundled.md`](worked-example-sync-notlater-vs-bundled.md)（不变量 815 item 1）；精读 [`worked-example-async-notreject-vs-bundled.md`](worked-example-async-notreject-vs-bundled.md)（不变量 816 item 2）。

## 官方三件事

规范把 Process 调用是同步的、异步之后不能再改票、非验证者可以立刻 ACCEPT 写成三件独立的实现事，不是「看见已经回了就已经能稍后改裁决、已经还能再 Reject、已经验过这块」一件事：

1. **看见 Process 调用是同步的 / 看见引擎在等回包 不是已经能在返回之后再改裁决，也不是已经离开关键路径。**  
   官方写：CometBFT 调 `ProcessProposal` 是同步的。看见是同步的，不是已经能稍后改裁决。看见引擎在等，不是已经离开关键路径。看见立刻执行，不是已经是立刻整块执行就已经离开关键路径。
2. **看见只做基本检查再异步 Process / 看见已经回了 `ACCEPT` 不是已经还能再 Reject，也不是已经还能强迫 prevote/precommit `nil`。**  
   官方写：应用可以先做基本检查再异步处理这块；这时不能再 Reject，也不能再强迫 prevote/precommit `nil`。看见异步了，不是已经还能改票。看见先回了，不是已经还能 Reject。看见还在跑，不是已经能强迫 `nil`。
3. **看见非验证者可以立刻回 `ACCEPT` / 看见不是验证者 不是已经验过这块，也不是已经是验证者也可以立刻交差。**  
   官方写：若 *p* 不是验证者，且应用不想让非验证者处理 `ProcessProposal`，可以立刻回 `ACCEPT`。看见立刻 `ACCEPT`，不是已经验过。看见不是验证者，不是已经交差。看见规范允许，不是已经是提议者那边也会叫 Process。

怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT 是规范里的做法，本页不抄。立刻整块执行就已经离开关键路径是不变量 327，本页不抄。

## 官方为什么这样拆

- **Process 调用是同步的 ≠ 已经能在返回之后再改裁决：** 官方把同步调用和稍后改裁决分开。
- **只做基本检查再异步 Process ≠ 已经还能再 Reject：** 官方把异步处理和还能改票分开。
- **非验证者可以立刻回 ACCEPT ≠ 已经验过这块：** 官方把立刻 ACCEPT 和已经验过分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 调用是同步的 | 不是已经能在返回之后再改裁决 | 不是立刻整块执行就已经离开关键路径（327） |
| 只做基本检查再异步 Process | 不是已经还能再 Reject | 不是四门已经结算（33） |
| 非验证者可以立刻回 ACCEPT | 不是已经验过这块 | 不是 Process 也会在提议者那边叫（351） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见已经回了就已经能稍后改裁决、已经还能再 Reject、已经验过这块」，必须分开 Process 调用是同步的是不是已经能在返回之后再改裁决、只做基本检查再异步 Process 是不是已经还能再 Reject、非验证者可以立刻回 ACCEPT 是不是已经验过这块。可以跳过「看见已经回了就已经能稍后改裁决」。不要另写怎样写 Process 何时调用。354 processwhen vs later bundled unbundling 续（815+816）。

## 本页不抄

- 怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
- 四门已经结算。那是不变量 33。
- Process 也会在提议者那边叫。那是不变量 351。
