# 先给状态里的历史执行哈希起名（name-the-history-hash）

> 类型：design pattern  
> 对读：不变量 195；C199；反模式 [`../anti-patterns/history-sold-as-blockhash.md`](../anti-patterns/history-sold-as-blockhash.md)；[`../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md`](../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md)。

设计或讲解「从状态供应历史块哈希」时，先分开五个名字：

1. **`BLOCKHASH` 操作码** — 窗口和代价本页不改。
2. **系统写入父哈希** — 开块、交易之前；必须跑完；不计入本块气。
3. **合约环缓冲** — 激活后要等一整窗才填满。
4. **合约读路径** — 按块号查；超出窗口回滚。
5. **4788 父信标根** — 另一份系统合约，另一类根。

四句对照：

- 看见的是操作码，还是这份合约存储？
- 系统刚写入父哈希，还是窗口已经填满？
- 能查更长，还是已经改了操作码语义？
- 这是执行块哈希，还是已经是信标根？

不要和 [`name-the-parent-root.md`](name-the-parent-root.md)（父信标根 ≠ 当前头）、[`name-the-coinbase-heat.md`](name-the-coinbase-heat.md)（开跑预热 ≠ 已经访问）糊成「链上能读历史」一句。
