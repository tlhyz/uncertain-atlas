# 先给返回数据缓冲起名（name-the-returndata）

> 类型：design pattern  
> 对读：不变量 232；C236；反模式 [`../anti-patterns/returndata-sold-as-memory.md`](../anti-patterns/returndata-sold-as-memory.md)；[`../../tracks/implementation/worked-example-returndata-vs-memory.md`](../../tracks/implementation/worked-example-returndata-vs-memory.md)。

设计或讲解「终于能返回不定长了」时，先分开四个名字：

1. **返回数据缓冲** — 类调用之后、调用方那份虚拟缓冲，不是已经是内存，也不是 CALL 预留输出区。
2. **下一次类调用** — 先清空再覆盖，不是旧返回还在。
3. **两次调用先问长度** — 不改 EVM 也能做、更贵，不是已经是本页。
4. **211** — 缓冲 + 读尺寸 / 再拷，不是已经是 140，也不是通用转发已经上线。

四句对照：

- 看见的是返回缓冲，还是已经在内存里？
- 看见的是很像 calldata，还是已经是 calldata？
- 看见的是能再取失败数据，还是已经是 140？
- 看见下一次类调用，还是旧缓冲还在？

不要和回滚留气≠烧光（不变量 177）、内存拷≠已是身份预编译（不变量 216）、压零≠已是带立即数的压 0（不变量 217）糊成「返回已经齐了」一句。
