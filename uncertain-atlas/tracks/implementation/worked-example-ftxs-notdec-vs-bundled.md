# 例：看见 Process all-exec-info is not already just-decided-fields interchangeable / not already processed interchangeable / not already settled interchangeable

**层次**：实现 / Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事（408 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事（408 余量）/ not 1113 ftxs-notdec interchangeable / not 408 fintxs-vs-control bundled interchangeable」，不是 Finalize 执行余量 bundled（408），也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359），也不是 Finalize 含刚决定那块的字段就已经是四门已经结算（1109）。不要另写怎样写 Finalize 执行余量。

## 官方三件事

1. **看见 Process 含提案块上执行所需的全部信息 / 看见填了信息 这份栏 is not already 已经是刚决定那块的字段 interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1113 ftxs-notdec interchangeable / 1112 ftxs-notsettle interchangeable / 408 fintxs item 1 exec-not-settled interchangeable，也不是已经 Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事 bundled（408 item 2 余量） interchangeable / 408 fintxs item 2 interchangeable。**  
   官方写：ProcessProposal 含提案块上执行所需的全部信息。看见填了信息，不是已经是刚决定那块的字段 interchangeable——本页从 408 item 2 侧钉 not already just-decided-fields 单句。408 fintxs vs control bundled unbundling 在本页 item 2 续。

2. **看见能执行 / 看见填了信息 / 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1113 ftxs-notdec interchangeable / 408 fintxs item 3 process-not-exec interchangeable / 1114 ftxs-notexec interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process interchangeable / 359 same-fields interchangeable。**  
   官方把能执行和已经跑过 Process 分开。看见能执行，不是已经跑过 Process interchangeable。本页钉 not already processed 单句。

3. **看见有提案块 / 看见填了信息 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1113 ftxs-notdec interchangeable / 1112 ftxs-notsettle interchangeable，也不是已经 Finalize 含刚决定那块的字段就已经是四门已经结算 interchangeable / 1109 ffields-notfour interchangeable。**  
   官方把有提案块和已经交差分开。看见有提案块，不是已经交差 interchangeable。408 fintxs vs control bundled unbundling 在本页 item 2 续。

怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process all-exec-info not already just-decided-fields ≠ 已经是刚决定那块的字段 interchangeable：** 官方把提案块上执行所需的全部信息和刚决定那块的字段分开。
- **看见能执行 not already processed ≠ 已经跑过 Process interchangeable：** 官方把能执行和已经跑过 Process 分开。
- **看见有提案块 not already settled ≠ 已经交差 interchangeable：** 官方把有提案块和已经交差分开；408 fintxs vs control bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 含提案块上执行所需的全部信息 | 不是已经是刚决定那块的字段 | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| 看见能执行 | 不是已经跑过 Process | 不是 Finalize 含刚决定那块的字段就已经是四门已经结算（1109） |
| 看见有提案块 | 不是已经交差 | 不是整块跑了就已经是 ExecuteTxState（1114） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事（408 余量），必须分开是不是已经是刚决定那块的字段、是不是已经跑过 Process、是不是已经交差。可以跳过「看见填了 Finalize 执行余量就已经交差」。不要另写怎样写 Finalize 执行余量。408 fintxs vs control bundled unbundling 在本页 item 2 续；续 [`worked-example-ftxs-notexec-vs-bundled.md`](worked-example-ftxs-notexec-vs-bundled.md)（不变量 1114 item 3）。

## 本页不抄

- 怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行。
- Finalize 执行余量 bundled。那是不变量 408。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- Finalize 含刚决定那块的字段就已经是四门已经结算。那是不变量 1109。
