# 先给 BLAKE2 压缩函数起名（name-the-blake2f）

> 类型：design pattern  
> 对读：不变量 230；C234；反模式 [`../anti-patterns/blake2f-sold-as-hash.md`](../anti-patterns/blake2f-sold-as-hash.md)；[`../../tracks/implementation/worked-example-blake2f-vs-hash.md`](../../tracks/implementation/worked-example-blake2f-vs-hash.md)。

设计或讲解「以太坊终于有 BLAKE2 了」时，先分开四个名字：

1. **压缩函数 F** — BLAKE2 里的一轮压缩预编译，不是已经是 BLAKE2b 哈希。
2. **定长输入** — 按规范紧凑编码，长度和旗标都有合法档，不是已经是任意哈希 API。
3. **互操作动机** — 让 Equihash / 跨链中继 / 原子交换变得可能，不是已经能验，也不是已经有隐私。
4. **152** — 给 EVM 加 F，不是完整 BLAKE2b，也不是 keccak / SHA3。

四句对照：

- 看见的是压缩函数，还是已经是哈希？
- 看见的是定长输入，还是已经能吃任意哈希 API？
- 看见的是互操作动机，还是中继 / 原子交换 / 隐私已经齐？
- 这是 152，还是已经是 keccak / SHA3？

不要和预编译算术≠已验 BLS（不变量 199）、bn128 预编译降价≠已验签（不变量 228）、代码哈希指令≠已看见代码（不变量 221）糊成「哈希已经齐了」一句。
