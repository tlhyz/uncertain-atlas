# 反模式：把同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事（328 余量）说成已经有了 CheckTxCode / 已经能说 OK / 已经是单元素

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了不同码 not already has-checktxcode ≠ bundled（328）](../../tracks/implementation/worked-example-checktxoscillate-notcode-vs-bundled.md)。

## 卖法

把同一高度 CheckTx 回了不同码 / 同一高度回了不同码 / 码不一致 写成已经有了 CheckTxCode interchangeable / 已经 has-checktxcode interchangeable / 已经有码交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable；把 CheckTxCodes 是集合 / 集合在 / 码收成集合 写成已经能说 OK interchangeable / 已经 ok-defined interchangeable；把回了两次 / 集合可以有多个码 / 不是单元素 写成已经是单元素集合 interchangeable / 已经 singleton-set interchangeable，或已经和 328 checktxoscillate bundled / checktxcode-sold-as-stable interchangeable / 740 checktxoscillate-notcode interchangeable。

## 为什么错

官方把同一高度回了不同码单句、already has-checktxcode、already ok-defined、already singleton-set 写成三件独立的实现事。把它们卖成 already has-checktxcode interchangeable / already ok-defined interchangeable / already singleton-set interchangeable，会把 not already has-checktxcode、not already ok-defined、not already singleton-set 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事（328 余量），必须分开 not already has-checktxcode、not already ok-defined、not already singleton-set 三件事，不要和 328 / 33 / 312 / 313 / 317 / 741 / 742 糊成一句。

## 和相邻反模式

- [checktxcode-sold-as-stable](checktxcode-sold-as-stable.md) 是 CheckTx 最终不再振荡 bundled 全段，不是本页有码 item 1 单句边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ ExecuteTxState（312），不是本页集合与 CheckTxCode 边界。
- [checktxoscillate-nothstable-sold-as-bundled](checktxoscillate-nothstable-sold-as-bundled.md) 是还在振荡过了 h_stable（328 item 2），不是本页有码 item 1 单句边界。
- [preparetimeout-notlivenesslost-sold-as-bundled](preparetimeout-notlivenesslost-sold-as-bundled.md) 是又开一轮丢掉活性（327 item 3），不是本页 CheckTx 码集合边界。
