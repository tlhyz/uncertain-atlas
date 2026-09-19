# 模式：点名 cl65-notfld 杠

**层次**：实现 / BIP-65 script-cltv not already nlocktime-locked / not already 165 / not already 164-bundled 正式三事（164 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应**：[`../tracks/state-models/worked-example-cl65-notfld-vs-bundled.md`](../tracks/state-models/worked-example-cl65-notfld-vs-bundled.md)。

- **脚本里的CLTV不是交易nLockTime已经把输出锁到那时 不是已经把输出锁住：看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时，不是已经把输出锁住 interchangeable / 1530 cl65-notfld interchangeable。**
- **script CLTV is not already an output locked by nLockTime 不是已经是不变量 165：看见script CLTV is not already an output locked by nLockTime，不是已经是不变量 165 interchangeable / 1530 cl65-notfld interchangeable。**
- **脚本里的CLTV不是交易nLockTime已经把输出锁到那时 不是已经 164 bundled：看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时，不是已经 164 bundled interchangeable / 1530 cl65-notfld interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 CLTV 正式三事（164 余量），必须分开 not already nlocktime-locked、not already present-unspendable、not already wall-clock 三件事。
