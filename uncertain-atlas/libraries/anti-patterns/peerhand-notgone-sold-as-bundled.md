# 反模式：把 StopPeerForError not already gone / not already forgotten / not already clean 正式三事（306 余量） 写成已经 已经断干净 / 持久名单已经忘了 / 已经按「踢了就干净」执行

**层次**：网络 / StopPeerForError not already gone / not already forgotten / not already clean 正式三事（306 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应**：[`../tracks/network/worked-example-peerhand-notgone-vs-bundled.md`](../tracks/network/worked-example-peerhand-notgone-vs-bundled.md)。

把 StopPeerForError not already gone / not already forgotten / not already clean 正式三事（306 余量） 写成已经 已经断干净 / 持久名单已经忘了 / 已经按「踢了就干净」执行，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 StopPeerForError 正式三事（306 余量），必须分开 not already gone、not already forgotten、not already clean 三件事，不要和 306 / 67 / 305 / 1004 / 1005 糊成一句。

也不是：

- [peerhand-notsent-sold-as-bundled](peerhand-notsent-sold-as-bundled.md) 是 Broadcast 仍未送到单句边界（1005 item 2），不是本页踢持久邻居仍未断干净边界。
- 入站配额已经认领 ID 是不变量 67，不是本页理由进了仍未忘持久名单边界。
