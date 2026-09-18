# 例：看见 Process whole-block-like-Finalize is not already ExecuteTxState interchangeable / not already Finalize-plus-Commit interchangeable / not already settled interchangeable

**层次**：实现 / Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事（408 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事（408 余量）/ not 1114 ftxs-notexec interchangeable / not 408 fintxs-vs-control bundled interchangeable」，不是 Finalize 执行余量 bundled（408），也不是候选已经是 ExecuteTxState（311），也不是立刻执行就已经交差（316）。不要另写怎样写 Finalize 执行余量。

## 官方三件事

1. **看见 Process 可以像在处理 Finalize 那样整块执行 / 看见整块跑了 这份栏 is not already 已经是 ExecuteTxState interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1114 ftxs-notexec interchangeable / 1112 ftxs-notsettle interchangeable / 408 fintxs item 1 exec-not-settled interchangeable，也不是已经 Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事 bundled（408 item 3 余量） interchangeable / 408 fintxs item 3 interchangeable。**  
   官方写：应用可以像在处理 FinalizeBlock 那样整块执行。看见整块跑了，不是已经是 ExecuteTxState interchangeable——本页从 408 item 3 侧钉 not already ExecuteTxState 单句。408 fintxs vs control bundled unbundling 在本页 item 3 完成。

2. **看见像 Finalize / 看见整块跑了 / 这份栏 is not already 已经 Finalize + Commit interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1114 ftxs-notexec interchangeable / 408 fintxs item 2 process-not-decided interchangeable / 1113 ftxs-notdec interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把像 Finalize 和已经 Finalize + Commit 分开。看见像 Finalize，不是已经 Finalize + Commit interchangeable。本页钉 not already Finalize-plus-Commit 单句。

3. **看见能跑 / 看见整块跑了 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1114 ftxs-notexec interchangeable / 1112 ftxs-notsettle interchangeable，也不是已经立刻执行就已经交差 interchangeable / 316 exectx interchangeable。**  
   官方把能跑和已经交差分开。看见能跑，不是已经交差 interchangeable。408 fintxs vs control bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process whole-block-like-Finalize not already ExecuteTxState ≠ 已经是 ExecuteTxState interchangeable：** 官方把像 Finalize 那样整块执行和候选已经是工作状态分开。
- **看见像 Finalize not already Finalize-plus-Commit ≠ 已经 Finalize + Commit interchangeable：** 官方把像 Finalize 和已经 Finalize + Commit 分开。
- **看见能跑 not already settled ≠ 已经交差 interchangeable：** 官方把能跑和已经交差分开；408 fintxs vs control bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 可以像在处理 Finalize 那样整块执行 | 不是已经是 ExecuteTxState | 不是候选已经是 ExecuteTxState（311） |
| 看见像 Finalize | 不是已经 Finalize + Commit | 不是立刻执行就已经交差（316） |
| 看见能跑 | 不是已经交差 | 不是先跑了就已经交差（1112） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事（408 余量），必须分开是不是已经是 ExecuteTxState、是不是已经 Finalize + Commit、是不是已经交差。可以跳过「看见填了 Finalize 执行余量就已经交差」。不要另写怎样写 Finalize 执行余量。408 fintxs vs control bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行。
- Finalize 执行余量 bundled。那是不变量 408。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 立刻执行就已经交差。那是不变量 316。
