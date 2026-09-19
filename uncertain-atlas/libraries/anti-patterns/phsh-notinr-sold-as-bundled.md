# 反模式：把 BIP-16 hash-match not already inner-verified / not already 152 / not already 297 正式三事（170 余量） 写成已经 已经验过内层 / 已经是不变量 152 / 已经是不变量 297

**层次**：实现 / BIP-16 hash-match not already inner-verified / not already 152 / not already 297 正式三事（170 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki)（Pay to Script Hash）。  
**对应**：[`../tracks/state-models/worked-example-phsh-notinr-vs-bundled.md`](../tracks/state-models/worked-example-phsh-notinr-vs-bundled.md)。

把 BIP-16 hash-match not already inner-verified / not already 152 / not already 297 正式三事（170 余量） 写成已经 已经验过内层 / 已经是不变量 152 / 已经是不变量 297，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-16 P2SH 正式三事（170 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 170 / 152 / 297 / 1533 / 1534 糊成一句。

也不是：

- [phsh-notrev-sold-as-bundled](phsh-notrev-sold-as-bundled.md) 是 notrev 单句边界（1533），不是本页边界。
- [phsh-notrun-sold-as-bundled](phsh-notrun-sold-as-bundled.md) 是 notrun 单句边界（1534），不是本页边界。
- [p2sh13-not16-sold-as-bundled](p2sh13-not16-sold-as-bundled.md) 是 BIP-13 地址边界（297/1208），不是本页 BIP-16 哈希承诺边界。
