# 把看见合并请求写成已经并成一把（consolidation-sold-as-done）

> 类型：anti-pattern  
> 对读：不变量 196；C200；模式 [`../design-patterns/name-the-consolidation.md`](../design-patterns/name-the-consolidation.md)；[`../../tracks/economic/worked-example-maxeb-vs-minact.md`](../../tracks/economic/worked-example-maxeb-vs-minact.md)。

## 坏句

- 「合约收下合并请求，两把就已经并成一把。」
- 「抬高了上限，最低激活额就已经取消。」
- 「进了待处理存款，有效余额就已经记上。」
- 「7251 就是 7002 / 6110 / 7685。」

## 为什么坏

[EIP-7251](https://eips.ethereum.org/EIPS/eip-7251) 官方页把抬高上限和另立最低激活额写成两句。合并请求先入队，再按出队顺序进本块名单，共识层再处理。存款先放进待处理名单，有效余额先写成零。7002 是退出/部分提款。6110 是存款供应。7685 只是总线。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见合并请求 | 还在合约队列或本块名单里 |
| 抬高了上限 | 最低激活额仍在 |
| 进了待处理存款 | 有效余额还没由待处理流程更新 |
| 7251 | 不是 7002，不是 6110，不是 7685 |

相关反模式：[`queued-sold-as-exited.md`](queued-sold-as-exited.md)、[`deposit-sold-as-validator.md`](deposit-sold-as-validator.md)、[`request-sold-as-action.md`](request-sold-as-action.md)。
