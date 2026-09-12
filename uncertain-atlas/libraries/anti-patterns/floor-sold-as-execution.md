# 把 calldata 地板写成已经改了执行气（floor-sold-as-execution）

> 类型：anti-pattern  
> 对读：不变量 197；C201；模式 [`../design-patterns/name-the-calldata-floor.md`](../design-patterns/name-the-calldata-floor.md)；[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)。

## 坏句

- 「看见 calldata 地板了，执行气就已经改了。」
- 「数据为主更贵了，普通转账也已经更贵。」
- 「气限预留了地板，就已经烧到地板。」
- 「7623 就是 4844 / 1559 / 2028。」

## 为什么坏

[EIP-7623](https://eips.ethereum.org/EIPS/eip-7623) 官方页把地板写成对**主要以 calldata 贴数据**的交易的上限。有显著 EVM 计算的交易仍走旧的零/非零字节路径。气限必须预留地板，即便实际 `gasUsed` 可以落在地板之下。4844 是另一套 blob 气。1559 是 tip / basefee。2028 是旧 calldata 价。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见 calldata 地板 | 还没改普通执行气 |
| 数据为主更贵 | 普通转账仍可走旧路径 |
| 气限预留了地板 | 不是已经烧到地板 |
| 7623 | 不是 4844，不是 1559，不是 2028 |

相关反模式：[`blob-fee-sold-as-gas.md`](blob-fee-sold-as-gas.md)、[`basefee-sold-as-tip.md`](basefee-sold-as-tip.md)、[`initcode-sold-as-runtime.md`](initcode-sold-as-runtime.md)。
