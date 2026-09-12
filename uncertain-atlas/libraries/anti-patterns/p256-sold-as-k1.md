# 把 P256 验签预编译写成已经在验 k1（p256-sold-as-k1）

> 类型：anti-pattern  
> 对读：不变量 204；C208；模式 [`../design-patterns/name-the-p256-verify.md`](../design-patterns/name-the-p256-verify.md)；[`../../tracks/crypto/worked-example-p256-vs-k1.md`](../../tracks/crypto/worked-example-p256-vs-k1.md)。

## 坏句

- 「有了 P256 预编译，就已经在验 Ethereum 默认的 k1。」
- 「验绿了，就已经不可延展。」
- 「失败返回空，就已经把剩余气烧光。」
- 「接口和 RIP-7212 兼容，那两个洞就已经没了。」
- 「7951 就是 2537 / 已经是 `ECRECOVER` / 已经是 116。」

## 为什么坏

[EIP-7951](https://eips.ethereum.org/EIPS/eip-7951) 官方页只加一条 secp256r1 上的 ECDSA **验签**预编译。默认用户交易仍是 k1。验绿不是不可延展。失败不得 revert，气和成功一样。与 RIP-7212 接口兼容，正是因为本页补了那两个洞，不是洞已经消失。2537 是曲线算术，不是验签。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见 P256 预编译 | 默认签还是 k1 |
| 验绿 | 按 NIST，r1 签不要求不可延展 |
| 空输出 | 不 revert，气和成功一样 |
| 接口兼容 | 本页补洞，不是 RIP-7212 已经没洞 |
| 7951 | 不是 2537，不是恢复，不是 116 |

相关反模式：[`pairing-sold-as-verify.md`](pairing-sold-as-verify.md)、[`subgroup-sold-as-on-curve.md`](subgroup-sold-as-on-curve.md)、[`valid-sold-as-der.md`](valid-sold-as-der.md)、[`revert-sold-as-invalid.md`](revert-sold-as-invalid.md)。
