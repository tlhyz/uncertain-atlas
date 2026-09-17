# 模式：点名 initpeer-notadd 杠

**层次**：网络 / Receive not already AddPeer / not already joined / not already forbidden-early 正式三事（305 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md) reactor / InitPeer vs AddPeer。  
**对应**：[`../tracks/network/worked-example-initpeer-notadd-vs-bundled.md`](../tracks/network/worked-example-initpeer-notadd-vs-bundled.md)。

- **Receive 不是已经过了 AddPeer：** 看见 Receive 来了，不是已经 AddPeer interchangeable / 1002 initpeer-notadd interchangeable。
- **看见信封在了 不是已经可以按「已加入」去发：** 看见信封在了，不是已经可以按「已加入」去发 interchangeable。
- **看见最常见的是 AddPeer 之后才开始收 不是官方禁止更早收：** 看见最常见的是 AddPeer 之后才开始收，不是官方禁止更早收 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Receive 正式三事（305 余量），先数清问的是是不是已经过了 AddPeer、是不是已经可以按「已加入」去发、还是看见最常见的是 AddPeer 之后才开始收是不是官方禁止更早收，再决定要不要同一次发布。305 initpeer vs addpeer bundled unbundling 在本页 item 2 续。
