# 例：看见 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock / 看见收成一门 is not already no Prepare/Process interchangeable / 已经 ABCI++ 只剩 Finalize 一门 interchangeable；不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 已经 finequiv bundled interchangeable

**层次**：实现 / FinalizeBlock equiv ABCI 1.0 not no Prepare/Process 正式三事（586 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock equiv ABCI 1.0 not no Prepare/Process / not finequiv bundled（586） interchangeable / not 600 notgates item 3 interchangeable / not 586 item 3 Contains newly decided interchangeable」，不是 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586），也不是 Finalize 回包义务 not four gates settled item 3（600 / 363 item 1 余量）。不要另写怎样写 Finalize 回包、怎样映射旧三步。

## 官方三件事

规范把 FinalizeBlock Usage 里 This method is equivalent to the call sequence BeginBlock, DeliverTx, and EndBlock in ABCI 1.0 和「已经没有 Prepare/Process interchangeable / 已经 ABCI++ 只剩 Finalize 一门 interchangeable / 已经是 finequiv bundled interchangeable」分开写成三件独立的实现事，不是「看见收成一门 就已经没有 Prepare/Process、已经 CheckTx 过了就可以跳过 Prepare/Process、已经 finequiv bundled interchangeable」一件事：

1. **看见 FinalizeBlock 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门 is not already no Prepare/Process interchangeable / 已经 ABCI++ 只剩 Finalize 一门 interchangeable / 已经 PrepareProposal / ProcessProposal 可有可无 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 603 notnoprep interchangeable / 586 finequiv interchangeable / 602 notgates interchangeable / 600 notgates item 3 interchangeable / 363 finresp interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351 余量） interchangeable / 351 Process also on proposer interchangeable / 505 preparewhen collect interchangeable / 506 preparewhen return interchangeable，也不是已经 CheckTx 技术上可选、不参与处理块 bundled（373 余量） interchangeable / 373 CheckTx optional interchangeable / 339 CheckTx weak filter interchangeable。**  
   官方把 Finalize 收成 ABCI 1.0 那三步，和 ABCI++ 另设 Prepare / Process 门分开写。看见 BeginBlock/DeliverTx/EndBlock 在 Finalize 里，不是已经没有 PrepareProposal / ProcessProposal——586 bundled 第二件事常被写成「看见收成一门 就已经没有 Prepare/Process interchangeable」，本页从 586 侧钉 not no Prepare/Process 单句。看见收成一门，不是已经 Process 也会在提议者那边叫（351） interchangeable——351 钉提议者也会 Process，本页钉 586 item 2 边界。看见旧三步语义在 Finalize，不是已经 CheckTx 过了就可以跳过 Prepare / Process——373 钉 CheckTx optional，本页钉 Usage equiv not no Prepare/Process 单句。
2. **看见 equiv / 看见收成一门 is not already CheckTx 过了就可以跳过 Prepare / Process interchangeable / 已经 CheckTx 绿就可以提案 interchangeable / 已经 Process 回了 Accept 就不需要 Prepare interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 603 notnoprep interchangeable / 586 finequiv interchangeable / 602 notgates interchangeable / 600 notgates interchangeable，也不是已经 validValue 跳过 Prepare bundled（356 余量） interchangeable / 356 validvalue interchangeable / 505 preparewhen collect interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 354 processwhen later interchangeable / 360 Process guarantee interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472 余量） interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable。**  
   官方把 equiv 收成一门 和 CheckTx / Process Accept 已经等于可以跳过 Prepare/Process 分开——586 item 2 常与 339 / 356 混成「看见 CheckTx 过了 / Process Accept 就已经没有 Prepare/Process interchangeable」，本页钉 not CheckTx skip Prepare/Process 单句。看见收成一门，不是已经 validValue 跳过 Prepare（356） interchangeable——356 钉 validValue 非 nil 就不调 Prepare，本页钉 586 item 2 第二件事。看见等价，不是已经 Process 通常紧跟 Prepare（351） interchangeable——351 钉 Process 也会在提议者那边叫，本页钉 not no Prepare/Process 单句。
3. **看见 equiv / 看见收成一门 is not already finequiv bundled（586） interchangeable / 已经 Contains newly decided block fields interchangeable / 已经 Process 跑过就不用在 Finalize 再执行 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 603 notnoprep interchangeable / 602 notgates interchangeable / 586 finequiv item 3 interchangeable / 460 fincand interchangeable / 461 finnewfields interchangeable，也不是已经 Finalize 回包义务 not four gates settled 正式三事（363 余量 / 600） interchangeable / 600 notgates interchangeable / 363 finresp interchangeable / 594 not settled interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 executes block v interchangeable / 595 notcand interchangeable / 584 apply candidate interchangeable，也不是已经 Finalize 含刚决定那块字段 bundled（461 余量） interchangeable / 474 finnewdec interchangeable / 555 not settled interchangeable。**  
   官方把 586 finequiv bundled 三事里的 no Prepare/Process 和 Contains newly decided / apply candidate 分开——586 bundled 常与 item 3 混成「看见收成一门 就已经 finequiv bundled interchangeable」，本页钉 586 item 2 第三件事。看见收成一门，不是已经 586 finequiv item 3 interchangeable——586 item 3 另钉 Contains newly decided / apply candidate，本页钉 item 2 单句。看见等价，不是已经 600 notgates item 3（363 item 1 余量） interchangeable——600 从 363 finresp 侧钉同一 Usage 句，本页从 586 item 2 侧钉 not no Prepare/Process 单句。

怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock、怎样在 Finalize 套用 candidate 是规范里的做法，本页不抄。FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586）、FinalizeBlock equiv not four gates settled（602 / 586 item 1）、Finalize 回包义务 not four gates settled item 3（600 / 363 item 1）、Finalize 含刚决定那块字段（461）、Finalize 套用候选（460）是另外那套，本页不抄。

## 官方为什么这样拆

- **equiv not no Prepare/Process ≠ finequiv bundled interchangeable：** 官方把收成一门和 ABCI++ 仍保留 Prepare/Process 分开。
- **equiv not CheckTx skip Prepare/Process ≠ Process also on proposer / validValue skip Prepare interchangeable：** 官方把 586 item 2 和 351 / 356 / 339 分开。
- **equiv not no Prepare/Process ≠ Contains newly decided / apply candidate interchangeable：** 官方把 586 item 2 和 586 item 3 / 460 / 461 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| equiv 收成一门 | 不是 already no Prepare/Process | 不是 four gates settled（602 / 586 item 1） |
| equiv 收成一门 | 不是 already CheckTx skip Prepare/Process | 不是 Process also on proposer（351） |
| equiv 收成一门 | 不是 already finequiv bundled | 不是 Contains newly decided（586 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not no Prepare/Process 正式三事（586 余量），必须分开 equiv 是不是 already no Prepare/Process interchangeable / 351 Process also on proposer interchangeable / 373 CheckTx optional interchangeable、equiv 是不是 already CheckTx 过了就可以跳过 Prepare/Process interchangeable / 356 validvalue interchangeable / 339 CheckTx weak filter interchangeable、equiv 是不是 already finequiv bundled interchangeable / 586 item 3 Contains newly decided interchangeable / 600 notgates item 3 interchangeable。可以跳过「看见收成一门 就已经没有 Prepare/Process interchangeable」。不要另写怎样写 Finalize 回包。

## 本页不抄

- 怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock、怎样在 Finalize 套用 candidate。
- FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled。那是不变量 586。
- FinalizeBlock equiv not four gates settled。那是不变量 602（586 item 1 余量）。
- Finalize 回包义务 not four gates settled item 3。那是不变量 600（363 item 1 余量）。
- Contains newly decided block fields / apply candidate。那是不变量 586 item 3 余量 / 461 / 460。
- Process 也会在提议者那边叫。那是不变量 351。
- CheckTx 技术上可选。那是不变量 373。
