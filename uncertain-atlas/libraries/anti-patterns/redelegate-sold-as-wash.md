# 反模式：再委托被写成待执行罚没的洗白

> 真值：[ASA-2024-005](../../tracks/failure-museum/asa-2024-005.md)、[不变式 72](../invariants/README.md)、[证据精读](../../tracks/economic/worked-example-evidence.md)。亲戚：[evidence-default-sold-as-unbonding](evidence-default-sold-as-unbonding.md)。

## 一句话

看见委托已经再挂到别人名下，就写成待执行的罚没追不到；或把「验证者还没被 slash」写成委托人已经干净。

## 正确写法

「待执行罚没必须跟着过错当时的质押走。再委托改的是现在的挂钩，不是过去的责任。」
