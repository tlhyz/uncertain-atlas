# 例：看见 ProcessProposal Contains all information on the proposed block needed to fully execute it / 看见含执行所需全部信息 is not already executed those txs / Finalize already ran 不是已经 ProcessProposal 含执行所需全部信息 bundled interchangeable / 已经 Finalize 跑过 interchangeable / 已经 Process MAY 整块执行就意味着已经交差 interchangeable

**层次**：实现 / ProcessProposal Contains all information not already executed 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Contains all information not already executed 不是 ProcessProposal 含执行所需全部信息 bundled interchangeable / 不是已经 Finalize 跑过 interchangeable / 不是已经 Process MAY 整块执行就意味着已经交差 interchangeable」，不是 ProcessProposal 含执行所需全部信息 bundled（453），也不是 ProcessProposal 候选执行 bundled（452），也不是 Process MAY fully execute not already committed（545）。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 官方三件事

规范把 ProcessProposal Contains all information on the proposed block needed to fully execute it 和已经执行那些交易、Finalize 跑过、Process MAY 整块执行交差分开写成三件独立的实现事，不是「看见 Process 含全部信息就已经执行那些交易 interchangeable、已经 Finalize 跑过 interchangeable、已经 Process MAY 整块执行就意味着已经交差 interchangeable」一件事：

1. **看见 ProcessProposal Contains all information on the proposed block needed to fully execute it / 看见含执行所需全部信息 is not already executed those txs / Finalize already ran 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经 immediate execution 交差 interchangeable / 已经 Finalize + Commit interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（460 余量） interchangeable / 已经不用再在 Process 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 AppHash 是本高度交易已经交差 bundled（147 余量） interchangeable / 已经本头 AppHash interchangeable / 已经本高度交易已经交差 interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable，也不是已经 ProcessProposal 含执行所需全部信息 bundled（453 第二件事 / 548 余量） interchangeable / 已经只有 PrepareProposalResponse.txs interchangeable / 已经 Request 八栏齐 interchangeable。**  
   官方写：Contains all information on the proposed block needed to fully execute it。看见能 fully execute 所需信息，不是已经 `FinalizeBlockRequest.txs` 已经按应用自己的规则确定地执行过——453 bundled 常被写成「看见 Process 含全部信息就已经执行那些交易」，本页钉 Contains all information not already executed 单句。看见有全部信息，不是已经 Process MAY 像 Finalize 整块执行（452）就已经是同一句 interchangeable——452 钉 MAY execute / candidate / read-only，本页钉 Usage「信息够执行」单句。看见能 fully execute，不是已经 FinalizeBlock 确定执行 txs（460 余量） interchangeable——460 钉 Finalize 确定执行，本页钉 Contains all information not executed 边界。
2. **看见 Contains all information is not Process MAY fully execute already committed / 看见含执行所需全部信息不是已经 Process MAY 整块执行就已经交差 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经 Process MAY 整块执行就意味着已经交差 interchangeable / 已经 immediate execution 交差 interchangeable，也不是已经 ProcessProposal MAY fully execute not already committed bundled（545 余量） interchangeable / 已经 MAY execute not committed interchangeable / 已经是 ExecuteTxState interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经交差 interchangeable / 已经改了已提交状态 interchangeable，也不是已经 candidate state must be kept bundled（544 余量） interchangeable / 已经 candidate not committed interchangeable / 已经 Process 回了 Accept 就换工作状态 interchangeable，也不是已经 read-only checks/processes bundled（546 余量） interchangeable / 已经 immediate execution committed interchangeable / 已经 checks/processes 就已经交差 interchangeable，也不是已经 ProcessProposal 含执行所需全部信息 bundled（453 第三件事 / 549 余量） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable。**  
   官方把「信息够执行」和 Process MAY 整块执行已经交差分开——453 bundled 常与 545 混成「含全部信息就已经 MAY execute 交差」，本页钉 Contains all information not MAY execute committed 单句。看见能 fully execute，不是已经 Process MAY fully execute not committed（545 余量） interchangeable——545 钉 Usage MAY execute not committed，本页钉 Contains all information 单句。看见有全部信息，不是已经 candidate state must be kept（544 余量） interchangeable——544 钉 candidate not committed，本页钉「信息够执行」边界。
3. **看见 Contains all information is not read-only checks/processes already settled / 看见含执行所需全部信息不是已经 read-only 处理就已经交差 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经 read-only 处理就已经交差 interchangeable / 已经 checks/processes 就已经执行那些交易 interchangeable，也不是已经 read-only checks/processes bundled（546 余量） interchangeable / 已经 mutate committed interchangeable / 已经 immediate execution committed interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable，也不是已经 ProcessProposal Response status valid/invalid bundled（533 余量） interchangeable / 已经 status ACCEPT interchangeable / 已经 assumes not valid interchangeable，也不是已经 ProcessProposal 含执行所需全部信息 bundled（453 第二件事 / 548 余量） interchangeable / 已经只有 PrepareProposalResponse.txs interchangeable / 已经 Request 八栏齐 interchangeable，也不是已经 FinalizeBlock 含刚决定那块字段 bundled（461 余量） interchangeable / 已经 newly decided block 字段 interchangeable。**  
   官方把 Contains all information needed to fully execute 和 read-only checks/processes 已经交差分开——453 bundled 常与 546 混成「含全部信息 = read-only 处理 = 已经执行那些交易」，本页钉 Contains all information not read-only settled 单句。看见能 fully execute，不是已经 read-only checks/processes（546 余量） interchangeable——546 钉 read-only not mutate committed / not immediate execution committed，本页钉 Contains all information 单句。看见有全部信息，不是已经 Process 回了 ACCEPT 就已经交差 interchangeable——430 钉 Response status 后效，本页钉 Usage Contains all information 边界。

怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐 是规范里的做法，本页不抄。ProcessProposal 含执行所需全部信息 bundled（453）、ProcessProposal 候选执行 bundled（452）、Process MAY fully execute not already committed（545）是另外那套，本页不抄。

## 官方为什么这样拆

- **Contains all information not already executed ≠ ProcessProposal 含执行所需全部信息 bundled interchangeable：** 官方把「信息够执行」和「已经执行那些交易 / Finalize 跑过」分开。
- **Contains all information not MAY execute committed ≠ Process MAY execute committed interchangeable：** 官方把 Contains all information 和 Process MAY 整块执行已经交差分开。
- **Contains all information not read-only settled ≠ read-only checks/processes committed interchangeable：** 官方把「信息够执行」和 read-only 处理已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Contains all information | 不是 already executed those txs | 不是 Finalize + Commit 交差（452） |
| 含执行所需全部信息 | 不是 MAY execute already committed | 不是 Process MAY execute（545） |
| Contains all information | 不是 read-only already settled | 不是 read-only checks/processes（546） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Contains all information not already executed 正式三事，必须分开 Contains all information 是不是 already executed those txs interchangeable / Finalize already ran interchangeable、Contains all information 是不是 MAY execute already committed interchangeable / 545 MAY execute interchangeable、Contains all information 是不是 read-only already settled interchangeable / 546 read-only interchangeable。可以跳过「看见 Process 含全部信息就已经执行那些交易 interchangeable」。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 本页不抄

- 怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐。
- Request 八栏齐 ≠ 已经只有 PrepareProposalResponse.txs。那是不变量 548（453 item 2 余量）。
- 含执行所需全部信息 ≠ 已经是 FinalizeBlockRequest 刚决定那块的字段。那是不变量 549（453 item 3 余量）。
- Process MAY fully execute not already committed。那是不变量 545（452 item 1 余量）。
