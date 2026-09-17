# 模式：点名 peerhand-notgone 杠

**层次**：网络 / StopPeerForError not already gone / not already forgotten / not already clean 正式三事（306 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应**：[`../tracks/network/worked-example-peerhand-notgone-vs-bundled.md`](../tracks/network/worked-example-peerhand-notgone-vs-bundled.md)。

- **StopPeerForError 不是已经对持久邻居也断干净：** 看见叫了停，不是已经不会再来 interchangeable / 1006 peerhand-notgone interchangeable。
- **看见理由进了 不是持久名单已经忘了：** 看见理由进了，不是持久名单已经忘了 interchangeable。
- **看见反应堆要踢 不是已经按「踢了就干净」执行：** 看见反应堆要踢，不是已经按「踢了就干净」执行 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 StopPeerForError 正式三事（306 余量），先数清问的是是不是已经不会再来、是不是持久名单已经忘了、还是看见反应堆要踢是不是已经按「踢了就干净」执行，再决定要不要同一次发布。306 peer-handler vs node bundled unbundling 在本页 item 3 完成。
