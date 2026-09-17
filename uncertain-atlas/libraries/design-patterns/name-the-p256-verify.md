# 先给 P256 验签预编译起名（name-the-p256-verify）

> 类型：design pattern  
> 对读：不变量 204；C208；反模式 [`../anti-patterns/p256-sold-as-k1.md`](../anti-patterns/p256-sold-as-k1.md)；[`../../tracks/crypto/worked-example-p256-vs-k1.md`](../../tracks/crypto/worked-example-p256-vs-k1.md)。

设计或讲解「链上能验硬件签了」时，先分开四个名字：

1. **P256 验签预编译** — secp256r1 上的 ECDSA 验，不是已经在验 k1。
2. **验绿** — 这份输入过了本页谓词，不是已经不可延展。
3. **空输出** — 失败且不 revert，不是已经烧光剩余气。
4. **7951** — 带两处修补的验签接口，不是 2537，不是 `ECRECOVER`，也不是 RIP-7212 洞已经没了。

四句对照：

- 看见的是 P256 验签，还是已经在验 k1？
- 看见的是验绿，还是已经不可延展？
- 看见的是空输出，还是已经烧光剩余气？
- 这是 7951，还是已经是 2537 / `ECRECOVER` / 116？

不要和 [`name-the-bls-precompile.md`](name-the-bls-precompile.md)（算术 ≠ 已验 BLS）、验得过≠DER（不变量 172）、子群≠在曲线上（不变量 116）糊成「链上验签」一句。
