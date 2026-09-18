# 反模式：把 BIP-352 silent-address not already output / not already paid / not already settled 正式三事（260 余量） 写成已经 已经有一笔链上输出 / 已经是旧见证地址 / 已经交差

**层次**：应用 / BIP-352 silent-address not already output / not already paid / not already settled 正式三事（260 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/lifecycle/worked-example-sil352-notout-vs-bundled.md`](../tracks/lifecycle/worked-example-sil352-notout-vs-bundled.md)。

把 BIP-352 silent-address not already output / not already paid / not already settled 正式三事（260 余量） 写成已经 已经有一笔链上输出 / 已经是旧见证地址 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看静默付款地址 正式三事（260 余量），必须分开 not already output、not already paid、not already settled 三件事，不要和 260 / 174 / 255 / 1218 / 1219 糊成一句。

也不是：

- [sig322-notfund-sold-as-bundled](sig322-notfund-sold-as-bundled.md) 是清单仍未齐边界（258/1216），不是本页静默码仍未有输出边界。
- [sil352-notscan-sold-as-bundled](sil352-notscan-sold-as-bundled.md) 是扫过仍未收到单句边界（1218 item 2），不是本页静默码仍未有输出边界。
- [uri321-notauth-sold-as-bundled](uri321-notauth-sold-as-bundled.md) 是付款 URI 仍未授权边界（255/1211），不是本页静默码仍未有输出边界。
