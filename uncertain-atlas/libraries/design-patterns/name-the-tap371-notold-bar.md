# 模式：点名 tap371-notold 杠

**层次**：应用 / BIP-371 old-psbt-fields not already can-hold-taproot / not already can-sign-taproot / not already settled 正式三事（279 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-tap371-notold-vs-bundled.md`](../tracks/implementation/worked-example-tap371-notold-vs-bundled.md)。

- **旧 PSBT 栏 不是已经能装 Taproot：** 看见旧 PSBT 栏，不是已经能装 Taproot interchangeable / 1157 tap371-notold interchangeable。
- **旧软件会忽略新栏 不是已经能签：** 看见旧软件会忽略新栏，不是已经能签 interchangeable / 1157 tap371-notold interchangeable。
- **包还在 不是已经交差：** 看见包还在，不是已经交差 interchangeable / 1157 tap371-notold interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看旧 PSBT 栏 正式三事（279 余量），必须分开 not already can-hold-taproot、not already can-sign-taproot、not already settled 三件事。
