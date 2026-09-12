# 把委员会下标写成已经签进投票（committee-sold-as-signed）

> 类型：anti-pattern  
> 对读：不变量 198；C202；模式 [`../design-patterns/name-the-committee-index.md`](../design-patterns/name-the-committee-index.md)；[`../../tracks/finality/worked-example-committee-index-vs-signed.md`](../../tracks/finality/worked-example-committee-index-vs-signed.md)。

## 坏句

- 「下标挪到外面了，就已经没有委员会。」
- 「`AttestationData.index` 是零，字段就已经删了。」
- 「分叉后第一块没有证明，LMD 票就已经没了。」
- 「7549 已经改了执行层 / 已经是同步委员会。」

## 为什么坏

[EIP-7549](https://eips.ethereum.org/EIPS/eip-7549) 官方页把委员会下标挪出已签名消息，好让相同共识票能聚合。`AttestationData.index` 保留、固定写成零，为的是不把 `AttesterSlashing` 弄复杂。分叉后第一块可以没有证明，但 LMD 票仍可通过 `on_attestation` 进分叉选择。本页不改执行层。同步委员会是另一份抽样对象。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 下标在签名外面 | 委员会还在外层位图里 |
| `index` 写成零 | 字段还在，只是固定为零 |
| 分叉后第一块没有证明 | LMD 仍可走 `on_attestation` |
| 7549 | 不是执行层，不是同步委员会 |

相关反模式：[`processed-sold-as-head.md`](processed-sold-as-head.md)、[`request-sold-as-action.md`](request-sold-as-action.md)、[`leak-sold-as-slash.md`](leak-sold-as-slash.md)。
