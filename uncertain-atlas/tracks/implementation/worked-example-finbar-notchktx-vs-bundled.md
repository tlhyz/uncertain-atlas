# 例：看见 FinalizeBlockResponse.tx_results is not already checktx-resp interchangeable / not already resulthash interchangeable / not already log-only interchangeable

**层次**：实现 / FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事（431 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事（431 余量）/ not 1071 finbar-notchktx interchangeable / not 431 finrespbar-vs-header bundled interchangeable」，不是 Finalize 回包栏 bundled（431），也不是 Code / Data 就已经印进本头（316），也不是结果列表和送来的交易同一顺序就已经印进 LastResultsHash。不要另写怎样写 Finalize 回包栏。

## 官方三件事

1. **看见 FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表 / 看见回了 tx_results 这份栏 is not already 已经是 CheckTx 回包 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1071 finbar-notchktx interchangeable / 1070 finbar-notheader interchangeable / 431 finrespbar item 1 events interchangeable，也不是已经 FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事 bundled（431 item 2 余量） interchangeable / 431 finrespbar item 2 interchangeable。**  
   官方写：tx_results 是 List of structures containing the data resulting from executing the transactions。Deterministic 列是 Yes。看见回了列表，不是已经是 CheckTx 回包 interchangeable——本页从 431 item 2 侧钉 not already checktx-resp 单句。431 finrespbar vs header bundled unbundling 在本页 item 2 续。

2. **看见有执行结果 / 看见回了 tx_results / 这份栏 is not already 已经印进 LastResultsHash interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1071 finbar-notchktx interchangeable / 431 finrespbar item 3 validator_updates interchangeable / 1072 finbar-notrotate interchangeable，也不是已经 Code / Data 就已经印进本头 interchangeable / 316 exectx interchangeable。**  
   官方把有执行结果和已经印进 LastResultsHash 分开。看见有执行结果，不是已经印进 LastResultsHash interchangeable。本页钉 not already resulthash 单句。

3. **看见 Deterministic 是 Yes / 看见回了 tx_results / 这份栏 is not already 已经只是记日志 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1071 finbar-notchktx interchangeable / 1070 finbar-notheader interchangeable，也不是已经 Info / Log 标成非确定那种只是记日志 interchangeable。**  
   官方把 Deterministic 是 Yes 和已经只是记日志分开。看见 Deterministic 是 Yes，不是已经只是记日志 interchangeable。431 finrespbar vs header bundled unbundling 在本页 item 2 续。

怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.tx_results not already checktx-resp ≠ 已经是 CheckTx 回包 interchangeable：** 官方把执行结果列表和已经是 CheckTx 回包分开。
- **看见有执行结果 not already resulthash ≠ 已经印进 LastResultsHash interchangeable：** 官方把有执行结果和已经印进 LastResultsHash 分开。
- **看见 Deterministic 是 Yes not already log-only ≠ 已经只是记日志 interchangeable：** 官方把 Deterministic 是 Yes 和已经只是记日志分开；431 finrespbar vs header bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表 | 不是已经是 CheckTx 回包 | 不是 Code / Data 就已经印进本头（316） |
| 看见有执行结果 | 不是已经印进 LastResultsHash | 不是结果列表同一顺序就已经印进 LastResultsHash |
| 看见 Deterministic 是 Yes | 不是已经只是记日志 | 不是 validator_updates 就已经在 H+1 换人（1072） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事（431 余量），必须分开是不是已经是 CheckTx 回包、是不是已经印进 LastResultsHash、是不是已经只是记日志。可以跳过「看见回了 Finalize 回包栏就已经印进本头」。不要另写怎样写 Finalize 回包栏。431 finrespbar vs header bundled unbundling 在本页 item 2 续；续 [`worked-example-finbar-notrotate-vs-bundled.md`](worked-example-finbar-notrotate-vs-bundled.md)（不变量 1072 item 3）。

## 本页不抄

- 怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate。
- Finalize 回包栏 bundled。那是不变量 431。
- Code / Data 就已经印进本头。那是不变量 316。
- 结果列表同一顺序就已经印进 LastResultsHash。那是相邻 Usage 页，不是本页。
