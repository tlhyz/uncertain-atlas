# 模式：把 FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block / not no index / not fintxcode bundled 正式三事（585 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**例**：[FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block ≠ bundled（585）](../../tracks/implementation/worked-example-fintxcode-notinvalid-vs-bundled.md)。

## 三个名字

1. **only if fully valid 不是 Code != 0 那种没进块：** 看见 only if fully valid，不是已经 Code 非零就等于没进块 interchangeable，不是 316 exectxresult interchangeable / 316 Code nonzero still in block interchangeable / 312 checktxopt interchangeable。
2. **only if fully valid 不是没索引就等于没进块：** 看见 only if fully valid，不是已经无效就不建索引 interchangeable，不是 316 invalid not indexed interchangeable / 431 finrespbar interchangeable / 489 chktxcodereject interchangeable。
3. **only if fully valid 不是 fintxcode bundled：** 看见 only if fully valid，不是已经 fintxcode bundled interchangeable，不是 626 notchecktx interchangeable / 628 notsettled interchangeable / 585 fintxcode item 1 CheckTx 过了 interchangeable / 585 fintxcode item 3 回了 tx_results interchangeable。

## 为什么要分开叫

官方把 only if fully valid、Code 非零仍可能在块里、Finalize 回包和交差 / 印进本头写成三个名字。把它们叫成一个「看见 only if fully valid 就已经 Code != 0 那种没进块 interchangeable、就已经没索引 interchangeable、就已经 fintxcode bundled interchangeable」，会把 not still in block、not no index、not fintxcode bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block / not no index / not fintxcode bundled 正式三事（585 余量），先数清问的是 only if fully valid 是不是 already Code != 0 那种没进块 / 316 / 312，是不是 already 没索引就等于没进块 / 316 invalid not indexed，还是 only if fully valid 是不是 already fintxcode bundled / 626 / 628，再决定要不要同一次发布。
