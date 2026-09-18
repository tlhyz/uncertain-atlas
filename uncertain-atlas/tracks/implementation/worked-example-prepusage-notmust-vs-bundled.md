# 例：看见MUST 删到回包上限内不是已经引擎会帮你裁；看见引擎会帮你裁不是已经从内存池删掉；看见MUST 删到回包上限内不是已经 -1 就按 100 MB 验已经没有上限

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareUsage must not already engine-trims / not already 355-pool / not already -1-no-cap 正式三事（503 余量）/ not 1306 prepusage-notmust interchangeable / not 503 prepareusage-rawmust-vs-bundled bundled interchangeable」，不是 prepareusage rawmust vs bundled bundled（503），也不是已经 Req 2（345），也不是已经 -1 没有上限（337）。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。

## 官方三件事

1. **看见MUST 删到回包上限内 / 看见MUST 删到回包上限内 这份对象 is not already 已经引擎会帮你裁 interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1306 prepusage-notmust interchangeable / 1304 prepusage-notraw interchangeable，也不是已经 PrepareUsage must not already engine-trims / not already 355-pool / not already -1-no-cap 正式三事 bundled（503 item 3 余量） interchangeable / 503 prepusage item 3 interchangeable。**  
   官方把MUST 删到回包上限内和已经引擎会帮你裁写成两件。看见MUST 删到回包上限内，不是已经引擎会帮你裁。

2. **看见引擎会帮你裁 / 看见MUST 删到回包上限内 / 这份对象 is not already 已经从内存池删掉 interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1306 prepusage-notmust interchangeable / 1305 prepusage-notexceed interchangeable，也不是已经 Req 2 interchangeable / 345 Req 2 interchangeable。**  
   官方把引擎会帮你裁和已经从内存池删掉写成两件。看见引擎会帮你裁，不是已经从内存池删掉。

3. **看见MUST 删到回包上限内 / 看见引擎会帮你裁 / 这份对象 is not already 已经 -1 就按 100 MB 验已经没有上限 interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1306 prepusage-notmust interchangeable / 1304 prepusage-notraw interchangeable，也不是已经 -1 没有上限 interchangeable / 337 -1 没有上限 interchangeable。**  
   官方把MUST 删到回包上限内和已经 -1 就按 100 MB 验已经没有上限写成两件。看见MUST 删到回包上限内，不是已经 -1 就按 100 MB 验已经没有上限。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。

## 官方为什么这样拆

- **MUST remove if > max_tx_bytes 不是引擎会帮你裁 interchangeable：官方把 Methods Usage MUST remove 单句和应用必须自己裁回包分开。**
- **看见 MUST 删到上限内 不是已经从内存池删掉：355 钉池后果，本页钉 Usage MUST remove 体积义务。**
- **看见 MUST remove 不是已经 -1 就按 100 MB 验已经没有上限：那是不变量 337。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经引擎会帮你裁 | 不是已经引擎会帮你裁 | 不是已经Req 2（345） |
| 已经从内存池删掉 | 不是已经从内存池删掉 | 不是已经-1 没有上限（337） |
| 已经 -1 就按 100 MB 验已经没有上限 | 不是已经 -1 就按 100 MB 验已经没有上限 | 不是已经1304 prepusage-notraw |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareUsage must not already engine-trims / not already 355-pool / not already -1-no-cap 正式三事（503 余量），必须分开是不是已经引擎会帮你裁、是不是已经从内存池删掉、是不是已经 -1 就按 100 MB 验已经没有上限。可以跳过「看见 Prepare 请求里带了 txs 就已经改列表 bundled interchangeable、已经能回超限、已经是引擎会帮你裁 interchangeable」。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。503 PrepareProposal Usage rawmust bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。
- 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。
