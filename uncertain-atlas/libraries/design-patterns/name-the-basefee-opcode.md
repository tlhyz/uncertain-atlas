# 先给基础费指令起名（name-the-basefee-opcode）

> 类型：design pattern  
> 对读：不变量 218；C222；反模式 [`../anti-patterns/basefee-opcode-sold-as-market.md`](../anti-patterns/basefee-opcode-sold-as-market.md)；[`../../tracks/implementation/worked-example-basefee-opcode-vs-market.md`](../../tracks/implementation/worked-example-basefee-opcode-vs-market.md)。

设计或讲解「能读基础费所以市场已经齐」时，先分开四个名字：

1. **基础费指令** — 把本块基础费压进栈，不是已经改了费用市场。
2. **能读本块基础费** — 合约看见头上已经公开的数，不是已经给了出块者。
3. **跑 EVM 前就已经有这个数** — 处理交易本来就要用，不是已经改了头怎么算。
4. **3198** — 读执行层基础费，不是 1559，也不是 blob 底价指令。

四句对照：

- 看见的是读数指令，还是已经改了费用市场？
- 看见的是能读到这个数，还是已经给了出块者？
- 看见的是跑之前就有这个数，还是已经改了头怎么算？
- 这是 3198，还是已经是 1559 / 158 / 7516？

不要和基础费≠小费（不变量 158）、blob 气≠执行气（不变量 145）、压零≠带立即数的压 0（不变量 217）糊成「费用已经齐了」一句。
