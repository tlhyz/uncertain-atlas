# 把请求写成已经促成动作（request-sold-as-action）

> 类型：anti-pattern  
> 对读：不变量 192；C196；模式 [`../design-patterns/name-the-request-bus.md`](../design-patterns/name-the-request-bus.md)；[`../../tracks/finality/worked-example-request-vs-action.md`](../../tracks/finality/worked-example-request-vs-action.md)。

## 坏句

- 「头上已经有请求承诺，共识层就处理完了。」
- 「看见类型字节就是已经解开这条请求。」
- 「承诺里没有这一项，这种请求从未出现。」
- 「请求已经能单独促成退出 / 提款。」
- 「7685 就是 4895 / 2718。」

## 为什么坏

[EIP-7685](https://eips.ethereum.org/EIPS/eip-7685) 官方页把头上的承诺、类型字节、不透明载荷和共识层再处理写成不同对象。请求并不自己带有单方面促成动作的权力。空载荷被排除出承诺，不是已经没有过这种类型。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见承诺 | 执行头上的一个字段，事后才交给共识层 |
| 类型字节 | 还没有解开该类型自己的载荷 |
| 承诺里没有 | 空载荷被排除，不是从未出现 |
| 请求 | 不是已经有权单独促成动作 |
| 7685 | 不是 4895，不是 2718 |

相关反模式：[`processed-sold-as-head.md`](processed-sold-as-head.md)、[`withdrawal-sold-as-tx.md`](withdrawal-sold-as-tx.md)、[`type-sold-as-payload.md`](type-sold-as-payload.md)。
