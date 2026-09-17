# 反模式：瞬时存储被写成已经进了账户

> 真值：[瞬时 ≠ 持久](../../tracks/state-models/worked-example-transient-vs-storage.md)、[不变式 159](../invariants/README.md)、[不变式 103](../invariants/README.md)。亲戚：[oog-sold-as-reverted](oog-sold-as-reverted.md)、[nested-ics20-sold-as-outer-state](nested-ics20-sold-as-outer-state.md)。

## 一句话

看见合约写了 `TSTORE` 或本笔稍后还能读到，就把瞬时店写成已经进了账户，或把交易结束丢掉写成本笔里从未存在，或把同合约共用一份店写成 memory。

## 正确写法

「瞬时存储不是账户持久存储。本笔结束丢掉不是本笔里从未存在。同合约各帧共用一份不是 memory。帧回滚不是已经落盘。」
