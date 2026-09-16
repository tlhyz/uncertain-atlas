# 例：看见 Currently, CometBFT will fill up all fields in FinalizeBlockRequest is not already no need to provide again / not FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / not Finalize 时的 Process 保证 bundled（360） interchangeable

**层次**：实现 / FinalizeBlock fill all fields not no need to provide again 正式三事（473 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock fill all fields not no need to provide again / not FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / not Finalize 时的 Process 保证 bundled（360） interchangeable」，不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473），也不是 Finalize 请求把字段再填一遍 not no need to provide again 正式三事（583 余量）。不要另写怎样写 Finalize、怎样再填字段。

## 官方三件事

规范把 FinalizeBlock Usage 里 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` 和「已经不用再给 Finalize / 已经是 Finalize 时的 Process 保证 bundled / 已经是 Finalize 请求把字段再填一遍 not no need to provide again bundled interchangeable」分开写成三件独立的实现事，不是「看见 will fill up all fields 就已经不用再给 interchangeable、已经 Prepare / Process 给过就不用再 Finalize interchangeable、已经 473 finfill bundled interchangeable」一件事：

1. **看见 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` / 看见引擎会把 Finalize 请求全部字段填齐 is not already no need to provide again / Prepare or Process already passed means don't need Finalize interchangeable / 看见再填一遍 is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经不用再 Finalize interchangeable / 已经交差 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable / 已经 persist decision interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 583 not refill interchangeable / 582 not every validator interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 407 finfields interchangeable / 584 apply candidate interchangeable。**  
   官方 Usage 写：Currently, CometBFT will fill up all fields in `FinalizeBlockRequest`。看见 will fill up all fields，不是已经 Prepare / Process 给过就不用再 Finalize——473 item 1 常被写成「看见再填一遍就已经不用再给 interchangeable」，本页钉 fill all fields not no need to provide again 单句。看见 Currently / 引擎会把字段填齐，不是已经 FinalizeBlock fill all fields even if Prepare/Process passed（473） interchangeable——473 另钉 even if passed / request complete 三事，本页钉 item 1 边界。看见 fill up all fields，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 at least one / apply candidate bundled，本页钉 finfill notrefill 单句。
2. **看见 will fill up all fields in FinalizeBlockRequest is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 看见再填一遍 is not already at least one non-byzantine ran Process interchangeable / 已经 persist decision interchangeable / 已经套用先前候选 interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经不用再 Finalize interchangeable / 565 not no need to provide again interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 583 not refill interchangeable / 563 not passed means ran Process interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 576 fincand committed interchangeable。**  
   官方把 will fill up all fields 和 Finalize 时的 Process 保证 bundled 分开——473 item 1 常与 360 混成「看见 will fill up all fields 就已经是 Finalize 时的 Process 保证 bundled interchangeable」，本页钉 fill all fields not 360 bundled 单句。看见 will fill up all fields，不是已经 at least one non-byzantine ran Process（582 余量） interchangeable——582 钉 360 item 1 边界，本页钉 473 item 1 单句。看见 Currently，不是已经 apply candidate / previously executed（584 余量） interchangeable——584 钉 360 item 3 边界，本页钉 finfill notrefill 单句。
3. **看见 will fill up all fields in FinalizeBlockRequest is not already Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 看见再填一遍 is not already refill fields not no need to provide again interchangeable / 583 not refill interchangeable / 已经 360 item 2 单句 interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 565 not no need to provide again interchangeable / 563 not passed means ran Process interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 407 finfields interchangeable / 335 finpersist interchangeable，也不是已经 even if already passed via PrepareProposalRequest or ProcessProposalRequest interchangeable / 359 same fields interchangeable / 351 Process also on proposer interchangeable。**  
   官方把 will fill up all fields 和 360 item 2 refill 单句分开——473 item 1 常与 583 混成「看见 will fill up all fields 就已经是 Finalize 请求把字段再填一遍 not no need to provide again interchangeable」，本页钉 fill all fields not 583 not refill 单句。看见 Currently，不是已经 Finalize 含刚决定那块的字段（407 余量） interchangeable——407 钉 newly decided block fields 边界，本页钉 473 item 1 第三件事。看见 fill up all fields，不是已经 even if already passed（563 余量） interchangeable——568 钉 473 item 2 边界，本页钉 finfill notrefill 单句。

怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段是规范里的做法，本页不抄。FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）、FinalizeBlock fill all fields not passed means ran Process 正式三事（563 余量）、Finalize 请求把字段再填一遍 not no need to provide again 正式三事（583 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **fill all fields not no need to provide again ≠ FinalizeBlock fill all fields even if Prepare/Process passed bundled interchangeable：** 官方把 will fill up all fields 和已经不用再 Finalize 分开。
- **fill all fields not no need to provide again ≠ Finalize 时的 Process 保证 bundled interchangeable：** 官方把 will fill up all fields 和 at least one / apply candidate bundled 分开。
- **fill all fields not no need to provide again ≠ 583 not refill interchangeable：** 官方把 473 item 1 和 360 item 2 refill 单句分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| will fill up all fields | 不是 already no need to provide again | 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） |
| will fill up all fields | 不是 already Finalize 时的 Process 保证 bundled | 不是 Finalize 时的 Process 保证 bundled（360） |
| will fill up all fields | 不是 already 583 not refill | 不是 Finalize 请求把字段再填一遍 not no need to provide again 正式三事（583） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not no need to provide again 正式三事（473 余量），必须分开 fill 是不是 already no need to provide again interchangeable / 473 finfill interchangeable / 583 not refill interchangeable、fill 是不是 already Finalize 时的 Process 保证 bundled interchangeable / 360 bundled interchangeable / 582 not every validator interchangeable、fill 是不是 already 583 not refill interchangeable / 407 finfields interchangeable / 563 not passed means ran Process interchangeable。可以跳过「看见 will fill up all fields 就已经不用再给 interchangeable」。不要另写怎样再填字段。

## 本页不抄

- 怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段。
- even if passed not field names match means ran Process。那是不变量 563（473 item 2 余量）。
- all fields / request complete not committed。那是不变量 569（473 item 3 余量）。
- FinalizeBlock fill all fields even if Prepare/Process passed bundled 三事。那是不变量 473。
- Finalize 请求把字段再填一遍 not no need to provide again 正式三事（360 余量）。那是不变量 583。
