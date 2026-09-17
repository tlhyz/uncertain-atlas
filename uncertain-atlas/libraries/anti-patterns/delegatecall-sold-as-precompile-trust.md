# 反模式：正确兑现的 DELEGATECALL 语义被写成预编译信任模型已经跟着改过

> 真值：[Avalanche 2025 delegatecall](../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md)、[不变式 119](../invariants/README.md)。亲戚：[precompile-oog-sold-as-reverted](precompile-oog-sold-as-reverted.md)、[nested-ics20-sold-as-outer-state](nested-ics20-sold-as-outer-state.md)、[preserve-origin-sold-as-bound](preserve-origin-sold-as-bound.md)。

## 一句话

看见执行库按规范兑现了 `DELEGATECALL` / `CALLCODE`，或看见已经热修 / 硬升级，就写成有状态预编译的调用者授权已经同步。

## 正确写法

「特权预编译必须写清授权看的是 EVM 语义调用者还是原始调用者。正确兑现字节码语义不是旧假设已经更新。」
