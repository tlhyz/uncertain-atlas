# 反模式：把 BIP-173 bech32-string not already on-chain-utxo / not already 181 / not already 174-bundled 正式三事（174 余量） 写成已经 已经有这笔输出 / 已经是不变量 181 / 已经 174 bundled

**层次**：实现 / BIP-173 bech32-string not already on-chain-utxo / not already 181 / not already 174-bundled 正式三事（174 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki)（Bech32 address format）。  
**对应**：[`../tracks/implementation/worked-example-adut-notout-vs-bundled.md`](../tracks/implementation/worked-example-adut-notout-vs-bundled.md)。

把 BIP-173 bech32-string not already on-chain-utxo / not already 181 / not already 174-bundled 正式三事（174 余量） 写成已经 已经有这笔输出 / 已经是不变量 181 / 已经 174 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-173 Bech32 正式三事（174 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 174 / 181 / 170 / 1537 / 1538 糊成一句。

也不是：

- [adut-notchk-sold-as-bundled](adut-notchk-sold-as-bundled.md) 是 notchk 单句边界（1537），不是本页边界。
- [adut-notpay-sold-as-bundled](adut-notpay-sold-as-bundled.md) 是 notpay 单句边界（1538），不是本页边界。
- [phsh-notrev-sold-as-bundled](phsh-notrev-sold-as-bundled.md) 是 BIP-16 哈希承诺边界（170/1533），不是本页 BIP-173 地址串边界。
