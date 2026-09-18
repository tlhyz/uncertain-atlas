# 反模式：把 BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事（243 余量） 写成已经 已经写进共识 / 块已经合法 / 已经不需要诚实对等节点

**层次**：轻客户端 / BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事（243 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)（Deployed, Peer Services；依赖 158）。  
**对应**：[`../tracks/light-clients/worked-example-cf157-notcons-vs-bundled.md`](../tracks/light-clients/worked-example-cf157-notcons-vs-bundled.md)。

把 BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事（243 余量） 写成已经 已经写进共识 / 块已经合法 / 已经不需要诚实对等节点，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看客户端侧过滤 / 过滤器头链 正式三事（243 余量），必须分开 not already have-block、not already consensus、not already full-node 三件事，不要和 243 / 22 / 242 / 1277 / 1279 糊成一句。

也不是：

- [cf157-nothave-sold-as-bundled](cf157-nothave-sold-as-bundled.md) 是 nothave 单句边界（1277），不是本页边界。
- [cf157-notfull-sold-as-bundled](cf157-notfull-sold-as-bundled.md) 是 notfull 单句边界（1279），不是本页边界。
- [vt324-notold-sold-as-bundled](vt324-notold-sold-as-bundled.md) 是 BIP-324 支持第 2 版仍未退役旧线边界（242/1276），不是本页客户端侧过滤边界。
