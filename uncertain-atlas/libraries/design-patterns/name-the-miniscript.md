# 先给分析语言起名（name-the-miniscript）

> 类型：design pattern  
> 对读：不变量 191；C195；反模式 [`../anti-patterns/miniscript-sold-as-script.md`](../anti-patterns/miniscript-sold-as-script.md)；[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)。

设计或讲解「结构化脚本 / 可分析花费条件」时，先分开五个名字：

1. **分析语言** — 用来写一部分 Bitcoin 脚本的结构化表示。
2. **链上脚本** — 实际放进输出、花费时揭开的字节。
3. **描述符扩张** — 从用户看不是另一门语言。
4. **共识健全** — 条件不满足就造不出共识合法见证。
5. **策略完备** — 在资源界和没有时间锁混用的前提下，每条路径都能造出策略合法见证。

四句对照：

- 看见的是分析语言，还是已经是链上脚本？
- 这是描述符的扩张，还是已经换了一门语言？
- 问的是共识健全，还是策略完备？
- 本页覆盖的是哪一种封装，付给脚本哈希算不算？

不要和 [`name-the-descriptor.md`](name-the-descriptor.md)（描述符总语法）、[`name-the-tapscript-leaf.md`](name-the-tapscript-leaf.md)（叶子语义）、[`name-the-redeem-reveal.md`](name-the-redeem-reveal.md)（哈希赎回）、[`name-the-spend-path.md`](name-the-spend-path.md)（钥匙路径 / 脚本路径）糊成「脚本」一句。
