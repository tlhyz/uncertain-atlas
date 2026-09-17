# 反模式：把 apply candidate state not ExecuteTxState 正式三事（460 余量）卖成 fincand bundled / 已经是 ExecuteTxState / Process 回了 Accept

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[apply candidate state not ExecuteTxState ≠ bundled（460）](../../tracks/implementation/worked-example-fincand-notcandstate-vs-bundled.md)。

## 卖法

- 「看见 Alternatively apply candidate state 就已经 ExecuteTxState interchangeable / 已经进 ExecuteTxState interchangeable。」
- 「看见套用了 candidate 就已经 Process 回了 Accept 就换工作状态 interchangeable / 已经 prevote interchangeable。」
- 「看见套用了 就已经不用再回 app_hash / tx_results interchangeable / 已经 candidate 就不需要 Commit interchangeable。」

## 为什么错

官方把 apply candidate state、ExecuteTxState、Process ACCEPT switched working state、previously executed 不用再 Finalize 执行 写成独立的实现事。把它们卖成 fincand bundled、已经是 ExecuteTxState、Process 回了 Accept，会把 not ExecuteTxState、not ACCEPT switched、not no re-execute 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 apply candidate state not ExecuteTxState 正式三事（460 余量），必须分开 not ExecuteTxState、not Process ACCEPT switched、not no re-execute 三个名字，不要把它们卖成 fincand bundled / 已经是 ExecuteTxState / Process 回了 Accept。

## 和相邻反模式

- [fincand-sold-as-commit](fincand-sold-as-commit.md) 是 460 bundled 三事专用，不是本页 apply candidate 单句边界。
- [fincand-notcommitted-sold-as-bundled](fincand-notcommitted-sold-as-bundled.md) 是 576 executes txs not committed 专用，不是本页 item 2 边界。
