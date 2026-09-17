# 模式：点名 sendq-notdisc 杠

**层次**：网络 / Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事（309 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应**：[`../tracks/network/worked-example-sendq-notdisc-vs-bundled.md`](../tracks/network/worked-example-sendq-notdisc-vs-bundled.md)。

- **Send 回假 不是已经断开：** 看见阻塞过，不是已经断开 interchangeable / 1011 sendq-notdisc interchangeable。
- **看见回了假 不是已经知道是哪一种理由：** 看见回了假，不是已经知道是哪一种理由 interchangeable。
- **看见方法还在 不是已经送到：** 看见方法还在，不是已经送到 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Send 回假 正式三事（309 余量），先数清问的是是不是已经断开、是不是已经知道是哪一种理由、还是看见方法还在是不是已经送到，再决定要不要同一次发布。309 send vs enqueued bundled unbundling 在本页 item 2 续。
