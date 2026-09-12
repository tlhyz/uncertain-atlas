# 先给块级访问名单起名（name-the-block-list）

> 类型：design pattern  
> 对读：不变量 212；C216；反模式 [`../anti-patterns/list-sold-as-parallel.md`](../anti-patterns/list-sold-as-parallel.md)；[`../../tracks/implementation/worked-example-block-list-vs-parallel.md`](../../tracks/implementation/worked-example-block-list-vs-parallel.md)。

设计或讲解「有了访问名单所以能并行」时，先分开四个名字：

1. **块级访问名单** — 本块真正碰到的账户和槽，不是已经并行跑完。
2. **强制名单** — 缺项或多出来的项让块非法，不是已经是 2930。
3. **事后状态差** — 执行后的值，不是已经不跑交易。
4. **7928** — 块级强制名单，不是计划访问，也不是声明调度。

四句对照：

- 看见的是块级记录，还是已经并行跑完？
- 看见的是强制名单，还是已经是 2930 可选名单？
- 看见的是事后状态差，还是已经不跑交易？
- 这是 7928，还是已经是 168 / 143 / 122？

不要和计划访问≠已读过（不变量 168）、谓词过了≠脚本已跑（不变量 143）、STM 跑完≠最终（不变量 122）糊成「有名单就已经并行」一句。
