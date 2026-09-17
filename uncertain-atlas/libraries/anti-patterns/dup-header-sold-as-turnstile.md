# 反模式：重复头复位跟踪被写成闸门还在转

> 真值：[Zcash ZIP 256](../../tracks/failure-museum/zcash-2026-zip209-header-reset.md)、[不变式 104](../invariants/README.md)。亲戚：[proof-ok-equals-no-inflation](proof-ok-equals-no-inflation.md)、[circuit-impl-sold-as-statement](circuit-impl-sold-as-statement.md)、[half-written-state](half-written-state.md)。

## 一句话

看见规范写着 ZIP 209 / 「池不得变负」，或看见闸门模块还在目录里，就写成跟踪字段被重复头清掉之后闸门仍在执行。

## 正确写法

「闸门吃的是跟踪状态。跟踪被静默复位不是闸门还在转。规范段落还在不是实现字段还活着。」
