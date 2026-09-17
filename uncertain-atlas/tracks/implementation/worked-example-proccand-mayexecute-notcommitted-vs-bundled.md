# 例：看见 ProcessProposal 里 Application MAY 像处理 FinalizeBlock 那样整块执行 / immediate execution 跑过了 / Process MAY fully execute is not already committed 不是已经 ProcessProposal 候选执行 bundled interchangeable / 已经交差 interchangeable / 已经是 ExecuteTxState interchangeable

**层次**：实现 / ProcessProposal MAY fully execute not already committed 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process MAY fully execute not already committed 不是 ProcessProposal 候选执行 bundled interchangeable / 不是已经交差 interchangeable / 不是已经是 ExecuteTxState interchangeable」，不是 ProcessProposal 候选执行 bundled（452），也不是 Prepare/Process 立刻执行出候选 bundled（311），也不是 Process REJECT assume not can't execute bundled（542）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 ProcessProposal 里 MAY 整块执行和已经交差、ExecuteTxState、本高度最终分开写成三件独立的实现事，不是「看见 Process 跑过就已经交差 interchangeable、已经是 ExecuteTxState interchangeable、已经能点名本高度最终 interchangeable」一件事：

1. **看见 ProcessProposal 里 Application MAY 像处理 FinalizeBlock 那样整块执行 / 看见 immediate execution 跑过了 / 看见 Process MAY fully execute is not already committed 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经交差 interchangeable / 已经 Finalize + Commit interchangeable，也不是已经 Process REJECT consensus assume not can't execute bundled（536 余量） interchangeable / 已经 can't execute interchangeable / 已经 candidate not committed interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable，也不是已经 AppHash 是本高度交易已经交差 bundled（147 余量） interchangeable / 已经本头 AppHash interchangeable。**  
   官方写：The Application may fully execute the block as though it was handling `FinalizeBlock`。Usage 也写：The Application MAY fully execute the block (immediate execution)。看见 MAY 整块执行，不是已经 Finalize + Commit 那种已经交差——452 bundled 常被写成「Process 跑过就已经交差」，本页钉 MAY fully execute not already committed 单句。看见像 Finalize 那样跑，不是已经 FinalizeBlock 套用 candidate（460 余量） interchangeable——460 钉 Finalize 确定执行 txs，本页钉 Process Usage MAY execute 单句。看见 immediate execution，不是已经 Process REJECT assume not can't execute（536 余量） interchangeable——536 钉 REJECT 与 MAY execute 可并存，本页钉 ACCEPT/REJECT 无关的 MAY execute not committed 单句。
2. **看见 Process MAY fully execute is not already ExecuteTxState / 看见像 Finalize 那样跑不是已经进 ExecuteTxState 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经是 ExecuteTxState interchangeable / 已经交差 interchangeable，也不是已经 Prepare/Process 立刻执行出候选 bundled（311） interchangeable / 已经 candidate 就是 ExecuteTxState interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经 CheckTxState 和 ExecuteTxState 可以并发 bundled（312 余量） interchangeable / 已经 CheckTx 过了就是 ExecuteTxState interchangeable，也不是已经 Process 不得改已提交状态 bundled（349 余量） interchangeable / 已经 Formal Requirement 9 已经测过 interchangeable / 已经 mutate committed state interchangeable，也不是已经 candidate state must be kept bundled（544 余量） interchangeable / 已经改了已提交状态 interchangeable。**  
   官方把 MAY 整块执行和进 ExecuteTxState 分开——452 bundled 常与 311 混成「Process 跑过就已经 ExecuteTxState」，本页钉 MAY execute not ExecuteTxState 单句。看见像 Finalize 那样跑，不是已经 Prepare/Process 立刻执行出候选（311） interchangeable——311 钉候选不是 ExecuteTxState，本页钉 Process Usage MAY execute 边界。看见 immediate execution，不是已经 CheckTxState / ExecuteTxState 并发（312 余量） interchangeable——312 钉 Check 和 Execute 分路，本页钉 Process MAY execute 单句。
3. **看见 Process MAY fully execute is not Process ACCEPT already final / 看见 Process 回了 ACCEPT 不是已经能点名本高度最终 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经能点名本高度最终 interchangeable / 已经 Process 回了 Accept 就已经换工作状态 interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable，也不是已经 ProcessProposal Response status valid/invalid bundled（533 余量） interchangeable / 已经 status ACCEPT interchangeable / 已经 assumes not valid interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（460 余量） interchangeable / 已经 Finalize 跑过就交差 interchangeable，也不是已经 candidate state must be kept bundled（544 余量） interchangeable / 已经 Process 回了 Accept 就已经换工作状态 interchangeable。**  
   官方把 Process MAY execute 和 Process 回了 ACCEPT 就已经最终分开——452 bundled 第三件事常与 430 混成「回了 ACCEPT 就已经交差」，本页钉 MAY execute not ACCEPT already final 单句。看见 Process 回了 ACCEPT，不是已经 ProcessProposalResponse.status ACCEPT（430 余量） interchangeable——430 钉 Response status 后效，本页钉 Usage MAY execute 边界。看见 immediate execution，不是已经 Finalize 确定执行（460 余量） interchangeable——460 钉 Finalize txs 交差，本页钉 Process MAY execute not committed 单句。

怎样做实现 candidate 缓存、怎样在 Finalize 套用 是规范里的做法，本页不抄。ProcessProposal 候选执行 bundled（452）、candidate state must be kept（544 余量）、read-only checks/processes（546 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **MAY fully execute not already committed ≠ ProcessProposal 候选执行 bundled interchangeable：** 官方把 immediate execution 和 Finalize + Commit 交差分开。
- **MAY execute not ExecuteTxState ≠ candidate is ExecuteTxState interchangeable：** 官方把 Process MAY execute 和 ExecuteTxState 分开。
- **MAY execute not ACCEPT already final ≠ Process resp ACCEPT settled interchangeable：** 官方把 Usage MAY execute 和 Response ACCEPT 后效分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MAY fully execute | 不是 already committed | 不是 Finalize + Commit 交差 |
| MAY execute | 不是 ExecuteTxState | 不是 Prepare/Process 候选 bundled（311） |
| Process MAY execute | 不是 ACCEPT already final | 不是 Process resp status bundled（430） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal MAY fully execute not already committed 正式三事，必须分开 MAY fully execute 是不是 already committed interchangeable / Finalize + Commit interchangeable、MAY execute 是不是 ExecuteTxState interchangeable / 311 candidate interchangeable、Process MAY execute 是不是 ACCEPT already final interchangeable / 430 ACCEPT settled interchangeable。可以跳过「看见 Process 跑过就已经交差 interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样做实现 candidate 缓存、怎样在 Finalize 套用。
- candidate state must be kept ≠ already changed committed state。那是不变量 544（452 item 2 余量）。
- read-only checks/processes ≠ already mutate committed state。那是不变量 546（452 item 3 余量）。
- Process REJECT assume not can't execute candidate。那是不变量 536。
