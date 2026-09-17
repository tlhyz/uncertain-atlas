# 模式：把 previously executed not no re-execute in Finalize 正式三事（460 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[previously executed not no re-execute in Finalize ≠ bundled（460）](../../tracks/implementation/worked-example-fincand-notnoreexecute-vs-bundled.md)。

## 三个名字

1. **previously executed not no re-execute txs 不是 fincand bundled：** 看见同一块先前 Prepare 或 Process 执行过不是已经不用再 execute txs，不是 460 bundled interchangeable / 576 executes txs interchangeable / 577 apply candidate interchangeable。
2. **previously executed not no return app_hash / tx_results 不是 must provide values：** 看见 previously executed 不是已经不用再回 app_hash / tx_results，不是 477 must provide interchangeable / 335 Finalize 改了就已经落盘 interchangeable。
3. **previously executed not guarantee satisfied / no Commit 不是 has run not apply candidate：** 看见 previously executed 不是已经 guarantee satisfied / candidate 就不需要 Commit，不是 572 has run not apply candidate interchangeable / 544 candidate not committed interchangeable。

## 为什么要分开叫

官方把 previously executed via PrepareProposal or ProcessProposal 写成三个名字。把它们叫成一个「看见 previously executed 就已经不用再在 Finalize 执行 interchangeable / 已经不用再回 app_hash interchangeable / 已经 fincand bundled interchangeable」，会把 not no re-execute txs、not no return app_hash、not guarantee satisfied 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 previously executed not no re-execute in Finalize 正式三事（460 余量），先数清问的是 previously executed 是不是 already no re-execute txs、是不是 already no return app_hash / tx_results、是不是 already guarantee satisfied / no Commit，再决定要不要同一次发布。
