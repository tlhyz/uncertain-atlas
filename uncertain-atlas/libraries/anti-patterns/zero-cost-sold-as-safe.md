# 反模式：估值为 0 被写成已经便宜所以安全

> 真值：[Sui 2024-11-21](../../tracks/failure-museum/sui-2024-11-21-zero-cost-assert.md)、[不变式 90](../invariants/README.md)。亲戚：[assert-sold-as-peer-filter](assert-sold-as-peer-filter.md)、[endblocker-error-sold-as-skippable](endblocker-error-sold-as-skippable.md)。

## 一句话

看见拥塞控制估出来的执行代价为 0，或看见「我们有共享对象限速」，就写成交易已经安全、assert 只是局部跳过。

## 正确写法

「估值为 0 必须当合法边角。估值失败必须拒或排队，不得 assert 崩进程。owned 快路径绿了不是共享路径已安全。」
