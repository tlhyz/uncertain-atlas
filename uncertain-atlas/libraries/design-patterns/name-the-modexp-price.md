# 先给模幂重计价起名（name-the-modexp-price）

> 类型：design pattern  
> 对读：不变量 227；C231；反模式 [`../anti-patterns/modexp-price-sold-as-bound.md`](../anti-patterns/modexp-price-sold-as-bound.md)；[`../../tracks/implementation/worked-example-modexp-price-vs-bound.md`](../../tracks/implementation/worked-example-modexp-price-vs-bound.md)。

设计或讲解「模幂终于便宜了」时，先分开四个名字：

1. **模幂重计价** — 新的复杂度 × 迭代近似，不是已经是 198 那道分段公式。
2. **接口未改** — 调用格式和算术还是原来那套，不是已经换了算法或得数。
3. **最低气价** — 挡住小输入被标得过低，不是已经能对小输入无限便宜。
4. **2565** — 给 198 那条预编译改价，不是 7823 输入帽，也不是已经不伤安全。

四句对照：

- 看见的是新公式，还是已经是 198？
- 看见的是更便宜，还是接口或算术已经改过？
- 看见的是最低气价，还是已经能无限便宜？
- 这是 2565，还是已经是 7823 / 206 / 已经不伤安全？

不要和模幂长度帽≠已改计价（不变量 206）、回滚≠烧光（不变量 177）、预编译算术≠已验 BLS（不变量 199）、单笔气帽≠块气限（不变量 203）糊成「模幂已经齐了」一句。
