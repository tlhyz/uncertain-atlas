# 先给模幂输入长度帽起名（name-the-modexp-bound）

> 类型：design pattern  
> 对读：不变量 206；C210；反模式 [`../anti-patterns/modexp-sold-as-reprice.md`](../anti-patterns/modexp-sold-as-reprice.md)；[`../../tracks/implementation/worked-example-modexp-bound-vs-price.md`](../../tracks/implementation/worked-example-modexp-bound-vs-price.md)。

设计或讲解「模幂终于有界了」时，先分开四个名字：

1. **输入长度帽** — 底数 / 指数 / 模数三段长度各有上限，不是已经改了计价公式。
2. **超帽** — 停住、报错、烧光剩余气，不是已经算出结果。
3. **长度有界** — 测试面不再无限，不是已经用 EVM 代码换掉预编译。
4. **7823** — 给 198 那条预编译加帽，不是 198 已经重定价，不是 7825，也不是 7951。

四句对照：

- 看见的是长度帽，还是已经改了计价？
- 看见的是超帽报错，还是已经算出结果？
- 看见的是测试面有界，还是预编译已经拆掉？
- 这是 7823，还是已经是 7825 / 7951 / 198 重定价？

不要和 [`name-the-tx-gas-cap.md`](name-the-tx-gas-cap.md)（单笔气帽 ≠ 块气限）、[`name-the-p256-verify.md`](name-the-p256-verify.md)（失败不烧光）、[`name-the-revert-leftover.md`](name-the-revert-leftover.md)（回滚 ≠ 烧光）糊成「预编译有帽」一句。
