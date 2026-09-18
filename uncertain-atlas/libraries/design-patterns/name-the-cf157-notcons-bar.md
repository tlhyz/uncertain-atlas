# 模式：点名 cf157-notcons 杠

**层次**：轻客户端 / BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事（243 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)（Deployed, Peer Services；依赖 158）。  
**对应**：[`../tracks/light-clients/worked-example-cf157-notcons-vs-bundled.md`](../tracks/light-clients/worked-example-cf157-notcons-vs-bundled.md)。

- **过滤器头链对上 不是已经写进共识：看见过滤器头链对上，不是已经写进共识 interchangeable / 1278 cf157-notcons interchangeable。**
- **至少一个诚实对等节点 不是块已经合法：看见至少一个诚实对等节点，不是块已经合法 interchangeable / 1278 cf157-notcons interchangeable。**
- **过滤器头链对上 不是已经不需要诚实对等节点：看见过滤器头链对上，不是已经不需要诚实对等节点 interchangeable / 1278 cf157-notcons interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看客户端侧过滤 / 过滤器头链 正式三事（243 余量），必须分开 not already have-block、not already consensus、not already full-node 三件事。
