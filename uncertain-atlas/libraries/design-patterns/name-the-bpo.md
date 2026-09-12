# 先给只改 blob 参数的专用分叉起名（name-the-bpo）

> 类型：design pattern  
> 对读：不变量 209；C213；反模式 [`../anti-patterns/bpo-sold-as-hardfork.md`](../anti-patterns/bpo-sold-as-hardfork.md)；[`../../tracks/light-clients/worked-example-bpo-vs-hardfork.md`](../../tracks/light-clients/worked-example-bpo-vs-hardfork.md)。

设计或讲解「blob 容量还能再加」时，先分开四个名字：

1. **只改 blob 的专用分叉** — 只动目标 / 上限 / 调价分母，不是已经改了执行规则。
2. **配置里的日程** — 参数写在节点配置，不是已经不需要分叉。
3. **摘要掺进上限** — 对等层域分离跟着当前上限走，不是已经换了分叉版本号。
4. **7892** — 改参数的专用机制，不是 7691 常规抬日程，也不是 PeerDAS。

四句对照：

- 看见的是只改 blob 参数，还是执行规则已经改了？
- 看见的是配置里的日程，还是已经不需要分叉？
- 看见的是摘要掺进上限，还是版本号已经换了？
- 这是 7892，还是已经是 200 / 201 / 23？

不要和抬高日程≠已改气种（不变量 200）、底价≠已并账（不变量 201）、短时 DA（不变量 23）糊成「blob 又能加了」一句。
