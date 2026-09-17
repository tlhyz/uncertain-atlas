# 先给 calldata 地板起名（name-the-calldata-floor）

> 类型：design pattern  
> 对读：不变量 197；C201；反模式 [`../anti-patterns/floor-sold-as-execution.md`](../anti-patterns/floor-sold-as-execution.md)；[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)。

设计或讲解「calldata 怎么计价」时，先分开四个名字：

1. **calldata 地板** — 数据为主的交易走的下限气，不是已经改了普通执行气。
2. **旧零/非零字节路径** — 有显著 EVM 计算时仍走的那条。
3. **气限必须预留地板** — 门槛写在 gas limit 上，不是已经烧到地板。
4. **7623** — 重估 calldata 定价，不是 4844，也不是 1559，也不是 2028。

四句对照：

- 看见的是地板公式，还是已经改了普通执行气？
- 看见的是数据为主更贵，还是已经让普通转账更贵？
- 看见的是气限必须预留地板，还是已经烧到地板？
- 这是 7623，还是已经是 4844 / 1559 / 2028？

不要和 [`name-the-history-hash.md`](name-the-history-hash.md)（历史哈希 ≠ BLOCKHASH）、blob 气（不变量 145）、基础费（不变量 158）糊成「gas」一句。
