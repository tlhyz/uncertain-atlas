# 反模式：把 BIP-137 header-byte not already have-address / not already spendable-output / not already settled 正式三事（294 余量） 写成已经 已经有那条地址 / 已经能花 / 已经交差

**层次**：应用 / BIP-137 header-byte not already have-address / not already spendable-output / not already settled 正式三事（294 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-137](https://github.com/bitcoin/bips/blob/master/bip-0137.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/lifecycle/worked-example-lsig137-notaddr-vs-bundled.md`](../tracks/lifecycle/worked-example-lsig137-notaddr-vs-bundled.md)。

把 BIP-137 header-byte not already have-address / not already spendable-output / not already settled 正式三事（294 余量） 写成已经 已经有那条地址 / 已经能花 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字节标了地址种类 正式三事（294 余量），必须分开 not already have-address、not already spendable-output、not already settled 三件事，不要和 294 / 174 / 179 / 1199 / 1201 糊成一句。

也不是：

- [lsig137-not322-sold-as-bundled](lsig137-not322-sold-as-bundled.md) 是旧式签仍未是 322 单句边界（1199 item 1），不是本页头字节仍未是地址边界。
- [lsig137-nothabit-sold-as-bundled](lsig137-nothabit-sold-as-bundled.md) 是旧习惯仍未互操作单句边界（1201 item 3），不是本页头字节仍未是地址边界。
