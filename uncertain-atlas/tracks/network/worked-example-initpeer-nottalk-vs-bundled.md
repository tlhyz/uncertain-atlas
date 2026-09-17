# 例：看见 InitPeer is not already talking interchangeable / not already connected interchangeable / not already added interchangeable

**层次**：网络 / InitPeer not already talking / not already connected / not already added 正式三事（305 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md) reactor / InitPeer vs AddPeer。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「InitPeer not already talking / not already connected / not already added 正式三事（305 余量）/ not 1001 initpeer-nottalk interchangeable / not 305 initpeer-vs-addpeer bundled interchangeable」，不是反应堆时序 bundled（305），也不是入站配额已经认领 ID（67），也不是断开就已经罚了签的人（304/1000）。不要另写怎样实现 Receive 并发或怎样发 Envelope。

## 官方三件事

1. **看见 InitPeer / 看见对等节点对象已经交给反应堆 这份时序 is not already 已经能跟它对说 interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1001 initpeer-nottalk interchangeable / 1002 initpeer-notadd interchangeable / 305 initpeer item 2 Receive interchangeable，也不是已经 InitPeer not already talking / not already connected / not already added 正式三事 bundled（305 item 1 余量） interchangeable / 305 initpeer item 1 interchangeable。**  
   官方写：InitPeer(Peer) 被叫时，这个 Peer 还没启动，收消息和发消息的例程都没在跑。这一步用来初始化跟这个新人对等节点有关的状态或数据，不要跟它对交互。看见对象在了，不是已经能发 interchangeable——本页从 305 item 1 侧钉 not already talking 单句。305 initpeer vs addpeer bundled unbundling 在本页 item 1 启动。

2. **看见状态建了 / 看见对象在了 / 这份时序 is not already 已经加进已连接集合 interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1001 initpeer-nottalk interchangeable / 305 initpeer item 3 再登记 interchangeable / 1003 initpeer-nothot interchangeable，也不是已经入站配额已经认领 ID interchangeable / 67 inbound quota interchangeable。**  
   官方把状态建了和已经加进已连接集合分开。看见状态建了，不是已经加进已连接集合 interchangeable。本页钉 not already connected 单句。

3. **看见叫了 InitPeer / 看见对象在了 / 这份时序 is not already 已经 AddPeer interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1001 initpeer-nottalk interchangeable / 1002 initpeer-notadd interchangeable，也不是已经断开就已经罚了签的人 interchangeable / 304/1000 votets-notslash interchangeable。**  
   官方把叫了 InitPeer 和已经 AddPeer 分开。看见叫了 InitPeer，不是已经 AddPeer interchangeable。305 initpeer vs addpeer bundled unbundling 在本页 item 1 启动。

通道号、Quint 模型、ABNF 文法、信封字段表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **InitPeer not already talking ≠ 已经能跟它对说 interchangeable：** 官方把对象已经交给反应堆，和收发例程还没跑分开。
- **看见状态建了 not already connected ≠ 已经加进已连接集合 interchangeable：** 官方把状态建了和已经加进已连接集合分开。
- **看见叫了 InitPeer not already added ≠ 已经 AddPeer interchangeable：** 官方把叫了 InitPeer 和已经 AddPeer 分开；305 initpeer vs addpeer bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitPeer | 不是已经能跟它对说 | 不是入站配额已经认领 ID（67） |
| 看见状态建了 | 不是已经加进已连接集合 | 不是断开就已经罚了签的人（304/1000） |
| 看见叫了 InitPeer | 不是已经 AddPeer | 不是 Receive 就已经过了 AddPeer（1002） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitPeer not already talking / not already connected / not already added 正式三事（305 余量），必须分开是不是已经能跟它对说、是不是已经加进已连接集合、是不是已经 AddPeer。可以跳过「看见对等节点对象就已经加进去」。不要另写怎样实现 Receive 并发或怎样发 Envelope。305 initpeer vs addpeer bundled unbundling 在本页 item 1 启动；续 [`worked-example-initpeer-notadd-vs-bundled.md`](worked-example-initpeer-notadd-vs-bundled.md)（不变量 1002 item 2）。

## 本页不抄

- Quint 模型、ABNF 文法、通道号、信封字段表。
- 反应堆时序 bundled。那是不变量 305。
- 入站配额已经认领 ID。那是不变量 67。
- 断开就已经罚了签的人。那是不变量 304/1000。
- 怎样在 InitPeer 里认领 ID。那是不变量 67。
