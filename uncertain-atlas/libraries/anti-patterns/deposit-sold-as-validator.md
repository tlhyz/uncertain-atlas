# 把存款日志写成已经是验证者（deposit-sold-as-validator）

> 类型：anti-pattern  
> 对读：不变量 194；C198；模式 [`../design-patterns/name-the-el-deposit.md`](../design-patterns/name-the-el-deposit.md)；[`../../tracks/economic/worked-example-el-deposit-vs-eth1data.md`](../../tracks/economic/worked-example-el-deposit-vs-eth1data.md)。

## 坏句

- 「合约记下存款，验证者就已经在。」
- 「本块请求名单里有一条，共识层就已经办完。」
- 「看见存款交易就是已经进了名单。」
- 「有了新字段，旧投票就已经关掉。」
- 「6110 就是 7685 / 7002 / 4895。」

## 为什么坏

[EIP-6110](https://eips.ethereum.org/EIPS/eip-6110) 官方页把存款交易、合约日志、本块请求名单和共识层再处理写成不同对象。名单必须按日志顺序出现。旧投票要等两个下标对齐才能各自关掉。同一公钥在不同分叉上可以有不同下标。7685 只是总线。7002 是另一方向的退出请求。4895 是共识层推进执行层的无条件加余额。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见存款交易 | 还要发出本页这种日志 |
| 看见日志 | 必须按顺序进入本块 7685 名单 |
| 本块名单里有一条 | 共识层再处理；下标跨分叉可以不同 |
| 6110 | 不是 7685，不是 7002，不是 4895 |

相关反模式：[`queued-sold-as-exited.md`](queued-sold-as-exited.md)、[`request-sold-as-action.md`](request-sold-as-action.md)、[`withdrawal-sold-as-tx.md`](withdrawal-sold-as-tx.md)。
