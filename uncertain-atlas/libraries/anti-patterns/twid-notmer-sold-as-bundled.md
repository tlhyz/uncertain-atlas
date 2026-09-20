# 反模式：把 BIP-141 header-txid-merkle not already wtxid-commit / not already 145 / not already 174 正式三事（152 余量） 写成已经 已经承诺wtxid / 已经是不变量 145 / 已经是不变量 174

**层次**：实现 / BIP-141 header-txid-merkle not already wtxid-commit / not already 145 / not already 174 正式三事（152 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)（Segregated Witness Consensus layer）。  
**对应**：[`../tracks/implementation/worked-example-twid-notmer-vs-bundled.md`](../tracks/implementation/worked-example-twid-notmer-vs-bundled.md)。

把 BIP-141 header-txid-merkle not already wtxid-commit / not already 145 / not already 174 正式三事（152 余量） 写成已经 已经承诺wtxid / 已经是不变量 145 / 已经是不变量 174，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-141 txid-wtxid 正式三事（152 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 152 / 145 / 174 / 1551 / 1552 糊成一句。

也不是：

- [twid-noteq-sold-as-bundled](twid-noteq-sold-as-bundled.md) 是 noteq 单句边界（1551），不是本页边界。
- [twid-notchg-sold-as-bundled](twid-notchg-sold-as-bundled.md) 是 notchg 单句边界（1552），不是本页边界。
- [sder-notmath-sold-as-bundled](sder-notmath-sold-as-bundled.md) 是 BIP-66 编码边界（172/1548），不是本页 BIP-141 身份边界。
