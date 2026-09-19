# 模式：点名 twid-notchg 杠

**层次**：实现 / BIP-141 change-witness not already change-txid / not already 144 / not already 12 正式三事（152 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)（Segregated Witness Consensus layer）。  
**对应**：[`../tracks/implementation/worked-example-twid-notchg-vs-bundled.md`](../tracks/implementation/worked-example-twid-notchg-vs-bundled.md)。

- **改见证不是已经改交易身份 不是已经改txid：看见改见证不是已经改交易身份，不是已经改txid interchangeable / 1552 twid-notchg interchangeable。**
- **changing the witness is not already changing the txid 不是已经是不变量 144：看见changing the witness is not already changing the txid，不是已经是不变量 144 interchangeable / 1552 twid-notchg interchangeable。**
- **改见证不是已经改交易身份 不是已经是不变量 12：看见改见证不是已经改交易身份，不是已经是不变量 12 interchangeable / 1552 twid-notchg interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-141 txid-wtxid 正式三事（152 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事。
