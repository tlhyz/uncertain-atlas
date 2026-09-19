# 反模式：把 BIP-173 encoded-program not already paid / not already 179 / not already 181 正式三事（174 余量） 写成已经 已经付过款 / 已经是不变量 179 / 已经是不变量 181

**层次**：实现 / BIP-173 encoded-program not already paid / not already 179 / not already 181 正式三事（174 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki)（Bech32 address format）。  
**对应**：[`../tracks/implementation/worked-example-adut-notpay-vs-bundled.md`](../tracks/implementation/worked-example-adut-notpay-vs-bundled.md)。

把 BIP-173 encoded-program not already paid / not already 179 / not already 181 正式三事（174 余量） 写成已经 已经付过款 / 已经是不变量 179 / 已经是不变量 181，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-173 Bech32 正式三事（174 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 174 / 179 / 181 / 1536 / 1537 糊成一句。

也不是：

- [adut-notout-sold-as-bundled](adut-notout-sold-as-bundled.md) 是 notout 单句边界（1536），不是本页边界。
- [adut-notchk-sold-as-bundled](adut-notchk-sold-as-bundled.md) 是 notchk 单句边界（1537），不是本页边界。
- [phsh-notrev-sold-as-bundled](phsh-notrev-sold-as-bundled.md) 是 BIP-16 哈希承诺边界（170/1533），不是本页 BIP-173 地址串边界。
