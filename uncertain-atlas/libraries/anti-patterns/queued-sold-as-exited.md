# 把进队写成已经退出（queued-sold-as-exited）

> 类型：anti-pattern  
> 对读：不变量 193；C197；模式 [`../design-patterns/name-the-el-exit.md`](../design-patterns/name-the-el-exit.md)；[`../../tracks/economic/worked-example-el-exit-vs-withdrawal.md`](../../tracks/economic/worked-example-el-exit-vs-withdrawal.md)。

## 坏句

- 「合约收下退出请求，验证者就已经退出。」
- 「本块请求名单里有一条，共识层就已经办完。」
- 「付了费进队就是已经出队。」
- 「校验失败，这块就已经非法。」
- 「7002 就是 4895 / 7685。」

## 为什么坏

[EIP-7002](https://eips.ethereum.org/EIPS/eip-7002) 官方页把进队、出队进本块名单、共识层再处理和校验失败块不必非法写成不同对象。方向是执行层请求共识层，不是 4895 那种共识层推进执行层的无条件加余额。7685 只是总线。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 付了费进队 | 还在合约队列里 |
| 本块名单里有一条 | 必须按出队顺序嵌进信标块体，共识层再处理 |
| 校验失败 | 类似存款，块不必失败 |
| 7002 | 不是 4895，不是 7685 |

相关反模式：[`withdrawal-sold-as-tx.md`](withdrawal-sold-as-tx.md)、[`request-sold-as-action.md`](request-sold-as-action.md)、[`processed-sold-as-head.md`](processed-sold-as-head.md)。
