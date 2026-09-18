# 例：看见MAY 让请求超上限不是已经 Req 2 bundled；看见MaxBytes=-1 会交来整池不是已经能回超限列表；看见MAY 让请求超上限不是已经整池都给 Prepare 就没有上限

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareUsage exceed not already Req-2 / not already can-return-oversize / not already no-cap 正式三事（503 余量）/ not 1305 prepusage-notexceed interchangeable / not 503 prepareusage-rawmust-vs-bundled bundled interchangeable」，不是 prepareusage rawmust vs bundled bundled（503），也不是已经 Req 2（345），也不是已经 整池没有上限（299）。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。

## 官方三件事

1. **看见MAY 让请求超上限 / 看见MAY 让请求超上限 这份对象 is not already 已经 Req 2 bundled interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1305 prepusage-notexceed interchangeable / 1304 prepusage-notraw interchangeable，也不是已经 PrepareUsage exceed not already Req-2 / not already can-return-oversize / not already no-cap 正式三事 bundled（503 item 2 余量） interchangeable / 503 prepusage item 2 interchangeable。**  
   官方把MAY 让请求超上限和已经 Req 2 bundled写成两件。看见MAY 让请求超上限，不是已经 Req 2 bundled。

2. **看见MaxBytes=-1 会交来整池 / 看见MAY 让请求超上限 / 这份对象 is not already 已经能回超限列表 interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1305 prepusage-notexceed interchangeable / 1306 prepusage-notmust interchangeable，也不是已经 Req 2 interchangeable / 345 Req 2 interchangeable。**  
   官方把MaxBytes=-1 会交来整池和已经能回超限列表写成两件。看见MaxBytes=-1 会交来整池，不是已经能回超限列表。

3. **看见MAY 让请求超上限 / 看见MaxBytes=-1 会交来整池 / 这份对象 is not already 已经整池都给 Prepare 就没有上限 interchangeable，也不是已经 prepareusage rawmust vs bundled bundled（503） interchangeable / 1305 prepusage-notexceed interchangeable / 1304 prepusage-notraw interchangeable，也不是已经 整池没有上限 interchangeable / 299 整池没有上限 interchangeable。**  
   官方把MAY 让请求超上限和已经整池都给 Prepare 就没有上限写成两件。看见MAY 让请求超上限，不是已经整池都给 Prepare 就没有上限。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。

## 官方为什么这样拆

- **MAY configure exceeding 不是 Req 2 bundled interchangeable：官方把 MAY 让请求超上限和 requirements 侧 Req 2 保证分开。**
- **看见会交来整池 不是已经能回超限列表：345 第三件事钉回包不得超过，本页钉 Usage 侧 MAY 让请求超上限。**
- **看见 MaxBytes=-1 不是已经整池都给 Prepare 就没有上限：那是不变量 299。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Req 2 bundled | 不是已经 Req 2 bundled | 不是已经Req 2（345） |
| 已经能回超限列表 | 不是已经能回超限列表 | 不是已经整池没有上限（299） |
| 已经整池都给 Prepare 就没有上限 | 不是已经整池都给 Prepare 就没有上限 | 不是已经1304 prepusage-notraw |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareUsage exceed not already Req-2 / not already can-return-oversize / not already no-cap 正式三事（503 余量），必须分开是不是已经 Req 2 bundled、是不是已经能回超限列表、是不是已经整池都给 Prepare 就没有上限。可以跳过「看见 Prepare 请求里带了 txs 就已经改列表 bundled interchangeable、已经能回超限、已经是引擎会帮你裁 interchangeable」。不要另写 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。503 PrepareProposal Usage rawmust bundled unbundling 在本页 item 2 续；续 [`worked-example-prepusage-notmust-vs-bundled.md`](worked-example-prepusage-notmust-vs-bundled.md)（不变量 1306 item 3）。

## 本页不抄

- 怎样做裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。
- 怎样裁回包、怎样设 MaxBytes = -1、怎样改 Prepare 列表。
