# 反模式：把 全网都删会永久丢 not already genesis reload / not already light-client verify / not already settled 正式三事（366 余量） 卖成 已经能从创世再装 / 已经能给轻客户端验 / 已经交差

**层次**：实现 / Commit 保留高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-retain-notgenesis-vs-bundled.md](../../tracks/implementation/worked-example-retain-notgenesis-vs-bundled.md)。

官方把 retain_height 默认 0 / 低于这个高度可删 / 全网都删会永久丢三条核心句写成三件独立的实现事。把它们卖成已经能从创世再装 / 已经能给轻客户端验 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看全网都删会永久丢 正式三事（366 余量），必须分开 not already genesis reload、not already light-client verify、not already settled 三件事，不要和 366 / 38 / 491 / 693 / 323 / 827 / 828 糊成一句。

## 和相邻反模式

- [retain-nothistory-sold-as-bundled](retain-nothistory-sold-as-bundled.md) 是可删单句边界（828 item 2），不是本页永久丢边界。
- [commitretaincaution-notgenesis-sold-as-bundled](commitretaincaution-notgenesis-sold-as-bundled.md) 是 retain_height caution 从创世（491/693），不是本页永久丢边界。
