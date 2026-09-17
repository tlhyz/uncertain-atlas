# 模式：点名 numpeers-notheight 杠

**层次**：网络 / PeerState not already verified / not already evidence-ready / not already spec-height 正式三事（308 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / NumPeers vs all。  
**对应**：[`../tracks/network/worked-example-numpeers-notheight-vs-bundled.md`](../tracks/network/worked-example-numpeers-notheight-vs-bundled.md)。

- **PeerState 不是已经验过高度：** 看见能 Get 到高度，不是已经验过 interchangeable / 1009 numpeers-notheight interchangeable。
- **看见 Consensus 写过 不是证据已经齐：** 看见 Consensus 写过，不是证据已经齐 interchangeable。
- **看见 Mempool 读到了 不是已经是规范高度：** 看见 Mempool 读到了，不是已经是规范高度 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PeerState 正式三事（308 余量），先数清问的是是不是已经验过高度、是不是证据已经齐、还是看见 Mempool 读到了是不是已经是规范高度，再决定要不要同一次发布。308 numpeers vs all bundled unbundling 在本页 item 3 完成。
