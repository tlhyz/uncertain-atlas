# 反模式：把应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事（362 余量）说成已经印进本头 / 已经是本头 AppHash / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了 ResultHash not already printed ≠ bundled（362）](../../tracks/implementation/worked-example-finwhen-notprinted-vs-bundled.md)。

## 卖法

把回了 / 应用回了 AppHash 和各笔输出 / 回了 AppHash 与各笔输出 写成已经印进本头 interchangeable / 已经 printed interchangeable / 已经印进本头交差 interchangeable / 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable；把有 ResultHash / 引擎把输出哈希进 ResultHash 写成已经是本头 AppHash interchangeable / 已经 header interchangeable / 已经是本头 AppHash 交差 interchangeable；把哈希了 / 把输出哈希进了 / 引擎哈希了 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 362 finwhen bundled / finalizewhen-sold-as-decided interchangeable / 838 finwhen-notprinted interchangeable。

## 为什么错

官方把回了、不是已经是本头 AppHash、不是已经交差写成三件独立的实现事。把它们卖成 already printed interchangeable / already header interchangeable / already settled interchangeable，会把 not already printed、not already header、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事（362 余量），必须分开 not already printed、not already header、not already settled 三件事，不要和 362 / 147 / 361 / 836 / 837 糊成一句。

## 和相邻反模式

- [finalizewhen-sold-as-decided](finalizewhen-sold-as-decided.md) 是 Finalize 何时调用 bundled 全段，不是本页回了 item 3 单句边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差（147），不是本页 not already printed 边界。
- [finwhen-notpersist-sold-as-bundled](finwhen-notpersist-sold-as-bundled.md) 是落决定再同步调 not already settled（362 item 2），不是本页 not already header 边界。
- [finwhen-notwillcall-sold-as-bundled](finwhen-notwillcall-sold-as-bundled.md) 是 +2/3 precommit 才决定再调 not already will-call（362 item 1），不是本页 not already settled 边界。
