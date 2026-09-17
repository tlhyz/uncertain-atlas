# 反模式：脚本里的 CLTV 被写成交易 nLockTime 已经把输出锁住

> 真值：[CLTV ≠ nLockTime 已锁](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)、[不变式 164](../invariants/README.md)、[不变式 41](../invariants/README.md)。亲戚：[coinbase-sold-as-spendable](coinbase-sold-as-spendable.md)。

## 一句话

看见交易填了 nLockTime 或脚本写了 CHECKLOCKTIMEVERIFY，就把输出写成已经锁到那时，或把 CLTV 写成已经在跟墙上现在比，或把输入 final 写成时间锁已经生效。

## 正确写法

「脚本里的 CLTV 不是交易 nLockTime 已经把输出锁到那时。nLockTime 能证明将来能花，不是已经证明现在不能花。CLTV 比的是花费交易的 nLockTime，不是墙上现在。输入已经 final 不是 CLTV 已经在生效。」
