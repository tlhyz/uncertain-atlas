# 例：看见 StopPeerForError is not already gone interchangeable / not already forgotten interchangeable / not already clean interchangeable

**层次**：网络 / StopPeerForError not already gone / not already forgotten / not already clean 正式三事（306 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / Peer handle vs node。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「StopPeerForError not already gone / not already forgotten / not already clean 正式三事（306 余量）/ not 1006 peerhand-notgone interchangeable / not 306 peer-handler-vs-node bundled interchangeable」，不是对等句柄 bundled（306），也不是入站配额已经认领 ID（67），也不是跑着就已经能再登记（305/1003）。不要另写怎样广播或怎样重连。

## 官方三件事

1. **看见 StopPeerForError / 看见反应堆要踢人 这份接口 is not already 已经对持久邻居也断干净 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1006 peerhand-notgone interchangeable / 1004 peerhand-notsame interchangeable / 306 peer item 1 句柄 interchangeable，也不是已经 StopPeerForError not already gone / not already forgotten / not already clean 正式三事 bundled（306 item 3 余量） interchangeable / 306 peer item 3 interchangeable。**  
   官方写：反应堆可以让 p2p 层停掉一个人对等节点：收发例程停掉，再 RemovePeer，再从已连接集合拿走。但若这个人配成持久邻居，Switch 还会试着重连同一个人。看见叫了停，不是已经不会再来 interchangeable——本页从 306 item 3 侧钉 not already gone 单句。306 peer-handler vs node bundled unbundling 在本页 item 3 完成。

2. **看见理由进了 / 看见叫了停 / 这份接口 is not already 持久名单已经忘了 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1006 peerhand-notgone interchangeable / 306 peer item 2 Broadcast interchangeable / 1005 peerhand-notsent interchangeable，也不是已经入站配额已经认领 ID interchangeable / 67 inbound quota interchangeable。**  
   官方把理由进了和持久名单已经忘了分开。看见理由进了，不是持久名单已经忘了 interchangeable。本页钉 not already forgotten 单句。

3. **看见反应堆要踢 / 看见叫了停 / 这份接口 is not already 已经按「踢了就干净」执行 interchangeable，也不是已经对等句柄 bundled（306） interchangeable / 1006 peerhand-notgone interchangeable / 1004 peerhand-notsame interchangeable，也不是已经跑着就已经能再登记 interchangeable / 305/1003 initpeer-nothot interchangeable。**  
   官方把反应堆要踢和已经按「踢了就干净」执行分开。看见反应堆要踢，不是已经按「踢了就干净」执行 interchangeable。306 peer-handler vs node bundled unbundling 在本页 item 3 完成。

通道号、好邻居计数、发送超时是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **StopPeerForError not already gone ≠ 已经对持久邻居也断干净 interchangeable：** 官方把反应堆要踢和持久邻居还会重连分开。
- **看见理由进了 not already forgotten ≠ 持久名单已经忘了 interchangeable：** 官方把理由进了和持久名单已经忘了分开。
- **看见反应堆要踢 not already clean ≠ 已经按「踢了就干净」执行 interchangeable：** 官方把反应堆要踢和已经按「踢了就干净」执行分开；306 peer-handler vs node bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 反应堆叫停持久邻居 | 不是已经断干净 | 不是入站配额已经认领 ID（67） |
| 看见理由进了 | 不是持久名单已经忘了 | 不是跑着就已经能再登记（305/1003） |
| 看见反应堆要踢 | 不是已经按「踢了就干净」执行 | 不是句柄就已经是那个人（1004） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 StopPeerForError not already gone / not already forgotten / not already clean 正式三事（306 余量），必须分开是不是已经不会再来、是不是持久名单已经忘了、是不是已经按「踢了就干净」执行。可以跳过「看见句柄就已经是那个人」。不要另写怎样广播或怎样重连。306 peer-handler vs node bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 好邻居票数、发送超时、通道号、信封字段表。
- 对等句柄 bundled。那是不变量 306。
- 入站配额已经认领 ID。那是不变量 67。
- 跑着就已经能再登记。那是不变量 305/1003。
