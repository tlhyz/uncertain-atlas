# 反模式：父信标根被写成当前头

> 真值：[父根 ≠ 当前头](../../tracks/light-clients/worked-example-parent-root-vs-head.md)、[不变式 156](../invariants/README.md)、[不变式 127](../invariants/README.md)。亲戚：[withdrawal-sold-as-tx](withdrawal-sold-as-tx.md)、[processed-sold-as-head](processed-sold-as-head.md)。

## 一句话

看见执行头多了一个信标根或合约读到一个根，就把父信标根写成当前信标头，或把合约里的根写成已经 finalized，或把环缓冲写成永存。

## 正确写法

「头里的父信标根不是当前信标头。合约里读到的根不是已经 finalized。环缓冲过期不是根已经永久可查。」
