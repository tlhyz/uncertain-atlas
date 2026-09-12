# 先给退款削减起名（name-the-refund-cut）

> 类型：design pattern  
> 对读：不变量 223；C227；反模式 [`../anti-patterns/refund-cut-sold-as-gone.md`](../anti-patterns/refund-cut-sold-as-gone.md)；[`../../tracks/implementation/worked-example-refund-vs-gone.md`](../../tracks/implementation/worked-example-refund-vs-gone.md)。

设计或讲解「退款削减所以已经没有退款」时，先分开四个名字：

1. **退款削减** — 清零退款仍在，但更薄，不是已经没有退款。
2. **去掉自毁退款** — 自毁不再加退款计数，不是已经改了自毁语义。
3. **执行后结算** — 退款在整笔跑完才结，不是已经能在某一帧里花。
4. **3529** — 削减退款，不是 2200 本身，也不是 6780，也不是 1559。

四句对照：

- 看见的是削薄，还是已经取消？
- 看见的是自毁不再退气，还是自毁已经只转余额？
- 看见的是退款计数，还是执行当中已经能花？
- 这是 3529，还是已经是 2200 / 160 / 158？

不要和基础费≠小费（不变量 158）、后来自毁≠已删（不变量 160）、瞬时存储≠持久存储（不变量 159）糊成「退款已经齐了」一句。
