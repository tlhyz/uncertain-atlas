# 模式：点名 cl65-notclk 杠

**层次**：实现 / BIP-65 cltv-compares-nlocktime not already wall-clock / not already 41 / not already 165 正式三事（164 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应**：[`../tracks/state-models/worked-example-cl65-notclk-vs-bundled.md`](../tracks/state-models/worked-example-cl65-notclk-vs-bundled.md)。

- **CLTV比的是花费交易的nLockTime不是墙上现在 不是已经在跟墙上现在比：看见CLTV比的是花费交易的nLockTime不是墙上现在，不是已经在跟墙上现在比 interchangeable / 1532 cl65-notclk interchangeable。**
- **CLTV comparing against nLockTime is not already comparing against wall-clock now 不是已经是不变量 41：看见CLTV comparing against nLockTime is not already comparing against wall-clock now，不是已经是不变量 41 interchangeable / 1532 cl65-notclk interchangeable。**
- **CLTV比的是花费交易的nLockTime不是墙上现在 不是已经是不变量 165：看见CLTV比的是花费交易的nLockTime不是墙上现在，不是已经是不变量 165 interchangeable / 1532 cl65-notclk interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 CLTV 正式三事（164 余量），必须分开 not already nlocktime-locked、not already present-unspendable、not already wall-clock 三件事。
