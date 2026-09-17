# 反模式：把 InitPeer not already talking / not already connected / not already added 正式三事（305 余量） 写成已经 已经能跟它对说 / 已经加进已连接集合 / 已经 AddPeer

**层次**：网络 / InitPeer not already talking / not already connected / not already added 正式三事（305 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md) reactor / InitPeer vs AddPeer。  
**对应**：[`../tracks/network/worked-example-initpeer-nottalk-vs-bundled.md`](../tracks/network/worked-example-initpeer-nottalk-vs-bundled.md)。

把 InitPeer not already talking / not already connected / not already added 正式三事（305 余量） 写成已经 已经能跟它对说 / 已经加进已连接集合 / 已经 AddPeer，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitPeer 正式三事（305 余量），必须分开 not already talking、not already connected、not already added 三件事，不要和 305 / 67 / 304 / 1002 / 1003 糊成一句。

也不是：

- [votets-notslash-sold-as-bundled](votets-notslash-sold-as-bundled.md) 是断开仍未罚边界（304/1000），不是本页 InitPeer 仍未能对说边界。
- 入站配额已经认领 ID 是不变量 67，不是本页状态建了仍未加进已连接集合边界。
