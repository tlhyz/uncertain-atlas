# 例：看见 Finalize 含刚决定那块的字段 / 看见填了字段 is not already four gates settled / 看见 newly decided block is not already ran Process / 看见 Contains is not already Finalize 字段余量 bundled（407） interchangeable / 已经四门已经结算 interchangeable / 已经跑过 Process interchangeable

**层次**：实现 / Finalize 含刚决定那块的字段 not already settled 正式三事（407 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 含刚决定那块的字段 not already settled / not finfields bundled（407） interchangeable / not four gates settled interchangeable / not ran Process interchangeable」，不是 Finalize 字段余量 bundled（407），也不是 FinalizeBlock 含刚决定那块字段 bundled（461），也不是 FinalizeBlock Contains newly decided block fields bundled（474）。不要另写怎样写 Finalize 字段余量。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlock` 含刚决定那块的字段 和四门已经结算、Process 跑过、实现必须确定 / Info 回应用状态信息 bundled interchangeable 分开写成三件独立的实现事，不是「看见填了 Finalize 字段余量就已经四门已经结算 interchangeable、已经跑过 Process interchangeable、已经实现必须确定 interchangeable」一件事：

1. **看见 Finalize 含刚决定那块的字段 / 看见填了字段 is not already four gates settled / 看见 newly decided block is not already Finalize 字段余量 bundled（407） interchangeable / 已经四门已经结算 interchangeable / 已经 ABCI 1.0 三步 interchangeable，也不是已经 Finalize 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock bundled（465 余量） interchangeable / 已经收成一门 interchangeable / 已经四门已经结算 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（461 第一件事 / 555 余量） interchangeable / 已经 ran Process interchangeable / 已经 Process ACCEPT switched working state interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（474 第一件事 / 564 余量） interchangeable / 已经 newly decided vs proposed interchangeable / 已经 height/time match header interchangeable，也不是已经 Finalize 字段余量 not already deterministic bundled（407 第二件事 / 574 余量） interchangeable / 已经像 Prepare 那样 interchangeable / 已经 Req 11–12 interchangeable。**  
   官方写：`FinalizeBlock` 含刚决定那块的字段。看见填了字段，不是已经 Finalize 等价于 ABCI 1.0 那三步（363 / 465 余量）那种四门已经结算 interchangeable——407 bundled 第一件事常被写成「看见填了 Finalize 字段余量就已经四门已经结算」，本页钉 Finalize 含刚决定那块的字段 not already four gates settled 单句。看见有刚决定那块，不是已经 fill all fields even if passed（363 余量） interchangeable——363 钉又填一遍，本页钉 407 item 1 边界。看见 newly decided block，不是已经 FinalizeBlock Contains newly decided block fields not already settled（564 余量 / 474 角度） interchangeable——564 钉 474 bundled 第一件事，本页钉 407 字段余量 单句。
2. **看见 Finalize 含刚决定那块的字段 is not already ran Process / 看见填了字段 is not already Prepare / Process 同一套字段就已经跑过 Process 不是已经 Finalize 字段余量 bundled（407） interchangeable / 已经跑过 Process interchangeable / 已经 Process 调用之前就已经跑过 interchangeable，也不是已经 Prepare 请求字段同一套 bundled（359 余量） interchangeable / 已经字段名对得上 interchangeable / 已经 local_last_commit interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable / 已经字段再填一遍 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already ran Process bundled（461 第一件事 / 555 余量） interchangeable / 已经 Process guarantee interchangeable / 已经 Process ACCEPT switched working state interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472 余量） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 has run ProcessProposal interchangeable，也不是已经 Finalize 字段余量 not Info handshake bundled（407 第三件事 / 575 余量） interchangeable / 已经握手对齐 interchangeable / 已经快照重放 interchangeable。**  
   官方把 Finalize 含刚决定那块的字段 和 Prepare / Process 同一套字段就已经跑过 Process 分开——407 bundled 常与 359 混成「填了字段 = 同一套字段名 = 已经跑过 Process」，本页钉 Finalize 含刚决定那块的字段 not already ran Process 单句。看见填了字段，不是已经 Prepare 请求字段同一套（359 余量） interchangeable——359 钉 Prepare 请求字段，本页钉 407 item 1 边界。看见 newly decided block，不是已经 Finalize 时的 Process 保证（360 余量） interchangeable——360 钉 guarantee bundled，本页钉 407 含刚决定那块的字段 单句。
3. **看见 Finalize 含刚决定那块的字段 is not already Contains the fields of the newly decided block bundled interchangeable / 看见填了字段 is not already FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经 newly decided block 字段 interchangeable / 已经 fill all fields interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（474 余量） interchangeable / 已经 newly decided vs proposed interchangeable / 已经 height/time match header interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not ProcessProposal full info bundled（461 第二件事 / 556 余量） interchangeable / 已经 proposed block 字段 interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable，也不是已经 FinalizeBlock fill all fields not decided/proposed interchangeable bundled（557 余量 / 473 角度） interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable / 已经 all fields 又填一遍 interchangeable，也不是已经 Finalize 字段余量 not already deterministic bundled（407 第二件事 / 574 余量） interchangeable / 已经 implementation must be deterministic interchangeable / 已经 state machine replication interchangeable。**  
   官方把 Finalize 含刚决定那块的字段 Usage 单句 和 Contains newly decided block fields 对象边界 bundled 分开——407 bundled 常与 461 / 474 混成「填了字段余量 = Contains newly decided bundled interchangeable」，本页钉 Finalize 含刚决定那块的字段 not Contains bundled 单句。看见填了字段，不是已经 FinalizeBlock 含刚决定那块字段 bundled（461 余量） interchangeable——461 钉 Contains / proposed vs decided / fill all fields 三事，本页钉 407 item 1 边界。看见 newly decided block，不是已经 Finalize 实现必须确定（407 item 2 / 574 余量） interchangeable——574 钉 deterministic / Prepare 对比，本页钉 407 item 1 not Contains bundled 单句。

怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info 是规范里的做法，本页不抄。Finalize 字段余量 bundled（407）、implementation must be deterministic not like Prepare（574 余量）、Info not handshake（575 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **Finalize 含刚决定那块的字段 not already four gates settled ≠ Finalize 字段余量 bundled interchangeable：** 官方把含刚决定那块的字段 和收成一门的三步 / 四门已经结算分开。
- **Finalize 含刚决定那块的字段 not already ran Process ≠ Prepare 同一套字段 interchangeable：** 官方把填了字段 和 Prepare / Process 同一套字段就已经跑过 Process 分开。
- **Finalize 含刚决定那块的字段 not Contains bundled interchangeable ≠ 461 / 474 newly decided bundled interchangeable：** 官方把 407 Usage 单句 和 Contains newly decided block fields 对象边界分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 含刚决定那块的字段 | 不是 already four gates settled | 不是 Finalize 等价于 ABCI 1.0（465） |
| Finalize 含刚决定那块的字段 | 不是 already ran Process | 不是 Prepare 请求字段同一套（359） |
| Finalize 含刚决定那块的字段 | 不是 Contains bundled interchangeable | 不是 FinalizeBlock 含刚决定那块字段 bundled（461） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 含刚决定那块的字段 not already settled 正式三事（407 余量），必须分开 Finalize 含刚决定那块的字段 是不是 already four gates settled interchangeable / 407 bundled interchangeable / 465 ABCI equiv interchangeable、Finalize 含刚决定那块的字段 是不是 already ran Process interchangeable / 359 Prepare 同一套字段 interchangeable / 360 Process guarantee interchangeable、Finalize 含刚决定那块的字段 是不是 Contains bundled interchangeable / 461 bundled interchangeable / 474 bundled interchangeable。可以跳过「看见填了 Finalize 字段余量就已经四门已经结算 interchangeable」。不要另写怎样写 Finalize 字段余量。

## 本页不抄

- 怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info。
- Finalize 实现必须确定 not like Prepare。那是不变量 574（407 item 2 余量）。
- Info not handshake aligned。那是不变量 575（407 item 3 余量）。
- FinalizeBlock Contains newly decided block fields not already settled（461/474 角度）。那是不变量 555 / 564。
