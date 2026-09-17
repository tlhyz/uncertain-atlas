# 反模式：委员会 DACert 被写成数据已经贴上父链

> 真值：[DACert ≠ 已贴文工作实例](../../tracks/light-clients/worked-example-dacert-vs-posted.md)、[不变式 142](../invariants/README.md)、[不变式 23](../invariants/README.md)。亲戚：[kzg-sold-as-das](kzg-sold-as-das.md)、[nmt-sold-as-square-available](nmt-sold-as-square-available.md)、[unsafe-sold-as-derived](unsafe-sold-as-derived.md)。

## 一句话

看见「也是 Arbitrum」或看见父链 Inbox 有一笔，就把 AnyTrust 的 DACert 写成批次全文已经在以太坊，或写成和 Rollup DA / Celestia DAS 同一把尺子。

## 正确写法

「DACert 是哈希 + 过期 + 委员会签，不是全文已经贴上父链。AnyTrust 不是已经 Rollup DA。凑不齐签回退贴全文是另一条路。委员会诚实假设不是纠删抽样。」
