# 模式：把 FinalizeBlockResponse tx_results returned not Finalize changed already settled / not Code Data printed in this header LastResultsHash / not fintxcode bundled 正式三事（585 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**例**：[FinalizeBlockResponse tx_results returned not Finalize changed already settled ≠ bundled（585）](../../tracks/implementation/worked-example-fintxcode-notsettled-vs-bundled.md)。

## 三个名字

1. **回了 tx_results 不是已经 Finalize 改了就已经交差：** 看见 tx_results / 有 Code，不是已经 Finalize 改了就已经交差 interchangeable，不是 335 finpersist interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 33 four gates interchangeable。
2. **回了 tx_results 不是 Code / Data 印进本头：** 看见 tx_results / Code / Data，不是已经 Code / Data 印进本头 LastResultsHash interchangeable，不是 316 exectxresult interchangeable / 615 notresulthash interchangeable / 404 finapphash item 3 Code==0 interchangeable。
3. **回了 tx_results 不是 fintxcode bundled：** 看见 tx_results，不是已经 fintxcode bundled interchangeable，不是 626 notchecktx interchangeable / 627 notinvalid interchangeable / 585 fintxcode item 1 only if fully valid interchangeable / 585 fintxcode item 2 Code 非零仍可能在块里 interchangeable。

## 为什么要分开叫

官方把 only if fully valid、Code 非零仍可能在块里、Finalize 回包 tx_results 和交差 / 印进本头写成三个名字。把它们叫成一个「看见回了 tx_results 就已经 Finalize 改了就已经交差 interchangeable、就已经 Code / Data 印进本头 interchangeable、就已经 fintxcode bundled interchangeable」，会把 not already settled、not Code Data printed in this header、not fintxcode bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results returned not Finalize changed already settled / not Code Data printed in this header LastResultsHash / not fintxcode bundled 正式三事（585 余量），先数清问的是 tx_results 是不是 already Finalize 改了就已经交差 / 335 / 403，是不是 already Code / Data 印进本头 / 316 / 615，还是 tx_results 是不是 already fintxcode bundled / 626 / 627，再决定要不要同一次发布。
