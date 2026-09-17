# 把 RLP 编码硬帽写成已经改了气限（cap-sold-as-gas）

> 类型：anti-pattern  
> 对读：不变量 202；C206；模式 [`../design-patterns/name-the-rlp-cap.md`](../design-patterns/name-the-rlp-cap.md)；[`../../tracks/implementation/worked-example-rlp-cap-vs-gas.md`](../../tracks/implementation/worked-example-rlp-cap-vs-gas.md)。

## 坏句

- 「执行块有了 RLP 编码硬帽，气限就已经改了。」
- 「共识层流言不传更大的块，执行层就已经判非法。」
- 「给信标块留了边，执行编码和信标编码就已经并成一份。」
- 「7934 就是 7623 / 1559 / 已经是 Sepolia 那次通道尺寸。」

## 为什么坏

[EIP-7934](https://eips.ethereum.org/EIPS/eip-7934) 官方页只给执行块的 RLP 编码加一道协议级上限，并且写明这道帽独立于气相关的尺子。共识层流言不传是传播。给信标块留边不是已经并成一份编码。各家 Engine API 的 HTTP 尺寸是不变量 96，不是本页。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见编码硬帽 | 气限还在，只多了一道编码字节谓词 |
| 流言不传 | 执行层还没自己判非法 |
| 给信标块留边 | 两份编码还在，只预留空间 |
| 7934 | 不是 7623，不是 1559，不是 96 |

相关反模式：[`floor-sold-as-execution.md`](floor-sold-as-execution.md)、[`pertx-sold-as-block-rpc.md`](pertx-sold-as-block-rpc.md)、[`gas-sold-as-wallclock.md`](gas-sold-as-wallclock.md)、[`basefee-sold-as-tip.md`](basefee-sold-as-tip.md)。
