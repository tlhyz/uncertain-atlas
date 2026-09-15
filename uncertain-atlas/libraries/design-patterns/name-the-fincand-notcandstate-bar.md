# 模式：把 apply candidate state not ExecuteTxState 正式三事（460 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[apply candidate state not ExecuteTxState ≠ bundled（460）](../../tracks/implementation/worked-example-fincand-notcandstate-vs-bundled.md)。

## 三个名字

1. **apply candidate state not ExecuteTxState 不是 fincand bundled：** 看见套用了不是已经进 ExecuteTxState，不是 460 bundled interchangeable / 311 candidate interchangeable / 452 candidate execution interchangeable。
2. **apply candidate state not Process ACCEPT switched 不是 Process 回了 Accept 就换工作状态：** 看见 apply candidate 不是已经 ACCEPT switched / prevote，不是 452 candidate interchangeable / 544 candidate not committed interchangeable。
3. **apply candidate state not no re-execute / no return app_hash 不是 previously executed 不用再 Finalize：** 看见套用了不是已经不用再回 app_hash / 不用再 execute，不是 578 not no re-execute interchangeable / 572 has run not apply candidate interchangeable。

## 为什么要分开叫

官方把 apply candidate state 写成三个名字。把它们叫成一个「看见套用了 candidate 就已经是 ExecuteTxState interchangeable / 已经 Process 回了 Accept interchangeable / 已经 fincand bundled interchangeable」，会把 not ExecuteTxState、not ACCEPT switched、not no re-execute 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 apply candidate state not ExecuteTxState 正式三事（460 余量），先数清问的是 apply candidate 是不是 already ExecuteTxState、是不是 already Process ACCEPT switched、是不是 already no re-execute / no return app_hash，再决定要不要同一次发布。
