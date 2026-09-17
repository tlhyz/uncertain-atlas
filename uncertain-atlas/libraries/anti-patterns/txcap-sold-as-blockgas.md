# 把单笔气帽写成已经改了块气限（txcap-sold-as-blockgas）

> 类型：anti-pattern  
> 对读：不变量 203；C207；模式 [`../design-patterns/name-the-tx-gas-cap.md`](../design-patterns/name-the-tx-gas-cap.md)；[`../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md`](../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md)。

## 坏句

- 「单笔交易有了气帽，块气限就已经改了。」
- 「入池拒掉了超帽的单笔，块就已经验过。」
- 「块里有一笔超帽，只是策略拒绝，块还可以收。」
- 「7825 就是 7934 / 7623 / 已经是 Sepolia 那次通道尺寸。」

## 为什么坏

[EIP-7825](https://eips.ethereum.org/EIPS/eip-7825) 官方页只给任何一笔交易的气用量加一道协议级上限，并且写明这道帽不论块气限设成多少都适用、独立于块气限。入池拒掉不是已经验过块。块里有一笔超帽，整块非法。编码体积帽是不变量 202，不是本页。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见单笔气帽 | 块气限还在，只多了一道单笔气谓词 |
| 入池拒掉 | 还没验这块 |
| 块里有一笔超帽 | 整块非法，不是策略 |
| 7825 | 不是 7934，不是 7623，不是 96 |

相关反模式：[`cap-sold-as-gas.md`](cap-sold-as-gas.md)、[`floor-sold-as-execution.md`](floor-sold-as-execution.md)、[`pertx-sold-as-block-rpc.md`](pertx-sold-as-block-rpc.md)、[`gas-sold-as-wallclock.md`](gas-sold-as-wallclock.md)。
