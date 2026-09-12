# 反模式：空账户被写成已经从状态里消失

> 真值：[空 ≠ 已消失](../../tracks/state-models/worked-example-empty-vs-dead.md)、[不变式 180](../invariants/README.md)、[不变式 103](../invariants/README.md)、[不变式 160](../invariants/README.md)。亲戚：[oog-sold-as-reverted](oog-sold-as-reverted.md)、[selfdestruct-sold-as-deleted](selfdestruct-sold-as-deleted.md)、[code-sender-sold-as-eoa](code-sender-sold-as-eoa.md)。

## 一句话

看见「空账户」，就把它写成状态里已经没有这个地址，或把死写成一种对象，或把规范 EIP-161 写成不变量 161 或 103。

## 正确写法

「空不是已经不存在。死是不存在或空，不是已经一种对象。碰到（含零值转账）不是已经付过钱。交易结束时空了不是已经是 103 那次漏撤。规范 EIP-161 不是不变量 161。」
