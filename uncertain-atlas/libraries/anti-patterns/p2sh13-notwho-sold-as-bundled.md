# 反模式：把 BIP-13 address-only not already know-payee / not already identity / not already settled 正式三事（297 余量） 写成已经 已经知道付给谁 / 已经核过收款人 / 已经交差

**层次**：应用 / BIP-13 address-only not already know-payee / not already identity / not already settled 正式三事（297 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-13](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-p2sh13-notwho-vs-bundled.md`](../tracks/implementation/worked-example-p2sh13-notwho-vs-bundled.md)。

把 BIP-13 address-only not already know-payee / not already identity / not already settled 正式三事（297 余量） 写成已经 已经知道付给谁 / 已经核过收款人 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只有本页这种地址 正式三事（297 余量），必须分开 not already know-payee、not already identity、not already settled 三件事，不要和 297 / 270 / 170 / 1208 / 1209 糊成一句。

也不是：

- [p2sh13-notpaid-sold-as-bundled](p2sh13-notpaid-sold-as-bundled.md) 是旧软件报无效仍未付过单句边界（1209 item 2），不是本页只有地址仍未知道付给谁边界。
- [enc38-notfrag-sold-as-bundled](enc38-notfrag-sold-as-bundled.md) 是地址片段仍未是地址边界（296/1207），不是本页只有地址仍未知道付给谁边界。
