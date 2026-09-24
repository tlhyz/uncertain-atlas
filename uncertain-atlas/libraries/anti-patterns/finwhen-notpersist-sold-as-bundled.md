# 反模式：把先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事（362 余量）说成已经交差 / 已经落盘应用状态 / 已经同步交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[落决定再同步调 not already settled ≠ bundled（362）](../../tracks/implementation/worked-example-finwhen-notpersist-vs-bundled.md)。

## 卖法

把决定了 / 先把 *v* 落成这一高的决定再同步调 Finalize / 决定了 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable；把先落了决定 / 先把 *v* 落成高度 *h* 的决定 写成已经落盘应用状态 interchangeable / 已经 app-persist interchangeable / 已经落盘应用状态交差 interchangeable；把是同步的 / 再同步调 Finalize / CometBFT 同步调用 写成已经交差 interchangeable / 已经 sync-settled interchangeable / 已经同步交差交差 interchangeable，或已经和 362 finwhen bundled / finalizewhen-sold-as-decided interchangeable / 837 finwhen-notpersist interchangeable。

## 为什么错

官方把决定了、不是已经落盘应用状态、不是已经交差写成三件独立的实现事。把它们卖成 already settled interchangeable / already app-persist interchangeable / already sync-settled interchangeable，会把 not already settled、not already app-persist、not already sync-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事（362 余量），必须分开 not already settled、not already app-persist、not already sync-settled 三件事，不要和 362 / 335 / 361 / 836 / 838 糊成一句。

## 和相邻反模式

- [finalizewhen-sold-as-decided](finalizewhen-sold-as-decided.md) 是 Finalize 何时调用 bundled 全段，不是本页决定了 item 2 单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 Finalize 改了就已经落盘（335），不是本页 not already settled 边界。
- [finwhen-notwillcall-sold-as-bundled](finwhen-notwillcall-sold-as-bundled.md) 是 +2/3 precommit 才决定再调 not already will-call（362 item 1），不是本页 not already sync-settled 边界。
