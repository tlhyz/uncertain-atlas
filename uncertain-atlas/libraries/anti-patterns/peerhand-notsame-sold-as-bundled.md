# 反模式：把 Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事（306 余量） 写成已经 已经是同一个人 / 已经是上一次那份 / 身份已经换了

**层次**：网络 / Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事（306 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应**：[`../tracks/network/worked-example-peerhand-notsame-vs-bundled.md`](../tracks/network/worked-example-peerhand-notsame-vs-bundled.md)。

把 Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事（306 余量） 写成已经 已经是同一个人 / 已经是上一次那份 / 身份已经换了，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Peer 句柄 正式三事（306 余量），必须分开 not already same-person、not already same-handle、not already new-id 三件事，不要和 306 / 305 / 67 / 1005 / 1006 糊成一句。

也不是：

- [initpeer-nothot-sold-as-bundled](initpeer-nothot-sold-as-bundled.md) 是跑着仍不能热加边界（305/1003），不是本页句柄仍不是那个人边界。
- InitPeer 已经能交互是不变量 305/1001，不是本页又拿到句柄仍不是上一次那份边界。
