# 反模式：把 回了 AppHash 和输出哈希进 ResultHash not already printed in header / not already this-height AppHash / not already settled 正式三事（362 余量） 卖成 已经印进本头 / 已经是本头 AppHash / 已经交差

**层次**：实现 / Finalize 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-when-notheader-vs-bundled.md](../../tracks/implementation/worked-example-finalize-when-notheader-vs-bundled.md)。

官方把 +2/3 precommit 才决定再调 Finalize / 先落决定再同步调 Finalize / 回了 AppHash 和输出哈希进 ResultHash 三条核心句写成三件独立的实现事。把它们卖成已经印进本头 / 已经是本头 AppHash / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回了 AppHash 和输出哈希进 ResultHash 正式三事（362 余量），必须分开 not already printed in header、not already this-height AppHash、not already settled 三件事，不要和 362 / 147 / 363 / 838 / 371 / 839 / 840 糊成一句。

## 和相邻反模式

- [finalize-when-notpersist-sold-as-bundled](finalize-when-notpersist-sold-as-bundled.md) 是先落决定单句边界（840 item 2），不是本页回 AppHash 边界。
- [finalize-equiv-notchanged-sold-as-bundled](finalize-equiv-notchanged-sold-as-bundled.md) 是必须回四列就已经印进本头（363/838），不是本页 ResultHash 边界。
