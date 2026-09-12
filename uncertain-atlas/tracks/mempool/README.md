# 横向：内存池

课：L9.2、L3.2、L5.4。  
精读：[`worked-example.md`](worked-example.md)（筐里有信 ≠ 局长盖章）；[`worked-example-who-orders.md`](worked-example-who-orders.md)（签了头 ≠ 自己排了序；Builder API ≠ 信标共识）；[`worked-example-orphan-resolution.md`](worked-example-orphan-resolution.md)（父交易进池后扫孤儿必须可中断）；[`worked-example-policy-vs-consensus.md`](worked-example-policy-vs-consensus.md)（策略拒绝 ≠ 共识非法；费率高 ≠ 更正确；策略不作用于块内交易；不变量 144）；[`worked-example-basefee-vs-tip.md`](worked-example-basefee-vs-tip.md)（基础费 ≠ 小费；烧掉 ≠ 已经给了出块者；弹性块大小 ≠ 整套费用市场已经齐；烧掉 ≠ MEV 已经解决；不变量 158）。Aptos 批次传播 ≠ 已经排序：[`../consensus/worked-example-quorum-store-vs-order.md`](../consensus/worked-example-quorum-store-vs-order.md)（不变量 132）。  
ABCI 四门（CheckTx ≠ Prepare）：[`../consensus/worked-example-prepare-process.md`](../consensus/worked-example-prepare-process.md)。  
单笔 CheckTx 绿 ≠ 整包可提案：[ASA-2024-002](../failure-museum/asa-2024-002.md)。  
外层交易上限 ≠ 内层解码已有界：[ASA-2024-0012 / 0013](../failure-museum/asa-2024-0012.md)。
