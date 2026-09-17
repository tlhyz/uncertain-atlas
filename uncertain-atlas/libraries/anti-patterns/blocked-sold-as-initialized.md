# 反模式：被挡地址被写成模块账户已初始化

> 真值：[ASA-2024-003](../../tracks/failure-museum/asa-2024-003.md)、[不变式 75](../invariants/README.md)。亲戚：[endblocker-error-sold-as-skippable](endblocker-error-sold-as-skippable.md)。

## 一句话

看见地址被标 blocked，就写成不能往上面挂归属 / 授权 / 代付；或把「并不常见」写成创世可以不初始化模块账户。

## 正确写法

「被挡住的模块账户必须先初始化。未初始化户口在 Begin/EndBlock 被 GetModuleAccount 叫到可以停链。vesting / authz / feegrant 是同一面。」
