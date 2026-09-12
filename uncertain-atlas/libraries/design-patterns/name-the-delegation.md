# 先给委托指示起名（name-the-delegation）

> 类型：design pattern  
> 对读：不变量 190；C194；反模式 [`../anti-patterns/auth-sold-as-delegated.md`](../anti-patterns/auth-sold-as-delegated.md)；[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)。

设计或讲解「账户一次交易改代码」时，先分开五个名字：

1. **授权名单** — 交易带的元组列表；空名单则该笔无效。
2. **委托指示** — 通过校验后写入授权账户的代码槽内容。
3. **目标代码** — 指示指向、执行时加载的代码。
4. **3607 开口** — 只允许代码是有效委托指示的发起者；不是整条禁止被取消。
5. **本笔执行结果** — 失败或回滚不撤回已经写好的指示。

四句对照：

- 看见名单了，还是已经委托成功？
- 代码槽里是指示，还是已经是目标代码？
- 3607 是只对有效指示放开，还是已经整条解除？
- 本笔失败了，指示还在不在？

不要和 [`name-the-sender-kind.md`](name-the-sender-kind.md)（有代码的发送方）、[`name-the-tx-envelope.md`](name-the-tx-envelope.md)（类型信封）、[`name-the-reserved-prefix.md`](name-the-reserved-prefix.md)（保留首字节）、[`name-the-suicide-tx.md`](name-the-suicide-tx.md)（自毁）糊成「有代码」一句。
