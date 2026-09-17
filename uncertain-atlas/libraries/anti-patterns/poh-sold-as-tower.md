# 反模式：PoH 槽钟被写成已经投票或已经 root

> 真值：[PoH ≠ Tower 工作实例](../../tracks/consensus/worked-example-poh-vs-tower.md)、[不变式 133](../invariants/README.md)。亲戚：[justified-sold-as-finalized](justified-sold-as-finalized.md)、[babe-sold-as-grandpa](babe-sold-as-grandpa.md)、[slot-sold-as-block-id](slot-sold-as-block-id.md)、[timeout-commit-sold-as-finality](timeout-commit-sold-as-finality.md)。

## 一句话

看见槽号往前走或 RPC `confirmed`，就把 PoH 逻辑钟写成已经 BFT，或把超多数票写成已经最大 lockout / 已经 root。

## 正确写法

「PoH / 槽是逻辑钟。账本票才是 lockout 承诺。`processed` 仍可切叉。`confirmed` 是超多数直接投票，比 `finalized` 弱。交易 finalized 当块成为 root。」
