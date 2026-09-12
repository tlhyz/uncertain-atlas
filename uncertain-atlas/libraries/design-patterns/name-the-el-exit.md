# 先给执行层退出请求起名（name-the-el-exit）

> 类型：design pattern  
> 对读：不变量 193；C197；反模式 [`../anti-patterns/queued-sold-as-exited.md`](../anti-patterns/queued-sold-as-exited.md)；[`../../tracks/economic/worked-example-el-exit-vs-withdrawal.md`](../../tracks/economic/worked-example-el-exit-vs-withdrawal.md)。

设计或讲解「执行层触发退出 / 部分提款」时，先分开五个名字：

1. **活动钥自愿退出** — 当时既有规则里唯一能发起退出的那把热钥。
2. **提款凭证触发的请求** — 本页补上的冷凭证路径。
3. **合约队列** — 付了费先入队，还没进本块名单。
4. **本块 7685 名单** — 按出队顺序嵌进信标块体。
5. **共识层办完** — 类似自愿退出，但校验失败块不必非法。

四句对照：

- 看见的是活动钥自愿退出，还是提款凭证触发的请求？
- 进了队，还是已经出队进本块名单？
- 名单里有一条，还是共识层已经办完？
- 这是请求共识层，还是已经是无条件加余额？

不要和 [`name-the-system-op.md`](name-the-system-op.md)（4895 提款 ≠ 用户交易）、[`name-the-request-bus.md`](name-the-request-bus.md)（总线 ≠ 已经处理）、[`name-the-forkchoice-event.md`](name-the-forkchoice-event.md)（处理完一块 ≠ 改头）糊成「提款」一句。
