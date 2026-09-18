# 例：看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events不是已经是 CheckTxResponse.events；看见pass via FinalizeBlockResponse is not already CheckTx or ExecTx events不是已经是 ExecTxResult.events；看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events不是已经印进 LastResultsHash

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepEv pass via FinalizeBlockResponse not already CheckTx events / not already ExecTxResult events / not already LastResultsHash 正式三事（448 余量）/ not 1370 prepev-notfin interchangeable / not 448 prepevents-vs-finalize bundled interchangeable」，不是 prepevents vs finalize bundled（448），也不是已经 FinalizeBlockResponse.events 就已经印进本头（431），也不是已经 CheckTx 回包 events（381）。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。

## 官方三件事

1. **看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events / 看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events 这份对象 is not already 已经是 CheckTxResponse.events interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1370 prepev-notfin interchangeable / 1368 prepev-notret interchangeable，也不是已经 PrepEv pass via FinalizeBlockResponse not already CheckTx events / not already ExecTxResult events / not already LastResultsHash 正式三事 bundled（448 item 3 余量） interchangeable / 448 prepev item 3 interchangeable。**  
   官方把经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events和已经是 CheckTxResponse.events写成两件。看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events，不是已经是 CheckTxResponse.events。

2. **看见pass via FinalizeBlockResponse is not already CheckTx or ExecTx events / 看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events / 这份对象 is not already 已经是 ExecTxResult.events interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1370 prepev-notfin interchangeable / 1369 prepev-notkeep interchangeable，也不是已经 FinalizeBlockResponse.events 就已经印进本头 interchangeable / 431 FinalizeBlockResponse.events 就已经印进本头 interchangeable。**  
   官方把pass via FinalizeBlockResponse is not already CheckTx or ExecTx events和已经是 ExecTxResult.events写成两件。看见pass via FinalizeBlockResponse is not already CheckTx or ExecTx events，不是已经是 ExecTxResult.events。

3. **看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events / 看见pass via FinalizeBlockResponse is not already CheckTx or ExecTx events / 这份对象 is not already 已经印进 LastResultsHash interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1370 prepev-notfin interchangeable / 1368 prepev-notret interchangeable，也不是已经 CheckTx 回包 events interchangeable / 381 CheckTx 回包 events interchangeable。**  
   官方把经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events和已经印进 LastResultsHash写成两件。看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events，不是已经印进 LastResultsHash。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。

## 官方为什么这样拆

- **经 Finalize 交回 不是已经 CheckTx events interchangeable：官方把保留路径和池门回包分开。**
- **看见块级 events 不是已经 ExecTxResult 逐笔 events（446）。**
- **看见给了 CometBFT 不是已经像 Code/Data 印进 LastResultsHash。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 CheckTxResponse.events | 不是已经是 CheckTxResponse.events | 不是已经FinalizeBlockResponse.events 就已经印进本头（431） |
| 已经是 ExecTxResult.events | 不是已经是 ExecTxResult.events | 不是已经CheckTx 回包 events（381） |
| 已经印进 LastResultsHash | 不是已经印进 LastResultsHash | 不是已经1368 prepev-notret |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepEv pass via FinalizeBlockResponse not already CheckTx events / not already ExecTxResult events / not already LastResultsHash 正式三事（448 余量），必须分开是不是已经是 CheckTxResponse.events、是不是已经是 ExecTxResult.events、是不是已经印进 LastResultsHash。可以跳过「看见 Prepare 里产出了事件就已经交给引擎」。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。448 Prepare events retention until Finalize bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样攒 Prepare 事件、怎样等块决定、怎样在 Finalize 交回。
- 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。
