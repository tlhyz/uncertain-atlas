# 反模式：把 BIP-341 scriptpath not already all-scripts-exposed / not already 189 / not already 152 正式三事（153 余量） 写成已经 已经揭开全部脚本 / 已经是不变量 189 / 已经是不变量 152

**层次**：实现 / BIP-341 scriptpath not already all-scripts-exposed / not already 189 / not already 152 正式三事（153 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)（Taproot: SegWit version 1 spending rules）。  
**对应**：[`../tracks/implementation/worked-example-kpsp-notall-vs-bundled.md`](../tracks/implementation/worked-example-kpsp-notall-vs-bundled.md)。

把 BIP-341 scriptpath not already all-scripts-exposed / not already 189 / not already 152 正式三事（153 余量） 写成已经 已经揭开全部脚本 / 已经是不变量 189 / 已经是不变量 152，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-341 keypath-scriptpath 正式三事（153 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 153 / 189 / 152 / 1554 / 1556 糊成一句。

也不是：

- [kpsp-notree-sold-as-bundled](kpsp-notree-sold-as-bundled.md) 是 notree 单句边界（1554），不是本页边界。
- [kpsp-notlook-sold-as-bundled](kpsp-notlook-sold-as-bundled.md) 是 notlook 单句边界（1556），不是本页边界。
- [twid-noteq-sold-as-bundled](twid-noteq-sold-as-bundled.md) 是 BIP-141 身份边界（152/1551），不是本页 BIP-341 花费路径边界。
