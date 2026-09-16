# 例：看见回了 `tx_results` / 看见有 Code is not already 已经 Finalize 改了就已经交差 interchangeable / 已经 Code / Data 印进本头 LastResultsHash interchangeable / 已经 fintxcode bundled interchangeable

**层次**：实现 / FinalizeBlockResponse tx_results returned not Finalize changed already settled / not Code Data printed in this header LastResultsHash / not fintxcode bundled 正式三事（585 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlockResponse tx_results returned not Finalize changed already settled / not Code Data printed in this header LastResultsHash / not fintxcode bundled 正式三事（585 余量）/ not 628 notsettled interchangeable / not 335 finpersist interchangeable / not 316 exectxresult interchangeable / not 404 finapphash interchangeable / not 626 notchecktx interchangeable / not 627 notinvalid interchangeable」，不是 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585），也不是 ExecTxResult 回执 bundled（316），也不是 Finalize 落盘禁令 bundled（335）。不要另写怎样编回执、怎样建索引、怎样算 LastResultsHash。

## 官方三件事

规范把 FinalizeBlock Usage 里回了 `tx_results` / 看见有 Code 和 Req 里 `Code` / `Data` 必须确定、编进结构再哈希进下一高度块头的 `LastResultsHash` 和「已经是已经 Finalize 改了就已经交差 interchangeable / 已经是已经 Code / Data 印进本头 interchangeable / 已经是 fintxcode bundled interchangeable」分开写成三件独立的实现事，不是「看见回了 tx_results 就已经 Finalize 改了就已经交差、就已经 Code / Data 印进本头、就已经 fintxcode bundled interchangeable」一件事：

1. **看见回了 `tx_results` / 看见有 Code / 看见 FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表 is not already 已经 Finalize 改了就已经交差 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 628 notsettled interchangeable / 585 fintxcode interchangeable / 626 notchecktx interchangeable / 404 finapphash item 3 Code==0 interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335 余量） interchangeable / 335 finpersist interchangeable / 335 item 1 Finalize 改了就已经落盘 interchangeable / 335 item 2 必须在 Commit 落盘 interchangeable / 616 notpersist interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 1 引擎才落盘这三份 interchangeable / 403 item 2 落完再锁内存池 interchangeable / 587 finreturn item 3 persists interchangeable，也不是已经 FinalizeBlock When CometBFT persists tx outputs / AppHash / ResultsHash not already settled bundled（587 item 3 余量 / 616） interchangeable / 616 notpersist interchangeable / 481 commitpersist interchangeable / 467 finpersist interchangeable / 478 finpersist interchangeable。**  
   官方写：`Code == 0` 只表示这笔完全合法。Req 另写：`Code` / `Data` 必须确定，编进结构再哈希进下一高度块头的 `LastResultsHash`。看见回了 tx_results，不是已经 Finalize 改了就已经交差（335） interchangeable——585 bundled 第三件事常被写成「看见回了 tx_results 就已经 Finalize 改了就已经交差 interchangeable」，本页从 585 item 3 侧钉 not already settled 单句。看见有 Code，不是已经 Finalize + Commit 交差（33） interchangeable——33 钉四门已经结算，本页钉 585 item 3 第一件事。看见 tx_results 列表，不是已经 Finalize 之后引擎才落盘（403） interchangeable——403 另钉 Finalize 之后全流程，本页钉 not Finalize changed already settled 单句。
2. **看见回了 `tx_results` / 看见有 Code / 看见 Code / Data is not already 已经 Code / Data 印进本头 LastResultsHash interchangeable / 已经是本头 LastResultsHash interchangeable / 316 exectxresult item 3 interchangeable / 316 Code Data LastResultsHash interchangeable / 615 notresulthash interchangeable / 147 apphash vs this block interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 628 notsettled interchangeable / 585 fintxcode interchangeable / 431 finrespbar interchangeable / 404 finapphash item 3 Code==0 interchangeable，也不是已经 ExecTxResult 回执 bundled（316 余量） interchangeable / 316 exectxresult interchangeable / 316 item 1 list order interchangeable / 316 item 2 Code nonzero still in block interchangeable / 384 exectxlog interchangeable，也不是已经 CometBFT hashes all the transaction outputs and stores it in ResultHash not Code / Data 印进本头 bundled（587 item 2 余量 / 615） interchangeable / 615 notresulthash interchangeable / 587 finreturn interchangeable / 616 notpersist interchangeable / 335 finpersist interchangeable，也不是已经 Finalize 回包余量 bundled（404 余量） interchangeable / 404 finapphash interchangeable / 404 item 3 Code==0 interchangeable / 404 item 1 empty hardcoded interchangeable / 404 item 2 Query proofs interchangeable / 475 finmerkle interchangeable。**  
   官方把 Code / Data 进下一头 LastResultsHash 和已经印进本头分开——585 item 3 常与 316 / 615 混成「看见有 Code 就已经 Code / Data 印进本头 interchangeable」，本页钉 not printed in this header LastResultsHash 单句。看见 Code / Data，不是已经 ExecTxResult 回执 bundled（316） item 3 interchangeable——316 钉 Code / Data 进下一高度 LastResultsHash / Events 只供索引，本页钉 585 item 3 第二件事。看见 tx_results，不是已经 CometBFT hashes into ResultHash（615） interchangeable——615 另钉 not Code / Data 印进本头 / not this header LastResultsHash，本页钉 not Code Data printed in this header 单句。
3. **看见回了 `tx_results` / 看见有 Code is not already fintxcode bundled（585） interchangeable / 已经 CheckTx 过了 interchangeable / 已经 Code != 0 那种没进块 interchangeable / 585 fintxcode item 1 interchangeable / 585 fintxcode item 2 interchangeable / 626 notchecktx interchangeable / 627 notinvalid interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable / 628 notsettled interchangeable / 626 notchecktx interchangeable / 627 notinvalid interchangeable / 404 finapphash interchangeable / 316 exectxresult interchangeable，也不是已经 Code == 0 only if fully valid not CheckTx passed bundled（585 item 1 余量 / 626） interchangeable / 626 notchecktx interchangeable / 339 checktxweak interchangeable / 347 req3coherence interchangeable / 530 procaccept interchangeable，也不是已经 Code == 0 only if fully valid not Code != 0 still in block bundled（585 item 2 余量 / 627） interchangeable / 627 notinvalid interchangeable / 316 exectxresult interchangeable / 312 checktxopt interchangeable / 489 chktxcodereject interchangeable，也不是已经 Finalize 回包余量 bundled（404 余量） interchangeable / 404 finapphash interchangeable / 404 item 3 Code==0 interchangeable / 404 item 1 empty hardcoded interchangeable / 404 item 2 Query proofs interchangeable。**  
   官方把 585 fintxcode bundled 三事里的回了 tx_results 和 only if fully valid / Code 非零仍可能在块里分开——585 bundled 常与 item 1 / item 2 混成「看见回了 tx_results 就已经 fintxcode bundled interchangeable」，本页钉 585 item 3 第三件事。看见 tx_results，不是已经 only if fully valid not CheckTx passed（585 item 1 余量 / 626） interchangeable——626 另钉 not CheckTx passed / not Process Accept，本页钉 item 3 单句。看见有 Code，不是已经 only if fully valid not still in block（585 item 2 余量 / 627） interchangeable——627 另钉 not Code != 0 still in block / not no index，本页钉 not fintxcode bundled 单句。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的做法，本页不抄。FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585）、Code == 0 only if fully valid not CheckTx passed（585 item 1 余量 / 626）、Code == 0 only if fully valid not Code != 0 still in block（585 item 2 余量 / 627）、ExecTxResult 回执 bundled（316）、Finalize 落盘禁令 bundled（335）、Finalize 回包余量 bundled（404）、CometBFT hashes into ResultHash not Code / Data 印进本头（587 item 2 余量 / 615）是另外那套，本页不抄。

## 官方为什么这样拆

- **tx_results returned not already settled ≠ 335 finpersist / 403 finafter interchangeable：** 官方把回了 tx_results 和 Finalize 改了就已经交差分开。
- **tx_results returned not Code Data printed in this header ≠ 316 exectxresult / 615 notresulthash interchangeable：** 官方把 585 item 3 和 Code / Data 印进本头 / 下一头 LastResultsHash 分开。
- **tx_results returned not fintxcode bundled ≠ 626 notchecktx / 627 notinvalid interchangeable：** 官方把 585 item 3 和 item 1 / item 2 分开；585 fintxcode unbundling 完成（628 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 tx_results | 不是 already Finalize 改了就已经交差 | 不是 finpersist bundled（335） |
| 回了 tx_results | 不是 already Code / Data 印进本头 | 不是 ExecTxResult bundled（316） |
| 回了 tx_results | 不是 already fintxcode bundled | 不是 not CheckTx passed（585 item 1 / 626） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results returned not Finalize changed already settled / not Code Data printed in this header LastResultsHash / not fintxcode bundled 正式三事（585 余量），必须分开 tx_results 是不是 already Finalize 改了就已经交差 interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable、tx_results 是不是 already Code / Data 印进本头 interchangeable / 316 exectxresult interchangeable / 615 notresulthash interchangeable / 404 finapphash interchangeable、tx_results 是不是 already fintxcode bundled interchangeable / 626 notchecktx interchangeable / 627 notinvalid interchangeable / 339 checktxweak interchangeable。可以跳过「看见回了 tx_results 就已经 Finalize 改了就已经交差 interchangeable」。不要另写怎样编回执。585 fintxcode unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- FinalizeBlock tx_results Code==0 完全合法正式三事 bundled。那是不变量 585。
- Code == 0 only if fully valid not CheckTx passed。那是不变量 585 item 1 余量 / 626。
- Code == 0 only if fully valid not Code != 0 still in block。那是不变量 585 item 2 余量 / 627。
- ExecTxResult 回执 bundled。那是不变量 316。
- Finalize 落盘禁令 bundled。那是不变量 335。
- Finalize 回包余量 bundled。那是不变量 404。
- CometBFT hashes into ResultHash not Code / Data 印进本头。那是不变量 587 item 2 余量 / 615。
