# 反模式：信标提款被写成用户交易

> 真值：[提款操作 ≠ 用户交易](../../tracks/economic/worked-example-withdrawal-vs-tx.md)、[不变式 154](../invariants/README.md)、[不变式 149](../invariants/README.md)。亲戚：[processed-sold-as-head](processed-sold-as-head.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)。

## 一句话

看见执行载荷里多了一笔到账或信标链已经出队，就把提款操作写成用户交易，或把出队写成执行账户已经加钱，或把无 gas 写成已经跑过 EVM。

## 正确写法

「提款操作不是用户交易。信标链出队不是执行账户已经加钱。无 gas / 不得失败不是已经跑过 EVM。」
