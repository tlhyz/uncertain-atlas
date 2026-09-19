# 反模式：把 BIP-173 checksum-pass not already program-on-chain / not already 170 / not already 152 正式三事（174 余量） 写成已经 已经在链上 / 已经是不变量 170 / 已经是不变量 152

**层次**：实现 / BIP-173 checksum-pass not already program-on-chain / not already 170 / not already 152 正式三事（174 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki)（Bech32 address format）。  
**对应**：[`../tracks/implementation/worked-example-adut-notchk-vs-bundled.md`](../tracks/implementation/worked-example-adut-notchk-vs-bundled.md)。

把 BIP-173 checksum-pass not already program-on-chain / not already 170 / not already 152 正式三事（174 余量） 写成已经 已经在链上 / 已经是不变量 170 / 已经是不变量 152，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-173 Bech32 正式三事（174 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 174 / 170 / 152 / 1536 / 1538 糊成一句。

也不是：

- [adut-notout-sold-as-bundled](adut-notout-sold-as-bundled.md) 是 notout 单句边界（1536），不是本页边界。
- [adut-notpay-sold-as-bundled](adut-notpay-sold-as-bundled.md) 是 notpay 单句边界（1538），不是本页边界。
- [phsh-notrev-sold-as-bundled](phsh-notrev-sold-as-bundled.md) 是 BIP-16 哈希承诺边界（170/1533），不是本页 BIP-173 地址串边界。
