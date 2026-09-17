# 把授权名单写成已经委托（auth-sold-as-delegated）

> 类型：anti-pattern  
> 对读：不变量 190；C194；模式 [`../design-patterns/name-the-delegation.md`](../design-patterns/name-the-delegation.md)；[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)。

## 坏句

- 「交易里有授权名单，账户就已经委托成功。」
- 「代码槽里的委托指示就是目标合约代码。」
- 「EIP-7702 已经让带代码的账户都能发起交易。」
- 「这笔执行失败了，刚才写的委托也撤回了。」
- 「7702 就是 3607 / 3541 / 2718。」

## 为什么坏

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) 官方页把名单、指示、目标代码、3607 开口和本笔执行结果写成不同对象。某个元组失败则跳过该元组；本笔失败不撤回已写指示。3607 只对有效委托指示放开，不是整条解除。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见名单 | 名单非空只说明交易形状合法；每项还要过校验才写指示 |
| 指示 | 指向目标的代码槽内容，不是目标本身 |
| 7702 修改了 3607 | 只加「有效委托指示可发起」 |
| 本笔回滚 | 已处理的指示仍在 |
| 7702 | 不是 3607，不是 3541，不是 2718 |

相关反模式：[`code-sender-sold-as-eoa.md`](code-sender-sold-as-eoa.md)、[`type-sold-as-payload.md`](type-sold-as-payload.md)、[`reserved-sold-as-eof.md`](reserved-sold-as-eof.md)、[`selfdestruct-sold-as-deleted.md`](selfdestruct-sold-as-deleted.md)。
