# 例：看见 any resulting state changes must be kept as candidate state / Application should be ready to discard it in case another block is decided / candidate state is not already changed committed state 不是已经 ProcessProposal 候选执行 bundled interchangeable / 已经改了已提交状态 interchangeable / 已经 Process 回了 Accept 就已经换工作状态 interchangeable

**层次**：实现 / ProcessProposal candidate state not already committed 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「candidate state not already committed 不是 ProcessProposal 候选执行 bundled interchangeable / 不是已经改了已提交状态 interchangeable / 不是已经 Process 回了 Accept 就已经换工作状态 interchangeable」，不是 ProcessProposal 候选执行 bundled（452），也不是 Process MAY fully execute not committed bundled（543），也不是 Process 不得改已提交状态 bundled（349）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 ProcessProposal 里须留 candidate state、另一块决定时要能丢掉、候选和已提交状态分开写成三件独立的实现事，不是「看见 Process 留着 candidate 就已经改了已提交状态 interchangeable、已经 Process 回了 Accept 就已经换工作状态 interchangeable、已经 Prepare/Process 立刻执行 bundled interchangeable」一件事：

1. **看见 any resulting state changes must be kept as candidate state / 看见任何状态改动必须留作 candidate state / 看见 candidate state is not already changed committed state 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经改了已提交状态 interchangeable / 已经改了 *s<sub>p,h-1</sub>* interchangeable，也不是已经 Process MAY fully execute not already committed bundled（543 余量） interchangeable / 已经交差 interchangeable / 已经是 ExecuteTxState interchangeable，也不是已经 Process 不得改已提交状态 bundled（349 余量） interchangeable / 已经 Formal Requirement 9 已经测过 interchangeable / 已经 mutate committed state interchangeable，也不是已经 Prepare/Process 立刻执行出候选 bundled（311 余量） interchangeable / 已经不得改 ExecuteTxState interchangeable / 已经 candidate 就是 ExecuteTxState interchangeable，也不是已经 Process REJECT assume not can't execute bundled（542 余量） interchangeable / 已经 candidate not committed interchangeable / 已经 REJECT can't execute interchangeable。**  
   官方写：However, any resulting state changes must be kept as _candidate state_。看见必须留候选，不是已经改了上一份已提交状态——452 bundled 常被写成「留着 candidate 就已经改了 s_{p,h-1}」，本页钉 candidate state not already committed 单句。看见 candidate state，不是已经 Process MAY fully execute not committed（543 余量） interchangeable——543 钉 MAY execute not committed，本页钉 candidate must be kept 单句。看见 must be kept，不是已经 Process 不得改已提交状态（349 余量） interchangeable——349 钉 Req 9 no side effects on committed state，本页钉 candidate state 边界。
2. **看见 Application should be ready to discard it in case another block is decided / 看见另一块被决定时要能丢掉 不是已经 Process 时产出的那份就可以不管 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经另一块决定就不用管 interchangeable / 已经 Process 产出就可以不管 interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 Prepare 事件保留路径 bundled（451 余量） interchangeable / 已经 REJECT 时就可以丢掉不算 interchangeable / 已经 prevote nil interchangeable，也不是已经 ProcessProposalResponse.status is REJECT bundled（430 余量） interchangeable / 已经 prevote nil interchangeable / 已经 assumes not valid interchangeable，也不是已经 read-only checks/processes bundled（545 余量） interchangeable / 已经 async 了还能 Reject interchangeable。**  
   官方写：and the Application should be ready to discard it in case another block is decided。看见要能丢掉，不是已经另一块被决定就不用管 interchangeable——452 bundled 常与 460 混成「有 candidate 就不用再在 Finalize 执行」，本页钉 ready to discard 单句。看见 discard，不是已经 FinalizeBlock 套用 candidate（460 余量） interchangeable——460 钉 Finalize 确定执行 txs / 可套用 candidate，本页钉 Process Usage candidate discard 边界。看见 another block decided，不是已经 Prepare 事件 REJECT 时就可以丢掉（451 余量） interchangeable——451 钉 Prepare events retention，本页钉 Process candidate discard 单句。
3. **看见 candidate state is not Process ACCEPT already switched working state / 看见留着 candidate state 不是已经 Process 回了 Accept 就已经换工作状态 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经 Process 回了 Accept 就已经换工作状态 interchangeable / 已经能点名本高度最终 interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable，也不是已经 Process MAY fully execute not ACCEPT already final bundled（543 余量） interchangeable / 已经 ACCEPT already final interchangeable / 已经 immediate execution 交差 interchangeable，也不是已经 Prepare/Process 立刻执行出候选 bundled（311 余量） interchangeable / 已经 candidate 就是 ExecuteTxState interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 已经套用 candidate 就是 ExecuteTxState interchangeable。**  
   官方把 candidate state 和 Process 回了 ACCEPT 就已经换工作状态分开——452 bundled 常与 430 混成「回了 ACCEPT 就已经换工作状态」，本页钉 candidate not ACCEPT switched working state 单句。看见 candidate state，不是已经 ProcessProposalResponse.status ACCEPT（430 余量） interchangeable——430 钉 Response status 后效，本页钉 candidate must be kept 边界。看见 must be kept，不是已经 Process MAY execute not ACCEPT final（543 余量） interchangeable——543 钉 MAY execute not final，本页钉 candidate state 单句。

怎样做实现 candidate 缓存、怎样在 Finalize 套用 是规范里的做法，本页不抄。ProcessProposal 候选执行 bundled（452）、Process MAY fully execute not committed（543）、read-only checks/processes（545 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **candidate state not already committed ≠ ProcessProposal 候选执行 bundled interchangeable：** 官方把 candidate state 和已提交状态 *s<sub>p,h-1</sub>* 分开。
- **ready to discard ≠ Finalize apply candidate interchangeable：** 官方把 discard candidate 和 Finalize 套用 candidate 分开。
- **candidate not ACCEPT switched working state ≠ Process resp ACCEPT settled interchangeable：** 官方把 candidate must be kept 和 Response ACCEPT 后效分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| candidate state | 不是 already committed | 不是 Process 不得改已提交状态（349） |
| ready to discard | 不是 can ignore output | 不是 Finalize apply candidate（460） |
| candidate must be kept | 不是 ACCEPT switched state | 不是 Process resp status bundled（430） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal candidate state not already committed 正式三事，必须分开 candidate state 是不是 already changed committed state interchangeable / 349 mutate committed interchangeable、ready to discard 是不是 Finalize apply candidate interchangeable / 460 no re-execute interchangeable、candidate must be kept 是不是 Process ACCEPT switched working state interchangeable / 430 ACCEPT settled interchangeable。可以跳过「看见 Process 留着 candidate 就已经改了已提交状态 interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样做实现 candidate 缓存、怎样在 Finalize 套用。
- Process MAY fully execute not already committed。那是不变量 543（452 item 1 余量）。
- read-only checks/processes ≠ already mutate committed state。那是不变量 545（452 item 3 余量）。
- Process REJECT assume candidate not committed。那是不变量 542。
