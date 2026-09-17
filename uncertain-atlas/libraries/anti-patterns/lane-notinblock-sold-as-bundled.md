# 反模式：把 优先级 0 留给不设道 not already in-block / not already deleted from pool / not already consensus order 正式三事（367 余量） 卖成 已经进了块 / 已经从池里删掉 / 已经是共识顺序

**层次**：实现 / Info 车道。  
**分类**：建议（产品）。  
**对应例**：[worked-example-lane-notinblock-vs-bundled.md](../../tracks/implementation/worked-example-lane-notinblock-vs-bundled.md)。

官方把没定义 lane_priorities / 空表对空默认 / 优先级 0 留给不设道三条核心句写成三件独立的实现事。把它们卖成已经进了块 / 已经从池里删掉 / 已经是共识顺序，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级 0 留给不设道 正式三事（367 余量），必须分开 not already in-block、not already deleted from pool、not already consensus order 三件事，不要和 367 / 301 / 317 / 498 / 664 / 482 / 704 / 824 / 825 糊成一句。

## 和相邻反模式

- [lane-notselected-sold-as-bundled](lane-notselected-sold-as-bundled.md) 是空表对空默认单句边界（825 item 2），不是本页优先级 0 边界。
- [infousage-notpriorityzero-sold-as-bundled](infousage-notpriorityzero-sold-as-bundled.md) 是 Info Usage 优先级 0 就已经是 367 bundled（498/664），不是本页优先级 0 边界。
