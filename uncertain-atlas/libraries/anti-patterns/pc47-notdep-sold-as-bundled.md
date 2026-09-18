# 反模式：把 BIP-47 payment-code not already deposit / not already paid / not already settled 正式三事（273 余量） 写成已经 已经是存款地址 / 已经付过 / 已经交差

**层次**：应用 / BIP-47 payment-code not already deposit / not already paid / not already settled 正式三事（273 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki)（Deployed, Applications）。  
**对应**：[`../tracks/lifecycle/worked-example-pc47-notdep-vs-bundled.md`](../tracks/lifecycle/worked-example-pc47-notdep-vs-bundled.md)。

把 BIP-47 payment-code not already deposit / not already paid / not already settled 正式三事（273 余量） 写成已经 已经是存款地址 / 已经付过 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看付款码 正式三事（273 余量），必须分开 not already deposit、not already paid、not already settled 三件事，不要和 273 / 260 / 255 / 1224 / 1225 糊成一句。

也不是：

- [dns353-notcache-sold-as-bundled](dns353-notcache-sold-as-bundled.md) 是缓存仍未当前 URI 边界（261/1222），不是本页付款码仍未是存款地址边界。
- [pc47-notnote-sold-as-bundled](pc47-notnote-sold-as-bundled.md) 是通知仍未是付款单句边界（1224 item 2），不是本页付款码仍未是存款地址边界。
- [sil352-notout-sold-as-bundled](sil352-notout-sold-as-bundled.md) 是静默码仍未有输出边界（260/1217），不是本页付款码仍未是存款地址边界。
