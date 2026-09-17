# 先给本账户余额指令起名（name-the-selfbalance）

> 类型：design pattern  
> 对读：不变量 229；C233；反模式 [`../anti-patterns/selfbalance-sold-as-balance.md`](../anti-patterns/selfbalance-sold-as-balance.md)；[`../../tracks/implementation/worked-example-selfbalance-vs-balance.md`](../../tracks/implementation/worked-example-selfbalance-vs-balance.md)。

设计或讲解「状态读终于涨价了」时，先分开四个名字：

1. **本账户余额指令** — 不弹地址，压回当前地址余额，不是已经是按地址查余额。
2. **按地址查自己** — 仍走按地址那条、价仍按地址，不是已经按本账户价扣。
3. **树依赖涨价** — 读存储 / 按地址查余额 / 读代码哈希更贵，不是已经是本笔冷热，也不是磁盘已经是常数时间。
4. **1884** — 涨价 + 本账户快捷窗口，不是 2929，也不是 150 原文。

四句对照：

- 看见的是本账户余额指令，还是按地址查余额？
- 看见的是给自己查余额，还是已经按本账户价扣？
- 看见的是整网涨价，还是本笔冷热 / 磁盘已经 O(1)？
- 这是 1884，还是已经是 2929 / 101 / 150？

不要和本笔第一次碰≠已经热（不变量 169）、气≠墙钟（不变量 101）、代码哈希指令≠已看见代码（不变量 221）糊成「状态读已经齐了」一句。
