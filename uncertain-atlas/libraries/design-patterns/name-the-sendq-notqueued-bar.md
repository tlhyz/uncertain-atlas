# 模式：点名 sendq-notqueued 杠

**层次**：网络 / HasChannel not already queued / not already delivered / not already sent 正式三事（309 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应**：[`../tracks/network/worked-example-sendq-notqueued-vs-bundled.md`](../tracks/network/worked-example-sendq-notqueued-vs-bundled.md)。

- **HasChannel 不是已经入队：** 看见通道在，不是已经入队 interchangeable / 1010 sendq-notqueued interchangeable。
- **看见对端宣布了 不是已经送到：** 看见对端宣布了，不是已经送到 interchangeable。
- **看见辅助方法绿了 不是已经发出去：** 看见辅助方法绿了，不是已经发出去 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 HasChannel 正式三事（309 余量），先数清问的是是不是已经入队、是不是已经送到、还是看见辅助方法绿了是不是已经发出去，再决定要不要同一次发布。309 send vs enqueued bundled unbundling 在本页 item 1 启动。
