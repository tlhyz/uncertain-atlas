# 反模式：把 BIP-338 disabletx not already no-compact / not already tx-illegal / not already no-block 正式三事（256 余量） 写成已经 已经没有紧凑块 / 那些交易消息已经共识非法 / 已经没有块

**层次**：网络 / BIP-338 disabletx not already no-compact / not already tx-illegal / not already no-block 正式三事（256 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-338](https://github.com/bitcoin/bips/blob/master/bip-0338.mediawiki)（Closed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-dis338-notcmpct-vs-bundled.md`](../tracks/network/worked-example-dis338-notcmpct-vs-bundled.md)。

把 BIP-338 disabletx not already no-compact / not already tx-illegal / not already no-block 正式三事（256 余量） 写成已经 已经没有紧凑块 / 那些交易消息已经共识非法 / 已经没有块，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看停交易转发 正式三事（256 余量），必须分开 not already lifetime、not already no-compact、not already forbidden 三件事，不要和 256 / 36 / 245 / 1241 / 1243 糊成一句。

也不是：

- [dis338-notlife-sold-as-bundled](dis338-notlife-sold-as-bundled.md) 是 notlife 单句边界（1241），不是本页边界。
- [dis338-notaddr-sold-as-bundled](dis338-notaddr-sold-as-bundled.md) 是 notaddr 单句边界（1243），不是本页边界。
- [fee133-notpool-sold-as-bundled](fee133-notpool-sold-as-bundled.md) 是 BIP-133 跳过通告仍未拒进池边界（245/1238），不是本页停交易转发边界。
