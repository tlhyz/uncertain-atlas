# 先给链号指令起名（name-the-chainid）

> 类型：design pattern  
> 对读：不变量 220；C224；反模式 [`../anti-patterns/chainid-opcode-sold-as-signed.md`](../anti-patterns/chainid-opcode-sold-as-signed.md)；[`../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md`](../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md)。

设计或讲解「能读链号所以交易已经绑了这条链」时，先分开四个名字：

1. **链号指令** — 把本链配置链号压进栈，不是已经是签进哈希的链号。
2. **指令返回配置链号** — 合约看见本链配置，不是这笔交易已经带了 EIP-155 标识。
3. **编译期写死的链号** — 当前 712 一类做法，不是已经在硬分叉后仍安全。
4. **1344** — 合约内读本链号，不是 155，也不是 712，也不是不变量 161。

四句对照：

- 看见的是读本链号，还是已经把链号编进这笔交易的哈希？
- 看见的是能读到配置链号，还是这笔交易已经带了 155 标识？
- 看见的是编译期写死，还是已经在硬分叉后仍安全？
- 这是 1344，还是已经是 155 / 161 / 712？

不要和 JSON chainId≠已编进哈希（不变量 161）、基础费指令≠已改市场（不变量 218）、blob 基础费指令≠已是 3198（不变量 219）糊成「链号已经齐了」一句。
