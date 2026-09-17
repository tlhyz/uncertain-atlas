# 反模式：因余额不足取消被写成已经不再扣款

> 真值：[Sui 2026-05 气费砸币](../../tracks/failure-museum/sui-2026-05-gas-smash-cancel.md)、[不变式 92](../invariants/README.md)。亲戚：[zero-cost-sold-as-safe](zero-cost-sold-as-safe.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)、[dkg-disabled-sold-as-persisted](dkg-disabled-sold-as-persisted.md)。

## 一句话

看见交易被标成 `InsufficientFundsForWithdraw` 取消，或看见星期四已经修了，就写成钱已经不再被扣、下溢已经消失。

## 正确写法

「取消只取消用户意图。hybrid gas 若仍对取消路径砸币，钱还在被花。一种取消理由盖住另一种，临时补丁当没写过。不要抄 1.72。不要写怎样竞态。」
