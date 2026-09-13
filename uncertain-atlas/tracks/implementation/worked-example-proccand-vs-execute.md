# 例：看见 ProcessProposal 里 Application MAY 像处理 FinalizeBlock 那样整块执行不是已经交差；看见任何状态改动必须留作 candidate state、另一块被决定时要能丢掉不是已经改了已提交状态；看见 Application checks/processes the proposed block, which is read-only 不是已经改了上一份已提交状态

**层次**：实现 / ProcessProposal 候选执行正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Process MAY 像 Finalize 整块执行不是已经交差 / 须留 candidate state 不是已经改了已提交状态 / read-only 处理不是已经改了上一份已提交状态」，不是 Prepare/Process 立刻执行出候选那套通用内存上限，也不是 Process 回包 status 那套 prevote nil。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 ProcessProposal 里 MAY 整块执行、须留 candidate state、拟议块 read-only 处理写成三件独立的实现事，不是「看见 Process 跑过就已经交差、已经是 ExecuteTxState、已经改了已提交状态」一件事：

1. **看见 ProcessProposal 里 Application MAY 像处理 FinalizeBlock 那样整块执行 / 看见 immediate execution 跑过了 不是已经交差，也不是已经是 ExecuteTxState。**  
   官方写：The Application may fully execute the block as though it was handling `FinalizeBlock`。Usage 也写：The Application MAY fully execute the block (immediate execution)。看见 MAY 整块执行，不是已经 Finalize + Commit 那种已经交差。看见像 Finalize 那样跑，不是已经进 `ExecuteTxState`。看见 Process 回了 `ACCEPT`，不是已经能点名本高度最终。
2. **看见任何 resulting state changes 必须留作 candidate state、Application should be ready to discard it in case another block is decided / 看见留着 不是已经改了上一份已提交状态，也不是已经 Process 回了 Accept 就已经换工作状态。**  
   官方写：However, any resulting state changes must be kept as _candidate state_, and the Application should be ready to discard it in case another block is decided。看见必须留候选，不是已经改了 *s<sub>p,h-1</sub>*。看见另一块被决定，不是已经 Process 时产出的那份就可以不管。看见有 candidate，不是已经 Prepare/Process 立刻执行那套「不得改 ExecuteTxState」就已经是同一句 interchangeable。
3. **看见 Application checks/processes the proposed block, which is read-only / 看见处理了 不是已经改了上一份已提交状态，也不是已经 async 了还能 Reject。**  
   官方写：The Application checks/processes the proposed block, which is read-only, and returns `ACCEPT` or `REJECT`。看见 read-only，不是已经 Process 不得改已提交状态（349）就已经是同一句 interchangeable。看见 checks/processes，不是已经立刻执行就已经交差。When 也写：after doing some basic checks, and process the block asynchronously … will not be able to reject the block。看见 read-only 处理，不是已经 async 了还能 Reject（354 另一切片）。

怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存是规范里的做法，本页不抄。Prepare/Process 立刻执行出候选（311）是 Prepare 没有头哈希 / 丢掉不是永远不用再执行那套另一切片，Process 不得改已提交状态（349）是 Formal Requirement 9 那套另一切片，Process 回包 status（430）是 REJECT 会让 prevote nil 那套另一切片，本页不抄。

## 官方为什么这样拆

- **MAY 像 Finalize 整块执行 ≠ 已经交差 / 已经是 ExecuteTxState：** 官方把 immediate execution 和 Finalize + Commit 分开。
- **须留 candidate state、另一块决定时要能丢掉 ≠ 已经改了已提交状态：** 官方把候选和 *s<sub>p,h-1</sub>* 分开。
- **read-only 处理 ≠ 已经改了上一份已提交状态：** 官方把 checks/processes read-only 和已经 mutate committed state 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MAY 像 Finalize 整块执行 | 不是已经交差 / 已经是 ExecuteTxState | 不是 Prepare/Process 立刻执行出候选那套通用三事（311） |
| 须留 candidate state | 不是已经改了已提交状态 | 不是 Process 不得改已提交状态就已经是同一句（349） |
| read-only 处理 | 不是已经改了上一份已提交状态 | 不是只做基本检查再 async Process 就已经还能 Reject（354） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 跑过就已经交差、已经是 ExecuteTxState、已经改了已提交状态」，必须分开 Process MAY 像 Finalize 整块执行是不是已经交差 / 已经是 ExecuteTxState、须留 candidate state 是不是已经改了已提交状态、read-only 处理是不是已经改了上一份已提交状态。可以跳过「看见 Process 跑过就已经交差」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存。
- Prepare 没有头哈希 / 丢掉不是永远不用再执行。那是不变量 311。
- Prepare / Process / Extend / Verify 不得改已提交状态。那是不变量 349。
- Process 调用是同步的 / async 不能再 Reject。那是不变量 354。
- ProcessProposalResponse.status / REJECT 会让 prevote nil。那是不变量 430。
