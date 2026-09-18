# 反模式：把 BIP-133 skip-inv not already rejected / not already illegal / not already filtered-net 正式三事（245 余量） 写成已经 已经拒进池 / 已经共识非法 / 全网低费率交易已经被滤掉

**层次**：内存池 / BIP-133 skip-inv not already rejected / not already illegal / not already filtered-net 正式三事（245 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/mempool/worked-example-fee133-notpool-vs-bundled.md`](../tracks/mempool/worked-example-fee133-notpool-vs-bundled.md)。

把 BIP-133 skip-inv not already rejected / not already illegal / not already filtered-net 正式三事（245 余量） 写成已经 已经拒进池 / 已经共识非法 / 全网低费率交易已经被滤掉，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看费率过滤器 正式三事（245 余量），必须分开 not already rejected、not already must、not already fee-pass 三件事，不要和 245 / 144 / 166 / 1239 / 1240 糊成一句。

也不是：

- [fee133-notmust-sold-as-bundled](fee133-notmust-sold-as-bundled.md) 是 notmust 单句边界（1239），不是本页边界。
- [fee133-notbloom-sold-as-bundled](fee133-notbloom-sold-as-bundled.md) 是 notbloom 单句边界（1240），不是本页边界。
- [hdr130-notswitch-sold-as-bundled](hdr130-notswitch-sold-as-bundled.md) 是 BIP-130 发了 sendheaders 仍未改通告边界（247/1235），不是本页费率过滤器边界。
