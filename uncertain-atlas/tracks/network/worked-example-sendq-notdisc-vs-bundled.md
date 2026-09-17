# 例：看见 Send 回了假 is not already disconnected interchangeable / not already known-reason interchangeable / not already delivered interchangeable

**层次**：网络 / Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事（309 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事（309 余量）/ not 1011 sendq-notdisc interchangeable / not 309 send-vs-enqueued bundled interchangeable」，不是对等发送 bundled（309），也不是 NumPeers 已经数完（308/1007），也不是踢持久邻居就已经断干净（306/1006）。不要另写怎样入队或怎样编 protobuf。

## 官方三件事

1. **看见 Send 回了假 / 看见阻塞过 这份发送 is not already 已经断开 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1011 sendq-notdisc interchangeable / 1010 sendq-notqueued interchangeable / 309 send item 1 HasChannel interchangeable，也不是已经 Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事 bundled（309 item 2 余量） interchangeable / 309 send item 2 interchangeable。**  
   官方写：两条发送方法回的是「编好的消息能不能进这条通道的发送队列」。最常见的假，是队列满。Send 是阻塞的：队列过了一段时间还满，才回假。看见阻塞过，不是已经断开 interchangeable——本页从 309 item 2 侧钉 not already disconnected 单句。309 send vs enqueued bundled unbundling 在本页 item 2 续。

2. **看见回了假 / 看见阻塞过 / 这份发送 is not already 已经知道是哪一种理由 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1011 sendq-notdisc interchangeable / 309 send item 3 TrySend interchangeable / 1012 sendq-notsame interchangeable，也不是已经 NumPeers 已经数完 interchangeable / 308/1007 numpeers-notall interchangeable。**  
   官方把回假的几种理由分开：队列满、人对等节点已经停、给了未登记的通道号、或编载荷出错。看见回了假，不是已经知道是哪一种理由 interchangeable。本页钉 not already known-reason 单句。

3. **看见方法还在 / 看见回了假 / 这份发送 is not already 已经送到 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1011 sendq-notdisc interchangeable / 1010 sendq-notqueued interchangeable，也不是已经踢持久邻居就已经断干净 interchangeable / 306/1006 peerhand-notgone interchangeable。**  
   官方把方法还在和已经送到分开。看见方法还在，不是已经送到 interchangeable。309 send vs enqueued bundled unbundling 在本页 item 2 续。

发送超时秒数、通道号、队列容量是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Send 回假 not already disconnected ≠ 已经断开 interchangeable：** 官方把阻塞后再回假和已经断开分开。
- **看见回了假 not already known-reason ≠ 已经知道是哪一种理由 interchangeable：** 官方把回假的几种理由分开。
- **看见方法还在 not already delivered ≠ 已经送到 interchangeable：** 官方把方法还在和已经送到分开；309 send vs enqueued bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Send 回了假 | 不是已经断开，也不是已经知道理由 | 不是 NumPeers 已经数完（308/1007） |
| 看见回了假 | 不是已经知道是哪一种理由 | 不是踢持久邻居就已经断干净（306/1006） |
| 看见方法还在 | 不是已经送到 | 不是 TrySend 就已经和 Send 同一把尺（1012） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Send 回假 not already disconnected / not already known-reason / not already delivered 正式三事（309 余量），必须分开是不是已经断开、是不是已经知道是哪一种理由、是不是已经送到。可以跳过「看见能发就已经入队」。不要另写怎样入队或怎样编 protobuf。309 send vs enqueued bundled unbundling 在本页 item 2 续；续 [`worked-example-sendq-notsame-vs-bundled.md`](worked-example-sendq-notsame-vs-bundled.md)（不变量 1012 item 3）。

## 本页不抄

- 发送超时秒数、通道号、队列容量、信封字段表。
- 对等发送 bundled。那是不变量 309。
- NumPeers 已经数完。那是不变量 308/1007。
- 踢持久邻居就已经断干净。那是不变量 306/1006。
