# 反模式：把 BIP-373 old-psbt-fields not already can-hold-musig / not already can-finish-rounds / not already settled 正式三事（284 余量） 写成已经 已经能装 MuSig2 / 已经能走完多轮 / 已经交差

**层次**：应用 / BIP-373 old-psbt-fields not already can-hold-musig / not already can-finish-rounds / not already settled 正式三事（284 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)（Complete, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-mpsbt373-notold-vs-bundled.md`](../tracks/implementation/worked-example-mpsbt373-notold-vs-bundled.md)。

把 BIP-373 old-psbt-fields not already can-hold-musig / not already can-finish-rounds / not already settled 正式三事（284 余量） 写成已经 已经能装 MuSig2 / 已经能走完多轮 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看旧栏 正式三事（284 余量），必须分开 not already can-hold-musig、not already can-finish-rounds、not already settled 三件事，不要和 284 / 1157 / 1169 / 1173 / 1174 糊成一句。

也不是：

- [musig328-nottweak-sold-as-bundled](musig328-nottweak-sold-as-bundled.md) 是子钥仍未能不带微调去签边界（283/1171），不是本页旧栏仍未装得下 MuSig2 边界。
- [mpsbt373-notout-sold-as-bundled](mpsbt373-notout-sold-as-bundled.md) 是聚合钥栏仍未是输出钥单句边界（1173 item 2），不是本页旧栏边界。
