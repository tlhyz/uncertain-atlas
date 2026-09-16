# 例：看见 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` / 看见引擎会把 Finalize 请求全部字段填齐 is not already Prepare / Process 给过就不用再 Finalize / 看见 will fill up all fields is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经 Prepare/Process 给过就不用再 Finalize interchangeable / 已经交差 interchangeable

**层次**：实现 / FinalizeBlock fill all fields not already don't need Finalize 正式三事（473 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「will fill up all fields not already don't need Finalize 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 不是已经 Prepare/Process 给过就不用再 Finalize interchangeable / 不是已经交差 interchangeable」，不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473），也不是 fill all fields not decided/proposed interchangeable（558），也不是 fill all fields not passed means ran Process（563 余量）。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock Usage 里 Currently / CometBFT will fill up all fields in `FinalizeBlockRequest` 和 Prepare/Process 已经传过就不叫 Finalize、Finalize + Commit 已经交差、Contains the fields of the newly decided block bundled 分开写成三件独立的实现事，不是「看见 will fill up all fields 就已经 Prepare/Process 给过就不用再 Finalize interchangeable、已经交差 interchangeable、已经 Contains newly decided bundled interchangeable」一件事：

1. **看见 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` / 看见引擎会把 Finalize 请求全部字段填齐 is not already Prepare / Process 给过就不用再 Finalize / 看见 will fill up all fields is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经 Prepare/Process 给过就不用再 Finalize interchangeable / 已经 even if passed interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 传过 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 已经收成一门 interchangeable / 已经四门已经结算 interchangeable，也不是已经 FinalizeBlock fill all fields not decided/proposed interchangeable bundled（558 余量） interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable / 已经 all fields 又填一遍 interchangeable，也不是已经 FinalizeBlock fill all fields not passed means ran Process bundled（473 第二件事 / 563 余量） interchangeable / 已经字段名对得上就代表已经跑过 Process interchangeable / 已经 newly decided 和 proposed interchangeable，也不是已经 FinalizeBlock fill all fields not decided/proposed interchangeable bundled（473 第三件事 / 564 余量） interchangeable / 已经 decided/proposed interchangeable / 已经 ran Process means don't need Finalize interchangeable。**  
   官方 Usage 写：Currently, CometBFT will fill up all fields in `FinalizeBlockRequest`, even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest`。看见 will fill up all fields，不是已经 Prepare / Process 传过就意味着已经不用再叫 Finalize interchangeable——473 bundled 第一件事常被写成「看见 fill all fields 就已经 Prepare/Process 给过就不用再 Finalize」，本页钉 will fill up all fields not already don't need Finalize 单句。看见 Currently，不是已经 CometBFT fill up all fields even if passed（363 余量） interchangeable——363 钉又填一遍，本页钉 will fill up 单句。看见 fill up all fields in FinalizeBlockRequest，不是已经 Finalize 等价于 ABCI 1.0 那三步（465 余量） interchangeable——465 钉收成一门，本页钉 473 item 1 边界。
2. **看见 will fill up all fields is not already Finalize + Commit committed / 看见引擎填齐 is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经交差 interchangeable / 已经 committed interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（460 余量） interchangeable / 已经不用再在 Process 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 immediate execution 交差 interchangeable / 已经 Finalize + Commit interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable / 已经字段再填一遍 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（474 第一件事 / 564 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 ran Process interchangeable，也不是已经 FinalizeBlock fill all fields not passed means ran Process bundled（473 第二件事 / 563 余量） interchangeable / 已经字段名对得上就代表已经跑过 Process interchangeable / 已经 newly decided 和 proposed interchangeable。**  
   官方把 will fill up all fields 和 Finalize + Commit 已经交差分开——473 bundled 常与 460 混成「引擎填齐 = 已经交差」，本页钉 will fill up all fields not already committed 单句。看见 fill up all fields，不是已经 FinalizeBlock 确定执行 txs（460 余量） interchangeable——460 钉 execute txs / apply candidate，本页钉 will fill up 单句。看见 Currently，不是已经 ProcessProposal 候选执行（452 余量） interchangeable——452 钉 MAY execute / candidate，本页钉 473 item 1 not committed 边界。
3. **看见 will fill up all fields is not already Contains the fields of the newly decided block bundled interchangeable / 看见引擎会把 Finalize 请求全部字段填齐 is not already FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经 newly decided block 字段 interchangeable / 已经 fill all fields interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（474 余量） interchangeable / 已经 newly decided vs proposed interchangeable / 已经 height/time match header interchangeable，也不是已经 FinalizeBlock 字段余量 bundled（407 余量） interchangeable / 已经实现必须确定 interchangeable / 已经 Info 回应用状态信息 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 FinalizeBlock fill all fields not passed means ran Process bundled（473 第二件事 / 563 余量） interchangeable / 已经 even if passed interchangeable / 已经字段名对得上 interchangeable。**  
   官方把 will fill up all fields 和 Contains the fields of the newly decided block 对象边界分开——473 bundled 常与 461 混成「will fill up all fields = Contains newly decided bundled interchangeable」，本页钉 will fill up not Contains bundled 单句。看见 fill up all fields in FinalizeBlockRequest，不是已经 FinalizeBlock Contains newly decided block fields bundled（474 余量） interchangeable——474 钉 Contains newly decided 三事，本页钉 will fill up 单句。看见 Currently，不是已经 Finalize 字段余量 bundled（407 余量） interchangeable——407 钉含刚决定那块的字段 + 实现必须确定 + Info，本页钉 473 item 1 边界。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐、怎样缓存 Prepare / Process 数据 是规范里的做法，本页不抄。FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）、fill all fields not passed means ran Process（563 余量）、fill all fields not decided/proposed interchangeable（564 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **will fill up all fields not already don't need Finalize ≠ FinalizeBlock fill all fields even if Prepare/Process passed bundled interchangeable：** 官方把 will fill up all fields 和 Prepare/Process 传过就不叫 Finalize 分开。
- **will fill up all fields not already committed ≠ 460 apply candidate interchangeable：** 官方把引擎填齐 Finalize 请求和 Finalize + Commit 已经交差分开。
- **will fill up all fields not Contains bundled interchangeable ≠ 461 newly decided bundled interchangeable：** 官方把 will fill up 单句和 Contains newly decided block fields 对象边界分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| will fill up all fields | 不是 already don't need Finalize | 不是 CometBFT fill up all fields even if passed（363） |
| will fill up all fields | 不是 already committed | 不是 Finalize 确定执行 txs（460） |
| will fill up all fields | 不是 Contains bundled interchangeable | 不是 FinalizeBlock 含刚决定那块字段 bundled（461） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not already don't need Finalize 正式三事（473 余量），必须分开 will fill up all fields 是不是 already don't need Finalize interchangeable / 473 bundled interchangeable / 363 fill all fields interchangeable、will fill up all fields 是不是 already committed interchangeable / 460 apply candidate interchangeable / 452 candidate interchangeable、will fill up all fields 是不是 Contains bundled interchangeable / 461 bundled interchangeable / 474 bundled interchangeable。可以跳过「看见 will fill up all fields 就已经 Prepare/Process 给过就不用再 Finalize interchangeable」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐、怎样缓存 Prepare / Process 数据。
- even if passed not already ran Process / same field names。那是不变量 563（473 item 2 余量）。
- all fields not decided/proposed interchangeable。那是不变量 564（473 item 3 余量）。
- fill all fields even if Prepare/Process passed bundled 三事。那是不变量 473。
