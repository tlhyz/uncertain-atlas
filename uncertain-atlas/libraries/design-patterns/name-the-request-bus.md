# 先给请求总线起名（name-the-request-bus）

> 类型：design pattern  
> 对读：不变量 192；C196；反模式 [`../anti-patterns/request-sold-as-action.md`](../anti-patterns/request-sold-as-action.md)；[`../../tracks/finality/worked-example-request-vs-action.md`](../../tracks/finality/worked-example-request-vs-action.md)。

设计或讲解「执行层往共识层递条子」时，先分开五个名字：

1. **请求承诺** — 执行头上那一个字段。
2. **类型字节** — 标明是哪一种请求。
3. **不透明载荷** — 该类型自己定义的字节。
4. **共识层再处理** — 承诺之后才发生。
5. **单独促成动作的权力** — 本页明确请求并不自带。

四句对照：

- 看见的是头上的承诺，还是共识层已经处理完？
- 看见的是类型字节，还是已经是载荷？
- 空项被排除了，还是这种类型从未出现？
- 这是请求，还是已经有权单独促成动作？

不要和 [`name-the-forkchoice-event.md`](name-the-forkchoice-event.md)（处理完一块 ≠ 改头）、[`name-the-system-op.md`](name-the-system-op.md)（提款 ≠ 用户交易）、[`name-the-tx-envelope.md`](name-the-tx-envelope.md)（类型信封）糊成「头上多了一样东西」一句。
