# 反模式：验根通过被写成外层下标已对齐

> 真值：[ASA-2025-002](../../tracks/failure-museum/asa-2025-002.md)、[不变式 59](../invariants/README.md)、[拼块精读](../../tracks/network/worked-example-compact-block.md)。

## 一句话

看见分片带 Merkle 证明且根对得上，就写成「这就是第 i 片」；或把错配的一片标成已收到，挡住正确片再来。

## 正确写法

「外层下标必须等于证明下标。对不上必须拒，不得标已收到，不得再流言。验根只说明某片属于这个提案。」
