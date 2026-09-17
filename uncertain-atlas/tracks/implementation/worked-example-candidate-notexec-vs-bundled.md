# 例：看见立刻执行出候选 is not already ExecuteTxState interchangeable / not already this-final interchangeable / not already settled interchangeable

**层次**：实现 / 立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事（311 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事（311 余量）/ not 972 candidate-notexec interchangeable / not 311 candidate-vs-execute bundled interchangeable」，不是候选 bundled（311），也不是默认锁已经 RPC 安全（310），也不是 Finalize 已经确定性（342）。不要另写怎样缓存候选或怎样算头哈希。

## 官方三件事

1. **看见立刻执行出一份候选 / 看见内存里有状态 这份候选 is not already 已经是 ExecuteTxState interchangeable，也不是已经候选 bundled（311） interchangeable / 972 candidate-notexec interchangeable / 971 candidate-nothash interchangeable / 311 candidate item 1 Prepare 没有头哈希 interchangeable，也不是已经立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事 bundled（311 item 2 余量） interchangeable / 311 candidate item 2 interchangeable。**  
   官方写：应用可以在 PrepareProposal / ProcessProposal 立刻执行，好避开非法交易，或让 FinalizeBlock 更快套用内存里那份。执行提案不得改 ExecuteTxState，要等 FinalizeBlock 确认哪一份（如果有）才能用来更新。看见跑过了，不是已经进工作状态 interchangeable——本页从 311 item 2 侧钉 not already ExecuteTxState 单句。311 candidate vs execute bundled unbundling 在本页 item 2 续。

2. **看见内存里有 / 看见跑过了 / 这份候选 is not already 已经能点名本高度最终 interchangeable，也不是已经候选 bundled（311） interchangeable / 972 candidate-notexec interchangeable / 311 candidate item 3 丢掉候选 interchangeable / 973 candidate-notdrop interchangeable，也不是已经默认锁已经 RPC 安全 interchangeable / 310 commit-lock interchangeable。**  
   官方写：这两门在同一高度可以叫很多次，无法准确预测哪一块会被决定、交到本高度的 FinalizeBlock。看见内存里有，不是已经能点名本高度最终 interchangeable。本页钉 not already this-final 单句。

3. **看见能加快 Finalize / 看见跑过了 / 这份候选 is not already 已经交差 interchangeable，也不是已经候选 bundled（311） interchangeable / 972 candidate-notexec interchangeable / 971 candidate-nothash interchangeable，也不是已经 Finalize 已经确定性 interchangeable / 342 finalize-det interchangeable。**  
   官方把能加快 Finalize 和已经交差分开。看见能加快 Finalize，不是已经交差 interchangeable。311 candidate vs execute bundled unbundling 在本页 item 2 续。

字段表、怎样实现缓存、内存上限取值是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **立刻执行出候选 not already ExecuteTxState ≠ 已经是 ExecuteTxState interchangeable：** 官方把候选、工作状态、无法预测哪一块被决定分开。
- **看见内存里有 not already this-final ≠ 已经能点名本高度最终 interchangeable：** 官方把内存里有和已经能点名本高度最终分开。
- **看见能加快 Finalize not already settled ≠ 已经交差 interchangeable：** 官方把能加快 Finalize 和已经交差分开；311 candidate vs execute bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻执行出候选 | 不是已经是 ExecuteTxState | 不是默认锁已经 RPC 安全（310） |
| 看见内存里有 | 不是已经能点名本高度最终 | 不是 Finalize 已经确定性（342） |
| 看见能加快 Finalize | 不是已经交差 | 不是丢掉就已经永远不用再执行（973） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事（311 余量），必须分开是不是已经是 ExecuteTxState、是不是已经能点名本高度最终、是不是已经交差。可以跳过「看见立刻执行就已经是本高度最终」。不要另写怎样缓存候选或怎样算头哈希。311 candidate vs execute bundled unbundling 在本页 item 2 续；续 [`worked-example-candidate-notdrop-vs-bundled.md`](worked-example-candidate-notdrop-vs-bundled.md)（不变量 973 item 3）。

## 本页不抄

- 字段表、怎样实现候选缓存、内存上限取值。
- 候选 bundled。那是不变量 311。
- 默认锁已经 RPC 安全。那是不变量 310。
- Finalize 已经确定性。那是不变量 342。
