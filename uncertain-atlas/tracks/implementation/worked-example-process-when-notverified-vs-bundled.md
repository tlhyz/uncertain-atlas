# 例：看见非验证者可以立刻回 ACCEPT is not already verified this block interchangeable / not already validators can skip interchangeable / not already settled interchangeable

**层次**：实现 / 非验证者可以立刻回 ACCEPT not already verified this block / not already validators can skip / not already settled 正式三事（354 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「非验证者可以立刻回 ACCEPT not already verified this block / not already validators can skip / not already settled 正式三事（354 余量）/ not 859 process-when-notverified interchangeable / not 354 process-when-vs-later bundled interchangeable」，不是 Process 何时调用 bundled（354），也不是 Process 也会在提议者那边叫（351），也不是四门已经结算（33）。不要另写怎样写 Process 何时调用。

## 官方三件事

1. **看见非验证者可以立刻回 `ACCEPT` / 看见不是验证者 这份立刻 is not already 已经验过这块 interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 859 process-when-notverified interchangeable / 857 process-when-notlater interchangeable / 354 process-when item 1 同步 interchangeable，也不是已经非验证者可以立刻回 ACCEPT not already verified this block / not already validators can skip / not already settled 正式三事 bundled（354 item 3 余量） interchangeable / 354 process-when item 3 interchangeable。**  
   官方写：若 *p* 不是验证者，且应用不想让非验证者处理 `ProcessProposal`，可以立刻回 `ACCEPT`。看见立刻 `ACCEPT`，不是已经验过这块 interchangeable——本页从 354 item 3 侧钉 not already verified this block 单句。354 process-when vs later bundled unbundling 在本页 item 3 完成。

2. **看见不是验证者 / 看见规范允许立刻 `ACCEPT` / 这份立刻 is not already 已经是验证者也可以立刻交差 interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 859 process-when-notverified interchangeable / 354 process-when item 2 异步 interchangeable / 858 process-when-notreject interchangeable，也不是已经 Process 也会在提议者那边叫 interchangeable / 351 process-also interchangeable。**  
   官方把规范允许和已经是验证者也可以立刻交差分开——354 bundled 第三件事常与 351 混成「看见立刻 ACCEPT 就已经验过这块或已经是验证者也可以立刻交差 interchangeable」，本页钉 not already validators can skip 单句。

3. **看见不是验证者 / 看见立刻 `ACCEPT` / 这份立刻 is not already 已经交差 interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 859 process-when-notverified interchangeable / 857 process-when-notlater interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把立刻 `ACCEPT` 和已经交差分开。看见立刻 `ACCEPT`，不是已经交差 interchangeable。354 process-when vs later bundled unbundling 在本页 item 3 完成。

怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **非验证者可以立刻回 ACCEPT not already verified this block ≠ 已经验过这块 interchangeable：** 官方把立刻 ACCEPT 和已经验过分开。
- **看见规范允许 not already validators can skip ≠ 已经是验证者也可以立刻交差 interchangeable：** 官方把规范允许和已经是验证者也可以立刻交差分开。
- **看见立刻 ACCEPT not already settled ≠ 已经交差 interchangeable：** 官方把立刻 ACCEPT 和已经交差分开；354 process-when vs later bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 非验证者可以立刻回 ACCEPT | 不是已经验过这块 | 不是 Process 也会在提议者那边叫（351） |
| 看见规范允许立刻 ACCEPT | 不是已经是验证者也可以立刻交差 | 不是四门已经结算（33） |
| 看见立刻 ACCEPT | 不是已经交差 | 不是同步就已经能稍后改裁决（857） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看非验证者可以立刻回 ACCEPT not already verified this block / not already validators can skip / not already settled 正式三事（354 余量），必须分开是不是已经验过这块、是不是已经是验证者也可以立刻交差、是不是已经交差。可以跳过「看见立刻 ACCEPT 就已经验过这块」。不要另写怎样写 Process 何时调用。354 process-when vs later bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT。
- Process 何时调用 bundled。那是不变量 354。
- Process 调用是同步的。那是不变量 354 item 1 余量 / 857。
- Process 也会在提议者那边叫。那是不变量 351。
- 四门已经结算。那是不变量 33。
