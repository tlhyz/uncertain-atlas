# 反模式：把 HasChannel not already queued / not already delivered / not already sent 正式三事（309 余量） 写成已经 已经入队 / 已经送到 / 已经发出去

**层次**：网络 / HasChannel not already queued / not already delivered / not already sent 正式三事（309 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应**：[`../tracks/network/worked-example-sendq-notqueued-vs-bundled.md`](../tracks/network/worked-example-sendq-notqueued-vs-bundled.md)。

把 HasChannel not already queued / not already delivered / not already sent 正式三事（309 余量） 写成已经 已经入队 / 已经送到 / 已经发出去，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 HasChannel 正式三事（309 余量），必须分开 not already queued、not already delivered、not already sent 三件事，不要和 309 / 306 / 308 / 1011 / 1012 糊成一句。

也不是：

- [numpeers-notheight-sold-as-bundled](numpeers-notheight-sold-as-bundled.md) 是 PeerState 仍未验过高度边界（308/1009），不是本页 HasChannel 仍未入队边界。
- Broadcast 已经送到是不变量 306/1005，不是本页对端宣布了仍未送到边界。
