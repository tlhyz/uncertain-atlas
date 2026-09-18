# 反模式：把 BIP-44 next-account-number not already has-history / not already same-identity / not already settled 正式三事（267 余量） 写成已经 已经有过往 / 已经和上一户同一身份 / 已经交差

**层次**：应用 / BIP-44 next-account-number not already has-history / not already same-identity / not already settled 正式三事（267 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)（Deployed, Applications）。  
**对应**：[`../tracks/implementation/worked-example-acc44-notpast-vs-bundled.md`](../tracks/implementation/worked-example-acc44-notpast-vs-bundled.md)。

把 BIP-44 next-account-number not already has-history / not already same-identity / not already settled 正式三事（267 余量） 写成已经 已经有过往 / 已经和上一户同一身份 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看下一个账户号 正式三事（267 余量），必须分开 not already has-history、not already same-identity、not already settled 三件事，不要和 267 / 266 / 1115 / 1117 糊成一句。

也不是：

- [acc44-notcoin-sold-as-bundled](acc44-notcoin-sold-as-bundled.md) 是同一份种子仍未是同一条币单句边界（1115 item 1），不是本页账户号仍未有过往边界。
- BIP32 compatible 就已经能互操作是不变量 266，不是本页两户仍未是同一身份边界。
