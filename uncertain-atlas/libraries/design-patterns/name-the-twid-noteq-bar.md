# 模式：点名 twid-noteq 杠

**层次**：实现 / BIP-141 txid not already wtxid / not already 248 / not already 152-bundled 正式三事（152 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)（Segregated Witness Consensus layer）。  
**对应**：[`../tracks/implementation/worked-example-twid-noteq-vs-bundled.md`](../tracks/implementation/worked-example-twid-noteq-vs-bundled.md)。

- **txid不是wtxid 不是已经是wtxid：看见txid不是wtxid，不是已经是wtxid interchangeable / 1551 twid-noteq interchangeable。**
- **txid is not already wtxid 不是已经是不变量 248：看见txid is not already wtxid，不是已经是不变量 248 interchangeable / 1551 twid-noteq interchangeable。**
- **txid不是wtxid 不是已经 152 bundled：看见txid不是wtxid，不是已经 152 bundled interchangeable / 1551 twid-noteq interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-141 txid-wtxid 正式三事（152 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事。
