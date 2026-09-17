# 反模式：默认块上限被写成第一轮活性 SLA

> 真值：[ASA-2023-002](../../tracks/failure-museum/asa-2023-002.md)、[不变式 63](../invariants/README.md)、[超时精读](../../tracks/consensus/worked-example-timeouts.md)。亲戚：[evidence-default-sold-as-unbonding](evidence-default-sold-as-unbonding.md)。

## 一句话

看见仓库里有 `BlockParams.MaxBytes` 默认值，就写成这个大小下第一轮一定能过；或把 `timeout_propose` 和块上限当成互不相关的两个旋钮。

## 正确写法

「默认 MaxBytes 对常见用例可能偏大。上限必须按传播与第一轮参与重算。timeout_propose 必须对照该上限。超限块必须拒。」
