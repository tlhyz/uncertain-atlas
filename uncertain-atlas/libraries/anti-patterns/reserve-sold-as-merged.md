# 把 blob 底价写成已经并成一套气（reserve-sold-as-merged）

> 类型：anti-pattern  
> 对读：不变量 201；C205；模式 [`../design-patterns/name-the-blob-reserve.md`](../design-patterns/name-the-blob-reserve.md)；[`../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md`](../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md)。

## 坏句

- 「blob 费被执行费托底了，两套气就已经并成一套。」
- 「执行费主导了，就已经没有 blob 价。」
- 「超额不再减目标，日程数字就已经改了。」
- 「7918 就是 4844 / 7691 / 已经是 PeerDAS 的定价。」

## 为什么坏

[EIP-7918](https://eips.ethereum.org/EIPS/eip-7918) 官方页只给 blob 基础费加一层相对执行基础费的储备下限。两套气还在。数据本身另加的费仍由 blob 费市场自己定。不减目标不是改日程。验 KZG 贵是动机，不是已经换成列抽样。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见底价 | 两套气还在，只钩了价的下限 |
| 执行费主导 | blob 价还在，只是不再是价信号 |
| 不减目标 | 日程数字没改 |
| 7918 | 不是 4844，不是 7691，不是 PeerDAS |

相关反模式：[`blob-fee-sold-as-gas.md`](blob-fee-sold-as-gas.md)、[`schedule-sold-as-peerdas.md`](schedule-sold-as-peerdas.md)、[`floor-sold-as-execution.md`](floor-sold-as-execution.md)、[`basefee-sold-as-tip.md`](basefee-sold-as-tip.md)。
