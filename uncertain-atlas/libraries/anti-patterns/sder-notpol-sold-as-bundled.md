# 反模式：把 BIP-66 relay-der not already consensus-der / not already 144 / not already 171 正式三事（172 余量） 写成已经 共识已经要 / 已经是不变量 144 / 已经是不变量 171

**层次**：实现 / BIP-66 relay-der not already consensus-der / not already 144 / not already 171 正式三事（172 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki)（Strict DER signatures）。  
**对应**：[`../tracks/implementation/worked-example-sder-notpol-vs-bundled.md`](../tracks/implementation/worked-example-sder-notpol-vs-bundled.md)。

把 BIP-66 relay-der not already consensus-der / not already 144 / not already 171 正式三事（172 余量） 写成已经 共识已经要 / 已经是不变量 144 / 已经是不变量 171，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-66 strict-DER 正式三事（172 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 172 / 144 / 171 / 1548 / 1549 糊成一句。

也不是：

- [sder-notmath-sold-as-bundled](sder-notmath-sold-as-bundled.md) 是 notmath 单句边界（1548），不是本页边界。
- [sder-notlib-sold-as-bundled](sder-notlib-sold-as-bundled.md) 是 notlib 单句边界（1549），不是本页边界。
- [vb9-notlock-sold-as-bundled](vb9-notlock-sold-as-bundled.md) 是 BIP-9 版本位边界（171/1545），不是本页 BIP-66 编码边界。
