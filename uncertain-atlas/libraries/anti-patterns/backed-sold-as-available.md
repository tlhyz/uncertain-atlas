# 反模式：backed 被写成已经可用或已经最终

> 真值：[backed ≠ available 工作实例](../../tracks/finality/worked-example-backed-vs-available.md)、[不变式 125](../invariants/README.md)。亲戚：[header-equals-settlement](header-equals-settlement.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)、[deprecated-api-sold-as-compat](deprecated-api-sold-as-compat.md)、[active-dispute-sold-as-confirmed](active-dispute-sold-as-confirmed.md)。

## 一句话

看见 collator 绿勾、中继头上的候选回执、或「已经 backed」，就写成平行块已经可用、已经审批、或已经 GRANDPA 最终。

## 正确写法

「Backed 是回执进了未最终的中继分叉，仍可能进不了平行链。可用、审批、GRANDPA 是后面三盏灯。回执不是 PoV。」
