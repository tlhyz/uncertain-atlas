# 模式：点名 numpeers-notall 杠

**层次**：网络 / NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事（308 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / NumPeers vs all。  
**对应**：[`../tracks/network/worked-example-numpeers-notall-vs-bundled.md`](../tracks/network/worked-example-numpeers-notall-vs-bundled.md)。

- **NumPeers 不是已经数完所有邻居：** 看见回了三个数，不是已经数完 interchangeable / 1007 numpeers-notall interchangeable。
- **看见出站加进站 不是无条件名单已经算进去：** 看见出站加进站，不是无条件名单已经算进去 interchangeable。
- **看见正在拨 不是已经连上：** 看见正在拨，不是已经连上，也不是协议层该当现行用法 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 NumPeers 正式三事（308 余量），先数清问的是是不是已经数完、是不是无条件名单已经算进去、还是看见正在拨是不是已经连上，再决定要不要同一次发布。308 numpeers vs all bundled unbundling 在本页 item 1 启动。
