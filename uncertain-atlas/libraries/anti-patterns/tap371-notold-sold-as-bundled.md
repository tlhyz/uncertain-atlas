# 反模式：把 BIP-371 old-psbt-fields not already can-hold-taproot / not already can-sign-taproot / not already settled 正式三事（279 余量） 写成已经 已经能装 Taproot / 已经能签 / 已经交差

**层次**：应用 / BIP-371 old-psbt-fields not already can-hold-taproot / not already can-sign-taproot / not already settled 正式三事（279 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-tap371-notold-vs-bundled.md`](../tracks/implementation/worked-example-tap371-notold-vs-bundled.md)。

把 BIP-371 old-psbt-fields not already can-hold-taproot / not already can-sign-taproot / not already settled 正式三事（279 余量） 写成已经 已经能装 Taproot / 已经能签 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看旧 PSBT 栏 正式三事（279 余量），必须分开 not already can-hold-taproot、not already can-sign-taproot、not already settled 三件事，不要和 279 / 179 / 1136 / 1158 / 1159 糊成一句。

也不是：

- [ma387-notsort-sold-as-bundled](ma387-notsort-sold-as-bundled.md) 是 sortedmulti_a 仍未是 383 排序边界（278/1156），不是本页旧栏仍未装得下 Taproot 边界。
- [tap371-notinner-sold-as-bundled](tap371-notinner-sold-as-bundled.md) 是输出脚本钥仍未是内部钥单句边界（1158 item 2），不是本页旧栏边界。
