# 先给出块人前瞻起名（name-the-proposer-lookahead）

> 类型：design pattern  
> 对读：不变量 205；C209；反模式 [`../anti-patterns/randao-sold-as-schedule.md`](../anti-patterns/randao-sold-as-schedule.md)；[`../../tracks/consensus/worked-example-lookahead-vs-randao.md`](../../tracks/consensus/worked-example-lookahead-vs-randao.md)。

设计或讲解「出块人提前看得见了」时，先分开四个名字：

1. **RANDAO 种子已知** — 选人随机输入提前齐，不是已经锁死下一纪元出块人。
2. **有效余额仍可变** — 本纪元里活跃者的余额还能动，不是种子已知就已经排完。
3. **前瞻名单** — 信标状态里预先算好的出块人下标，不是已经是 based 预确认，也不是已经是秘密领袖选举。
4. **7917** — 把种子延迟和余额快照对齐，不是 4399，也不是 7251。

四句对照：

- 看见的是种子已知，还是日程已经锁死？
- 看见的是余额还能变，还是已经排完？
- 看见的是前瞻名单，还是已经预确认 / 已经秘密选举？
- 这是 7917，还是已经是 4399 / 7251？

不要和 [`name-the-randao.md`](name-the-randao.md)（mix ≠ 无偏骰子）、[`name-the-consolidation.md`](name-the-consolidation.md)（上限 ≠ 最低激活额）、谁排序（不变量 27）糊成「链上随机已经排好班」一句。
