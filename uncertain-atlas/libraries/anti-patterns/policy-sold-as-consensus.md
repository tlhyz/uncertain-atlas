# 反模式：策略拒绝被写成共识非法

> 真值：[策略 ≠ 共识工作实例](../../tracks/mempool/worked-example-policy-vs-consensus.md)、[不变式 144](../invariants/README.md)、[不变式 44](../invariants/README.md)。亲戚：[flood-sold-as-halt](flood-sold-as-halt.md)、[durable-nonce-sold-as-consumed](durable-nonce-sold-as-consumed.md)。

## 一句话

看见邻居不转发或看见钱包写「失败」，就把策略拒绝写成共识非法，或把费率高写成更正确，或把策略写成已经检查过块内交易。

## 正确写法

「策略是共识之外、只管未确认交易进本节点 mempool 之前的本地规则。策略拒绝不是共识非法。策略通过不是已经进块。费率高不是更正确。策略不作用于块内交易。」
