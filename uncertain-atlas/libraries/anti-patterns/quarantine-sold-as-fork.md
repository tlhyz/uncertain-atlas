# 反模式：检查点隔离拒证被写成已经分叉

> 真值：[Sui 2026-01-14](../../tracks/failure-museum/sui-2026-01-14-commit-divergence.md)、[不变式 91](../invariants/README.md)。亲戚：[halt-sold-as-one-kind](halt-sold-as-one-kind.md)、[header-equals-settlement](header-equals-settlement.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)。

## 一句话

看见超过 ⅓ 签了另一检查点摘要、或看见 RPC 还能读，就写成已经分叉、或写成链还在结算。

## 正确写法

「隔离区拒证、进度停住，是为了不最终不一致。读上一份已认证状态不是新交易已执行。不要把 ⅓ 抄进不确定法定人数。」
