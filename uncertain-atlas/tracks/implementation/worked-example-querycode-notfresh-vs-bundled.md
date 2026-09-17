# 例：看见 Query 回包 log 是应用日志输出 is not already fresh interchangeable / not already replicated interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 log not already fresh / not already replicated / not already settled 正式三事（384 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 log not already fresh / not already replicated / not already settled 正式三事（384 余量）/ not 777 querycode-notfresh interchangeable / not 384 querycode-vs-consensus bundled interchangeable」，不是 Query 回包码 bundled（384），也不是 Query 回了就已经复制到各节点（329），也不是 ExecTxResult.log 就已经是 Query 日志（414/758），也不是 CheckTx log 就已经是 Query 日志（390/745）。不要另写怎样写 Query 回包码。

## 官方三件事

1. **看见 Query 回包 `log` 是应用日志输出 / 看见回了日志 / Query 这份应用日志 is not already 已经新鲜 interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 777 querycode-notfresh interchangeable / 776 querycode-notconsensus interchangeable / 384 querycode item 1 code interchangeable，也不是已经 log not already fresh / not already replicated / not already settled 正式三事 bundled（384 item 2 余量） interchangeable / 384 querycode item 2 interchangeable。**  
   官方写：`log` 是应用日志的输出。看见回了日志，不是已经新鲜 interchangeable——本页从 384 item 2 侧钉 not already fresh 单句。384 querycode vs consensus bundled unbundling 在本页 item 2 续。

2. **看见回了日志 / 看见有日志 / Query 这份应用日志 is not already 已经复制到各节点 interchangeable / 329 queryrep interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 777 querycode-notfresh interchangeable / 384 querycode item 3 info interchangeable / 778 querycode-notkey interchangeable，也不是已经 ExecTxResult.log 就已经是 Query 日志 interchangeable / 414 exectxlog / 758 exectxlog-notquerylog interchangeable，也不是已经 CheckTx log 就已经是 Query 日志 interchangeable / 390 proofop / 745 proofop-notquerylog interchangeable。**  
   官方把应用日志和已经复制到各节点分开——384 bundled 第二件事常与 329 / 414 / 390 混成「看见回了日志就已经新鲜或已经复制到各节点 interchangeable」，本页钉 not already replicated 单句。

3. **看见回了日志 / 看见能读 / Query 这份应用日志 is not already 已经交差 interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 777 querycode-notfresh interchangeable / 776 querycode-notconsensus interchangeable。**  
   官方把能读 Query log 和已经交差分开。看见能读，不是已经交差 interchangeable。384 querycode vs consensus bundled unbundling 在本页 item 2 续。

怎样写 Query 回包码、怎样填日志、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **log not already fresh ≠ 已经新鲜 interchangeable：** 官方把应用日志和已经新鲜分开。
- **log not already replicated ≠ 329 interchangeable：** 官方把有日志和已经复制到各节点分开。
- **log not already settled ≠ 已经交差 interchangeable：** 官方把能读 log 和已经交差分开；384 querycode vs consensus bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 log 是应用日志输出 | 不是已经新鲜 | 不是 Query 回包 code（776/384 item 1） |
| 看见回了日志 | 不是已经复制到各节点（329） | 不是 ExecTxResult.log（414/758） |
| 看见能读 | 不是已经交差 | 不是 CheckTx log（390/745） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 log not already fresh / not already replicated / not already settled 正式三事（384 余量），必须分开 log 是不是已经新鲜、是不是已经复制到各节点 interchangeable / 329、是不是已经交差。可以跳过「看见回了日志就已经新鲜」。不要另写怎样写 Query 回包码。384 querycode vs consensus bundled unbundling 在本页 item 2 续；完成 [`worked-example-querycode-notkey-vs-bundled.md`](worked-example-querycode-notkey-vs-bundled.md)（不变量 778 item 3）。

## 本页不抄

- 怎样写 Query 回包码、怎样填日志、怎样填附加信息。
- Query 回包码 bundled。那是不变量 384。
- Query 回包 code。那是不变量 384 item 1 余量 / 776。
- Query 回包 info。那是不变量 384 item 3 余量 / 778。
- Query 回了就已经复制到各节点。那是不变量 329。
- ExecTxResult.log 就已经是 Query 日志。那是不变量 414 / 758。
- CheckTx log 就已经是 Query 日志。那是不变量 390 / 745。
