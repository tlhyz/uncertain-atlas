# 反模式：本头 AppHash 被写成本高度交易已经交差

> 真值：[本头 AppHash ≠ 本块已交差](../../tracks/consensus/worked-example-apphash-vs-this-block.md)、[不变式 147](../invariants/README.md)、[不变式 136](../invariants/README.md)。亲戚：[order-sold-as-state](order-sold-as-state.md)、[statesync-sold-as-genesis](statesync-sold-as-genesis.md)。

## 一句话

看见头上有 `AppHash` 或看见本块 `DataHash` 里有一笔，就把本头根写成本高度已经入账，或把 `FinalizeBlock` 刚回的根写成已经印在本头上。

## 正确写法

「本头 AppHash 是上一块执行并提交之后的应用根，不是本高度交易已经交差。本块 DataHash 是交易目录，不是效果已经进本头。本高度 Finalize 回的根进下一块头。」
