# 例：看见初步交易列表叫 raw proposal不是已经 Prepare 改列表 bundled；看见应用可以改这套不是已经从内存池删掉；看见初步交易列表叫 raw proposal不是已经只有 raw proposal

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareUsage raw not already Prepare-改列表 / not already deleted-from-mempool / not already only-raw 正式三事（503 余量）/ not 1304 prepusage-notraw interchangeable / not 503 prepareusage-rawmust-vs-bundled bundled interchangeable」，不是 prepareusage rawmust vs bundled bundled（503），也不是已经 Prepare 改列表（355），也不是已经 Prepare Request 栏（423）。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。

## 官方三件事

1. **看见初步交易列表叫 raw proposal / 看见初步交易列表叫 raw proposal 这份对象 is not already 已经 Prepare 改列表 bundled interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1304 prepusage-notraw interchangeable / 1305 prepusage-notexceed interchangeable，也不是已经 PrepareUsage raw not already Prepare-改列表 / not already deleted-from-mempool / not already only-raw 正式三事 bundled（503 item 1 余量） interchangeable / 503 prepusage item 1 interchangeable。**  
   官方把初步交易列表叫 raw proposal和已经 Prepare 改列表 bundled写成两件。看见初步交易列表叫 raw proposal，不是已经 Prepare 改列表 bundled。

2. **看见应用可以改这套 / 看见初步交易列表叫 raw proposal / 这份对象 is not already 已经从内存池删掉 interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1304 prepusage-notraw interchangeable / 1306 prepusage-notmust interchangeable，也不是已经 Prepare 改列表 interchangeable / 355 Prepare 改列表 interchangeable。**  
   官方把应用可以改这套和已经从内存池删掉写成两件。看见应用可以改这套，不是已经从内存池删掉。

3. **看见初步交易列表叫 raw proposal / 看见应用可以改这套 / 这份对象 is not already 已经只有 raw proposal interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1304 prepusage-notraw interchangeable / 1305 prepusage-notexceed interchangeable，也不是已经 Prepare Request 栏 interchangeable / 423 Prepare Request 栏 interchangeable。**  
   官方把初步交易列表叫 raw proposal和已经只有 raw proposal写成两件。看见初步交易列表叫 raw proposal，不是已经只有 raw proposal。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。

## 官方为什么这样拆

- **raw proposal / can modify this set 不是 Prepare 改列表 bundled interchangeable：官方把 Methods Usage raw proposal 单句和改列表后果 bundled 分开。**
- **看见可以改这套 不是已经从内存池删掉：官方写回包改列表不是池后果。**
- **看见 raw proposal 不是已经只有 raw proposal：本页钉 Usage 侧 can modify set，不是已经冻结成只能原样交回。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Prepare 改列表 bundled | 不是已经 Prepare 改列表 bundled | 不是已经Prepare 改列表（355） |
| 已经从内存池删掉 | 不是已经从内存池删掉 | 不是已经Prepare Request 栏（423） |
| 已经只有 raw proposal | 不是已经只有 raw proposal | 不是已经1305 prepusage-notexceed |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareUsage raw not already Prepare-改列表 / not already deleted-from-mempool / not already only-raw 正式三事（503 余量），必须分开是不是已经 Prepare 改列表 bundled、是不是已经从内存池删掉、是不是已经只有 raw proposal。可以跳过「看见 Prepare 请求里带了 txs 就已经改列表 bundled interchangeable、已经能回超限、已经是引擎会帮你裁 interchangeable」。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。503 PrepareProposal Usage rawmust bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepusage-notexceed-vs-bundled.md`](worked-example-prepusage-notexceed-vs-bundled.md)（不变量 1305 item 2）。

## 本页不抄

- 怎样做裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。
- 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。
