# 先给委托调用起名（name-the-delegatecall）

> 类型：design pattern  
> 对读：不变量 233；C237；反模式 [`../anti-patterns/delegatecall-sold-as-callcode.md`](../anti-patterns/delegatecall-sold-as-callcode.md)；[`../../tracks/implementation/worked-example-delegatecall-vs-callcode.md`](../../tracks/implementation/worked-example-delegatecall-vs-callcode.md)。

设计或讲解「终于能做库了」时，先分开四个名字：

1. **委托调用** — 跑目标代码，发送者与附带值和父作用域相同，不是已经是 CALLCODE。
2. **CALLCODE** — 想法上的近亲，不传父作用域的发送者与附带值，不是已经是委托调用。
3. **可变代码源动机** — 把另一地址当代码、把调用穿过去，不是已经是 7702。
4. **7** — Homestead 新加委托调用，不是已经是普通 CALL，也不是已经能靠调用数据复刻。

四句对照：

- 看见的是委托调用，还是已经是 CALLCODE？
- 看见的是父作用域的发送者传下去，还是已经是普通 CALL？
- 看见的是可变代码源动机，还是 7702 已经齐？
- 看见能把发送者塞进调用数据，还是已经是本页？

不要和正确兑现委托≠预编译信任已改（不变量 119）、授权名单≠已委托（不变量 190）、静态帧≠ view（不变量 178）糊成「委托已经齐了」一句。
