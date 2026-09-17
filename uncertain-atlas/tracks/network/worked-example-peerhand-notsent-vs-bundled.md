# 例：看见 Broadcast 回了通道 is not already delivered interchangeable / not already named interchangeable / not already current interchangeable

**层次**：网络 / Broadcast 回通道 not already delivered / not already named / not already current 正式三事（306 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Broadcast 回通道 not already delivered / not already named / not already current 正式三事（306 余量）/ not 1005 peerhand-notsent interchangeable / not 306 peer-handler-vs-node bundled interchangeable」，不是对等句柄 bundled（306），也不是宣布已经收到（36），也不是 HasChannel 就已经入队（309）。不要另写怎样广播或怎样重连。

## 官方三件事

1. **看见 Broadcast 回了通道 / 看见通道里有 bool 这份接口 is not already 已经送到每一家 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1005 peerhand-notsent interchangeable / 1004 peerhand-notsame interchangeable / 306 peer item 1 句柄 interchangeable，也不是已经 Broadcast 回通道 not already delivered / not already named / not already current 正式三事 bundled（306 item 2 余量） interchangeable / 306 peer item 2 interchangeable。**  
   官方写：Switch.Broadcast 多半是历史兼容。它不阻塞，回一条 bool 通道。每个已连接的人各起一条后台去发。看见回了通道，不是已经送到 interchangeable——本页从 306 item 2 侧钉 not already delivered 单句。306 peer-handler vs node bundled unbundling 在本页 item 2 续。

2. **看见一串真假 / 看见回了通道 / 这份接口 is not already 已经能点名 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1005 peerhand-notsent interchangeable / 306 peer item 3 StopPeer interchangeable / 1006 peerhand-notgone interchangeable，也不是已经宣布已经收到 interchangeable / 36 announce interchangeable。**  
   官方把通道里每个 bool 对不上是哪一个人和已经能点名分开。看见一串真假，不是已经能点名 interchangeable。本页钉 not already named 单句。

3. **看见方法还在 / 看见回了通道 / 这份接口 is not already 已经该当现行用法 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1005 peerhand-notsent interchangeable / 1004 peerhand-notsame interchangeable，也不是已经 HasChannel 就已经入队 interchangeable / 309 send-vs-enqueued interchangeable。**  
   官方把方法还在和已经该当现行用法分开。标准反应堆都不看这个返回值。看见方法还在，不是已经该当现行用法 interchangeable。306 peer-handler vs node bundled unbundling 在本页 item 2 续。

通道号、好邻居计数、发送超时是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Broadcast 回通道 not already delivered ≠ 已经送到每一家 interchangeable：** 官方把发出去和已经送到分开。
- **看见一串真假 not already named ≠ 已经能点名 interchangeable：** 官方把通道里的 bool 对不上是谁和已经能点名分开。
- **看见方法还在 not already current ≠ 已经该当现行用法 interchangeable：** 官方把方法还在和已经该当现行用法分开；306 peer-handler vs node bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Broadcast 回了通道 | 不是已经送到、也不是已经能点名 | 不是宣布已经收到（36） |
| 看见一串真假 | 不是已经能点名 | 不是 HasChannel 就已经入队（309） |
| 看见方法还在 | 不是已经该当现行用法 | 不是踢持久邻居就已经断干净（1006） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Broadcast 回通道 not already delivered / not already named / not already current 正式三事（306 余量），必须分开是不是已经送到、是不是已经能点名、是不是已经该当现行用法。可以跳过「看见句柄就已经是那个人」。不要另写怎样广播或怎样重连。306 peer-handler vs node bundled unbundling 在本页 item 2 续；续 [`worked-example-peerhand-notgone-vs-bundled.md`](worked-example-peerhand-notgone-vs-bundled.md)（不变量 1006 item 3）。

## 本页不抄

- 好邻居票数、发送超时、通道号、信封字段表。
- 对等句柄 bundled。那是不变量 306。
- 宣布已经收到。那是不变量 36。
- HasChannel 就已经入队。那是不变量 309。
