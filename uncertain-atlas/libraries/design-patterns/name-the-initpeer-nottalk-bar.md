# 模式：点名 initpeer-nottalk 杠

**层次**：网络 / InitPeer not already talking / not already connected / not already added 正式三事（305 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md) reactor / InitPeer vs AddPeer。  
**对应**：[`../tracks/network/worked-example-initpeer-nottalk-vs-bundled.md`](../tracks/network/worked-example-initpeer-nottalk-vs-bundled.md)。

- **InitPeer 不是已经能跟它对说：** 看见对象在了，不是已经能发 interchangeable / 1001 initpeer-nottalk interchangeable。
- **看见状态建了 不是已经加进已连接集合：** 看见状态建了，不是已经加进已连接集合 interchangeable。
- **看见叫了 InitPeer 不是已经 AddPeer：** 看见叫了 InitPeer，不是已经 AddPeer interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitPeer 正式三事（305 余量），先数清问的是是不是已经能跟它对说、是不是已经加进已连接集合、还是看见叫了 InitPeer 是不是已经 AddPeer，再决定要不要同一次发布。305 initpeer vs addpeer bundled unbundling 在本页 item 1 启动。
