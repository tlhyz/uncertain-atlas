# 反模式：奖励池溢出被写成只是金额算错

> 真值：[ISA-2025-005](../../tracks/failure-museum/isa-2025-005.md)、[不变式 74](../invariants/README.md)。亲戚：[halt-msg-sold-as-halt](halt-msg-sold-as-halt.md)。

## 一句话

看见分配 / 奖励池整数溢出，就写成「金额非法、拒掉即可」；或假装能向该池存款的验证者不是活性对手。

## 正确写法

「模块奖励池入金溢出必须拒，不得变成停链。能向该池存款的验证者是活性对手。」
