# 先给 blob 基础费指令起名（name-the-blobbasefee）

> 类型：design pattern  
> 对读：不变量 219；C223；反模式 [`../anti-patterns/blobbasefee-sold-as-basefee.md`](../anti-patterns/blobbasefee-sold-as-basefee.md)；[`../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md`](../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md)。

设计或讲解「能读 blob 基础费所以已经是基础费」时，先分开四个名字：

1. **blob 基础费指令** — 把本块 blob 基础费压进栈，不是已经是执行层基础费指令。
2. **能读本块 blob 基础费** — 合约看见头上已经公开的 blob 价，不是已经并成一套气。
3. **跑 EVM 前就已经有这个数** — 处理 blob 交易本来就要用，不是已经改了 4844 日程。
4. **7516** — 读 blob 基础费，不是 3198，也不是 4844，也不是 blob 底价规则。

四句对照：

- 看见的是读 blob 价，还是已经是读执行层基础费？
- 看见的是能读到这个数，还是已经并成一套气？
- 看见的是跑之前就有这个数，还是已经改了 4844 日程？
- 这是 7516，还是已经是 3198 / 218 / 4844 / 201？

不要和基础费指令≠已改市场（不变量 218）、blob 气≠执行气（不变量 145）、blob 底价≠已并账（不变量 201）糊成「blob 费已经齐了」一句。
