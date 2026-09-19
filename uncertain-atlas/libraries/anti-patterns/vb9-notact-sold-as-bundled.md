# 反模式：把 BIP-9 locked-in not already active / not already 165 / not already 41 正式三事（171 余量） 写成已经 已经激活 / 已经是不变量 165 / 已经是不变量 41

**层次**：实现 / BIP-9 locked-in not already active / not already 165 / not already 41 正式三事（171 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)（Version bits with timeout and delay）。  
**对应**：[`../tracks/implementation/worked-example-vb9-notact-vs-bundled.md`](../tracks/implementation/worked-example-vb9-notact-vs-bundled.md)。

把 BIP-9 locked-in not already active / not already 165 / not already 41 正式三事（171 余量） 写成已经 已经激活 / 已经是不变量 165 / 已经是不变量 41，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-9 versionbits 正式三事（171 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 171 / 165 / 41 / 1545 / 1547 糊成一句。

也不是：

- [vb9-notlock-sold-as-bundled](vb9-notlock-sold-as-bundled.md) 是 notlock 单句边界（1545），不是本页边界。
- [vb9-notfail-sold-as-bundled](vb9-notfail-sold-as-bundled.md) 是 notfail 单句边界（1547），不是本页边界。
- [cbht-nothdr-sold-as-bundled](cbht-nothdr-sold-as-bundled.md) 是 BIP-34 高度边界（173/1542），不是本页 BIP-9 版本位边界。
