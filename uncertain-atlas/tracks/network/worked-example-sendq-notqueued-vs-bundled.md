# 例：看见 HasChannel 为真 is not already queued interchangeable / not already delivered interchangeable / not already sent interchangeable

**层次**：网络 / HasChannel not already queued / not already delivered / not already sent 正式三事（309 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「HasChannel not already queued / not already delivered / not already sent 正式三事（309 余量）/ not 1010 sendq-notqueued interchangeable / not 309 send-vs-enqueued bundled interchangeable」，不是对等发送 bundled（309），也不是 Broadcast 已经送到（306/1005），也不是 NumPeers 已经数完（308/1007）。不要另写怎样入队或怎样编 protobuf。

## 官方三件事

1. **看见 HasChannel 为真 / 看见对端宣布了通道 这份发送 is not already 已经入队 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1010 sendq-notqueued interchangeable / 1011 sendq-notdisc interchangeable / 309 send item 2 Send 回假 interchangeable，也不是已经 HasChannel not already queued / not already delivered / not already sent 正式三事 bundled（309 item 1 余量） interchangeable / 309 send item 1 interchangeable。**  
   官方写：HasChannel() 用来测对端实不实现这条通道。若对端没有这条通道，Send 和 TrySend 都会立刻回假，因为发送一定失败。看见通道在，不是已经入队 interchangeable——本页从 309 item 1 侧钉 not already queued 单句。309 send vs enqueued bundled unbundling 在本页 item 1 启动。

2. **看见对端宣布了 / 看见通道在 / 这份发送 is not already 已经送到 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1010 sendq-notqueued interchangeable / 309 send item 3 TrySend interchangeable / 1012 sendq-notsame interchangeable，也不是已经 Broadcast 已经送到 interchangeable / 306/1005 peerhand-notsent interchangeable。**  
   官方把对端宣布了和已经送到分开。看见对端宣布了，不是已经送到 interchangeable。本页钉 not already delivered 单句。

3. **看见辅助方法绿了 / 看见通道在 / 这份发送 is not already 已经发出去 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1010 sendq-notqueued interchangeable / 1011 sendq-notdisc interchangeable，也不是已经 NumPeers 已经数完 interchangeable / 308/1007 numpeers-notall interchangeable。**  
   官方把辅助方法绿了和已经发出去分开。看见辅助方法绿了，不是已经发出去 interchangeable。309 send vs enqueued bundled unbundling 在本页 item 1 启动。

发送超时秒数、通道号、队列容量是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **HasChannel not already queued ≠ 已经入队 interchangeable：** 官方把对端有没有这条通道和已经进了发送队列分开。
- **看见对端宣布了 not already delivered ≠ 已经送到 interchangeable：** 官方把对端宣布了和已经送到分开。
- **看见辅助方法绿了 not already sent ≠ 已经发出去 interchangeable：** 官方把辅助方法绿了和已经发出去分开；309 send vs enqueued bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| HasChannel 为真 | 不是已经入队 | 不是 Broadcast 已经送到（306/1005） |
| 看见对端宣布了 | 不是已经送到 | 不是 NumPeers 已经数完（308/1007） |
| 看见辅助方法绿了 | 不是已经发出去 | 不是 Send 回假就已经断开（1011） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 HasChannel not already queued / not already delivered / not already sent 正式三事（309 余量），必须分开是不是已经入队、是不是已经送到、是不是已经发出去。可以跳过「看见能发就已经入队」。不要另写怎样入队或怎样编 protobuf。309 send vs enqueued bundled unbundling 在本页 item 1 启动；续 [`worked-example-sendq-notdisc-vs-bundled.md`](worked-example-sendq-notdisc-vs-bundled.md)（不变量 1011 item 2）。

## 本页不抄

- 发送超时秒数、通道号、队列容量、信封字段表。
- 对等发送 bundled。那是不变量 309。
- Broadcast 已经送到。那是不变量 306/1005。
- NumPeers 已经数完。那是不变量 308/1007。
- 怎样广播。那是不变量 306。
