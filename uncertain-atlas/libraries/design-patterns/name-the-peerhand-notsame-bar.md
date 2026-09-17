# 模式：点名 peerhand-notsame 杠

**层次**：网络 / Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事（306 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应**：[`../tracks/network/worked-example-peerhand-notsame-vs-bundled.md`](../tracks/network/worked-example-peerhand-notsame-vs-bundled.md)。

- **Peer 句柄 不是已经是同一个人：** 看见又拿到句柄，不是已经是同一个人 interchangeable / 1004 peerhand-notsame interchangeable。
- **看见又拿到句柄 不是已经是上一次那份：** 看见又拿到句柄，不是已经是上一次那份 interchangeable。
- **看见 InitPeer 又来了 不是身份已经换了：** 看见 InitPeer 又来了，不是身份已经换了 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Peer 句柄 正式三事（306 余量），先数清问的是是不是已经是同一个人、是不是已经是上一次那份、还是看见 InitPeer 又来了是不是身份已经换了，再决定要不要同一次发布。306 peer-handler vs node bundled unbundling 在本页 item 1 启动。
