# 反模式：coinbase 正屏蔽余额被写成重启能起来

> 真值：[Zcash ZIP 256](../../tracks/failure-museum/zcash-2026-coinbase-balance-crash.md)、[不变式 109](../invariants/README.md)。亲戚：[pool-overflow-sold-as-amount-only](pool-overflow-sold-as-amount-only.md)、[half-written-state](half-written-state.md)、[dup-header-sold-as-turnstile](dup-header-sold-as-turnstile.md)。

## 一句话

看见 `ConnectBlock` 发现供给与池对不上，或看见官方说合法集没变，就写成节点会拒块、重启还能同步。

## 正确写法

「两本账对不上必须拒并停在上一高度。中止再开机再中止是活性崩溃循环，不是合法集已改，也不是原子高度。」
