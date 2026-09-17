# 反模式：Int/Dec 被写成位宽已对齐

> 真值：[ASA-2024-010](../../tracks/failure-museum/asa-2024-010.md)、[不变式 76](../invariants/README.md)。亲戚：[pool-overflow-sold-as-amount-only](pool-overflow-sold-as-amount-only.md)。

## 一句话

看见有 Int 也有 Dec，就写成上界已经同一把尺；或把数学库补丁一律写成必须硬分叉 / 一律写成不必协调。

## 正确写法

「会互转的数值类型必须对齐最大位宽。Dec 进 Int 不得 panic。是否硬分叉以该官方页为准：本条出处 1.3.0→1.4.0 可只改依赖；更低版本先协调升级。」
