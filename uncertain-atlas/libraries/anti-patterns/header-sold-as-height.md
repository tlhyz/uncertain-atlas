# 反模式：看见块头被写成高度已经在头上

> 真值：[高度 ≠ 已在头上](../../tracks/implementation/worked-example-coinbase-height-vs-header.md)、[不变式 173](../invariants/README.md)、[不变式 163](../invariants/README.md)、[不变式 171](../invariants/README.md)。亲戚：[coinbase-sold-as-spendable](coinbase-sold-as-spendable.md)、[bit-sold-as-active](bit-sold-as-active.md)、[slot-sold-as-block-id](slot-sold-as-block-id.md)。

## 一句话

看见块头或块 version 加大，就把高度写成已经在头上，或把 34 写成 9 位向量，或把 coinbase 写了高度写成已经能花。

## 正确写法

「coinbase 第一项写了高度不是头上已经有高度字段。块 version 加大不是已经按 BIP-9 位向量激活。写了高度不是 coinbase 已经能花。BIP-34 不是 BIP-9，也不是 BIP-66 那条新规则。」
