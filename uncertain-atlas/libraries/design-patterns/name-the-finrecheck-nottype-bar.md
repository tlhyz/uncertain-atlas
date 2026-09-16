# 模式：把 FinalizeBlock When against newly persisted Application state not Type=RECHECK / not CheckTxState / ExecuteTxState / not finrecheck bundled 正式三事（591 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 9。  
**例**：[FinalizeBlock When against newly persisted Application state not Type=RECHECK ≠ bundled（591）](../../tracks/implementation/worked-example-finrecheck-nottype-vs-bundled.md)。

## 三个名字

1. **against newly persisted 不是 Type=RECHECK：** 看见 against the newly persisted Application state / 对照刚落盘的应用状态，不是已经 CheckTxRequest Type RECHECK interchangeable，不是 312 checktxtype RECHECK interchangeable / 484 chktxtype RECHECK interchangeable / 634 notrecheck interchangeable。
2. **against newly persisted 不是 CheckTxState / ExecuteTxState：** 看见 re-checks against newly persisted，不是已经 CheckTxState interchangeable / ExecuteTxState interchangeable，不是 339 checktxweak interchangeable / 310 querystate interchangeable / 335 finpersist interchangeable。
3. **against newly persisted 不是 finrecheck bundled：** 看见 When 第 9 步 optional recheck 对象，不是已经 finrecheck bundled interchangeable，不是 635 finrecheck-notmust interchangeable / 636 finrecheck-notoutstanding interchangeable / 591 finrecheck item 1 optionally re-checks interchangeable / 591 finrecheck item 2 outstanding txs interchangeable。

## 为什么要分开叫

官方把 When 第 9 步 against newly persisted Application state、Type=RECHECK、CheckTxState / ExecuteTxState、591 finrecheck bundled 三事 写成三个名字。把它们叫成一个「看见对照刚落盘的应用状态 就已经 Type=RECHECK interchangeable、就已经 CheckTxState / ExecuteTxState interchangeable、就已经 finrecheck bundled interchangeable」，会把 not Type=RECHECK、not CheckTxState / ExecuteTxState、not finrecheck bundled / not 591 item 1 / item 2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When against newly persisted Application state not Type=RECHECK / not CheckTxState / ExecuteTxState / not finrecheck bundled 正式三事（591 余量），先数清问的是 against newly persisted 是不是 already Type=RECHECK / 312 / 484 / 634，是不是 already CheckTxState / ExecuteTxState / 339 / 310 / 335，还是 against newly persisted 是不是 already finrecheck bundled / 635 / 636，再决定要不要同一次发布。591 finrecheck unbundling 在本页 item 3 完成。
