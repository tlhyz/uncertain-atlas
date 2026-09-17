# 反模式：块 gas 上限被写成墙钟已经有界

> 真值：[Ethereum 2021-05](../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md)、[不变式 101](../invariants/README.md)。亲戚：[flood-sold-as-halt](flood-sold-as-halt.md)、[pertx-sold-as-block-rpc](pertx-sold-as-block-rpc.md)、[zero-cost-sold-as-safe](zero-cost-sold-as-safe.md)。

## 一句话

看见块有 gas 上限，或看见状态访问操作码标了固定 gas，就写成执行时间已经有界、磁盘已经是常数。

## 正确写法

「gas 是协议计量，不是墙钟。状态访问的真实代价可以随集合变大。快照是实现加速，不是 gas 已经等于时间。」
