# 先给对等节点历史窗起名（name-the-history-window）

> 类型：design pattern  
> 对读：不变量 207；C211；反模式 [`../anti-patterns/window-sold-as-consensus.md`](../anti-patterns/window-sold-as-consensus.md)；[`../../tracks/network/worked-example-history-window-vs-consensus.md`](../../tracks/network/worked-example-history-window-vs-consensus.md)。

设计或讲解「历史可以过期了」时，先分开四个名字：

1. **历史窗宣布** — 这个对等节点还服务哪一段，不是共识已经删历史。
2. **线上无布隆** — 线协议收据不再带可现算字段，不是共识收据编码已经改。
3. **握手无总难度** — 合并后该字段没意义，不是已经能判断同步完没完。
4. **7642** — 新版线协议，不是硬分叉，不是 blob 服务窗，也不是 assumevalid。

四句对照：

- 看见的是对等节点还服哪一段，还是共识已经删历史？
- 看见的是线上收据，还是共识收据编码？
- 看见的是握手不再报总难度，还是已经判断同步完没完？
- 这是 7642，还是已经是 23 / 25 / 195 / 硬分叉？

不要和短时 DA（不变量 23）、[`skip-sold-as-full-verify.md`](../anti-patterns/skip-sold-as-full-verify.md) 对读的跳过须点名（不变量 25）、历史哈希≠BLOCKHASH（不变量 195）糊成「历史没了」一句。
