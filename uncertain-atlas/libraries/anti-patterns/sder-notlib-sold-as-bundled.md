# 反模式：把 BIP-66 library-accept not already consensus-accept / not already 3 / not already 152 正式三事（172 余量） 写成已经 共识已经接受 / 已经是不变量 3 / 已经是不变量 152

**层次**：实现 / BIP-66 library-accept not already consensus-accept / not already 3 / not already 152 正式三事（172 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki)（Strict DER signatures）。  
**对应**：[`../tracks/implementation/worked-example-sder-notlib-vs-bundled.md`](../tracks/implementation/worked-example-sder-notlib-vs-bundled.md)。

把 BIP-66 library-accept not already consensus-accept / not already 3 / not already 152 正式三事（172 余量） 写成已经 共识已经接受 / 已经是不变量 3 / 已经是不变量 152，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-66 strict-DER 正式三事（172 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 172 / 3 / 152 / 1548 / 1550 糊成一句。

也不是：

- [sder-notmath-sold-as-bundled](sder-notmath-sold-as-bundled.md) 是 notmath 单句边界（1548），不是本页边界。
- [sder-notpol-sold-as-bundled](sder-notpol-sold-as-bundled.md) 是 notpol 单句边界（1550），不是本页边界。
- [vb9-notlock-sold-as-bundled](vb9-notlock-sold-as-bundled.md) 是 BIP-9 版本位边界（171/1545），不是本页 BIP-66 编码边界。
