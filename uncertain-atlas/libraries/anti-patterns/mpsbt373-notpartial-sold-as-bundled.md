# 反模式：把 BIP-373 participant-key not already have-partial / not already bip340-sig / not already settled 正式三事（284 余量） 写成已经 已经有部分签 / 已经是 371 那种 Taproot 签 / 已经交差

**层次**：应用 / BIP-373 participant-key not already have-partial / not already bip340-sig / not already settled 正式三事（284 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)（Complete, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-mpsbt373-notpartial-vs-bundled.md`](../tracks/implementation/worked-example-mpsbt373-notpartial-vs-bundled.md)。

把 BIP-373 participant-key not already have-partial / not already bip340-sig / not already settled 正式三事（284 余量） 写成已经 已经有部分签 / 已经是 371 那种 Taproot 签 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看参与者钥 正式三事（284 余量），必须分开 not already have-partial、not already bip340-sig、not already settled 三件事，不要和 284 / 179 / 1157 / 1172 / 1173 糊成一句。

也不是：

- [mpsbt373-notout-sold-as-bundled](mpsbt373-notout-sold-as-bundled.md) 是聚合钥栏仍未是输出钥单句边界（1173 item 2），不是本页参与者钥仍未有部分签边界。
- [tap371-notold-sold-as-bundled](tap371-notold-sold-as-bundled.md) 是旧栏仍未装得下 Taproot 边界（279/1157），不是本页仍未有部分签边界。
