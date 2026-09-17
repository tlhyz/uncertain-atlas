# 例：看见 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock / 看见收成一门 is not already Contains newly decided block fields interchangeable / 已经 Process 跑过就不用在 Finalize 再执行 interchangeable；不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 已经 finequiv bundled interchangeable

**层次**：实现 / FinalizeBlock equiv ABCI 1.0 not Contains newly decided / apply candidate 正式三事（586 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock equiv ABCI 1.0 not Contains newly decided / not apply candidate / not finequiv bundled（586） interchangeable / not 602 notgates interchangeable / not 603 notnoprep interchangeable」，不是 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586），也不是 Finalize 含刚决定那块字段 bundled（461 / 474 余量），也不是 Finalize 套用候选 bundled（460）。不要另写怎样写 Finalize 回包、怎样映射旧三步、怎样实现 candidate 缓存。

## 官方三件事

规范把 FinalizeBlock Usage 里 This method is equivalent to the call sequence BeginBlock, DeliverTx, and EndBlock in ABCI 1.0、Contains the fields of the newly decided block、executes the transactions in FinalizeBlockRequest.txs deterministically / Alternatively apply candidate state 和「已经是 finequiv bundled interchangeable / 已经 Process 跑过就不用在 Finalize 再执行 interchangeable」分开写成三件独立的实现事，不是「看见收成一门 就已经 Contains newly decided block fields interchangeable、已经 Process 跑过就不用在 Finalize 再执行 interchangeable、已经 finequiv bundled interchangeable」一件事：

1. **看见 FinalizeBlock 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门 is not already Contains the fields of the newly decided block interchangeable / 已经 newly decided block fields interchangeable / 已经含刚决定那块的字段 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 604 notnewdec interchangeable / 586 finequiv interchangeable / 602 notgates interchangeable / 603 notnoprep interchangeable / 461 finnewfields interchangeable / 474 finnewdec interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（474 余量 / 556） interchangeable / 555 not settled interchangeable / 407 finfields interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473 余量） interchangeable / 359 same fields interchangeable / 563 not passed means ran Process interchangeable，也不是已经 Finalize 含刚决定那块字段 bundled（461 余量） interchangeable / 557 not proposed interchangeable / 558 not dec/prop interchangeable。**  
   官方另写：Contains the fields of the newly decided block。看见收成一门，不是已经 newly decided block fields 就等于已经跑过 Process（461 / 474） interchangeable——461 钉 finnewfields bundled，474 钉 finnewdec bundled，本页从 586 item 3 侧钉 not Contains newly decided 单句。看见等价，不是已经 height/time match header 就代表对象已经分清（474 item 1 余量 / 561） interchangeable——561 钉 not match header，本页钉 586 item 3 第一件事。看见 BeginBlock/DeliverTx/EndBlock，不是已经 fill all fields 又填一遍（473） interchangeable——473 钉 even if passed，本页钉 Usage equiv not Contains newly decided 单句。
2. **看见 equiv / 看见收成一门 is not already Process 跑过 / 已经有 candidate 就不用在 Finalize 再执行 interchangeable / 已经 executes txs deterministically interchangeable / 已经 apply candidate state interchangeable / 已经 previously executed via Prepare or Process interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 604 notnewdec interchangeable / 586 finequiv interchangeable / 602 notgates interchangeable / 603 notnoprep interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 576 not committed interchangeable / 577 apply candidate interchangeable / 578 not no re-execute interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 executes block v interchangeable / 584 apply candidate interchangeable / 595 notcand interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 351 Process also on proposer interchangeable / 547 not already executed interchangeable / 546 candidate not committed interchangeable。**  
   官方另写：executes the transactions in FinalizeBlockRequest.txs deterministically before returning control；Alternatively, it can apply the candidate state corresponding to the same block previously executed via PrepareProposal or ProcessProposal。看见收成一门，不是已经 Process 整块执行过就不需要再在 Finalize 执行（460） interchangeable——460 钉 fincand bundled，本页钉 586 item 3 第二件事。看见等价，不是已经 Application executes block _v_（466） interchangeable——466 钉 When 第 3 步 executes block v，本页钉 not apply candidate / previously executed 单句。看见 deterministically execute txs，不是已经 apply candidate state not ExecuteTxState（577 / 584） interchangeable——577 从 460 侧钉 candidate，本页从 586 item 3 侧钉 not Process 就不需要 Finalize 单句。
3. **看见 equiv / 看见收成一门 is not already finequiv bundled（586） interchangeable / 已经 must provide 四列 interchangeable / 已经 no Prepare/Process interchangeable / 已经 four gates settled interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 604 notnewdec interchangeable / 602 notgates interchangeable / 603 notnoprep interchangeable / 600 notgates item 3 interchangeable / 363 finresp interchangeable，也不是已经 Finalize 回包义务 not four gates settled 正式三事（363 余量 / 600） interchangeable / 600 notgates interchangeable / 594 not settled interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477 余量） interchangeable / 595 notcand interchangeable / 596 notempty interchangeable，也不是已经 FinalizeBlock equiv not four gates settled（602 余量） interchangeable / 603 notnoprep interchangeable / 586 item 1 interchangeable / 586 item 2 interchangeable。**  
   官方把 586 finequiv bundled 三事里的 Contains newly decided / apply candidate 和 equiv 收成一门 / four gates settled / no Prepare/Process 分开——586 bundled 常与 item 1 / item 2 混成「看见收成一门 就已经 finequiv bundled interchangeable」，本页钉 586 item 3 第三件事。看见等价，不是已经 602 notgates（586 item 1 余量） interchangeable——602 另钉 not four gates settled，本页钉 item 3 单句。看见收成一门，不是已经 603 notnoprep（586 item 2 余量） interchangeable——603 另钉 not no Prepare/Process，本页钉 not Contains newly decided / apply candidate 单句。

怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock、怎样在 Finalize 套用 candidate 是规范里的做法，本页不抄。FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586）、FinalizeBlock equiv not four gates settled（602 / 586 item 1）、FinalizeBlock equiv not no Prepare/Process（603 / 586 item 2）、Finalize 含刚决定那块字段（461 / 474）、Finalize 套用候选（460）是另外那套，本页不抄。

## 官方为什么这样拆

- **equiv not Contains newly decided ≠ finnewfields / finnewdec bundled interchangeable：** 官方把收成一门和 newly decided block fields 分开。
- **equiv not apply candidate / previously executed ≠ fincand bundled / executes block v interchangeable：** 官方把 586 item 3 和 execute txs / apply candidate 路分开。
- **equiv not Contains newly decided / apply candidate ≠ finequiv bundled / 602 / 603 interchangeable：** 官方把 586 item 3 和 item 1 / item 2 / 363 finresp 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| equiv 收成一门 | 不是 already Contains newly decided | 不是 finnewfields bundled（461 / 474） |
| equiv 收成一门 | 不是 already apply candidate / previously executed | 不是 fincand bundled（460） |
| equiv 收成一门 | 不是 already finequiv bundled | 不是 not four gates（602 / 586 item 1） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not Contains newly decided / apply candidate 正式三事（586 余量），必须分开 equiv 是不是 already Contains newly decided block fields interchangeable / 461 finnewfields interchangeable / 474 finnewdec interchangeable / 473 finfill interchangeable、equiv 是不是 already Process 跑过就不用在 Finalize 再执行 interchangeable / 460 fincand interchangeable / 466 executes block v interchangeable / 577 apply candidate interchangeable、equiv 是不是 already finequiv bundled interchangeable / 602 notgates interchangeable / 603 notnoprep interchangeable / 600 notgates item 3 interchangeable。可以跳过「看见收成一门 就已经 Contains newly decided block fields interchangeable」。不要另写怎样写 Finalize 回包。

## 本页不抄

- 怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock、怎样在 Finalize 套用 candidate。
- FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled。那是不变量 586。
- FinalizeBlock equiv not four gates settled。那是不变量 602（586 item 1 余量）。
- FinalizeBlock equiv not no Prepare/Process。那是不变量 603（586 item 2 余量）。
- Finalize 含刚决定那块字段 bundled。那是不变量 461 / 474 余量。
- Finalize 套用候选 bundled。那是不变量 460。
- 四门已经结算。那是不变量 33。
