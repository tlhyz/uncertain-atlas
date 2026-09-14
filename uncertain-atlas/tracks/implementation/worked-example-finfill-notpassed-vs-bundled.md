# 例：看见 even if already passed via PrepareProposalRequest or ProcessProposalRequest is not already field names match means already ran Process / not FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / not Prepare/Process/Finalize same fields interchangeable

**层次**：实现 / FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock fill all fields not passed means ran Process / not FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / not Prepare/Process/Finalize same fields interchangeable」，不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473），也不是 Prepare 和 Process / Finalize 同一套字段（359 余量）。不要另写怎样写 Finalize、怎样再填字段。

## 官方三件事

规范把 FinalizeBlock Usage 里 even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest` 和「已经字段名对得上就代表已经跑过 Process / 已经是 Prepare 和 Process / Finalize 同一套字段 / 已经是 Process 通常紧跟 Prepare bundled interchangeable」分开写成三件独立的实现事，不是「看见 Prepare / Process 已经传过就已经跑过 Process interchangeable、已经字段名对得上 interchangeable、已经 Prepare/Process passed interchangeable」一件事：

1. **看见 even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest` / 看见即使 Prepare / Process 已经传过 is not already field names match means already ran Process / 看见字段名对得上 is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经跑过 Process interchangeable / 已经 Prepare/Process passed interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经不用再给 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 583 even if passed not field names match interchangeable / 582 not every validator interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段 bundled（359 余量） interchangeable / 359 same fields interchangeable / 351 Process also on proposer interchangeable。**  
   官方 Usage 写：even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest`。看见 even if already passed，不是已经 field names match means ran Process——473 bundled 第二件事常被写成「看见 Prepare / Process 已经传过就已经跑过 Process interchangeable」，本页钉 even if passed not field names match 单句。看见 passed via Prepare/Process，不是已经 FinalizeBlock fill all fields even if Prepare/Process passed（473） interchangeable——473 另钉 fill all fields 三事，本页钉 item 2 边界。看见字段名对得上，不是已经 Finalize 请求把字段再填一遍 not no need to provide again（583 余量） interchangeable——583 从 360 item 2 角度钉 refill 单句，本页从 473 item 2 角度钉 even if passed 单句。
2. **看见 even if already passed via PrepareProposalRequest or ProcessProposalRequest is not already Prepare 和 Process / Finalize 同一套字段 bundled（359 余量） interchangeable / 看见字段名对得上 is not already Prepare 请求字段 / Process 请求字段 / Finalize 请求字段就代表已经 Process 过 interchangeable / 已经跑过 Process interchangeable / 已经 Finalize interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经 even if passed interchangeable / 已经 field names match interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经不用再给 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 351 Process also on proposer interchangeable / 568 not passed means ran Process interchangeable。**  
   官方把 even if already passed 和 Prepare/Process/Finalize same fields 分开——473 item 2 常与 359 混成「看见字段名对得上就已经是 Prepare 和 Process / Finalize 同一套字段 interchangeable」，本页钉 even if passed not same fields 单句。看见 even if passed，不是已经 Prepare 和 Process / Finalize 同一套字段（359 余量） interchangeable——359 钉 Prepare 请求字段边界，本页钉 473 item 2 边界。看见 passed via Prepare/Process，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 proposer Process path，本页钉 finfill notpassed 单句。
3. **看见 even if already passed via PrepareProposalRequest or ProcessProposalRequest is not already Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 看见 Prepare / Process 已经传过 is not already Process 也会在提议者那边叫 interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 已经不用再 Process interchangeable / 已经提议者 Process 过就代表已经跑过 Process interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经 even if passed interchangeable / 已经 field names match interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable / 已经 persist decision interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段 bundled（359 余量） interchangeable / 359 same fields interchangeable / 583 even if passed not field names match interchangeable。**  
   官方把 even if already passed 和 proposer Process path 分开——473 item 2 常与 351 混成「看见 Prepare / Process 已经传过就已经是 Process 也会在提议者那边叫 interchangeable」，本页钉 even if passed not Process also on proposer 单句。看见 even if passed，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 proposer Process path，本页钉 473 item 2 第三件事。看见 passed via Prepare/Process，不是已经 at least one non-byzantine ran Process（582 余量） interchangeable——582 钉 360 item 1 边界，本页钉 finfill notpassed 单句。

怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段是规范里的做法，本页不抄。FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）、Finalize 请求把字段再填一遍 not no need to provide again 正式三事（583 余量）、Prepare 和 Process / Finalize 同一套字段（359 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **even if passed not field names match means ran Process ≠ FinalizeBlock fill all fields even if Prepare/Process passed bundled interchangeable：** 官方把 even if already passed 和已经跑过 Process 分开。
- **even if passed not Prepare/Process/Finalize same fields ≠ 359 same fields interchangeable：** 官方把 even if passed 和同一套字段就代表已经 Process 过分开。
- **even if passed not Process also on proposer ≠ 351 Process also on proposer interchangeable：** 官方把 even if passed 和提议者 Process path 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| even if Prepare/Process passed | 不是 already field names match means ran Process | 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） |
| even if Prepare/Process passed | 不是 already Prepare/Process/Finalize same fields | 不是 Prepare 和 Process / Finalize 同一套字段（359） |
| even if Prepare/Process passed | 不是 already Process also on proposer means ran Process | 不是 Process 通常紧跟 Prepare（351） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量），必须分开 even if passed 是不是 already field names match means ran Process interchangeable / 473 finfill interchangeable / 583 not refill interchangeable、even if passed 是不是 already Prepare/Process/Finalize same fields interchangeable / 359 same fields interchangeable / 568 not passed means ran Process interchangeable、even if passed 是不是 already Process also on proposer interchangeable / 351 Process also on proposer interchangeable / 582 not every validator interchangeable。可以跳过「看见 Prepare / Process 已经传过就已经跑过 Process interchangeable」。不要另写怎样再填字段。

## 本页不抄

- 怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段。
- will fill up all fields not no need to provide again。那是不变量 583（360 item 2 余量）或 473 item 1。
- all fields / request complete not committed。那将是不变量 569（473 item 3 余量）。
- FinalizeBlock fill all fields even if Prepare/Process passed bundled 三事。那是不变量 473。
- Prepare 和 Process / Finalize 同一套字段。那是不变量 359。
