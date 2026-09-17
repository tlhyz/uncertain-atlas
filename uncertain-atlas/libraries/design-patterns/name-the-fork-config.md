# 先给分叉配置 RPC 起名（name-the-fork-config）

> 类型：design pattern  
> 对读：不变量 210；C214；反模式 [`../anti-patterns/config-sold-as-aligned.md`](../anti-patterns/config-sold-as-aligned.md)；[`../../tracks/implementation/worked-example-config-rpc-vs-aligned.md`](../../tracks/implementation/worked-example-config-rpc-vs-aligned.md)。

设计或讲解「分叉前各家对过配置」时，先分开四个名字：

1. **分叉配置 RPC** — 本节点报告当前 / 下一份 / 最后一份，不是已经过多客户端同根。
2. **current / next / last** — 三份配置对象，不是已经改了共识。
3. **RPC 绿** — 接口回了对象，不是对等节点没有撒谎。
4. **7910** — 分叉前核对配置的 RPC，不是 Engine API 已经改头，也不是专用分叉机制。

四句对照：

- 看见的是配置对上了，还是已经过多客户端同根？
- 看见的是三份配置对象，还是共识已经改了？
- 看见的是 RPC 绿，还是对等节点已经诚实？
- 这是 7910，还是已经是 149 / 209 / 207？

不要和处理完一块≠改头（不变量 149）、专用分叉≠已改执行（不变量 209）、对等窗≠已改共识（不变量 207）糊成「分叉已经齐了」一句。
