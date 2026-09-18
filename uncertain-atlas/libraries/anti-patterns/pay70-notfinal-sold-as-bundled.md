# 反模式：把 BIP-70 ack not already final / not already confirmed / not already refunded 正式三事（295 余量） 写成已经 已经最终 / 已经确认 / 已经交差

**层次**：应用 / BIP-70 ack not already final / not already confirmed / not already refunded 正式三事（295 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/lifecycle/worked-example-pay70-notfinal-vs-bundled.md`](../tracks/lifecycle/worked-example-pay70-notfinal-vs-bundled.md)。

把 BIP-70 ack not already final / not already confirmed / not already refunded 正式三事（295 余量） 写成已经 已经最终 / 已经确认 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回执 正式三事（295 余量），必须分开 not already final、not already confirmed、not already refunded 三件事，不要和 295 / 255 / 294 / 1202 / 1203 糊成一句。

也不是：

- [pay70-notack-sold-as-bundled](pay70-notack-sold-as-bundled.md) 是付款报文仍未是回执单句边界（1203 item 2），不是本页回执仍未最终边界。
- [lsig137-nothabit-sold-as-bundled](lsig137-nothabit-sold-as-bundled.md) 是旧习惯仍未互操作边界（294/1201），不是本页回执仍未最终边界。
