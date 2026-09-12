# 反模式：反序列化归一化被写成编码必须为零已经成立

> 真值：[Zcash ZIP 256](../../tracks/failure-museum/zcash-2026-valuebalance-normalized.md)、[不变式 105](../invariants/README.md)。亲戚：[noncanonical-accepted](noncanonical-accepted.md)、[model-equals-implementation](model-equals-implementation.md)、[circuit-impl-sold-as-statement](circuit-impl-sold-as-statement.md)。

## 一句话

看见「该字段必须为 0」的检查还在跑，或看见本地结构里已经是零，就写成规范编码已经是零、规则已经开火。

## 正确写法

「必须为零指编码。反序列化先改成零再检查，失败分支不可达。一家拒一家收不是多实现已经同根。」
