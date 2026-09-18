# 反模式：把 BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事（289 余量） 写成已经 已经能扫整棵钱包 / 已经是盲签 / 已经交差

**层次**：应用 / BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事（289 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-89](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-del89-notblind-vs-bundled.md`](../tracks/implementation/worked-example-del89-notblind-vs-bundled.md)。

把 BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事（289 余量） 写成已经 已经能扫整棵钱包 / 已经是盲签 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看这一输入的微调 正式三事（289 余量），必须分开 not already whole-tree、not already blind-sign、not already settled 三件事，不要和 289 / 280 / 287 / 1139 / 1140 糊成一句。

也不是：

- [del89-nottree-sold-as-bundled](del89-nottree-sold-as-bundled.md) 是委托方非扩展钥仍未能推出整棵钱包单句边界（1140 item 2），不是本页这一输入微调仍未是盲签边界。
- 登记过就已经批准这笔花是不变量 280，不是本页能签仍未是盲签边界。
