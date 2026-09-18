# 反模式：把 BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事（295 余量） 写成已经 已经是回执 / 已经商家收下 / 已经交差

**层次**：应用 / BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事（295 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/lifecycle/worked-example-pay70-notack-vs-bundled.md`](../tracks/lifecycle/worked-example-pay70-notack-vs-bundled.md)。

把 BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事（295 余量） 写成已经 已经是回执 / 已经商家收下 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看付款报文 正式三事（295 余量），必须分开 not already ack、not already merchant-accepted、not already settled 三件事，不要和 295 / 290 / 174 / 1202 / 1204 糊成一句。

也不是：

- [pay70-notauth-sold-as-bundled](pay70-notauth-sold-as-bundled.md) 是付款请求仍未授权单句边界（1202 item 1），不是本页付款报文仍未是回执边界。
- [pay70-notfinal-sold-as-bundled](pay70-notfinal-sold-as-bundled.md) 是回执仍未最终单句边界（1204 item 3），不是本页付款报文仍未是回执边界。
