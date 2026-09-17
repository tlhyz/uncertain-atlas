# 反模式：txid 被写成已经含见证

> 真值：[txid ≠ wtxid](../../tracks/implementation/worked-example-txid-vs-wtxid.md)、[不变式 152](../invariants/README.md)、[不变式 144](../invariants/README.md)。亲戚：[policy-sold-as-consensus](policy-sold-as-consensus.md)、[blob-fee-sold-as-gas](blob-fee-sold-as-gas.md)。

## 一句话

看见一个交易哈希或块头 Merkle 绿了，就把 txid 写成已经含见证，或把 wtxid 写成已经等于 txid，或把头上的交易 Merkle 写成已经承诺见证根。

## 正确写法

「txid 不是 wtxid。改见证不是已经改交易身份。头上的 txid Merkle 不是已经承诺 wtxid。旧节点看见 txid 不是已经验过见证。」
