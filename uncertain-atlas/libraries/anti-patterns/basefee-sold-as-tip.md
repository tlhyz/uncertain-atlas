# 反模式：基础费被写成已经给了出块者

> 真值：[基础费 ≠ 小费](../../tracks/mempool/worked-example-basefee-vs-tip.md)、[不变式 158](../invariants/README.md)、[不变式 145](../invariants/README.md)。亲戚：[blob-fee-sold-as-gas](blob-fee-sold-as-gas.md)、[policy-sold-as-consensus](policy-sold-as-consensus.md)。

## 一句话

看见钱包写基础费或块偶尔比目标大，就把烧掉的网络费写成已经给了出块者，或把弹性写成整套费用市场已经齐，或把烧掉写成 MEV 已经解决。

## 正确写法

「基础费不是小费。烧掉不是已经给了出块者。弹性块大小不是整套费用市场已经齐。烧掉不是 MEV 已经解决。」
