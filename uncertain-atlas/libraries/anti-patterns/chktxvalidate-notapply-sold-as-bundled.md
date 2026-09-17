# 反模式：把 CheckTx Usage does not apply state changes not already mutated / not Finalize executed / not Process candidate committed 正式三事（486 余量）说成已经改了状态 / 已经 Finalize 执行 / 已经 Process candidate 已提交

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[does not apply state changes not already mutated ≠ bundled（486）](../../tracks/implementation/worked-example-chktxvalidate-notapply-vs-bundled.md)。

## 卖法

把 does not apply any of the state changes described in the transaction 写成已经在 CheckTx 里把余额扣了 interchangeable / 已经改了状态 interchangeable / 已经参与处理块 interchangeable；把不应用改动写成已经 Finalize 确定执行 txs interchangeable / 408 finexec interchangeable；把看见没应用写成已经 Process candidate 就等于已经改了已提交状态 interchangeable / 452 proccand interchangeable / 301 forever valid interchangeable，或已经和 486 chktxvalidate-vs-apply bundled / chktxvalidate-notapply-sold-as-bundled interchangeable / 681 chktxvalidate-notapply interchangeable。

## 为什么错

官方把 CheckTx Usage 不应用改动、Finalize 执行、Process candidate 已提交写成三件独立的实现事。把它们卖成 already mutated interchangeable / Finalize executed interchangeable / Process candidate committed interchangeable，会把 not mutated、not Finalize executed、not Process candidate committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage does not apply state changes 正式三事（486 余量），必须分开 not mutated、not Finalize executed、not Process candidate committed 三件事，不要和 486 / 408 / 452 / 301 / 680 / 682 糊成一句。

## 和相邻反模式

- [chktxvalidate-sold-as-applied](chktxvalidate-sold-as-applied.md) 是 CheckTx Usage validate-no-apply bundled（486），不是本页 item 2 单句边界。
- [chktxvalidate-notoptional-sold-as-bundled](chktxvalidate-notoptional-sold-as-bundled.md) 是 Technically optional + Code≠0 单句边界（682 item 3），不是本页不应用改动边界。
