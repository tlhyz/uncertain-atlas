# 例：看见 CometBFT will fill up all fields in FinalizeBlockRequest is not already no need to provide again / not Finalize 时的 Process 保证 bundled（360） interchangeable / not Prepare/Process passed means ran Process interchangeable

**层次**：实现 / Finalize 请求把字段再填一遍 not no need to provide again 正式三事（360 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 请求把字段再填一遍 not no need to provide again / not Finalize 时的 Process 保证 bundled（360） interchangeable / not Prepare/Process passed means ran Process interchangeable」，不是 Finalize 时的 Process 保证 bundled（360），也不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）。不要另写怎样写 Finalize、怎样再填字段。

## 官方三件事

规范把 FinalizeBlock Usage 里 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` / even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest` 和「已经不用再给 / 字段名对得上就代表已经跑过 Process / 请求齐了就是已经交差」分开写成三件独立的实现事，不是「看见 Prepare / Process 已经给过就已经不用再给 interchangeable、已经跑过 Process interchangeable、已经交差 interchangeable」一件事：

1. **看见 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` / 看见引擎会把 Finalize 请求全部字段填齐 is not already no need to provide again / Prepare or Process already passed means don't need Finalize interchangeable / 看见再填一遍 is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 已经不用再给 interchangeable / 已经 Prepare / Process 给过就不用再 Finalize interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经不用再 Finalize interchangeable / 已经交差 interchangeable，也不是已经 at least one non-byzantine ran Process not every validator bundled（582 余量） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 persist decision interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 ran Process interchangeable。**  
   官方 Usage 写：Currently, CometBFT will fill up all fields in `FinalizeBlockRequest`。看见 will fill up all fields，不是已经 Prepare / Process 给过就不用再 Finalize——360 bundled 第二件事常被写成「看见再填一遍就已经不用再给 interchangeable」，本页钉 refill fields not no need to provide again 单句。看见 Currently / 引擎会把字段填齐，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 at least one / apply candidate bundled，本页钉 item 2 边界。看见 fill up all fields，不是已经 FinalizeBlock fill all fields even if Prepare/Process passed（473） interchangeable——473 另钉 fill all fields 三事，本页钉 360 item 2 单句。
2. **看见 even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest` / 看见即使 Prepare / Process 已经传过 is not already field names match means already ran Process / 看见字段名对得上 is not already Prepare 和 Process / Finalize 同一套字段 bundled（359 余量） interchangeable / 已经跑过 Process interchangeable / 已经 Finalize interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经不用再给 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 已经不用再 Process interchangeable，也不是已经 FinalizeBlock fill all fields not passed means ran Process bundled（473 第二件事 / 568 余量） interchangeable / 已经字段名对得上就代表已经跑过 Process interchangeable / 已经 Prepare/Process passed interchangeable。**  
   官方把 even if already passed 和 field names match means ran Process 分开——360 bundled 第二件事常与 359 混成「看见字段名对得上就已经跑过 Process interchangeable」，本页钉 even if passed not field names match 单句。看见 even if already passed，不是已经 Prepare 和 Process / Finalize 同一套字段（359 余量） interchangeable——359 钉 Prepare 请求字段边界，本页钉 360 item 2 单句。看见 passed via Prepare/Process，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 proposer Process path，本页钉 refill 边界。
3. **看见 all fields / 又填一遍 / request complete is not already committed / already settled interchangeable / 看见请求齐了 is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经不用再 Finalize interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 newly decided block fields interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 已经套用先前候选 interchangeable / 已经 previously executed interchangeable。**  
   官方把 refill all fields 和 request complete means committed 分开——360 bundled 第二件事第三句「看见请求齐了，不是已经交差」常被写成 473 / 407 bundled interchangeable，本页钉 refill not request complete means committed 单句。看见 all fields 填齐，不是已经 Finalize + Commit 那种已经交差 interchangeable——335 / 576 各钉 committed 边界，本页钉 360 item 2 第三件事。看见又填一遍，不是已经 apply candidate / previously executed（584 余量） interchangeable——584 钉 item 3 边界，本页钉 refill 单句。

怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段是规范里的做法，本页不抄。at least one non-byzantine ran Process not every validator（582 余量）、apply candidate not ExecuteTxState（584 余量）、FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）是另外那套，本页不抄。

## 官方为什么这样拆

- **refill fields not no need to provide again ≠ Finalize 时的 Process 保证 bundled interchangeable：** 官方把 will fill up all fields 和已经不用再给分开。
- **even if passed not field names match means ran Process ≠ Prepare/Process/Finalize same fields interchangeable：** 官方把 even if passed 和已经跑过 Process 分开。
- **refill not request complete means committed ≠ finfill / finfields bundled interchangeable：** 官方把再填一遍和已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| refill all fields | 不是 already no need to provide again | 不是 Finalize 时的 Process 保证 bundled（360） |
| even if Prepare/Process passed | 不是 already field names match means ran Process | 不是 Prepare 和 Process / Finalize 同一套字段（359） |
| request complete | 不是 already committed / settled | 不是 FinalizeBlock fill all fields bundled（473） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 请求把字段再填一遍 not no need to provide again 正式三事（360 余量），必须分开 refill 是不是 already no need to provide again interchangeable / 360 bundled interchangeable / 473 finfill interchangeable、even if passed 是不是 already field names match means ran Process interchangeable / 359 same fields interchangeable / 568 not passed means ran Process interchangeable、refill 是不是 already request complete means committed interchangeable / 407 finfields interchangeable / 584 apply candidate interchangeable。可以跳过「看见 Prepare / Process 已经给过就已经不用再给 interchangeable」。不要另写怎样再填字段。

## 本页不抄

- 怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段。
- at least one non-byzantine ran Process not every validator。那是不变量 582（360 item 1 余量）。
- apply candidate not ExecuteTxState。那是不变量 584（360 item 3 余量）。
- Finalize 时的 Process 保证 bundled 三事。那是不变量 360。
- FinalizeBlock fill all fields even if Prepare/Process passed bundled 三事。那是不变量 473。
