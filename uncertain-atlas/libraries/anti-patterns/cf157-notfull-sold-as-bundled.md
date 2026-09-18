# 反模式：把 BIP-157 cfilter not already full-node / not already scripts-checked / not already bloom-retired 正式三事（243 余量） 写成已经 已经是全节点 / 脚本已经验完 / BIP-37 已经退役

**层次**：轻客户端 / BIP-157 cfilter not already full-node / not already scripts-checked / not already bloom-retired 正式三事（243 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)（Deployed, Peer Services；依赖 158）。  
**对应**：[`../tracks/light-clients/worked-example-cf157-notfull-vs-bundled.md`](../tracks/light-clients/worked-example-cf157-notfull-vs-bundled.md)。

把 BIP-157 cfilter not already full-node / not already scripts-checked / not already bloom-retired 正式三事（243 余量） 写成已经 已经是全节点 / 脚本已经验完 / BIP-37 已经退役，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看客户端侧过滤 / 过滤器头链 正式三事（243 余量），必须分开 not already have-block、not already consensus、not already full-node 三件事，不要和 243 / 252 / 244 / 1277 / 1278 糊成一句。

也不是：

- [cf157-nothave-sold-as-bundled](cf157-nothave-sold-as-bundled.md) 是 nothave 单句边界（1277），不是本页边界。
- [cf157-notcons-sold-as-bundled](cf157-notcons-sold-as-bundled.md) 是 notcons 单句边界（1278），不是本页边界。
- [vt324-notold-sold-as-bundled](vt324-notold-sold-as-bundled.md) 是 BIP-324 支持第 2 版仍未退役旧线边界（242/1276），不是本页客户端侧过滤边界。
