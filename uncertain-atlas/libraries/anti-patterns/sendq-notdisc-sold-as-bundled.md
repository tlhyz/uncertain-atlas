# 反模式：把 Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事（309 余量） 写成已经 已经断开 / 已经知道是哪一种理由 / 已经送到

**层次**：网络 / Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事（309 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应**：[`../tracks/network/worked-example-sendq-notdisc-vs-bundled.md`](../tracks/network/worked-example-sendq-notdisc-vs-bundled.md)。

把 Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事（309 余量） 写成已经 已经断开 / 已经知道是哪一种理由 / 已经送到，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Send 回假 正式三事（309 余量），必须分开 not already disconnected、not already known-reason、not already delivered 三件事，不要和 309 / 308 / 306 / 1010 / 1012 糊成一句。

也不是：

- [sendq-notqueued-sold-as-bundled](sendq-notqueued-sold-as-bundled.md) 是 HasChannel 仍未入队单句边界（1010 item 1），不是本页 Send 回假仍未断开边界。
- NumPeers 已经数完是不变量 308/1007，不是本页回了假仍未知道理由边界。
