# 先给 BLS12-381 预编译起名（name-the-bls-precompile）

> 类型：design pattern  
> 对读：不变量 199；C203；反模式 [`../anti-patterns/pairing-sold-as-verify.md`](../anti-patterns/pairing-sold-as-verify.md)；[`../../tracks/crypto/worked-example-bls-precompile-vs-verify.md`](../../tracks/crypto/worked-example-bls-precompile-vs-verify.md)。

设计或讲解「链上能不能验 BLS」时，先分开四个名字：

1. **BLS12-381 预编译套件** — 加、多标量乘、配对检查、域到点，不是已经在验签。
2. **加法** — 不查子群。
3. **MSM / 配对** — 必须查子群；配对乘积为 1 不是已经验过签。
4. **2537** — BLS12-381，不是 196/197，也不是 116 那次洞。

四句对照：

- 看见的是预编译算术，还是已经在验 BLS 签？
- 看见的是加法不查子群，还是 MSM/配对也不查？
- 看见的是全零字节约定无穷远，还是已经在曲线上？
- 这是 2537，还是已经是 196/197 / 不变量 116？

不要和子群≠在曲线上（不变量 116）、KZG≠DAS（不变量 23）糊成「BLS」一句。
