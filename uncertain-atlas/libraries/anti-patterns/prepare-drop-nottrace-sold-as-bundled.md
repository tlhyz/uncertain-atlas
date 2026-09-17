# 反模式：把 把 t1 改成 t2 not already can look up t1 / not already someone knows t2 from t1 / not already settled 正式三事（355 余量） 卖成 已经还能按 t1 查到 / 已经有人知道 t2 来自 t1 / 已经交差

**层次**：实现 / Prepare 改列表。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-drop-nottrace-vs-bundled.md](../../tracks/implementation/worked-example-prepare-drop-nottrace-vs-bundled.md)。

官方把从提案拿掉 tx / 往提案加了一笔新的 / 把 t1 改成 t2 三条核心句写成三件独立的实现事。把它们卖成已经还能按 t1 查到 / 已经有人知道 t2 来自 t1 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把 t1 改成 t2 正式三事（355 余量），必须分开 not already can look up t1、not already someone knows t2 from t1、not already settled 三件事，不要和 355 / 33 / 356 / 853 / 854 / 855 糊成一句。

## 和相邻反模式

- [prepare-drop-notinpool-sold-as-bundled](prepare-drop-notinpool-sold-as-bundled.md) 是加新的单句边界（855 item 2），不是本页改哈希边界。
- 四门已经结算是不变量 33，不是本页可追踪性边界。
