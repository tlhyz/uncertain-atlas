# 先给弃用警告起名（name-the-deprecation）

> 类型：design pattern  
> 对读：不变量 224；C228；反模式 [`../anti-patterns/deprecate-sold-as-changed.md`](../anti-patterns/deprecate-sold-as-changed.md)；[`../../tracks/implementation/worked-example-deprecate-vs-changed.md`](../../tracks/implementation/worked-example-deprecate-vs-changed.md)。

设计或讲解「已弃用所以行为已经变」时，先分开四个名字：

1. **弃用警告** — 文档劝阻使用，并警告以后可能变，不是已经改了现在的共识行为。
2. **不改客户端** — 元层页，对客户端不适用任何改动，不是已经硬分叉，也不是已经删掉指令。
3. **以后可能变** — 官方写会改点什么，不是已经改完。
4. **6049** — 弃用文档，不是 6780，也不是 3529，也不是 160 的自毁语义。

四句对照：

- 看见的是告示，还是已经改了现在做什么？
- 看见的是元层页，还是客户端已经改？
- 看见的是「以后可能变」，还是已经变了？
- 这是 6049，还是已经是 6780 / 160 / 223？

不要和后来自毁≠已删（不变量 160）、退款削减≠已没有退款（不变量 223）、盐创建≠已创建（不变量 222）糊成「自毁已经齐了」一句。
