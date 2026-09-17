# 反模式：把 CheckTx Usage validates against current state not ExecuteTxState / not about-to-execute / not CheckTxState is ExecuteTxState 正式三事（486 余量）说成已经 ExecuteTxState / 已经 about-to-execute / 已经 CheckTxState is ExecuteTxState

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[validates against current state not ExecuteTxState ≠ bundled（486）](../../tracks/implementation/worked-example-chktxvalidate-notexecstate-vs-bundled.md)。

## 卖法

把 validates against current state / checking signatures and account balances 写成已经按 ExecuteTxState 验过 interchangeable / 312 checktxstate-vs-execute interchangeable / 已经按将要执行的那份状态验过 interchangeable；把对照当前状态验写成已经 candidate 就是 ExecuteTxState interchangeable / 311 candidate-vs-execute interchangeable；把看见验了写成已经 CheckTxState 与 ExecuteTxState 同时在改就等于同一份 interchangeable / 312 bundled interchangeable / 314 querystate interchangeable，或已经和 486 chktxvalidate-vs-apply bundled / chktxvalidate-notexecstate-sold-as-bundled interchangeable / 680 chktxvalidate-notexecstate interchangeable。

## 为什么错

官方把 CheckTx Usage current state、ExecuteTxState、将要执行的那份状态、两份同时在改写成三件独立的实现事。把它们卖成 ExecuteTxState interchangeable / about-to-execute interchangeable / CheckTxState is ExecuteTxState interchangeable，会把 not ExecuteTxState、not about-to-execute、not CheckTxState is ExecuteTxState 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage validates against current state 正式三事（486 余量），必须分开 not ExecuteTxState、not about-to-execute、not CheckTxState is ExecuteTxState 三件事，不要和 486 / 312 / 311 / 314 / 408 / 681 / 682 糊成一句。

## 和相邻反模式

- [chktxvalidate-sold-as-applied](chktxvalidate-sold-as-applied.md) 是 CheckTx Usage validate-no-apply bundled（486），不是本页 item 1 单句边界。
- [chktxvalidate-notapply-sold-as-bundled](chktxvalidate-notapply-sold-as-bundled.md) 是 does not apply 单句边界（681 item 2），不是本页 current state 边界。
