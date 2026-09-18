# 反模式：把 BIP-321 required-param not already payable / not already confirmed / not already settled 正式三事（255 余量） 写成已经 已经能付 / 已经确认 / 已经交差

**层次**：生命周期 / BIP-321 required-param not already payable / not already confirmed / not already settled 正式三事（255 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-321](https://github.com/bitcoin/bips/blob/master/bip-0321.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/lifecycle/worked-example-uri321-notreq-vs-bundled.md`](../tracks/lifecycle/worked-example-uri321-notreq-vs-bundled.md)。

把 BIP-321 required-param not already payable / not already confirmed / not already settled 正式三事（255 余量） 写成已经 已经能付 / 已经确认 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不认识的必选参数 正式三事（255 余量），必须分开 not already payable、not already confirmed、not already settled 三件事，不要和 255 / 181 / 55 / 1211 / 1212 糊成一句。

也不是：

- [uri321-notempty-sold-as-bundled](uri321-notempty-sold-as-bundled.md) 是路径空仍未没有指示单句边界（1212 item 2），不是本页必选参数仍未能付边界。
- [p2sh13-notwho-sold-as-bundled](p2sh13-notwho-sold-as-bundled.md) 是只有地址仍未知道付给谁边界（297/1210），不是本页必选参数仍未能付边界。
