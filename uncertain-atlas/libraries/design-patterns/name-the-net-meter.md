# 先给净计量起名（name-the-net-meter）

> 类型：design pattern  
> 对读：不变量 225；C229；反模式 [`../anti-patterns/net-meter-sold-as-transient.md`](../anti-patterns/net-meter-sold-as-transient.md)；[`../../tracks/implementation/worked-example-net-meter-vs-transient.md`](../../tracks/implementation/worked-example-net-meter-vs-transient.md)。

设计或讲解「净计量所以已经是瞬时存储」时，先分开四个名字：

1. **净计量** — 按原来值 / 当前值 / 新值计价，不是已经是瞬时存储。
2. **原来值** — 这一笔开始时槽上的值，不是已经是当前值，也不是已经是新值。
3. **津贴帧禁写** — 剩余气不够则写存储失败，不是已经能在转账津贴里改槽。
4. **2200** — 净计量，不是 1153，也不是 3529，也不是 2929，也不是 1283 那道洞。

四句对照：

- 看见的是三值计价，还是已经另开瞬时店？
- 看见的是原来值，还是已经只有当前值和新值？
- 看见的是津贴帧禁写，还是已经能在转账津贴里改槽？
- 这是 2200，还是已经是 1153 / 159 / 3529 / 223？

不要和瞬时存储≠持久存储（不变量 159）、退款削减≠已没有退款（不变量 223）、本笔第一次碰≠已经热（不变量 169）糊成「存储计价已经齐了」一句。
