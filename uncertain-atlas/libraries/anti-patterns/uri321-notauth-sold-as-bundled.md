# 反模式：把 BIP-321 uri not already authorized / not already paid / not already settled 正式三事（255 余量） 写成已经 已经授权 / 已经付了 / 已经交差

**层次**：生命周期 / BIP-321 uri not already authorized / not already paid / not already settled 正式三事（255 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-321](https://github.com/bitcoin/bips/blob/master/bip-0321.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/lifecycle/worked-example-uri321-notauth-vs-bundled.md`](../tracks/lifecycle/worked-example-uri321-notauth-vs-bundled.md)。

把 BIP-321 uri not already authorized / not already paid / not already settled 正式三事（255 余量） 写成已经 已经授权 / 已经付了 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看付款 URI 正式三事（255 余量），必须分开 not already authorized、not already paid、not already settled 三件事，不要和 255 / 55 / 290 / 1212 / 1213 糊成一句。

也不是：

- [p2sh13-notwho-sold-as-bundled](p2sh13-notwho-sold-as-bundled.md) 是只有地址仍未知道付给谁边界（297/1210），不是本页付款 URI 仍未授权边界。
- [uri321-notempty-sold-as-bundled](uri321-notempty-sold-as-bundled.md) 是路径空仍未没有指示单句边界（1212 item 2），不是本页付款 URI 仍未授权边界。
- [pj78-noturi-sold-as-bundled](pj78-noturi-sold-as-bundled.md) 是 pj= 仍未是 payjoin 付款边界（290/1184），不是本页付款 URI 仍未授权边界。
