# 反模式：把 BIP-70 payment-request not already authorized / not already that-address / not already settled 正式三事（295 余量） 写成已经 已经授权 / 已经是那条地址 / 已经交差

**层次**：应用 / BIP-70 payment-request not already authorized / not already that-address / not already settled 正式三事（295 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/lifecycle/worked-example-pay70-notauth-vs-bundled.md`](../tracks/lifecycle/worked-example-pay70-notauth-vs-bundled.md)。

把 BIP-70 payment-request not already authorized / not already that-address / not already settled 正式三事（295 余量） 写成已经 已经授权 / 已经是那条地址 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看付款请求 正式三事（295 余量），必须分开 not already authorized、not already that-address、not already settled 三件事，不要和 295 / 255 / 55 / 1203 / 1204 糊成一句。

也不是：

- [lsig137-nothabit-sold-as-bundled](lsig137-nothabit-sold-as-bundled.md) 是旧习惯仍未互操作边界（294/1201），不是本页付款请求仍未授权边界。
- [pay70-notack-sold-as-bundled](pay70-notack-sold-as-bundled.md) 是付款报文仍未是回执单句边界（1203 item 2），不是本页付款请求仍未授权边界。
