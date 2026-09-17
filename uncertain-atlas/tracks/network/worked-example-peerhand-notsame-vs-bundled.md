# 例：看见 Peer 句柄 is not already same-person interchangeable / not already same-handle interchangeable / not already new-id interchangeable

**层次**：网络 / Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事（306 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事（306 余量）/ not 1004 peerhand-notsame interchangeable / not 306 peer-handler-vs-node bundled interchangeable」，不是对等句柄 bundled（306），也不是 InitPeer 已经能交互（305/1001），也不是入站配额已经认领 ID（67）。不要另写怎样广播或怎样重连。

## 官方三件事

1. **看见 Peer 句柄 / 看见又一次 InitPeer 这份接口 is not already 已经是同一个人 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1004 peerhand-notsame interchangeable / 1005 peerhand-notsent interchangeable / 306 peer item 2 Broadcast interchangeable，也不是已经 Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事 bundled（306 item 1 余量） interchangeable / 306 peer item 1 interchangeable。**  
   官方写：每次连上一个对等节点（包括断开再连），都会经 InitPeer(Peer) 再给反应堆一份新的、不一样的 Peer 句柄。这份句柄绑的是这一次连接，不是网上那个节点本身。要认人，得用 p2p.ID。看见又拿到句柄，不是已经是同一个人 interchangeable——本页从 306 item 1 侧钉 not already same-person 单句。306 peer-handler vs node bundled unbundling 在本页 item 1 启动。

2. **看见又拿到句柄 / 看见对象换了 / 这份接口 is not already 已经是上一次那份 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1004 peerhand-notsame interchangeable / 306 peer item 3 StopPeer interchangeable / 1006 peerhand-notgone interchangeable，也不是已经 InitPeer 已经能交互 interchangeable / 305/1001 initpeer-nottalk interchangeable。**  
   官方把又拿到句柄和已经是上一次那份分开。看见又拿到句柄，不是已经是上一次那份 interchangeable。本页钉 not already same-handle 单句。

3. **看见 InitPeer 又来了 / 看见对象换了 / 这份接口 is not already 身份已经换了 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1004 peerhand-notsame interchangeable / 1005 peerhand-notsent interchangeable，也不是已经入站配额已经认领 ID interchangeable / 67 inbound quota interchangeable。**  
   官方把对象换了和网上那个人换了分开。看见 InitPeer 又来了，不是身份已经换了 interchangeable。306 peer-handler vs node bundled unbundling 在本页 item 1 启动。

通道号、好邻居计数、发送超时是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Peer 句柄 not already same-person ≠ 已经是同一个人 interchangeable：** 官方把连接对象和网上节点身份分开。
- **看见又拿到句柄 not already same-handle ≠ 已经是上一次那份 interchangeable：** 官方把又拿到句柄和已经是上一次那份分开。
- **看见 InitPeer 又来了 not already new-id ≠ 身份已经换了 interchangeable：** 官方把对象换了和网上那个人换了分开；306 peer-handler vs node bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 又一次 InitPeer 的新句柄 | 不是已经是同一个人 | 不是 InitPeer 已经能交互（305/1001） |
| 看见又拿到句柄 | 不是已经是上一次那份 | 不是入站配额已经认领 ID（67） |
| 看见 InitPeer 又来了 | 不是身份已经换了 | 不是 Broadcast 就已经送到（1005） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Peer 句柄 not already same-person / not already same-handle / not already new-id 正式三事（306 余量），必须分开是不是已经是同一个人、是不是已经是上一次那份、是不是身份已经换了。可以跳过「看见句柄就已经是那个人」。不要另写怎样广播或怎样重连。306 peer-handler vs node bundled unbundling 在本页 item 1 启动；续 [`worked-example-peerhand-notsent-vs-bundled.md`](worked-example-peerhand-notsent-vs-bundled.md)（不变量 1005 item 2）。

## 本页不抄

- 好邻居票数、发送超时、通道号、信封字段表。
- 对等句柄 bundled。那是不变量 306。
- InitPeer 已经能交互。那是不变量 305/1001。
- 入站配额已经认领 ID。那是不变量 67。
