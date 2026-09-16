# 例：看见 FinalizeBlock Contains the fields of the newly decided block / 看见含刚决定那块的字段 is not already four gates settled / 看见 newly decided block is not already ran Process / Finalize already committed 不是已经 FinalizeBlock Contains newly decided block fields bundled（474） interchangeable / 已经四门已经结算 interchangeable / 已经跑过 Process interchangeable

**层次**：实现 / FinalizeBlock Contains newly decided block fields not already settled 正式三事（474 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Contains newly decided block fields not already settled 不是 FinalizeBlock Contains newly decided block fields bundled（474） interchangeable / 不是已经四门已经结算 interchangeable / 不是已经跑过 Process interchangeable」，不是 FinalizeBlock Contains newly decided block fields bundled（474），也不是 FinalizeBlock 含刚决定那块字段 bundled（461），也不是 FinalizeBlock Contains newly decided block fields not already settled（556）。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock Usage 第一句 Contains the fields of the newly decided block 和四门已经结算、Process 跑过、Process 回了 Accept 就换工作状态分开写成三件独立的实现事，不是「看见含刚决定那块的字段就已经四门已经结算 interchangeable、已经跑过 Process interchangeable、已经 Process 回了 Accept 就换工作状态 interchangeable」一件事：

1. **看见 FinalizeBlock Contains the fields of the newly decided block / 看见含刚决定那块的字段 is not already four gates settled / 看见 newly decided block is not already FinalizeBlock Contains newly decided block fields bundled（474） interchangeable / 已经四门已经结算 interchangeable / 已经 ABCI 1.0 三步 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 已经收成一门 interchangeable / 已经四门已经结算 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 FinalizeBlock 字段余量 bundled（407 余量） interchangeable / 已经实现必须确定 interchangeable / 已经 Info 回应用状态信息 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（461 第一件事 / 556 余量） interchangeable / 已经 ran Process interchangeable / 已经 Process ACCEPT switched working state interchangeable，也不是已经 FinalizeBlock newly decided block fields not ProcessProposal contains all information bundled（474 第二件事 / 560 余量） interchangeable / 已经 proposed block 字段 interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable。**  
   官方写：Contains the fields of the newly decided block。看见有刚决定那块的字段，不是已经 Finalize 等价于 ABCI 1.0 那三步（465）或收成一门（363）那种四门已经结算 interchangeable——474 bundled 第一件事常被写成「看见含刚决定那块的字段就已经四门已经结算」，本页钉 Contains newly decided block fields not already four gates settled 单句。看见 Contains the fields，不是已经 Finalize 字段余量 bundled（407 余量） interchangeable——407 钉含刚决定那块的字段 + 实现必须确定 + Info，本页钉 Usage Contains 单句。看见 newly decided block，不是已经 FinalizeBlock Contains newly decided block fields not already settled（556 余量） interchangeable——556 钉 461 bundled item 1 余量，本页钉 474 bundled item 1 边界。
2. **看见 Contains newly decided block fields is not already ran Process / 看见含刚决定那块的字段 is not already Prepare / Process 同一套字段就已经跑过 Process / 已经交差 不是已经 FinalizeBlock Contains newly decided block fields bundled（474） interchangeable / 已经跑过 Process interchangeable / 已经 Process 调用之前就已经跑过 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经不用再 Process interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（547 余量） interchangeable / 已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 immediate execution 交差 interchangeable / 已经 Finalize + Commit interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（461 第一件事 / 556 余量） interchangeable / 已经 Process ACCEPT switched working state interchangeable / 已经 candidate not committed interchangeable。**  
   官方把 Contains the fields of the newly decided block 和 Process 调用之前就已经跑过 Process / 已经交差分开——474 bundled 常与 360 混成「含刚决定那块的字段就已经跑过 Process」，本页钉 Contains newly decided block fields not already ran Process 单句。看见有字段，不是已经 Finalize 时的 Process 保证（360 余量） interchangeable——360 钉至少一名非拜占庭验证者跑过 Process，本页钉 Contains newly decided 单句。看见 newly decided block，不是已经 ProcessProposal Contains all information not already executed（547 余量） interchangeable——546 钉「信息够执行」≠ 已经执行，本页钉 Contains newly decided not ran Process 边界。
3. **看见 Contains newly decided block fields is not Process ACCEPT switched working state / 看见含刚决定那块的字段 is not already Process 回了 Accept 就换工作状态 不是已经 FinalizeBlock Contains newly decided block fields bundled（474） interchangeable / 已经 Process 回了 Accept 就换工作状态 interchangeable / 已经 candidate not committed interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 ACCEPT settled interchangeable / 已经 prevote interchangeable，也不是已经 candidate state must be kept bundled（545 余量） interchangeable / 已经 ready to discard interchangeable / 已经 Process ACCEPT switched working state interchangeable，也不是已经 ProcessProposal read-only checks/processes bundled（546 余量） interchangeable / 已经 mutate committed interchangeable / 已经 immediate execution committed interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（460 余量） interchangeable / 已经不用再在 Process 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 FinalizeBlock newly decided block fields not ProcessProposal contains all information bundled（474 第二件事 / 560 余量） interchangeable / 已经 proposed block 字段 interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable。**  
   官方把 Contains the fields of the newly decided block 和 Process 回了 Accept 就换工作状态分开——474 bundled 常与 452 混成「含刚决定那块的字段 = Process 回了 Accept 就已经换工作状态」，本页钉 Contains newly decided block fields not Process ACCEPT switched working state 单句。看见有字段，不是已经 candidate state must be kept（545 余量） interchangeable——544 钉 candidate not committed，本页钉 Contains newly decided 单句。看见 newly decided block，不是已经 ProcessProposal 候选执行（452 余量） interchangeable——452 钉 MAY execute / candidate，本页钉 Contains newly decided not ACCEPT switched 边界。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐 是规范里的做法，本页不抄。FinalizeBlock Contains newly decided block fields bundled（474）、FinalizeBlock 含刚决定那块字段 bundled（461）、Finalize 字段余量 bundled（407）是另外那套，本页不抄。

## 官方为什么这样拆

- **Contains newly decided block fields not already four gates settled ≠ FinalizeBlock Contains newly decided block fields bundled interchangeable：** 官方把 Contains the fields of the newly decided block 和收成一门的三步 / 四门已经结算分开。
- **Contains newly decided block fields not already ran Process ≠ Finalize Process guarantee interchangeable：** 官方把 Contains newly decided 和 Process 调用之前就已经跑过 Process 分开。
- **Contains newly decided block fields not Process ACCEPT switched working state ≠ 452 candidate interchangeable：** 官方把 Contains newly decided 和 Process 回了 Accept 就换工作状态分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Contains newly decided block fields | 不是 already four gates settled | 不是 Finalize 等价于 ABCI 1.0（465） |
| Contains newly decided block fields | 不是 already ran Process | 不是 Finalize Process guarantee（360） |
| Contains newly decided block fields | 不是 Process ACCEPT switched working state | 不是 ProcessProposal 候选执行（452） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Contains newly decided block fields not already settled 正式三事（474 余量），必须分开 Contains newly decided block fields 是不是 already four gates settled interchangeable / 363 / 465 equiv interchangeable、Contains newly decided block fields 是不是 already ran Process interchangeable / 360 Process guarantee interchangeable、Contains newly decided block fields 是不是 Process ACCEPT switched working state interchangeable / 452 candidate interchangeable。可以跳过「看见含刚决定那块的字段就已经四门已经结算 interchangeable」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐。
- newly decided block 不是 proposed block / ProcessProposal 含执行所需全部信息。那是不变量 560（474 item 2 余量）。
- fields of the newly decided block 不是 height/time match header 就代表对象已经分清。那是不变量 561（474 item 3 余量）。
- FinalizeBlock Contains newly decided block fields not already settled（461 余量）。那是不变量 556。
- FinalizeBlock Contains newly decided block fields bundled 三事。那是不变量 474。
