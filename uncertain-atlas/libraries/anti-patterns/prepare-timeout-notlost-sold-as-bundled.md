# 反模式：把 又开一轮 not already lost liveness / not already timeout frozen / not already settled 正式三事（327 余量） 卖成 已经丢了活性 / 超时已经不再涨 / 已经交差

**层次**：实现 / PrepareProposal 及时性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-timeout-notlost-vs-bundled.md](../../tracks/implementation/worked-example-prepare-timeout-notlost-vs-bundled.md)。

官方把立刻整块执行 / 填了 TimeoutPropose / 又开一轮 三条核心句写成三件独立的实现事。把它们卖成已经丢了活性 / 超时已经不再涨 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看又开一轮 正式三事（327 余量），必须分开 not already lost liveness、not already timeout frozen、not already settled 三件事，不要和 327 / 340 / 52 / 311 / 899 / 900 糊成一句。

## 和相邻反模式

- [prepare-timeout-notfit-sold-as-bundled](prepare-timeout-notfit-sold-as-bundled.md) 是 TimeoutPropose 初值单句边界（900 item 2），不是本页又开一轮边界。
- Process 非确定 bug 已经丢了安全性是不变量 340 / 895，不是本页又开一轮丢活性边界。
