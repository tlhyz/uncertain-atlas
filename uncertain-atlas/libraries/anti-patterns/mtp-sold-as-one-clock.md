# 反模式：MTP、太新窗、locktime 被写成一把钟

> 真值：[MTP 精读](../../tracks/consensus/worked-example-mtp.md)、[BIP 113](https://github.com/bitcoin/bips/blob/master/bip-0113.mediawiki)、[不变式 41](../invariants/README.md#41-mtp-的两份工作必须与太新窗分开)。

## 一句话

看见 Bitcoin 头上有时间，就写「MTP」，不指出：太早看父块中位、BIP113 之后 locktime 也看父 MTP、太新看本节点钟。

## 正确写法

| 尺子 | 能说的句子 |
|------|------------|
| 太早 | 「新块 nTime 必须严格大于父块 GetMedianTimePast；否则 time-too-old」 |
| locktime | 「CSV 之后 IsFinalTx 用父 MTP，不用本块 nTime」 |
| 太新 | 「相对本节点钟的宽限；拒绝码是 TIME_FUTURE，注释承认钟可能坏」 |
