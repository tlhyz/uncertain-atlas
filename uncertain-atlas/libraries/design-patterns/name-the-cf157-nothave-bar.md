# 模式：点名 cf157-nothave 杠

**层次**：轻客户端 / BIP-157 match not already have-block / not already have-tx / not already bip37 正式三事（243 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)（Deployed, Peer Services；依赖 158）。  
**对应**：[`../tracks/light-clients/worked-example-cf157-nothave-vs-bundled.md`](../tracks/light-clients/worked-example-cf157-nothave-vs-bundled.md)。

- **过滤器对上 不是已经有块：看见过滤器对上，不是已经有块 interchangeable / 1277 cf157-nothave interchangeable。**
- **确定性 不是已经有那笔交易：看见确定性，不是已经有那笔交易 interchangeable / 1277 cf157-nothave interchangeable。**
- **过滤器对上 不是已经是 BIP-37：看见过滤器对上，不是已经是 BIP-37 interchangeable / 1277 cf157-nothave interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看客户端侧过滤 / 过滤器头链 正式三事（243 余量），必须分开 not already have-block、not already consensus、not already full-node 三件事。
