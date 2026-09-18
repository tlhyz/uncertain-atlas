# 例：看见逐笔 events 不是已经是块级 Finalize events不是已经是 FinalizeBlockResponse.events；看见per-tx events is not already FinalizeBlockResponse.events不是已经是 CheckTxResponse.events；看见逐笔 events 不是已经是块级 Finalize events不是已经和池门回包 interchangeable

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields events 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxEv per-tx events in tx_results not already block-level 431 / not already CheckTx 381 / not already interchangeable 正式三事（446 余量）/ not 1364 etxev-notlvl interchangeable / not 446 exectxevents-vs-header bundled interchangeable」，不是 exectxevents vs header bundled（446），也不是已经 FinalizeBlockResponse.events 块级索引（431），也不是已经 CheckTx 回包 events（381）。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。

## 官方三件事

1. **看见逐笔 events 不是已经是块级 Finalize events / 看见逐笔 events 不是已经是块级 Finalize events 这份对象 is not already 已经是 FinalizeBlockResponse.events interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1364 etxev-notlvl interchangeable / 1362 etxev-notidx interchangeable，也不是已经 ExecTxEv per-tx events in tx_results not already block-level 431 / not already CheckTx 381 / not already interchangeable 正式三事 bundled（446 item 3 余量） interchangeable / 446 etxev item 3 interchangeable。**  
   官方把逐笔 events 不是已经是块级 Finalize events和已经是 FinalizeBlockResponse.events写成两件。看见逐笔 events 不是已经是块级 Finalize events，不是已经是 FinalizeBlockResponse.events。

2. **看见per-tx events is not already FinalizeBlockResponse.events / 看见逐笔 events 不是已经是块级 Finalize events / 这份对象 is not already 已经是 CheckTxResponse.events interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1364 etxev-notlvl interchangeable / 1363 etxev-notdet interchangeable，也不是已经 FinalizeBlockResponse.events 块级索引 interchangeable / 431 FinalizeBlockResponse.events 块级索引 interchangeable。**  
   官方把per-tx events is not already FinalizeBlockResponse.events和已经是 CheckTxResponse.events写成两件。看见per-tx events is not already FinalizeBlockResponse.events，不是已经是 CheckTxResponse.events。

3. **看见逐笔 events 不是已经是块级 Finalize events / 看见per-tx events is not already FinalizeBlockResponse.events / 这份对象 is not already 已经和池门回包 interchangeable interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1364 etxev-notlvl interchangeable / 1362 etxev-notidx interchangeable，也不是已经 CheckTx 回包 events interchangeable / 381 CheckTx 回包 events interchangeable。**  
   官方把逐笔 events 不是已经是块级 Finalize events和已经和池门回包 interchangeable写成两件。看见逐笔 events 不是已经是块级 Finalize events，不是已经和池门回包 interchangeable。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。

## 官方为什么这样拆

- **逐笔 tx_results.events 不是已经是块级 events interchangeable：官方把逐笔回执和 FinalizeBlockResponse.events 分开。**
- **看见 Finalize 回执里 events 不是已经 CheckTx 回包 events interchangeable。**
- **看见每笔有 events 不是已经和 381 池门回包同一份。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 FinalizeBlockResponse.events | 不是已经是 FinalizeBlockResponse.events | 不是已经FinalizeBlockResponse.events 块级索引（431） |
| 已经是 CheckTxResponse.events | 不是已经是 CheckTxResponse.events | 不是已经CheckTx 回包 events（381） |
| 已经和池门回包 interchangeable | 不是已经和池门回包 interchangeable | 不是已经1362 etxev-notidx |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxEv per-tx events in tx_results not already block-level 431 / not already CheckTx 381 / not already interchangeable 正式三事（446 余量），必须分开是不是已经是 FinalizeBlockResponse.events、是不是已经是 CheckTxResponse.events、是不是已经和池门回包 interchangeable。可以跳过「看见 ExecTxResult 里填了 events 就已经印进本头」。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。446 ExecTxResult events vs header bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样写 ExecTxResult events 栏、怎样填 events、怎样建索引。
- 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。
