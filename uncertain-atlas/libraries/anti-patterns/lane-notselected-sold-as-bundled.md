# 反模式：把 空表对空默认 not already selected / not already prioritized / not already in-block 正式三事（367 余量） 卖成 已经选型 / 已经排了优先 / 已经进了块

**层次**：实现 / Info 车道。  
**分类**：建议（产品）。  
**对应例**：[worked-example-lane-notselected-vs-bundled.md](../../tracks/implementation/worked-example-lane-notselected-vs-bundled.md)。

官方把没定义 lane_priorities / 空表对空默认 / 优先级 0 留给不设道三条核心句写成三件独立的实现事。把它们卖成已经选型 / 已经排了优先 / 已经进了块，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空表对空默认 正式三事（367 余量），必须分开 not already selected、not already prioritized、not already in-block 三件事，不要和 367 / 497 / 667 / 498 / 663 / 824 / 826 糊成一句。

## 和相邻反模式

- [lane-notpriority-sold-as-bundled](lane-notpriority-sold-as-bundled.md) 是没定义车道单句边界（824 item 1），不是本页空表对空默认边界。
- [infousage-notemptyiff-sold-as-bundled](infousage-notemptyiff-sold-as-bundled.md) 是 Info Usage 空对空就已经是 367 bundled（497/667），不是本页空表对空默认边界。
