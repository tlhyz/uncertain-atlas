# 反模式：把 没定义 lane_priorities not already prioritized / not already CheckTx Priority / not already settled 正式三事（367 余量） 卖成 已经排了优先 / 已经是 CheckTx Priority / 已经交差

**层次**：实现 / Info 车道。  
**分类**：建议（产品）。  
**对应例**：[worked-example-lane-notpriority-vs-bundled.md](../../tracks/implementation/worked-example-lane-notpriority-vs-bundled.md)。

官方把没定义 lane_priorities / 空表对空默认 / 优先级 0 留给不设道三条核心句写成三件独立的实现事。把它们卖成已经排了优先 / 已经是 CheckTx Priority / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没定义 lane_priorities 正式三事（367 余量），必须分开 not already prioritized、not already CheckTx Priority、not already settled 三件事，不要和 367 / 317 / 497 / 666 / 312 / 825 / 826 糊成一句。

## 和相邻反模式

- [infousage-notlaneoptional-sold-as-bundled](infousage-notlaneoptional-sold-as-bundled.md) 是 Info Usage 可选车道就已经是 367 bundled（497/666），不是本页没定义车道边界。
- CheckTx 的 Priority 就已经是共识顺序是不变量 317，不是本页没定义车道边界。
