# 反模式：把 填了 TimeoutPropose not already fits / not already clock silent / not already settled 正式三事（327 余量） 卖成 已经装得下 / 钟已经不会响 / 已经交差

**层次**：实现 / PrepareProposal 及时性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-timeout-notfit-vs-bundled.md](../../tracks/implementation/worked-example-prepare-timeout-notfit-vs-bundled.md)。

官方把立刻整块执行 / 填了 TimeoutPropose / 又开一轮 三条核心句写成三件独立的实现事。把它们卖成已经装得下 / 钟已经不会响 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 TimeoutPropose 正式三事（327 余量），必须分开 not already fits、not already clock silent、not already settled 三件事，不要和 327 / 47 / 344 / 899 / 901 糊成一句。

## 和相邻反模式

- [prepare-timeout-notpath-sold-as-bundled](prepare-timeout-notpath-sold-as-bundled.md) 是立刻整块执行单句边界（899 item 1），不是本页 TimeoutPropose 初值边界。
- 本地超时已经是最终性是不变量 47，不是本页 TimeoutPropose 装得下边界。
