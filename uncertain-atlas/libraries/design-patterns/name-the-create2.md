# 先给盐创建起名（name-the-create2）

> 类型：design pattern  
> 对读：不变量 222；C226；反模式 [`../anti-patterns/create2-sold-as-created.md`](../anti-patterns/create2-sold-as-created.md)；[`../../tracks/implementation/worked-example-create2-vs-created.md`](../../tracks/implementation/worked-example-create2-vs-created.md)。

设计或讲解「能算出盐地址所以已经创建」时，先分开四个名字：

1. **盐创建指令** — 按发送者、盐、initcode 哈希占址，不是已经是按序号占址的普通创建。
2. **算出来的盐地址** — 可以事先算出、链上可能还空着，不是已经创建，也不是已经有那份代码。
3. **碰撞变得可能** — 可能撞上已有序号或已有代码的地址，不是已经覆盖已有代码。
4. **1014** — 盐创建，不是 3860，也不是 684 本身，也不是自毁删户。

四句对照：

- 看见的是盐算址，还是已经按发送者加序号占址？
- 看见的是能算出地址，还是已经创建？
- 看见的是碰撞变得可能，还是已经覆盖？
- 这是 1014，还是已经是 3860 / 176 / 684？

不要和 initcode 超界≠部署代码超界（不变量 176）、碰到上限≠已经创建（不变量 175）、后来自毁≠已删（不变量 160）糊成「创建已经齐了」一句。
