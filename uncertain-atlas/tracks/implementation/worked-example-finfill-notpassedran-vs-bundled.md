# 例：看见 even if they were already passed on to the Application via `PrepareProposalRequest` or `ProcessProposalRequest` / 看见即使 Prepare / Process 已经传过 is not already field names match means ran Process / 看见 even if passed is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经字段名对得上就代表已经跑过 Process interchangeable / 已经 Prepare/Process 同一套字段 interchangeable

**层次**：实现 / FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「even if passed not already field names match means ran Process 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 不是 already newly decided vs proposed interchangeable / 不是 already previously executed interchangeable」，不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473），也不是 fill all fields not already don't need Finalize（567），也不是 fill all fields not decided/proposed interchangeable（569 余量）。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock Usage 里 even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest`、字段名对得上就代表已经跑过 Process、Prepare/Process/Finalize 同一套字段就已经是 newly decided block 字段分开写成三件独立的实现事，不是「看见 even if passed 就已经字段名对得上就代表已经跑过 Process interchangeable、Prepare/Process 同一套字段 interchangeable、已经 previously executed interchangeable」一件事：

1. **看见 even if they were already passed on to the Application via `PrepareProposalRequest` or `ProcessProposalRequest` / 看见即使 Prepare / Process 已经传过 is not already field names match means ran Process / 看见 even if passed is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经字段名对得上就代表已经跑过 Process interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 Prepare 请求字段同一套 bundled（359 余量） interchangeable / 已经字段名对得上 interchangeable / 已经 local_last_commit interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经字段再填一遍 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 已经不用再 Process interchangeable，也不是已经 FinalizeBlock fill all fields not already don't need Finalize bundled（473 第一件事 / 567 余量） interchangeable / 已经 Prepare/Process 给过就不用再 Finalize interchangeable / 已经 even if passed interchangeable，也不是已经 FinalizeBlock fill all fields not decided/proposed interchangeable bundled（473 第三件事 / 569 余量） interchangeable / 已经 decided/proposed interchangeable / 已经 ran Process means don't need Finalize interchangeable。**  
   官方写 even if they were already passed on via PrepareProposalRequest or ProcessProposalRequest。看见已经传过，不是已经 Prepare 请求字段同一套（359 余量） interchangeable——359 钉字段名对得上 / local_last_commit，473 bundled 第二件事常被写成「even if passed = 字段名对得上就代表已经跑过 Process」，本页钉 even if passed not field names match means ran Process 单句。看见 even if passed，不是已经 Finalize 时的 Process 保证（360 余量） interchangeable——360 钉至少一名非拜占庭跑过 Process / 字段再填一遍，本页钉 even if passed 边界。看见已经经 Prepare 或 Process 给过，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 ProcessProposalRequest.txs equals PrepareProposalResponse.txs，本页钉 473 item 2 单句。
2. **看见 even if passed is not already Prepare / Process / Finalize same fields means newly decided block fields / 看见即使 Prepare / Process 已经传过 is not already newly decided block 的字段和 proposed block 字段 interchangeable 不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经 newly decided and proposed interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 FinalizeBlock newly decided block fields not ProcessProposal contains all information bundled（556 余量） interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable / 已经 proposed block 字段 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（555 余量） interchangeable / 已经 ran Process interchangeable / 已经四门已经结算 interchangeable，也不是已经 FinalizeBlock newly decided block fields not proposed block bundled（565 余量） interchangeable / 已经 ProcessProposal contains all information interchangeable / 已经 only raw proposal enough interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 传过 interchangeable。**  
   官方把 even if passed 和 newly decided block 的字段 vs proposed block 字段分开——473 bundled 常与 461 混成「Prepare/Process 传过 = newly decided 和 proposed interchangeable」，本页钉 even if passed not newly decided/proposed interchangeable 单句。看见已经传过，不是已经 FinalizeBlock newly decided block fields not ProcessProposal contains all information（556 余量） interchangeable——556 钉 newly decided vs Process contains all information，本页钉 even if passed 边界。看见 even if passed，不是已经 FinalizeBlock newly decided block fields not proposed block（565 余量） interchangeable——565 钉 newly decided not proposed，本页钉 473 item 2 单句。
3. **看见 even if passed is not already previously executed / apply candidate interchangeable / 看见已经经 Prepare 或 Process 给过 is not already FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 已经 previously executed interchangeable / 已经 candidate 就不需要 Commit interchangeable 不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经 even if passed interchangeable / 已经不用再填 Finalize 请求 interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 immediate execution 交差 interchangeable / 已经 MAY execute interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable，也不是已经 FinalizeBlock fill all fields not already don't need Finalize bundled（473 第一件事 / 567 余量） interchangeable / 已经 Prepare/Process 给过就不用再 Finalize interchangeable / 已经 committed interchangeable，也不是已经 FinalizeBlock fill all fields not decided/proposed interchangeable bundled（473 第三件事 / 569 余量） interchangeable / 已经 decided/proposed interchangeable / 已经 all fields 又填一遍 interchangeable。**  
   官方把 even if passed 和已经可以套用先前 candidate / previously executed 分开——473 bundled 常与 460 混成「even if passed = 已经 previously executed interchangeable」，本页钉 even if passed not previously executed 单句。看见已经传过，不是已经 ProcessProposal 候选执行（452 余量） interchangeable——452 钉 MAY execute / candidate，本页钉 even if passed 边界。看见 even if passed，不是已经 ProcessProposal Contains all information not already executed（546 余量） interchangeable——546 钉「信息够执行」≠ 已经执行，本页钉 473 item 2 单句。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐、怎样缓存 Prepare / Process 数据 是规范里的做法，本页不抄。FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）、fill all fields not already don't need Finalize（567 余量）、fill all fields not decided/proposed interchangeable（569 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **even if passed not field names match means ran Process ≠ Prepare 请求字段同一套 interchangeable：** 官方把 even if passed 和字段名对得上就代表已经跑过 Process 分开。
- **even if passed not newly decided/proposed interchangeable ≠ 556 newly decided vs ProcessProposal full info interchangeable：** 官方把 even if passed 和 newly decided vs proposed 对象分开。
- **even if passed not previously executed interchangeable ≠ 460 apply candidate interchangeable：** 官方把 even if passed 和 previously executed / 套用候选分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| even if passed | 不是 field names match means ran Process | 不是 Prepare 请求字段同一套（359） |
| even if passed | 不是 newly decided/proposed interchangeable | 不是 FinalizeBlock newly decided fields not ProcessProposal full info（556） |
| even if passed | 不是 previously executed interchangeable | 不是 FinalizeBlock 套用候选（460） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量），必须分开 even if passed 是不是 field names match means ran Process interchangeable / 359 Prepare 同一套字段 interchangeable / 360 Process guarantee interchangeable、even if passed 是不是 newly decided/proposed interchangeable / 556 not ProcessProposal full info interchangeable / 565 not proposed block interchangeable、even if passed 是不是 previously executed interchangeable / 460 apply candidate interchangeable / 546 not already executed interchangeable。可以跳过「看见 even if passed 就已经字段名对得上就代表已经跑过 Process interchangeable」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐、怎样缓存 Prepare / Process 数据。
- will fill up all fields not already don't need Finalize。那是不变量 567（473 item 1 余量）。
- all fields not decided/proposed interchangeable。那是不变量 569（473 item 3 余量）。
- fill all fields even if Prepare/Process passed bundled 三事。那是不变量 473。
