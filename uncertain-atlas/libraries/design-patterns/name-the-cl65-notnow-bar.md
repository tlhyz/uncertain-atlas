# 模式：点名 cl65-notnow 杠

**层次**：实现 / BIP-65 nlocktime-future-spend not already present-unspendable / not already 163 / not already 41 正式三事（164 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应**：[`../tracks/state-models/worked-example-cl65-notnow-vs-bundled.md`](../tracks/state-models/worked-example-cl65-notnow-vs-bundled.md)。

- **nLockTime能证明将来能花不是已经证明现在不能花 不是已经证明现在不能花：看见nLockTime能证明将来能花不是已经证明现在不能花，不是已经证明现在不能花 interchangeable / 1531 cl65-notnow interchangeable。**
- **nLockTime proving a future spend is not already proving it cannot be spent now 不是已经是不变量 163：看见nLockTime proving a future spend is not already proving it cannot be spent now，不是已经是不变量 163 interchangeable / 1531 cl65-notnow interchangeable。**
- **nLockTime能证明将来能花不是已经证明现在不能花 不是已经是不变量 41：看见nLockTime能证明将来能花不是已经证明现在不能花，不是已经是不变量 41 interchangeable / 1531 cl65-notnow interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 CLTV 正式三事（164 余量），必须分开 not already nlocktime-locked、not already present-unspendable、not already wall-clock 三件事。
