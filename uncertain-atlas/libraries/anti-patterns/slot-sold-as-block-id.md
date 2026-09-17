# 反模式：槽号被写成块身份

> 真值：[Solana 2020-12-04](../../tracks/failure-museum/solana-2020-12-04-slot-as-block-id.md)、[不变式 94](../invariants/README.md)。亲戚：[confirmed-dup-sold-as-parent](confirmed-dup-sold-as-parent.md)、[announce-sold-as-received](announce-sold-as-received.md)、[recovery-shred-sold-as-filtered](recovery-shred-sold-as-filtered.md)。

## 一句话

看见同槽已经有一块、或看见 Turbine 对这个下标传过一次，就写成对面拿到的是同一块、分区已经能互修。

## 正确写法

「块与银行主键是内容哈希。槽号只当索引。同槽两份不同块必须能像不同槽的分叉一样修。乐观确认不是已经 rooted。」
