# 先给执行层存款请求起名（name-the-el-deposit）

> 类型：design pattern  
> 对读：不变量 194；C198；反模式 [`../anti-patterns/deposit-sold-as-validator.md`](../anti-patterns/deposit-sold-as-validator.md)；[`../../tracks/economic/worked-example-el-deposit-vs-eth1data.md`](../../tracks/economic/worked-example-el-deposit-vs-eth1data.md)。

设计或讲解「执行层供应验证者存款」时，先分开五个名字：

1. **存款交易** — 用户在执行层交的那笔。
2. **存款合约日志** — 本块收据里、按地址和事件签名滤出来的那几条。
3. **本块 7685 名单** — 必须按日志顺序出现。
4. **共识层办完** — 处理存款请求；不是看见名单就已经是验证者。
5. **旧 eth1data 投票** — 过渡期还在；两个下标对齐之后才能各自关掉。

四句对照：

- 看见的是存款交易，还是已经解析成请求？
- 进了日志，还是已经按顺序进了本块名单？
- 名单里有一条，还是共识层已经办完？
- 旧投票还在过渡，还是两个下标已经对齐？

不要和 [`name-the-el-exit.md`](name-the-el-exit.md)（退出请求 ≠ 已经退出）、[`name-the-request-bus.md`](name-the-request-bus.md)（总线 ≠ 已经处理）、[`name-the-system-op.md`](name-the-system-op.md)（4895 提款 ≠ 用户交易）糊成「存款」一句。
