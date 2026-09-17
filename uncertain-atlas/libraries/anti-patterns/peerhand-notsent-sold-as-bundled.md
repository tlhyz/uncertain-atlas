# 反模式：把 Broadcast 回通道 not already delivered / not already named / not already current 正式三事（306 余量） 写成已经 已经送到 / 已经能点名 / 已经该当现行用法

**层次**：网络 / Broadcast 回通道 not already delivered / not already named / not already current 正式三事（306 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应**：[`../tracks/network/worked-example-peerhand-notsent-vs-bundled.md`](../tracks/network/worked-example-peerhand-notsent-vs-bundled.md)。

把 Broadcast 回通道 not already delivered / not already named / not already current 正式三事（306 余量） 写成已经 已经送到 / 已经能点名 / 已经该当现行用法，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Broadcast 回通道 正式三事（306 余量），必须分开 not already delivered、not already named、not already current 三件事，不要和 306 / 36 / 309 / 1004 / 1006 糊成一句。

也不是：

- [peerhand-notsame-sold-as-bundled](peerhand-notsame-sold-as-bundled.md) 是句柄仍不是那个人单句边界（1004 item 1），不是本页 Broadcast 仍未送到边界。
- 宣布已经收到是不变量 36，不是本页一串真假仍不能点名边界。
