# 模式：点名 mpsbt373-notout 杠

**层次**：应用 / BIP-373 aggregate-key-field not already tap-output-key / not already x-only-or-internal / not already settled 正式三事（284 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)（Complete, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-mpsbt373-notout-vs-bundled.md`](../tracks/implementation/worked-example-mpsbt373-notout-vs-bundled.md)。

- **聚合钥栏 不是已经是输出钥：** 看见聚合钥栏，不是已经是 Taproot 输出钥 interchangeable / 1173 mpsbt373-notout interchangeable。
- **压缩 不是已经是 371 那种 x-only：** 看见压缩，不是已经是 371 那种 x-only interchangeable / 1173 mpsbt373-notout interchangeable。
- **栏里有聚合钥 不是已经交差：** 看见栏里有聚合钥，不是已经交差 interchangeable / 1173 mpsbt373-notout interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看聚合钥栏 正式三事（284 余量），必须分开 not already tap-output-key、not already x-only-or-internal、not already settled 三件事。
