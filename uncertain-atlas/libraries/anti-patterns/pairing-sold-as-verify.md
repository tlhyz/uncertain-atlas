# 把配对预编译写成已经在验 BLS 签（pairing-sold-as-verify）

> 类型：anti-pattern  
> 对读：不变量 199；C203；模式 [`../design-patterns/name-the-bls-precompile.md`](../design-patterns/name-the-bls-precompile.md)；[`../../tracks/crypto/worked-example-bls-precompile-vs-verify.md`](../../tracks/crypto/worked-example-bls-precompile-vs-verify.md)。

## 坏句

- 「有了 BLS12-381 预编译，就已经在验 BLS 签。」
- 「加法不查子群，MSM 和配对也不查。」
- 「全零字节就是已经在曲线上的点。」
- 「2537 就是 196/197 / 就是 116 那次洞。」

## 为什么坏

[EIP-2537](https://eips.ethereum.org/EIPS/eip-2537) 官方页加入的是曲线运算和聚合用的多标量乘，用来**高效做** BLS 验签这类事，不是一条「验 BLS 签」指令。加法官方不查子群；MSM 和配对必须查。`(0,0)` 不在 BLS12 曲线上，全零字节只是无穷远的约定编码。196/197 是 BN254。116 是 Besu 把子群检查当成曲线检查。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见 BLS12-381 预编译 | 还只是曲线算术 |
| 加法不查子群 | MSM/配对必须查 |
| 全零字节 | 约定的无穷远，不是已经在曲线上 |
| 2537 | 不是 196/197，不是 116 |

相关反模式：[`subgroup-sold-as-on-curve.md`](subgroup-sold-as-on-curve.md)、[`valid-sold-as-der.md`](valid-sold-as-der.md)、[`blob-fee-sold-as-gas.md`](blob-fee-sold-as-gas.md)。
