# 反模式：把 BIP-133 permission not already must / not already sending / not already obeying 正式三事（245 余量） 写成已经 对等节点已经照做 / 已经在发 / 已经必须滤

**层次**：内存池 / BIP-133 permission not already must / not already sending / not already obeying 正式三事（245 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/mempool/worked-example-fee133-notmust-vs-bundled.md`](../tracks/mempool/worked-example-fee133-notmust-vs-bundled.md)。

把 BIP-133 permission not already must / not already sending / not already obeying 正式三事（245 余量） 写成已经 对等节点已经照做 / 已经在发 / 已经必须滤，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看费率过滤器 正式三事（245 余量），必须分开 not already rejected、not already must、not already fee-pass 三件事，不要和 245 / 247 / 144 / 1238 / 1240 糊成一句。

也不是：

- [fee133-notpool-sold-as-bundled](fee133-notpool-sold-as-bundled.md) 是 notpool 单句边界（1238），不是本页边界。
- [fee133-notbloom-sold-as-bundled](fee133-notbloom-sold-as-bundled.md) 是 notbloom 单句边界（1240），不是本页边界。
- [hdr130-notswitch-sold-as-bundled](hdr130-notswitch-sold-as-bundled.md) 是 BIP-130 发了 sendheaders 仍未改通告边界（247/1235），不是本页费率过滤器边界。
