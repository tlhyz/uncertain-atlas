# 先给有效余额上限和合并请求起名（name-the-consolidation）

> 类型：design pattern  
> 对读：不变量 196；C200；反模式 [`../anti-patterns/consolidation-sold-as-done.md`](../anti-patterns/consolidation-sold-as-done.md)；[`../../tracks/economic/worked-example-maxeb-vs-minact.md`](../../tracks/economic/worked-example-maxeb-vs-minact.md)。

设计或讲解「一把验证者可变大小」时，先分开五个名字：

1. **最低激活额** — 官方保留的下限，不是已经取消。
2. **有效余额上限** — 本页抬高的那道天花板。
3. **合并请求** — 7685 总线上的一种类型；付了费先入队。
4. **待处理存款** — 进来先排队，有效余额先写成零。
5. **协议内合并办完** — 下标并起来，并且切到复利凭证。

四句对照：

- 看见的是抬高上限，还是已经取消最低激活额？
- 看见的是合并请求，还是已经并成一把？
- 进了待处理存款，还是已经记上有效余额？
- 这是协议内合并，还是已经走了退出再激活？

不要和 [`name-the-el-exit.md`](name-the-el-exit.md)（退出请求 ≠ 已经退出）、[`name-the-el-deposit.md`](name-the-el-deposit.md)（存款日志 ≠ 已经办完）、[`name-the-request-bus.md`](name-the-request-bus.md)（总线 ≠ 已经处理）糊成「质押」一句。
