# 例：看见字段名对得上 / 看见同一套 / 看见请求在 is not already already ran-process interchangeable / already finalize interchangeable / already settled interchangeable

**层次**：实现 / Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事（359 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事（359 余量）/ not 830 prepfields-notprocess interchangeable / not 359 preparefields bundled interchangeable」，不是 Prepare 请求字段 bundled（359），也不是 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展（831 item 2 余量）或 height / time / proposer_address 对上拟议头不是已经知道本头哈希（832 item 3 余量）。不要另写怎样填 Prepare 请求字段。

## 官方三件事

规范把 Methods 里 `PrepareProposalRequest` 的 `txs`、`misbehavior`、`height`、`time`、`next_validators_hash`、`proposer_address` 和 `ProcessProposalRequest`、`FinalizeBlockRequest` 是同一套 和「已经是字段名对得上就已经跑过 Process interchangeable / 已经是同一套就已经 Finalize interchangeable / 已经是请求在就已经交差 interchangeable / 已经是 preparefields bundled interchangeable」分开写成三件独立的实现事，不是「看见字段名对得上就已经跑过 Process interchangeable / 就已经 Finalize interchangeable / 就已经交差 interchangeable」一件事：

1. **看见字段名对得上 / 看见 `txs` / `misbehavior` / `height` / `time` / `next_validators_hash` / `proposer_address` 和 Process / Finalize 同一套 / 看见同一套字段 is not already 已经跑过 Process interchangeable / 已经 ran-process interchangeable / 已经叫过 Process 交差 interchangeable / 359 preparefields bundled interchangeable / 351 processalso interchangeable / preparefields-sold-as-same interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 830 prepfields-notprocess interchangeable / 359 preparefields item 1 interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事 bundled（359 item 1 余量） interchangeable / 359 preparefields item 1 interchangeable，也不是已经是本高度刚签的扩展（831） interchangeable / 832 prepfields-nothash interchangeable / 351 process-also interchangeable，也不是已经 Process 也会在提议者那边叫就已经不用再 Process（351） interchangeable。**  
   官方写：`PrepareProposalRequest` 的 `txs`、`misbehavior`、`height`、`time`、`next_validators_hash`、`proposer_address` 和 `ProcessProposalRequest`、`FinalizeBlockRequest` 是同一套。看见字段名对得上，不是已经叫过 Process。看见字段名对得上，不是已经 ran-process interchangeable——359 钉 bundled 三事，本页从 item 1 侧钉 not already ran-process 单句。看见同一套字段，不是已经 Prepare 请求字段 bundled（359） interchangeable——359 钉 bundled，本页钉 item 1 第一件事。看见字段名对得上，不是已经是本高度刚签的扩展（831） interchangeable——831 另钉 item 2。看见字段名对得上，不是已经 Process 也会在提议者那边叫就已经不用再 Process（351） interchangeable——351 另钉。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。

2. **看见同一套 / 看见和 Process / Finalize 同一套 / 看见字段名对得上同一套 is not already 已经 Finalize interchangeable / 已经 finalize interchangeable / 已经 Finalize 交差 interchangeable / 359 preparefields bundled interchangeable / 351 processalso interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 830 prepfields-notprocess interchangeable / 359 preparefields item 2 上一高 interchangeable / 359 preparefields item 3 拟议头 interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事 bundled（359 item 1 余量） interchangeable / 359 preparefields item 1 interchangeable，也不是已经跑过 Process（本页第一件事） interchangeable。**  
   官方写：看见同一套，不是已经 Finalize。看见和 Process / Finalize 同一套，不是已经 finalize interchangeable——本页钉 not already finalize 单句。看见字段名对得上同一套，不是已经跑过 Process（本页第一件事） interchangeable——三件事分开钉。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。

3. **看见请求在 / 看见 Prepare 请求在 / 看见同一套字段进了请求 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 359 preparefields bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 830 prepfields-notprocess interchangeable / 359 preparefields item 2 / 359 preparefields item 3，也不是已经 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事 bundled（359 item 1 余量） interchangeable / 359 preparefields item 1 interchangeable，也不是已经跑过 Process（本页第一件事） interchangeable / 已经 Finalize（本页第二件事） interchangeable。**  
   官方写：看见请求在，不是已经交差。看见 Prepare 请求在，不是已经 settled interchangeable——本页钉 not already settled 单句。看见同一套字段进了请求，不是已经 Finalize（本页第二件事） interchangeable——三件事分开钉。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。

怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头是规范里的做法，本页不抄。Prepare 请求字段 bundled（359）、local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展（359 item 2 余量 / 831）、height / time / proposer_address 对上拟议头不是已经知道本头哈希（359 item 3 余量 / 832）、Process 也会在提议者那边叫就已经不用再 Process（351）、到了 H 就已经 Prepare 带了扩展（330）、候选已经是 ExecuteTxState（311）是另外那套，本页不抄。

## 官方为什么这样拆

- **字段名对得上 not already ran-process ≠ 359 / 351 interchangeable：** 官方把同一套字段和已经叫过 Process 分开。
- **同一套 not already finalize ≠ 已经 Finalize interchangeable：** 官方把同一套和已经 Finalize 分开。
- **请求在 not already settled ≠ 已经交差 interchangeable：** 官方把请求在和已经交差分开；359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 字段名对得上 | 不是 already ran-process | 不是 Process 也会在提议者那边叫就已经不用再 Process alone（351） |
| 同一套 | 不是 already finalize | 不是上一高 already this-signed alone（831） |
| 请求在 | 不是 already settled | 不是拟议头 already header-hash alone（832） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事（359 余量），必须分开字段名对得上 是不是 already ran-process interchangeable / 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable、同一套 是不是 already finalize interchangeable、请求在 是不是 already settled interchangeable。可以跳过「看见字段名对得上就已经跑过 Process interchangeable / 就已经 Finalize interchangeable / 就已经交差 interchangeable」。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动；完成 [`worked-example-prepfields-notthissigned-vs-bundled.md`](worked-example-prepfields-notthissigned-vs-bundled.md)（不变量 831 item 2）；完成 [`worked-example-prepfields-nothash-vs-bundled.md`](worked-example-prepfields-nothash-vs-bundled.md)（不变量 832 item 3）。

## 本页不抄

- 怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头。
- Prepare 请求字段 bundled。那是不变量 359。
- local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展。那是不变量 359 item 2 余量 / 831。
- height / time / proposer_address 对上拟议头不是已经知道本头哈希。那是不变量 359 item 3 余量 / 832。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 候选已经是 ExecuteTxState。那是不变量 311。
