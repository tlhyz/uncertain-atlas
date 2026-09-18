# 模式：点名 del89-notblind 杠

**层次**：应用 / BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事（289 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-89](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-del89-notblind-vs-bundled.md`](../tracks/implementation/worked-example-del89-notblind-vs-bundled.md)。

- **这一输入的微调 不是已经能扫整棵钱包：** 看见这一输入的微调，不是已经能扫整棵钱包 interchangeable / 1141 del89-notblind interchangeable。
- **看见能签 不是已经是盲签：** 看见能签，不是已经是盲签 interchangeable。
- **看见签过了 不是已经交差：** 看见签过了，不是已经核过找零 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看这一输入的微调 正式三事（289 余量），先数清问的是是不是已经能扫整棵钱包、是不是已经是盲签、还是看见签过了是不是已经交差，再决定要不要同一次发布。289 delegation vs xpub bundled unbundling 在本页 item 3 完成。
