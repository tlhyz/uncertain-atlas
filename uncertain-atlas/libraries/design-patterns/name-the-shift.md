# 先给原生移位起名（name-the-shift）

> 类型：design pattern  
> 对读：不变量 231；C235；反模式 [`../anti-patterns/shift-sold-as-arithmetic.md`](../anti-patterns/shift-sold-as-arithmetic.md)；[`../../tracks/implementation/worked-example-shift-vs-arithmetic.md`](../../tracks/implementation/worked-example-shift-vs-arithmetic.md)。

设计或讲解「以太坊终于能移位了」时，先分开四个名字：

1. **原生移位** — 左移、逻辑右移、算术右移三条指令，不是已经用乘除拼过移位。
2. **算术右移** — 有符号值、无符号移位量、符号扩展，不是已经是有符号除。
3. **更便宜 / 更省主机** — 原生指令的动机，不是已经是位域打包产品。
4. **145** — 新加三条移位，不是已经改了旧字节码。

四句对照：

- 看见的是原生移位，还是已经用算术拼过？
- 看见的是算术右移，还是已经是有符号除？
- 看见的是更便宜，还是位域打包已经齐？
- 这是 145，还是旧合约行为已经变了？

不要和数前导零≠已便宜 ZK（不变量 208）、压零≠已是带立即数的压 0（不变量 217）、BLAKE2 压缩函数≠已是哈希（不变量 230）糊成「比特操作已经齐了」一句。
