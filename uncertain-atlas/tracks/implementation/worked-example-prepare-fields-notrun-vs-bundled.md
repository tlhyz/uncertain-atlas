# 例：看见 Prepare 和 Process / Finalize 同一套字段 is not already ran Process interchangeable / not already Finalize interchangeable / not already settled interchangeable

**层次**：实现 / Prepare 和 Process / Finalize 同一套字段 not already ran Process / not already Finalize / not already settled 正式三事（359 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 和 Process / Finalize 同一套字段 not already ran Process / not already Finalize / not already settled 正式三事（359 余量）/ not 845 prepare-fields-notrun interchangeable / not 359 prepare-fields-vs-same bundled interchangeable」，不是 Prepare 请求字段 bundled（359），也不是 Process 也会在提议者那边叫（351），也不是 Finalize 时的 Process 保证就已经跑过 Process（360/finprocgua）。不要另写怎样填 Prepare 请求字段。

## 官方三件事

1. **看见 `txs` / `misbehavior` / `height` / `time` / `next_validators_hash` / `proposer_address` 和 Process / Finalize 同一套 / 看见字段名对得上 这份同一套 is not already 已经跑过 Process interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 845 prepare-fields-notrun interchangeable / 846 prepare-fields-notlocal interchangeable / 359 prepare-fields item 2 local_last_commit interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段 not already ran Process / not already Finalize / not already settled 正式三事 bundled（359 item 1 余量） interchangeable / 359 prepare-fields item 1 interchangeable。**  
   官方写：`PrepareProposalRequest` 的 `txs`、`misbehavior`、`height`、`time`、`next_validators_hash`、`proposer_address` 和 `ProcessProposalRequest`、`FinalizeBlockRequest` 是同一套。看见字段名对得上，不是已经叫过 Process interchangeable——本页从 359 item 1 侧钉 not already ran Process 单句。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。

2. **看见字段名对得上 / 看见同一套 / 这份同一套 is not already 已经 Finalize interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 845 prepare-fields-notrun interchangeable / 359 prepare-fields item 3 对上拟议头 interchangeable / 847 prepare-fields-nothash interchangeable，也不是已经 Finalize 时的 Process 保证就已经跑过 Process interchangeable / 360 finprocgua interchangeable。**  
   官方把同一套和已经 Finalize 分开——359 bundled 第一件事常与 351 / 360 混成「看见字段名对得上就已经跑过 Process 或已经 Finalize interchangeable」，本页钉 not already Finalize 单句。

3. **看见字段名对得上 / 看见请求在 / 这份同一套 is not already 已经交差 interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 845 prepare-fields-notrun interchangeable / 846 prepare-fields-notlocal interchangeable，也不是已经 Process 也会在提议者那边叫 interchangeable / 351 procalso interchangeable。**  
   官方把请求在和已经交差分开。看见请求在，不是已经交差 interchangeable。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。

怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Prepare 和 Process / Finalize 同一套字段 not already ran Process ≠ 已经跑过 Process interchangeable：** 官方把同一套字段和已经叫过分开。
- **看见同一套 not already Finalize ≠ 已经 Finalize interchangeable：** 官方把同一套和已经 Finalize 分开。
- **看见请求在 not already settled ≠ 已经交差 interchangeable：** 官方把请求在和已经交差分开；359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 和 Process / Finalize 同一套字段 | 不是已经跑过 Process | 不是 Process 也会在提议者那边叫（351） |
| 看见同一套 | 不是已经 Finalize | 不是 Finalize 时的 Process 保证（360/finprocgua） |
| 看见请求在 | 不是已经交差 | 不是 473 finfill 再填一遍 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 和 Process / Finalize 同一套字段 not already ran Process / not already Finalize / not already settled 正式三事（359 余量），必须分开是不是已经跑过 Process、是不是已经 Finalize、是不是已经交差。可以跳过「看见字段名对得上就已经跑过 Process」。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepare-fields-notlocal-vs-bundled.md`](worked-example-prepare-fields-notlocal-vs-bundled.md)（不变量 846 item 2）。

## 本页不抄

- 怎样填 Prepare 请求字段、怎样读 local_last_commit、怎样对头。
- Prepare 请求字段 bundled。那是不变量 359。
- local_last_commit 是上一高度的预提交带扩展。那是不变量 359 item 2 余量 / 846。
- Process 也会在提议者那边叫。那是不变量 351。
- Finalize 时的 Process 保证。那是不变量 360。
