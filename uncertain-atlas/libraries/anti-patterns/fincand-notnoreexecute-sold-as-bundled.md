# 反模式：把 previously executed not no re-execute in Finalize 正式三事（460 余量）卖成 fincand bundled / 已经不用再在 Finalize 执行 / candidate 就不需要 Commit

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[previously executed not no re-execute in Finalize ≠ bundled（460）](../../tracks/implementation/worked-example-fincand-notnoreexecute-vs-bundled.md)。

## 卖法

- 「看见 the same block previously executed via Prepare or Process 就已经不用再在 Finalize 执行 interchangeable / 已经 Process 跑过就不执行 interchangeable。」
- 「看见 previously executed 就已经不用再回 app_hash / tx_results interchangeable / 已经 candidate 就不需要 Commit interchangeable。」
- 「看见 previously executed 就已经 guarantee satisfied interchangeable / 已经套用 candidate 就不需要 guarantee interchangeable。」

## 为什么错

官方把 previously executed、no need to execute txs in Finalize、must return app_hash / tx_results、has run ProcessProposal guarantee 写成独立的实现事。把它们卖成 fincand bundled、已经不用再在 Finalize 执行、candidate 就不需要 Commit，会把 not no re-execute txs、not no return app_hash、not guarantee satisfied 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 previously executed not no re-execute in Finalize 正式三事（460 余量），必须分开 not no re-execute txs、not no return app_hash / tx_results、not guarantee satisfied / no Commit 三个名字，不要把它们卖成 fincand bundled / 已经不用再在 Finalize 执行 / candidate 就不需要 Commit。

## 和相邻反模式

- [fincand-sold-as-commit](fincand-sold-as-commit.md) 是 460 bundled 三事专用，不是本页 previously executed 单句边界。
- [fincand-notcandstate-sold-as-bundled](fincand-notcandstate-sold-as-bundled.md) 是 577 apply candidate not ExecuteTxState 专用，不是本页 item 3 边界。
- [fincand-notcommitted-sold-as-bundled](fincand-notcommitted-sold-as-bundled.md) 是 576 executes txs not committed 专用，不是本页 item 1 边界。
