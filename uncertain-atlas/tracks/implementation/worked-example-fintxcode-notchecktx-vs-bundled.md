# 例：看见 `FinalizeBlockResponse.tx_results[i].Code == 0` only if the i-th transaction is fully valid / 看见 only if fully valid is not already 已经 CheckTx 过了 interchangeable / 已经 Process 回了 Accept interchangeable / 已经 fintxcode bundled interchangeable

**层次**：实现 / FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed / not Process Accept / not fintxcode bundled 正式三事（585 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed / not Process Accept / not fintxcode bundled 正式三事（585 余量）/ not 626 notchecktx interchangeable / not 339 checktxweak interchangeable / not 347 procaccept interchangeable / not 530 procaccept interchangeable / not 627 notinvalid interchangeable / not 628 notsettled interchangeable」，不是 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585），也不是 ExecTxResult 回执 bundled（316），也不是 Finalize 落盘禁令（335）。不要另写怎样编回执、怎样建索引、怎样算 LastResultsHash。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.tx_results[i].Code == 0` only if the _i_-th transaction is fully valid 和「已经是已经 CheckTx 过了 interchangeable / 已经是已经 Process 回了 Accept interchangeable / 已经是 fintxcode bundled interchangeable」分开写成三件独立的实现事，不是「看见 only if fully valid 就已经 CheckTx 过了、就已经 Process Accept、就已经 fintxcode bundled interchangeable」一件事：

1. **看见 `FinalizeBlockResponse.tx_results[i].Code == 0` only if the _i_-th transaction is fully valid / 看见 only if fully valid / 看见回了 0 is not already 已经 CheckTx 过了 interchangeable / CheckTx 弱过滤器 interchangeable / 339 checktxweak interchangeable / 312 checktxopt interchangeable / 313 checktxguard interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 626 notchecktx interchangeable / 585 fintxcode interchangeable / 404 finapphash item 3 Code==0 interchangeable / 316 exectxresult interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339 余量） interchangeable / 339 checktxweak interchangeable / 312 checktxopt interchangeable / 313 checktxguard interchangeable / 339 item 2 ProcessProposal interchangeable / 339 item 3 mempool interchangeable，也不是已经 CheckTx 守卫 bundled（313 余量） interchangeable / 313 checktxguard interchangeable / 373 checktxresponse interchangeable / 312 checktxopt interchangeable / 339 checktxweak interchangeable，也不是已经 CheckTx 可选 bundled（312 余量） interchangeable / 312 checktxopt interchangeable / 373 checktxresponse interchangeable / 316 exectxresult interchangeable / 33 four gates interchangeable。**  
   官方 Usage 写：`FinalizeBlockResponse.tx_results[i].Code == 0` only if the _i_-th transaction is fully valid。Req 另写：若 `Code ≠ 0`，这笔会被标成无效，但仍在块里。看见 only if fully valid，不是已经 CheckTx 弱过滤器（339） interchangeable——585 bundled 第一件事常被写成「看见回了 0 就已经 CheckTx 过了 interchangeable」，本页从 585 item 1 侧钉 not CheckTx passed 单句。看见 fully valid，不是已经 CheckTx 是内存池守卫（313） interchangeable——313 另钉 CheckTx 守卫 / 每条节点先跑 CheckTx，本页钉 585 item 1 第一件事。看见 Code==0 only if fully valid，不是已经 CheckTx 技术上可选（312） interchangeable——312 另钉 CheckTx 不参与处理块 / Code≠0 会被拒，本页钉 not CheckTx passed 单句。
2. **看见 `FinalizeBlockResponse.tx_results[i].Code == 0` only if fully valid / 看见 only if fully valid is not already 已经 Process 回了 Accept interchangeable / ProcessProposal ACCEPT interchangeable / 347 procaccept interchangeable / 530 procaccept interchangeable / 456 procaccept interchangeable / 347 req3coherence interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 626 notchecktx interchangeable / 585 fintxcode interchangeable / 354 processwhen interchangeable / 351 processalso interchangeable / 360 finprocgua interchangeable，也不是已经 ProcessProposal SHOULD always set ACCEPT bundled（530 余量） interchangeable / 530 procaccept interchangeable / 531 procliveness interchangeable / 532 procdefault interchangeable / 347 req3coherence interchangeable，也不是已经 ProcessProposal Usage SHOULD Accept default strategy bundled（532 余量） interchangeable / 532 procdefault interchangeable / 533 procreject interchangeable / 347 req3coherence interchangeable / 354 processwhen interchangeable，也不是已经 正确提议者的准备提案必须被正确接收者 Accept bundled（347 余量） interchangeable / 347 req3coherence interchangeable / 347 item 2 Prepare Process bug interchangeable / 347 item 3 Req 3 tested interchangeable / 338 preparenondet interchangeable。**  
   官方把 only if fully valid 和 Process 回了 Accept 分开——585 item 1 常与 347 混成「看见 only if fully valid 就已经 Process 回了 Accept interchangeable」，本页钉 not Process Accept 单句。看见 fully valid，不是已经 ProcessProposal SHOULD always set ACCEPT（530） interchangeable——530 钉 SHOULD 通则，本页钉 585 item 1 第二件事。看见 Code==0 only if fully valid，不是已经 Req 3 诚实提案必须 Accept（347） interchangeable——347 另钉 Prepare / Process 一致性 / 347 item 2 bug，本页钉 not Process Accept 单句。
3. **看见 `FinalizeBlockResponse.tx_results[i].Code == 0` only if fully valid / 看见 only if fully valid is not already fintxcode bundled（585） interchangeable / 已经 Code != 0 那种没进块 interchangeable / 已经 Finalize 改了就已经交差 interchangeable / 585 fintxcode item 2 interchangeable / 585 fintxcode item 3 interchangeable / 627 notinvalid interchangeable / 628 notsettled interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 626 notchecktx interchangeable / 627 notinvalid interchangeable / 628 notsettled interchangeable / 404 finapphash interchangeable / 316 exectxresult interchangeable / 335 finpersist interchangeable，也不是已经 Code == 0 only if fully valid not Code != 0 still in block bundled（585 item 2 余量 / 627） interchangeable / 627 notinvalid interchangeable / 316 exectxresult interchangeable / 316 Code nonzero still in block interchangeable / 316 Code Data LastResultsHash interchangeable，也不是已经 回了 tx_results not Finalize changed already settled bundled（585 item 3 余量 / 628） interchangeable / 628 notsettled interchangeable / 335 finpersist interchangeable / 404 finapphash item 3 Code==0 interchangeable / 587 finreturn interchangeable，也不是已经 Finalize 回包余量 bundled（404 余量） interchangeable / 404 finapphash interchangeable / 404 item 3 Code==0 interchangeable / 404 item 1 empty hardcoded interchangeable / 404 item 2 Query proofs interchangeable。**  
   官方把 585 fintxcode bundled 三事里的 only if fully valid 和 Code 非零仍可能在块里 / 回了 tx_results 已经交差分开——585 bundled 常与 item 2 / item 3 混成「看见 only if fully valid 就已经 fintxcode bundled interchangeable」，本页钉 585 item 1 第三件事。看见 only if fully valid，不是已经 Code != 0 那种没进块（585 item 2 余量 / 627） interchangeable——627 另钉 not still in block / not no index，本页钉 item 1 单句。看见 fully valid，不是已经 Finalize 改了就已经交差（585 item 3 余量 / 628） interchangeable——628 另钉 not settled / not Code Data 印进本头，本页钉 not fintxcode bundled 单句。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的做法，本页不抄。FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585）、Code == 0 only if fully valid not Code != 0 still in block（585 item 2 余量 / 627）、回了 tx_results not Finalize changed already settled（585 item 3 余量 / 628）、ExecTxResult 回执 bundled（316）、Finalize 落盘禁令（335）、Finalize 回包余量 bundled（404）、CheckTx 弱过滤器（339）是另外那套，本页不抄。

## 官方为什么这样拆

- **Code==0 only if fully valid not CheckTx passed ≠ 339 checktxweak / 313 checktxguard interchangeable：** 官方把 Finalize 这笔 fully valid 和 CheckTx 池门分开。
- **Code==0 only if fully valid not Process Accept ≠ 347 req3coherence / 530 procaccept interchangeable：** 官方把 only if fully valid 和 Process Accept 分开。
- **Code==0 only if fully valid not fintxcode bundled ≠ 627 notinvalid / 628 notsettled interchangeable：** 官方把 585 item 1 和 item 2 / item 3 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code==0 only if fully valid | 不是 already CheckTx 过了 | 不是 CheckTx 弱过滤器（339） |
| Code==0 only if fully valid | 不是 already Process Accept | 不是 Req 3 / procaccept（347 / 530） |
| Code==0 only if fully valid | 不是 already fintxcode bundled | 不是 Code 非零仍可能在块里（585 item 2 / 627） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed / not Process Accept / not fintxcode bundled 正式三事（585 余量），必须分开 only if fully valid 是不是 already CheckTx 过了 interchangeable / 339 checktxweak interchangeable / 313 checktxguard interchangeable、only if fully valid 是不是 already Process Accept interchangeable / 347 req3coherence interchangeable / 530 procaccept interchangeable、only if fully valid 是不是 already fintxcode bundled interchangeable / 627 notinvalid interchangeable / 628 notsettled interchangeable / 404 finapphash interchangeable。可以跳过「看见 only if fully valid 就已经 CheckTx 过了 interchangeable」。不要另写怎样编回执。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- FinalizeBlock tx_results Code==0 完全合法正式三事 bundled。那是不变量 585。
- Code == 0 only if fully valid not Code != 0 still in block。那是不变量 585 item 2 余量 / 627。
- 回了 tx_results not Finalize changed already settled。那是不变量 585 item 3 余量 / 628。
- ExecTxResult 回执 bundled。那是不变量 316。
- Finalize 落盘禁令。那是不变量 335。
- Finalize 回包余量 bundled。那是不变量 404。
- CheckTx 弱过滤器。那是不变量 339。
