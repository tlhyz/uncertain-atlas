# 反模式：把 PeerState not already verified / not already evidence-ready / not already spec-height 正式三事（308 余量） 写成已经 已经验过高度 / 证据已经齐 / 已经是规范高度

**层次**：网络 / PeerState not already verified / not already evidence-ready / not already spec-height 正式三事（308 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / NumPeers vs all。  
**对应**：[`../tracks/network/worked-example-numpeers-notheight-vs-bundled.md`](../tracks/network/worked-example-numpeers-notheight-vs-bundled.md)。

把 PeerState not already verified / not already evidence-ready / not already spec-height 正式三事（308 余量） 写成已经 已经验过高度 / 证据已经齐 / 已经是规范高度，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PeerState 正式三事（308 余量），必须分开 not already verified、not already evidence-ready、not already spec-height 三件事，不要和 308 / 67 / 309 / 1007 / 1008 糊成一句。

也不是：

- [numpeers-notindep-sold-as-bundled](numpeers-notindep-sold-as-bundled.md) 是按名拿到仍未独立单句边界（1008 item 2），不是本页 PeerState 仍未验过高度边界。
- 入站配额已经认领 ID 是不变量 67，不是本页 Consensus 写过仍未证据齐边界。
