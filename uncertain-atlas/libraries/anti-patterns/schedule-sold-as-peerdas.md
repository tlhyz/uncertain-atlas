# 把抬高 blob 日程写成已经是 PeerDAS（schedule-sold-as-peerdas）

> 类型：anti-pattern  
> 对读：不变量 200；C204；模式 [`../design-patterns/name-the-blob-schedule.md`](../design-patterns/name-the-blob-schedule.md)；[`../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md`](../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md)。

## 坏句

- 「目标和上限抬高了，两套气就已经并成一套。」
- 「新的目标上限比，调价还是旧的对称。」
- 「共识层换了名字，执行层就已经激活。」
- 「7691 就是 4844 / 已经是 PeerDAS。」

## 为什么坏

[EIP-7691](https://eips.ethereum.org/EIPS/eip-7691) 官方页只抬高短期吞吐。4844 的气种拆分还在。新的目标上限比打破旧对称。共识层换名和执行层激活是两份配置。官方把本页写成把力气留给 PeerDAS 等以后的方案，自己不是列抽样。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 抬高了日程 | 两套气还在 |
| 新的目标上限比 | 不再对称 |
| 共识层换名 | 执行层还没自动激活 |
| 7691 | 不是 4844，不是 PeerDAS |

相关反模式：[`blob-fee-sold-as-gas.md`](blob-fee-sold-as-gas.md)、[`floor-sold-as-execution.md`](floor-sold-as-execution.md)、[`dacert-sold-as-posted.md`](dacert-sold-as-posted.md)。
