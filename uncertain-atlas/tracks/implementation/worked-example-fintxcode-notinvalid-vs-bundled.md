# 例：看见 Code == 0 only if fully valid / 看见这笔完全合法 is not already 已经 Code != 0 那种没进块 interchangeable / 已经无效就不建索引 interchangeable / 已经 fintxcode bundled interchangeable

**层次**：实现 / FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block / not no index / not fintxcode bundled 正式三事（585 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block / not no index / not fintxcode bundled 正式三事（585 余量）/ not 627 notinvalid interchangeable / not 316 exectxresult interchangeable / not 312 checktxopt interchangeable / not 626 notchecktx interchangeable / not 628 notsettled interchangeable」，不是 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585），也不是 ExecTxResult 回执 bundled（316），也不是 Finalize 落盘禁令（335）。不要另写怎样编回执、怎样建索引、怎样算 LastResultsHash。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.tx_results[i].Code == 0` only if the _i_-th transaction is fully valid 和 Req 里若 `Code ≠ 0` 这笔会被标成无效但仍在块里 / 无效交易不建索引 和「已经是已经 Code != 0 那种没进块 interchangeable / 已经是已经无效就不建索引 interchangeable / 已经是 fintxcode bundled interchangeable」分开写成三件独立的实现事，不是「看见 only if fully valid 就已经 Code != 0 那种没进块、就已经没索引就等于没进块、就已经 fintxcode bundled interchangeable」一件事：

1. **看见 Code == 0 only if fully valid / 看见 only if fully valid / 看见这笔完全合法 is not already 已经 Code != 0 那种没进块 interchangeable / Code 非零仍可能在块里 interchangeable / 316 exectxresult interchangeable / 316 Code nonzero still in block interchangeable / 585 fintxcode item 2 interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 627 notinvalid interchangeable / 585 fintxcode interchangeable / 626 notchecktx interchangeable / 404 finapphash item 3 Code==0 interchangeable，也不是已经 ExecTxResult 回执 bundled（316 余量） interchangeable / 316 exectxresult interchangeable / 316 item 2 Code nonzero still in block interchangeable / 316 item 3 Code Data LastResultsHash interchangeable / 315 exectxgas interchangeable，也不是已经 CheckTx 可选 bundled（312 余量） interchangeable / 312 checktxopt interchangeable / 312 item 2 Code≠0 rejected interchangeable / 373 checktxresponse interchangeable / 489 chktxcodereject interchangeable，也不是已经 CheckTx Usage Code≠0 rejected bundled（489 余量） interchangeable / 489 chktxcodereject interchangeable / 312 checktxopt interchangeable / 339 checktxweak interchangeable / 313 checktxguard interchangeable。**  
   官方 Usage 写 only if fully valid。Req 写：若 `Code ≠ 0`，这笔会被标成无效，但仍在块里。看见 fully valid，不是已经 Code 非零就等于没进块（316） interchangeable——585 bundled 第二件事常被写成「看见 only if fully valid 就已经 Code != 0 那种没进块 interchangeable」，本页从 585 item 2 侧钉 not still in block 单句。看见 only if fully valid，不是已经 ExecTxResult 回执 bundled（316） item 2 interchangeable——316 另钉 Code 非零仍可能在块里 / 不建索引，本页钉 585 item 2 第一件事。看见 Code==0 only if fully valid，不是已经 CheckTx Code≠0 会被拒不会进提案（312 / 489） interchangeable——312 / 489 钉池门 / 提案前拒，本页钉 Finalize fully valid 与在块里与否单句。
2. **看见 Code == 0 only if fully valid / 看见 only if fully valid is not already 已经无效就不建索引 interchangeable / 没索引就等于没进块 interchangeable / 316 exectxresult item 2 no index interchangeable / 316 invalid not indexed interchangeable / 312 checktxopt item 2 not in block interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 627 notinvalid interchangeable / 585 fintxcode interchangeable / 431 finrespbar interchangeable / 316 exectxresult interchangeable，也不是已经 ExecTxResult 回执 bundled（316 余量） interchangeable / 316 exectxresult interchangeable / 316 item 1 list order interchangeable / 316 item 3 Code Data LastResultsHash interchangeable / 384 exectxlog interchangeable，也不是已经 FinalizeBlockResponse tx_results 是执行结果列表 bundled（431 余量） interchangeable / 431 finrespbar interchangeable / 373 checktxresponse interchangeable / 316 exectxresult interchangeable / 312 checktxopt interchangeable，也不是已经 CheckTx 可选 bundled（312 余量） interchangeable / 312 checktxopt interchangeable / 312 item 3 engine ignores Data interchangeable / 373 checktxresponse interchangeable / 339 checktxweak interchangeable。**  
   官方把 invalid not indexed 和 still in block 分开——585 item 2 常与 316 混成「看见 only if fully valid 就已经没索引就等于没进块 interchangeable」，本页钉 not no index 单句。看见 fully valid，不是已经无效交易不建索引（316 item 2） interchangeable——316 钉标无效 / 仍在块里 / 不建索引，本页钉 585 item 2 第二件事。看见 only if fully valid，不是已经 CheckTx Code≠0 不会广播也不会进提案（312） interchangeable——312 另钉池门拒 / 不参与处理块，本页钉 not no index 单句。
3. **看见 Code == 0 only if fully valid / 看见 only if fully valid is not already fintxcode bundled（585） interchangeable / 已经 CheckTx 过了 interchangeable / 已经 Process Accept interchangeable / 585 fintxcode item 1 interchangeable / 585 fintxcode item 3 interchangeable / 626 notchecktx interchangeable / 628 notsettled interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 627 notinvalid interchangeable / 626 notchecktx interchangeable / 628 notsettled interchangeable / 404 finapphash interchangeable / 335 finpersist interchangeable，也不是已经 Code == 0 only if fully valid not CheckTx passed bundled（585 item 1 余量 / 626） interchangeable / 626 notchecktx interchangeable / 339 checktxweak interchangeable / 347 req3coherence interchangeable / 530 procaccept interchangeable，也不是已经 回了 tx_results not Finalize changed already settled bundled（585 item 3 余量 / 628） interchangeable / 628 notsettled interchangeable / 335 finpersist interchangeable / 404 finapphash item 3 Code==0 interchangeable / 587 finreturn interchangeable，也不是已经 Finalize 回包余量 bundled（404 余量） interchangeable / 404 finapphash interchangeable / 404 item 3 Code==0 interchangeable / 404 item 1 empty hardcoded interchangeable / 404 item 2 Query proofs interchangeable。**  
   官方把 585 fintxcode bundled 三事里的 only if fully valid 与 Code 非零仍可能在块里 / 回了 tx_results 已经交差分开——585 bundled 常与 item 1 / item 3 混成「看见 only if fully valid 就已经 fintxcode bundled interchangeable」，本页钉 585 item 2 第三件事。看见 fully valid，不是已经 CheckTx 过了（585 item 1 余量 / 626） interchangeable——626 另钉 not CheckTx passed / not Process Accept，本页钉 item 2 单句。看见 only if fully valid，不是已经 Finalize 改了就已经交差（585 item 3 余量 / 628） interchangeable——628 另钉 not settled / not Code Data 印进本头，本页钉 not fintxcode bundled 单句。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的做法，本页不抄。FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585）、Code == 0 only if fully valid not CheckTx passed（585 item 1 余量 / 626）、回了 tx_results not Finalize changed already settled（585 item 3 余量 / 628）、ExecTxResult 回执 bundled（316）、Finalize 落盘禁令（335）、Finalize 回包余量 bundled（404）、CheckTx 可选（312）是另外那套，本页不抄。

## 官方为什么这样拆

- **only if fully valid not still in block ≠ 316 exectxresult / 312 checktxopt interchangeable：** 官方把 fully valid 语义和 Code 非零仍可能在块里分开。
- **only if fully valid not no index ≠ 316 invalid not indexed / 431 finrespbar interchangeable：** 官方把 585 item 2 和无效不建索引 / 没索引不等于没进块分开。
- **only if fully valid not fintxcode bundled ≠ 626 notchecktx / 628 notsettled interchangeable：** 官方把 585 item 2 和 item 1 / item 3 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| only if fully valid | 不是 already Code != 0 那种没进块 | 不是 ExecTxResult bundled（316） |
| only if fully valid | 不是 already 没索引就等于没进块 | 不是 CheckTx 可选（312） |
| only if fully valid | 不是 already fintxcode bundled | 不是 not CheckTx passed（585 item 1 / 626） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block / not no index / not fintxcode bundled 正式三事（585 余量），必须分开 only if fully valid 是不是 already Code != 0 那种没进块 interchangeable / 316 exectxresult interchangeable / 312 checktxopt interchangeable、only if fully valid 是不是 already 没索引就等于没进块 interchangeable / 316 invalid not indexed interchangeable / 431 finrespbar interchangeable、only if fully valid 是不是 already fintxcode bundled interchangeable / 626 notchecktx interchangeable / 628 notsettled interchangeable / 404 finapphash interchangeable。可以跳过「看见 only if fully valid 就已经 Code != 0 那种没进块 interchangeable」。不要另写怎样编回执。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- FinalizeBlock tx_results Code==0 完全合法正式三事 bundled。那是不变量 585。
- Code == 0 only if fully valid not CheckTx passed。那是不变量 585 item 1 余量 / 626。
- 回了 tx_results not Finalize changed already settled。那是不变量 585 item 3 余量 / 628。
- ExecTxResult 回执 bundled。那是不变量 316。
- Finalize 落盘禁令。那是不变量 335。
- Finalize 回包余量 bundled。那是不变量 404。
- CheckTx 弱过滤器。那是不变量 339。
