# 例：看见已经在 Receive is not already AddPeer interchangeable / not already joined interchangeable / not already forbidden-early interchangeable

**层次**：网络 / Receive not already AddPeer / not already joined / not already forbidden-early 正式三事（305 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md) reactor / InitPeer vs AddPeer。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Receive not already AddPeer / not already joined / not already forbidden-early 正式三事（305 余量）/ not 1002 initpeer-notadd interchangeable / not 305 initpeer-vs-addpeer bundled interchangeable」，不是反应堆时序 bundled（305），也不是宣布已经收到（36），也不是 ABCI 连接就已经是四门（307）。不要另写怎样实现 Receive 并发或怎样发 Envelope。

## 官方三件事

1. **看见已经在 Receive / 看见消息已经进来 这份时序 is not already 已经过了 AddPeer interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1002 initpeer-notadd interchangeable / 1001 initpeer-nottalk interchangeable / 305 initpeer item 1 InitPeer interchangeable，也不是已经 Receive not already AddPeer / not already joined / not already forbidden-early 正式三事 bundled（305 item 2 余量） interchangeable / 305 initpeer item 2 interchangeable。**  
   官方写：从一个 Peer 收消息的前置条件，是 p2p 层先前已经叫过 InitPeer(Peer)，不是已经叫过 AddPeer。反应堆必须能在 AddPeer 之前收下消息。看见 Receive 来了，不是已经 AddPeer interchangeable——本页从 305 item 2 侧钉 not already AddPeer 单句。305 initpeer vs addpeer bundled unbundling 在本页 item 2 续。

2. **看见信封在了 / 看见 Receive / 这份时序 is not already 已经可以按「已加入」去发 interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1002 initpeer-notadd interchangeable / 305 initpeer item 3 再登记 interchangeable / 1003 initpeer-nothot interchangeable，也不是已经宣布已经收到 interchangeable / 36 announce interchangeable。**  
   官方把信封在了和已经可以按「已加入」去发分开。看见信封在了，不是已经可以按「已加入」去发 interchangeable。本页钉 not already joined 单句。

3. **看见最常见的是 AddPeer 之后才开始收 / 看见 Receive / 这份时序 is not already 官方禁止更早收 interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1002 initpeer-notadd interchangeable / 1001 initpeer-nottalk interchangeable，也不是已经 ABCI 连接就已经是四门 interchangeable / 307 abci-conn interchangeable。**  
   官方把最常见的是 AddPeer 之后才开始收和官方禁止更早收分开。看见最常见的是 AddPeer 之后才开始收，不是官方禁止更早收 interchangeable。305 initpeer vs addpeer bundled unbundling 在本页 item 2 续。

通道号、Quint 模型、ABNF 文法、信封字段表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Receive not already AddPeer ≠ 已经过了 AddPeer interchangeable：** 官方把收消息的前置写成先前的 InitPeer，不是 AddPeer。
- **看见信封在了 not already joined ≠ 已经可以按「已加入」去发 interchangeable：** 官方把信封在了和已经可以按「已加入」去发分开。
- **看见最常见的是 AddPeer 之后才开始收 not already forbidden-early ≠ 官方禁止更早收 interchangeable：** 官方把常见顺序和禁止更早收分开；305 initpeer vs addpeer bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Receive 先于 AddPeer | 不是已经过了 AddPeer | 不是宣布已经收到（36） |
| 看见信封在了 | 不是已经可以按「已加入」去发 | 不是 ABCI 连接就已经是四门（307） |
| 看见最常见的是 AddPeer 之后才开始收 | 不是官方禁止更早收 | 不是跑着就已经能再登记（1003） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Receive not already AddPeer / not already joined / not already forbidden-early 正式三事（305 余量），必须分开是不是已经过了 AddPeer、是不是已经可以按「已加入」去发、是不是官方禁止更早收。可以跳过「看见对等节点对象就已经加进去」。不要另写怎样实现 Receive 并发或怎样发 Envelope。305 initpeer vs addpeer bundled unbundling 在本页 item 2 续；续 [`worked-example-initpeer-nothot-vs-bundled.md`](worked-example-initpeer-nothot-vs-bundled.md)（不变量 1003 item 3）。

## 本页不抄

- Quint 模型、ABNF 文法、通道号、信封字段表。
- 反应堆时序 bundled。那是不变量 305。
- 宣布已经收到。那是不变量 36。
- ABCI 连接就已经是四门。那是不变量 307。
