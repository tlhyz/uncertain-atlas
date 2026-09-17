# 先给激活流失帽起名（name-the-activation-churn）

> 类型：design pattern  
> 对读：不变量 215；C219；反模式 [`../anti-patterns/churn-sold-as-rewards.md`](../anti-patterns/churn-sold-as-rewards.md)；[`../../tracks/economic/worked-example-activation-churn-vs-rewards.md`](../../tracks/economic/worked-example-activation-churn-vs-rewards.md)。

设计或讲解「质押涨太快所以奖励已经改了」时，先分开四个名字：

1. **激活流失帽** — 每纪元最多能激活多少把的上沿，不是已经改了奖励曲线。
2. **入口帽** — 只约束激活队列，不是已经是出口帽。
3. **推迟里程碑** — 总质押占比到关键点更慢，不是已经改了发奖公式。
4. **7514** — 给激活流失加顶，不是 7251，也不是不变量 196。

四句对照：

- 看见的是激活帽，还是已经改了奖励曲线？
- 看见的是入口帽，还是已经是出口帽？
- 看见的是推迟里程碑，还是已经改了发奖公式？
- 这是 7514，还是已经是 7251 / 196？

不要和抬高上限≠取消最低激活额（不变量 196）、执行层退出≠已退出（不变量 193）、预签退出≠已永远有效（不变量 213）糊成「质押已经改完」一句。
