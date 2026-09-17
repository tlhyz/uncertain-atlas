# 先给代码哈希指令起名（name-the-extcodehash）

> 类型：design pattern  
> 对读：不变量 221；C225；反模式 [`../anti-patterns/extcodehash-sold-as-copy.md`](../anti-patterns/extcodehash-sold-as-copy.md)；[`../../tracks/implementation/worked-example-extcodehash-vs-copy.md`](../../tracks/implementation/worked-example-extcodehash-vs-copy.md)。

设计或讲解「能读代码哈希所以已经看见代码」时，先分开四个名字：

1. **代码哈希指令** — 把某账户代码的哈希压进栈，不是已经看见代码本身。
2. **返回 0** — 不存在或按 161 是空，不是已经是「有账户、没代码」。
3. **返回空数据哈希** — 账户在但没有代码，不是已经是账户不存在。
4. **1052** — 合约内读代码哈希，不是 161，也不是 3607，也不是读尺寸或拷代码。

四句对照：

- 看见的是读哈希，还是已经把代码拷出来？
- 看见的是返回 0，还是已经能写成没代码的账户？
- 看见的是空数据哈希，还是已经能写成不存在？
- 这是 1052，还是已经是 161 / 180 / 162？

不要和空≠已经不存在（不变量 180）、发送者已有代码≠已经能发（不变量 162）、链号指令≠已签进哈希（不变量 220）糊成「代码已经齐了」一句。
