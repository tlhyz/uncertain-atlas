# 模式：点名 mpsbt373-notold 杠

**层次**：应用 / BIP-373 old-psbt-fields not already can-hold-musig / not already can-finish-rounds / not already settled 正式三事（284 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)（Complete, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-mpsbt373-notold-vs-bundled.md`](../tracks/implementation/worked-example-mpsbt373-notold-vs-bundled.md)。

- **旧 PSBT 栏 不是已经能装 MuSig2：** 看见旧 PSBT 栏，不是已经能装 MuSig2 interchangeable / 1172 mpsbt373-notold interchangeable。
- **371 Taproot 栏 不是已经能走完多轮：** 看见 371 补了 Taproot 栏，不是已经能走完多轮 interchangeable / 1172 mpsbt373-notold interchangeable。
- **174 那套栏 不是已经交差：** 看见 174 那套栏，不是已经交差 interchangeable / 1172 mpsbt373-notold interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看旧栏 正式三事（284 余量），必须分开 not already can-hold-musig、not already can-finish-rounds、not already settled 三件事。
