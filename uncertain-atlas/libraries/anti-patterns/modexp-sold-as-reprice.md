# 把 MODEXP 输入长度帽写成已经改了计价（modexp-sold-as-reprice）

> 类型：anti-pattern  
> 对读：不变量 206；C210；模式 [`../design-patterns/name-the-modexp-bound.md`](../design-patterns/name-the-modexp-bound.md)；[`../../tracks/implementation/worked-example-modexp-bound-vs-price.md`](../../tracks/implementation/worked-example-modexp-bound-vs-price.md)。

## 坏句

- 「模幂输入有上限了，计价公式就已经改过。」
- 「超帽了，还能算出结果。」
- 「长度有界了，预编译就已经换成普通 EVM 代码。」
- 「7823 就是 198 已经重定价 / 已经是 7825 / 已经是 7951。」

## 为什么坏

[EIP-7823](https://eips.ethereum.org/EIPS/eip-7823) 官方页只给模幂预编译的三段长度加帽。官方明确现在不借本页重写计价；上限是为以后才可能改价、才可能换成 EVM 代码做准备。超帽必须停、必须报错、必须烧光剩余气。7825 是单笔交易气用量。7951 失败不 revert，气和成功一样。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见长度帽 | 计价公式还是原来那套 |
| 超帽 | 停住、报错、烧光剩余气 |
| 长度有界 | 预编译还在；换成 EVM 是以后的事 |
| 7823 | 不是 198 重定价，不是 7825，不是 7951 |

相关反模式：[`txcap-sold-as-blockgas.md`](txcap-sold-as-blockgas.md)、[`p256-sold-as-k1.md`](p256-sold-as-k1.md)、[`revert-sold-as-invalid.md`](revert-sold-as-invalid.md)。
