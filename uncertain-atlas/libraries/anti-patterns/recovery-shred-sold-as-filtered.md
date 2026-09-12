# 反模式：恢复 shred 被写成已经按父槽滤掉

> 真值：[Solana 2023-02-25](../../tracks/failure-museum/solana-2023-02-25-turbine-recovery.md)、[不变式 87](../invariants/README.md)。亲戚：[part-index-sold-as-proof-index](part-index-sold-as-proof-index.md)、[announce-sold-as-received](announce-sold-as-received.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)。

## 一句话

看见数据 shred 能按父槽丢掉，或看见「我们有去重 / 有 Turbine 过滤」，就写成恢复碎片也被滤了、转发服务不会把它们送回树里；或把 vote-only 写成已经停链。

## 正确写法

「恢复对象与数据对象字段不同，必须各自写过滤。坐在过滤前面的转发是另一信任对象。vote-only / 落到后备补洞不是高度已停，也不是已最终经济交易被回滚。不要抄 400 槽或 66%。」
