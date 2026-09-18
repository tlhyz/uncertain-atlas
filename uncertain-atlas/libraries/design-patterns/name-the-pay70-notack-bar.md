# 模式：点名 pay70-notack 杠

**层次**：应用 / BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事（295 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/lifecycle/worked-example-pay70-notack-vs-bundled.md`](../tracks/lifecycle/worked-example-pay70-notack-vs-bundled.md)。

- **付款报文 不是已经是回执：** 看见付款报文，不是已经是回执 interchangeable / 1203 pay70-notack interchangeable。
- **里面有签过的交易 不是商家已经收下：** 看见里面有签过的交易，不是商家已经收下 interchangeable / 1203 pay70-notack interchangeable。
- **送到了付款网址 不是已经交差：** 看见送到了付款网址，不是已经交差 interchangeable / 1203 pay70-notack interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看付款报文 正式三事（295 余量），必须分开 not already ack、not already merchant-accepted、not already settled 三件事。
