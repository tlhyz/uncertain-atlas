# 反模式：把 BIP-34 block-version-bump not already bip9-bits / not already 171 / not already 172 正式三事（173 余量） 写成已经 已经按BIP-9激活 / 已经是不变量 171 / 已经是不变量 172

**层次**：实现 / BIP-34 block-version-bump not already bip9-bits / not already 171 / not already 172 正式三事（173 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki)（Block v2, Height in Coinbase）。  
**对应**：[`../tracks/implementation/worked-example-cbht-notv9-vs-bundled.md`](../tracks/implementation/worked-example-cbht-notv9-vs-bundled.md)。

把 BIP-34 block-version-bump not already bip9-bits / not already 171 / not already 172 正式三事（173 余量） 写成已经 已经按BIP-9激活 / 已经是不变量 171 / 已经是不变量 172，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-34 coinbase-height 正式三事（173 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 173 / 171 / 172 / 1542 / 1544 糊成一句。

也不是：

- [cbht-nothdr-sold-as-bundled](cbht-nothdr-sold-as-bundled.md) 是 nothdr 单句边界（1542），不是本页边界。
- [cbht-notmat-sold-as-bundled](cbht-notmat-sold-as-bundled.md) 是 notmat 单句边界（1544），不是本页边界。
- [b32m-notold-sold-as-bundled](b32m-notold-sold-as-bundled.md) 是 BIP-350 后继校验边界（181/1539），不是本页 BIP-34 高度边界。
