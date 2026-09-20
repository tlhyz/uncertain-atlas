# 反模式：把 BIP-65 cltv-compares-nlocktime not already wall-clock / not already 41 / not already 165 正式三事（164 余量） 写成已经 已经在跟墙上现在比 / 已经是不变量 41 / 已经是不变量 165

**层次**：实现 / BIP-65 cltv-compares-nlocktime not already wall-clock / not already 41 / not already 165 正式三事（164 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应**：[`../tracks/state-models/worked-example-cl65-notclk-vs-bundled.md`](../tracks/state-models/worked-example-cl65-notclk-vs-bundled.md)。

把 BIP-65 cltv-compares-nlocktime not already wall-clock / not already 41 / not already 165 正式三事（164 余量） 写成已经 已经在跟墙上现在比 / 已经是不变量 41 / 已经是不变量 165，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 CLTV 正式三事（164 余量），必须分开 not already nlocktime-locked、not already present-unspendable、not already wall-clock 三件事，不要和 164 / 41 / 165 / 1530 / 1531 糊成一句。

也不是：

- [cl65-notfld-sold-as-bundled](cl65-notfld-sold-as-bundled.md) 是 notfld 单句边界（1530），不是本页边界。
- [cl65-notnow-sold-as-bundled](cl65-notnow-sold-as-bundled.md) 是 notnow 单句边界（1531），不是本页边界。
- [csvd-notseq-sold-as-bundled](csvd-notseq-sold-as-bundled.md) 是 BIP-112 CSV 边界（165/1527），不是本页 CLTV 边界。
