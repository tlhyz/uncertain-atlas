# 反模式：把 低于这个高度可删 not already no history / not already snapshot truncated / not already deleted 正式三事（366 余量） 卖成 已经没有历史 / 已经是快照截断 / 已经删完

**层次**：实现 / Commit 保留高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-retain-nothistory-vs-bundled.md](../../tracks/implementation/worked-example-retain-nothistory-vs-bundled.md)。

官方把 retain_height 默认 0 / 低于这个高度可删 / 全网都删会永久丢三条核心句写成三件独立的实现事。把它们卖成已经没有历史 / 已经是快照截断 / 已经删完，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看低于这个高度可删 正式三事（366 余量），必须分开 not already no history、not already snapshot truncated、not already deleted 三件事，不要和 366 / 323 / 491 / 694 / 320 / 827 / 829 糊成一句。

## 和相邻反模式

- [retain-notpruning-sold-as-bundled](retain-notpruning-sold-as-bundled.md) 是默认 0 单句边界（827 item 1），不是本页可删边界。
- [commitretaincaution-nothistorical-sold-as-bundled](commitretaincaution-nothistorical-sold-as-bundled.md) 是 retain_height caution Historical blocks（491/694），不是本页可删边界。
