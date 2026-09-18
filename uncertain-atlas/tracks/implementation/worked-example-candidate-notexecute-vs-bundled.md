# 例：看见立刻执行出一份候选 / 内存里有状态 is not already already ExecuteTxState interchangeable / already can name this height final interchangeable / already settled interchangeable

**层次**：实现 / 候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事（311 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事（311 余量）/ not 693 candidate-notexecute interchangeable / not 311 candidate bundled interchangeable」，不是候选 ≠ ExecuteTxState bundled（311），也不是 Prepare 没有头哈希（692 item 1 余量）或丢掉不是已经永远不用再执行（694 item 3 余量）。不要另写怎样缓存候选或怎样对上决定块。

## 官方三件事

规范把 Requirements 里应用可以在 `PrepareProposal` / `ProcessProposal` 立刻执行、立刻执行的结果叫候选状态应留在内存里当可能的最终、执行提案**不得**改 `ExecuteTxState`、要等 `FinalizeBlock` 确认哪一份才能用来更新、**无法准确预测**哪一块会被决定交到本高度 `FinalizeBlock` 和「已经是立刻执行出候选就已经是 ExecuteTxState interchangeable / 已经是内存里有就已经能点名本高度最终 interchangeable / 已经是能加快 Finalize 就已经交差 interchangeable / 已经是候选 ≠ ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见立刻执行 就已经进工作状态 interchangeable / 就已经能预测 Finalize 交哪一块 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见立刻执行出一份候选 / 看见跑过了 / 看见 Prepare 或 Process 立刻执行了 is not already 已经是 ExecuteTxState interchangeable / 已经进工作状态 interchangeable / 已经改了 ExecuteTxState interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 693 candidate-notexecute interchangeable / 311 candidate item 2 interchangeable，也不是已经候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事 bundled（311 item 2 余量） interchangeable / 311 candidate item 2 interchangeable，也不是已经 Prepare 没有头哈希（692） interchangeable / 694 candidate-notdiscarded interchangeable / 310 commitlock interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：立刻执行的结果叫候选状态；执行提案**不得**改 `ExecuteTxState`，要等 `FinalizeBlock` 确认哪一份（如果有）才能用来更新。看见跑过了，不是已经进工作状态 interchangeable——311 钉 bundled 三事，本页从 item 2 侧钉 not already ExecuteTxState 单句。看见立刻执行出一份候选，不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable——311 钉 bundled，本页钉 item 2 第一件事。看见 Prepare 或 Process 立刻执行了，不是已经 Prepare 没有头哈希（692） interchangeable——692 另钉 item 1，本页钉 item 2 第一件事。311 candidate vs execute bundled unbundling 在本页 item 2 启动。

2. **看见内存里有状态 / 看见候选状态留在内存 / 看见可能的最终 is not already 已经能点名本高度最终 interchangeable / 已经 can name this height final interchangeable / 已经能预测 Finalize 会交哪一块 interchangeable / 311 candidate bundled interchangeable / 403 finafter interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 693 candidate-notexecute interchangeable / 311 candidate item 1 头哈希 interchangeable / 311 candidate item 3 丢掉候选 interchangeable，也不是已经候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事 bundled（311 item 2 余量） interchangeable / 311 candidate item 2 interchangeable，也不是已经是 ExecuteTxState（本页第一件事） interchangeable。**  
   官方把候选留在内存当可能的最终 和已经能点名本高度最终 / 已经能准确预测哪一块被决定路径分开——同一高度可以叫很多次，**无法准确预测**哪一块会被决定。看见内存里有，不是已经能点名本高度最终 interchangeable——本页钉 not already can name this height final 单句。看见候选状态留在内存，不是已经 Prepare 没有头哈希（692） interchangeable——692 另钉 item 1，本页钉 item 2 第二件事。看见可能的最终，不是已经丢掉不是已经永远不用再执行（694） interchangeable——694 另钉 item 3，本页钉 item 2 第二件事。311 candidate vs execute bundled unbundling 在本页 item 2 启动。

3. **看见能加快 Finalize / 看见更快套用内存里那份 / 看见 Quick FinalizeBlock execution is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经 Finalize + Commit interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 693 candidate-notexecute interchangeable / 311 candidate item 1 / 311 candidate item 3，也不是已经候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事 bundled（311 item 2 余量） interchangeable / 311 candidate item 2 interchangeable，也不是已经是 ExecuteTxState（本页第一件事） interchangeable / 已经能点名本高度最终（本页第二件事） interchangeable。**  
   官方把让 Finalize 更快套用内存里那份 和已经交差路径分开——加快套用意图不等于已经 Finalize 交差，也不等于已经进 ExecuteTxState。看见能加快 Finalize，不是已经交差 interchangeable——本页钉 not already settled 单句。看见更快套用内存里那份，不是已经是 ExecuteTxState（本页第一件事） interchangeable——三件事分开钉。看见 Quick FinalizeBlock execution，不是已经四门已经结算（33） interchangeable——33 另钉。311 candidate vs execute bundled unbundling 在本页 item 2 完成。

怎样缓存候选、怎样对上决定块、怎样写四门是规范里的做法，本页不抄。候选 ≠ ExecuteTxState bundled（311）、Prepare 没有头哈希（311 item 1 余量 / 692）、丢掉不是已经永远不用再执行（311 item 3 余量 / 694）、四门已经结算（33）、默认锁已经 RPC 安全（310）、半写已经原子（5）是另外那套，本页不抄。

## 官方为什么这样拆

- **立刻执行 not already ExecuteTxState ≠ 311 / 33 interchangeable：** 官方把跑过了单句和已经进工作状态路径分开。
- **内存里有 not already can name this height final ≠ 已经能预测 Finalize 交哪一块 interchangeable：** 官方把候选留内存单句和已经点名本高度最终路径分开。
- **能加快 Finalize not already settled ≠ 已经交差 interchangeable：** 官方把加快套用意图单句和已经 Finalize 交差路径分开；311 candidate vs execute bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻执行出候选 | 不是 already ExecuteTxState | 不是 Prepare 没有头哈希 alone（692） |
| 内存里有状态 | 不是 already can name this height final | 不是丢掉候选 alone（694） |
| 能加快 Finalize | 不是 already settled | 不是四门已经结算（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事（311 余量），必须分开立刻执行 是不是 already ExecuteTxState interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable、内存里有 是不是 already can name this height final interchangeable、能加快 Finalize 是不是 already settled interchangeable / 403 finafter interchangeable。可以跳过「看见立刻执行 就已经进工作状态 interchangeable / 就已经能预测 Finalize 交哪一块 interchangeable / 就已经交差 interchangeable」。不要另写怎样缓存候选。311 candidate vs execute bundled unbundling 在本页 item 2 完成；完成见 [`worked-example-candidate-notdiscarded-vs-bundled.md`](worked-example-candidate-notdiscarded-vs-bundled.md)（不变量 694 item 3）。

## 本页不抄

- 怎样缓存候选、怎样对上决定块、怎样写四门。
- 候选 ≠ ExecuteTxState bundled。那是不变量 311。
- Prepare 没有头哈希。那是不变量 311 item 1 余量 / 692。
- 丢掉不是已经永远不用再执行。那是不变量 311 item 3 余量 / 694。
- 四门已经结算。那是不变量 33。
- 默认锁已经 RPC 安全。那是不变量 310。
- 半写已经原子。那是不变量 5。
