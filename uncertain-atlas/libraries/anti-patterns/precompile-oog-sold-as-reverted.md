# 反模式：预编译中途出错被写成 SDK 已写入已经撤回

> 真值：[ISA-2025-004](../../tracks/failure-museum/isa-2025-004.md)、[不变式 117](../invariants/README.md)。亲戚：[oog-sold-as-reverted](oog-sold-as-reverted.md)、[statedb-spendable-sold-as-bank](statedb-spendable-sold-as-bank.md)。

## 一句话

看见 EVM 报了错或气费不够，就写成跨到 SDK 的那一笔已经撤回；或把领奖转出写成可领已经清零。

## 正确写法

「跨模块预编译必须对失败与写入同一原子。领奖转出不是可领已经清零。更低 gas 不是已经更安全。」
