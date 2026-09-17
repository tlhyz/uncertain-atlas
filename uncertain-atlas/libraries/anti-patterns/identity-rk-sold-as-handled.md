# 反模式：规范允许身份 rk 被写成验证明已经能吃

> 真值：[Zcash ZIP 256](../../tracks/failure-museum/zcash-2026-identity-rk-panic.md)、[不变式 107](../invariants/README.md)。亲戚：[circuit-impl-sold-as-statement](circuit-impl-sold-as-statement.md)、[zero-cost-sold-as-safe](zero-cost-sold-as-safe.md)、[enable-height-sold-as-safe](enable-height-sold-as-safe.md)。

## 一句话

看见规范允许 `rk` 为零点，或看见电路支持向量 `(0,0)`，就写成公开输入转换已经能吃、进程不会退出。

## 正确写法

「允许集里的点，转换必须覆盖或入口显式拒。电路支持不是门口已经能吃。排除零点是收紧，不是陈述本来就禁止。」
