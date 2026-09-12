# 先给内存拷贝指令起名（name-the-mcopy）

> 类型：design pattern  
> 对读：不变量 216；C220；反模式 [`../anti-patterns/mcopy-sold-as-identity.md`](../anti-patterns/mcopy-sold-as-identity.md)；[`../../tracks/implementation/worked-example-mcopy-vs-identity.md`](../../tracks/implementation/worked-example-mcopy-vs-identity.md)。

设计或讲解「有拷贝指令所以已经不用预编译」时，先分开四个名字：

1. **内存拷贝指令** — 内存到内存、只动内存，不是已经是身份预编译。
2. **「像用了中间缓冲」** — 允许重叠的语义，不是已经必须真分配缓冲。
3. **能重叠拷** — 目的和来源可以相交，不是已经是 calldata / 返回数据拷。
4. **5656** — 专用内存拷，不是 2929，也不是数前导零。

四句对照：

- 看见的是内存拷，还是已经是身份预编译？
- 看见的是「像缓冲」，还是已经必须真分配？
- 看见的是能重叠拷，还是已经是 calldata / 返回数据拷？
- 这是 5656，还是已经是 2929 / 208？

不要和本笔第一次碰≠已经热（不变量 169）、数前导零≠已更便宜 ZK（不变量 208）、initcode 超界≠部署代码超界（不变量 176）糊成「拷贝已经齐了」一句。
