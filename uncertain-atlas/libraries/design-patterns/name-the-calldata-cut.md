# 先给 calldata 降价起名（name-the-calldata-cut）

> 类型：design pattern  
> 对读：不变量 226；C230；反模式 [`../anti-patterns/calldata-cut-sold-as-unlimited.md`](../anti-patterns/calldata-cut-sold-as-unlimited.md)；[`../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md`](../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md)。

设计或讲解「calldata 降价所以已经没有上限」时，先分开四个名字：

1. **非零 calldata 降价** — 有内容的字节更便宜，不是已经给零字节也降价。
2. **潜在更大块** — 一块里能多塞数据，不是已经没有块大小上限。
3. **延迟与安全** — 更大块可能加大延迟、降低攻击成本，不是已经不改安全。
4. **2028** — 非零降价，不是 7623 地板，也不是 4844 blob，也不是 1559。

四句对照：

- 看见的是非零降价，还是零字节也降了？
- 看见的是能多塞，还是已经没有上限？
- 看见的是贴在 calldata，还是 DA 已经齐 / 已经是 blob？
- 这是 2028，还是已经是 7623 / 197 / 4844？

不要和 calldata 地板≠已改执行气（不变量 197）、blob 气≠执行气（不变量 145）、基础费≠小费（不变量 158）糊成「calldata 已经齐了」一句。
