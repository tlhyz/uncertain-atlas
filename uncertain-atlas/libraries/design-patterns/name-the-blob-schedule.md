# 先给 blob 日程起名（name-the-blob-schedule）

> 类型：design pattern  
> 对读：不变量 200；C204；反模式 [`../anti-patterns/schedule-sold-as-peerdas.md`](../anti-patterns/schedule-sold-as-peerdas.md)；[`../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md`](../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md)。

设计或讲解「blob 更多了」时，先分开四个名字：

1. **blob 日程** — 每块目标与上限，不是已经改了两套气的拆分。
2. **目标上限比** — 本页打破旧对称，不是已经还是旧调价。
3. **共识层换名 / 执行层激活** — 两份配置，不是已经同一天。
4. **7691** — 短期抬高吞吐，不是 4844，也不是 PeerDAS。

四句对照：

- 看见的是抬高日程，还是已经改了 blob 气与执行气的拆分？
- 看见的是新的目标上限比，还是已经还是旧对称？
- 看见的是共识层换名，还是执行层已经激活？
- 这是 7691，还是已经是 4844 / PeerDAS？

不要和 [`name-the-calldata-floor.md`](name-the-calldata-floor.md)（地板 ≠ 执行气）、blob 气（不变量 145）糊成「DA」一句。
