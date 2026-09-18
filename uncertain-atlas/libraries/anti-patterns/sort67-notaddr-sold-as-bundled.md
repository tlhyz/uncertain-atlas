# 反模式：把 BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事（270 余量） 写成已经 已经是同一条赎回脚本 / 已经是同一条 P2SH 地址 / 已经交差

**层次**：应用 / BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事（270 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-67](https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/implementation/worked-example-sort67-notaddr-vs-bundled.md`](../tracks/implementation/worked-example-sort67-notaddr-vs-bundled.md)。

把 BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事（270 余量） 写成已经 已经是同一条赎回脚本 / 已经是同一条 P2SH 地址 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一套钥 正式三事（270 余量），必须分开 not already same-redeem、not already same-p2sh、not already settled 三件事，不要和 270 / 170 / 1129 / 1134 / 1135 糊成一句。

也不是：

- [cos45-notdone-sold-as-bundled](cos45-notdone-sold-as-bundled.md) 是前面分支没有交易仍未发现完边界（271/1132），不是本页同一套钥仍未是同一条赎回边界。
- 付给脚本哈希就已经揭开赎回是不变量 170，不是本页门限一样仍未是同一条地址边界。
