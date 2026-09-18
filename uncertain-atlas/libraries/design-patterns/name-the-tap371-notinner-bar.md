# 模式：点名 tap371-notinner 杠

**层次**：应用 / BIP-371 output-script-key not already internal-key / not already same-key / not already settled 正式三事（279 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-tap371-notinner-vs-bundled.md`](../tracks/implementation/worked-example-tap371-notinner-vs-bundled.md)。

- **输出脚本里的钥 不是已经是内部钥：** 看见输出脚本里的钥，不是已经是内部钥 interchangeable / 1158 tap371-notinner interchangeable。
- **钥匙路径签 不是已经不必再给内部钥：** 看见钥匙路径签，不是已经不必再给内部钥 interchangeable / 1158 tap371-notinner interchangeable。
- **341 微调建议 不是已经交差：** 看见 341 建议用钥对自己的哈希做微调，不是已经交差 interchangeable / 1158 tap371-notinner interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看内部钥 正式三事（279 余量），必须分开 not already internal-key、not already same-key、not already settled 三件事。
