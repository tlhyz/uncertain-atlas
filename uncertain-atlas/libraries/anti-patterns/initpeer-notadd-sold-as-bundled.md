# 反模式：把 Receive not already AddPeer / not already joined / not already forbidden-early 正式三事（305 余量） 写成已经 已经过了 AddPeer / 已经可以按「已加入」去发 / 官方禁止更早收

**层次**：网络 / Receive not already AddPeer / not already joined / not already forbidden-early 正式三事（305 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md) reactor / InitPeer vs AddPeer。  
**对应**：[`../tracks/network/worked-example-initpeer-notadd-vs-bundled.md`](../tracks/network/worked-example-initpeer-notadd-vs-bundled.md)。

把 Receive not already AddPeer / not already joined / not already forbidden-early 正式三事（305 余量） 写成已经 已经过了 AddPeer / 已经可以按「已加入」去发 / 官方禁止更早收，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Receive 正式三事（305 余量），必须分开 not already AddPeer、not already joined、not already forbidden-early 三件事，不要和 305 / 36 / 307 / 1001 / 1003 糊成一句。

也不是：

- [initpeer-nottalk-sold-as-bundled](initpeer-nottalk-sold-as-bundled.md) 是 InitPeer 仍未能对说单句边界（1001 item 1），不是本页 Receive 仍未 AddPeer 边界。
- 宣布已经收到是不变量 36，不是本页信封在了仍未按已加入去发边界。
