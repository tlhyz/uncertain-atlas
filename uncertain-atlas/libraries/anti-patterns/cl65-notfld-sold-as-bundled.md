# 反模式：把 BIP-65 script-cltv not already nlocktime-locked / not already 165 / not already 164-bundled 正式三事（164 余量） 写成已经 已经把输出锁住 / 已经是不变量 165 / 已经 164 bundled

**层次**：实现 / BIP-65 script-cltv not already nlocktime-locked / not already 165 / not already 164-bundled 正式三事（164 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应**：[`../tracks/state-models/worked-example-cl65-notfld-vs-bundled.md`](../tracks/state-models/worked-example-cl65-notfld-vs-bundled.md)。

把 BIP-65 script-cltv not already nlocktime-locked / not already 165 / not already 164-bundled 正式三事（164 余量） 写成已经 已经把输出锁住 / 已经是不变量 165 / 已经 164 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 CLTV 正式三事（164 余量），必须分开 not already nlocktime-locked、not already present-unspendable、not already wall-clock 三件事，不要和 164 / 165 / 163 / 1531 / 1532 糊成一句。

也不是：

- [cl65-notnow-sold-as-bundled](cl65-notnow-sold-as-bundled.md) 是 notnow 单句边界（1531），不是本页边界。
- [cl65-notclk-sold-as-bundled](cl65-notclk-sold-as-bundled.md) 是 notclk 单句边界（1532），不是本页边界。
- [csvd-notseq-sold-as-bundled](csvd-notseq-sold-as-bundled.md) 是 BIP-112 CSV 边界（165/1527），不是本页 CLTV 边界。
