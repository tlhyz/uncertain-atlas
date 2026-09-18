# 模式：点名 musig328-nottweak 杠

**层次**：应用 / BIP-328 child-key not already sign-without-tweak / not already x-only-tweak / not already settled 正式三事（283 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-328](https://github.com/bitcoin/bips/blob/master/bip-0328.mediawiki)（Complete, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-musig328-nottweak-vs-bundled.md`](../tracks/implementation/worked-example-musig328-nottweak-vs-bundled.md)。

- **子钥 不是已经能不带微调去签：** 看见派生出的子钥，不是已经能不带微调去签 interchangeable / 1171 musig328-nottweak interchangeable。
- **写了微调 不是已经是 x-only 那种微调：** 看见写了微调，不是已经是 x-only 那种微调 interchangeable / 1171 musig328-nottweak interchangeable。
- **一次签名会话 不是已经交差：** 看见一次签名会话，不是已经交差 interchangeable / 1171 musig328-nottweak interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看子钥签名 正式三事（283 余量），必须分开 not already sign-without-tweak、not already x-only-tweak、not already settled 三件事。
