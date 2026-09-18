# 反模式：把 BIP-133 bloom-and not already fee-pass / not already exact-min / not already policy-off 正式三事（245 余量） 写成已经 已经过了费率门 / 已经是本节点精确的最低费率 / 已经关掉全部策略

**层次**：内存池 / BIP-133 bloom-and not already fee-pass / not already exact-min / not already policy-off 正式三事（245 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/mempool/worked-example-fee133-notbloom-vs-bundled.md`](../tracks/mempool/worked-example-fee133-notbloom-vs-bundled.md)。

把 BIP-133 bloom-and not already fee-pass / not already exact-min / not already policy-off 正式三事（245 余量） 写成已经 已经过了费率门 / 已经是本节点精确的最低费率 / 已经关掉全部策略，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看费率过滤器 正式三事（245 余量），必须分开 not already rejected、not already must、not already fee-pass 三件事，不要和 245 / 44 / 166 / 1238 / 1239 糊成一句。

也不是：

- [fee133-notpool-sold-as-bundled](fee133-notpool-sold-as-bundled.md) 是 notpool 单句边界（1238），不是本页边界。
- [fee133-notmust-sold-as-bundled](fee133-notmust-sold-as-bundled.md) 是 notmust 单句边界（1239），不是本页边界。
- [hdr130-notswitch-sold-as-bundled](hdr130-notswitch-sold-as-bundled.md) 是 BIP-130 发了 sendheaders 仍未改通告边界（247/1235），不是本页费率过滤器边界。
