# 例：看见 CheckTx 回包 log 是应用日志输出 is not already Query log interchangeable / not already CheckTx Data used interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx 回包 log not Query log / not CheckTx Data used / not already settled 正式三事（390 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 回包 log not Query log / not CheckTx Data used / not already settled 正式三事（390 余量）/ not 745 proofop-notquerylog interchangeable / not 390 proofop-vs-key bundled interchangeable」，不是 ProofOp 键 bundled（390），也不是 Query 回包 log 就已经新鲜（384）。不要另写怎样写 ProofOp 键。

## 官方三件事

1. **看见 CheckTx 回包 `log` 是应用日志输出 / 看见回了日志 / CheckTx 这份日志 is not already 已经是 Query 回包那份日志 interchangeable / 384 querylog interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 745 proofop-notquerylog interchangeable / 743 proofop-notquerykey interchangeable / 390 proofop item 1 key interchangeable，也不是已经 log not Query log / not CheckTx Data used / not already settled 正式三事 bundled（390 item 3 余量） interchangeable / 390 proofop item 3 interchangeable。**  
   官方写：`log` 是应用日志的输出。看见回了日志，不是已经是 Query 回包那份日志 interchangeable——本页从 390 item 3 侧钉 not Query log 单句。390 proofop vs key bundled unbundling 在本页 item 3 完成。

2. **看见回了日志 / 看见有日志 / CheckTx 这份日志 is not already 已经是 CheckTx 的 Data 被引擎用了 interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 745 proofop-notquerylog interchangeable / 390 proofop item 2 data interchangeable / 744 proofop-notproofops interchangeable。**  
   官方把 CheckTx 这份日志和 Data 被引擎用了分开——390 bundled 第三件事常与 Data 混成「看见回了日志就已经被引擎用了 interchangeable」，本页钉 not CheckTx Data used 单句。

3. **看见回了日志 / 看见能回 / CheckTx 这份日志 is not already 已经交差 interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 745 proofop-notquerylog interchangeable / 743 proofop-notquerykey interchangeable。**  
   官方把能回日志和已经交差分开。看见能回，不是已经交差 interchangeable。390 proofop vs key bundled unbundling 在本页 item 3 完成。

怎样写 ProofOp 键、怎样填 key、怎样编 data 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **log not Query log ≠ 384 interchangeable：** 官方把 CheckTx 这份日志和 Query 那份日志分开。
- **log not CheckTx Data used ≠ Data interchangeable：** 官方把有日志和 Data 被引擎用了分开。
- **log not already settled ≠ 已经交差 interchangeable：** 官方把能回日志和已经交差分开；390 proofop vs key bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 回包 log 是应用日志输出 | 不是已经是 Query 日志（384） | 不是 key（743/390 item 1） |
| 看见回了日志 | 不是已经 Data 被引擎用了 | 不是 ProofOp 键 bundled（390） |
| 看见能回 | 不是已经交差 | 不是 data（744/390 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 log not Query log / not CheckTx Data used / not already settled 正式三事（390 余量），必须分开 log 是不是已经是 Query 日志 interchangeable / 384、是不是已经 Data 被引擎用了、是不是已经交差。可以跳过「看见回了日志就已经是 Query 日志」。不要另写怎样写 ProofOp 键。390 proofop vs key bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ProofOp 键、怎样填 key、怎样编 data。
- ProofOp 键 bundled。那是不变量 390。
- ProofOp.key。那是不变量 390 item 1 余量 / 743。
- ProofOp.data。那是不变量 390 item 2 余量 / 744。
- Query 回包 log 就已经新鲜。那是不变量 384。
