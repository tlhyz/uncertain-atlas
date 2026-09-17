# 反模式：把 timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare / not already left critical path / not already settled 正式三事（344 余量） 卖成 已经填了 TimeoutPropose 就装得下这次 Prepare 执行 / 已经离开关键路径 / 已经交差

**层次**：实现 / BlockParams.MaxBytes 开销与投递。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-overhead-nottimeout-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-overhead-nottimeout-vs-bundled.md)。

官方把 MaxBytes 减去头集合证据才是交易上限 / 诚实验证者 MAY 出满 MaxBytes / timeout 必须按满块投递延迟算 三条核心句写成三件独立的实现事。把它们卖成已经填了 TimeoutPropose 就装得下这次 Prepare 执行 / 已经离开关键路径 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 timeout 必须按满块投递延迟算 正式三事（344 余量），必须分开 not already TimeoutPropose covers Prepare、not already left critical path、not already settled 三件事，不要和 344 / 327 / 33 / 881 / 882 糊成一句。

## 和相邻反模式

- [maxbytes-overhead-not21mb-sold-as-bundled](maxbytes-overhead-not21mb-sold-as-bundled.md) 是 MAY 出满单句边界（882 item 2），不是本页满块投递超时边界。
- 立刻整块执行已经离开关键路径是不变量 327，不是本页满块投递超时边界。
