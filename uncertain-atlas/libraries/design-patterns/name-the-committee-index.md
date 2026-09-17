# 先给委员会下标起名（name-the-committee-index）

> 类型：design pattern  
> 对读：不变量 198；C202；反模式 [`../anti-patterns/committee-sold-as-signed.md`](../anti-patterns/committee-sold-as-signed.md)；[`../../tracks/finality/worked-example-committee-index-vs-signed.md`](../../tracks/finality/worked-example-committee-index-vs-signed.md)。

设计或讲解「证明怎么聚合」时，先分开四个名字：

1. **已签名的 AttestationData** — LMD 票 + FFG 票；`index` 固定为零。
2. **外层 committee_bits** — 委员会下标现在住的地方，不是已经签进 Data。
3. **链上证明名单** — 分叉后第一块可以空，不是已经没有 LMD 票。
4. **7549** — 只改共识层证明容器，不是已经改执行层，也不是同步委员会。

四句对照：

- 看见的是外层位图，还是已经签进 AttestationData？
- 看见的是 `index` 写成零，还是已经删掉该字段？
- 看见的是分叉后第一块没有证明，还是已经没有 LMD 票？
- 这是 7549，还是已经改了执行层 / 已经是同步委员会抽样？

不要和 [`name-the-request-bus.md`](name-the-request-bus.md)（请求承诺 ≠ 已处理）、head / justified / finalized（不变量 127）糊成「证明」一句。
