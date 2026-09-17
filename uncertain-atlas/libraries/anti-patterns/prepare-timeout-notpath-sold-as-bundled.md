# 反模式：把 立刻整块执行 not already left critical path / not already not blocking clock / not already settled 正式三事（327 余量） 卖成 已经离开关键路径 / 已经不挡提议钟 / 已经交差

**层次**：实现 / PrepareProposal 及时性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-timeout-notpath-vs-bundled.md](../../tracks/implementation/worked-example-prepare-timeout-notpath-vs-bundled.md)。

官方把立刻整块执行 / 填了 TimeoutPropose / 又开一轮 三条核心句写成三件独立的实现事。把它们卖成已经离开关键路径 / 已经不挡提议钟 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻整块执行 正式三事（327 余量），必须分开 not already left critical path、not already not blocking clock、not already settled 三件事，不要和 327 / 344 / 33 / 900 / 901 糊成一句。

## 和相邻反模式

- [maxbytes-overhead-nottimeout-sold-as-bundled](maxbytes-overhead-nottimeout-sold-as-bundled.md) 是满块投递延迟（344/883），不是本页立刻执行站在提议钟上边界。
- timeout 必须按满块投递延迟算是不变量 344 / 883，不是本页立刻整块执行边界。
