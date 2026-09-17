# 先给 blob 底价起名（name-the-blob-reserve）

> 类型：design pattern  
> 对读：不变量 201；C205；反模式 [`../anti-patterns/reserve-sold-as-merged.md`](../anti-patterns/reserve-sold-as-merged.md)；[`../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md`](../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md)。

设计或讲解「blob 费跟执行费挂钩了」时，先分开四个名字：

1. **blob 底价** — 执行基础费托住的储备下限，不是已经把两套气并成一套。
2. **执行费主导** — blob 基础费不再是价信号，不是已经没有 blob 价。
3. **不减目标** — 底价生效时超额只准涨，不是已经改了日程数字。
4. **7918** — 让拍卖还能看见价，不是 4844，不是 7691，也不是 PeerDAS。

四句对照：

- 看见的是底价，还是已经并了两套气？
- 看见的是执行费主导，还是已经没有 blob 价？
- 看见的是不减目标，还是日程数字已经改了？
- 这是 7918，还是已经是 4844 / 7691 / PeerDAS？

不要和 [`name-the-blob-schedule.md`](name-the-blob-schedule.md)（抬高日程 ≠ 已改气种）、[`name-the-calldata-floor.md`](name-the-calldata-floor.md)（地板 ≠ 执行气）、blob 气（不变量 145）糊成「DA 费」一句。
