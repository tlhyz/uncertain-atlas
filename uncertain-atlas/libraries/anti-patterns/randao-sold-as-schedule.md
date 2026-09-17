# 把 RANDAO 种子已知写成已经锁死出块日程（randao-sold-as-schedule）

> 类型：anti-pattern  
> 对读：不变量 205；C209；模式 [`../design-patterns/name-the-proposer-lookahead.md`](../design-patterns/name-the-proposer-lookahead.md)；[`../../tracks/consensus/worked-example-lookahead-vs-randao.md`](../../tracks/consensus/worked-example-lookahead-vs-randao.md)。

## 坏句

- 「下一纪元的 RANDAO 种子已经知道，出块人就已经锁死。」
- 「有效余额还会变，但种子已知就已经排完。」
- 「信标状态里有前瞻名单，就已经是 based 预确认。」
- 「有了前瞻名单，就已经是秘密领袖选举 / 执行层已经能用。」
- 「7917 就是 4399 / 已经是 7251。」

## 为什么坏

[EIP-7917](https://eips.ethereum.org/EIPS/eip-7917) 官方页写的正是：种子提前齐，**不等于** N+1 纪元出块日程在 N 纪元已经能从状态完全预知，因为有效余额还能变。本页才把种子延迟和余额快照对齐。看见名单不是已经预确认，也不是已经秘密选举。4399 是执行层读 mix。7251 是上限。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 种子已知 | 日程仍可能因有效余额变 |
| 看见前瞻名单 | 预先算好并写进状态，不是预确认产品 |
| 字段在状态里 | 不是执行层已经接上，也不是 SSLE |
| 7917 | 不是 4399，不是 7251 |

相关反模式：[`prevrandao-sold-as-fair.md`](prevrandao-sold-as-fair.md)、[`consolidation-sold-as-done.md`](consolidation-sold-as-done.md)、[`builder-sold-as-consensus.md`](builder-sold-as-consensus.md)。
