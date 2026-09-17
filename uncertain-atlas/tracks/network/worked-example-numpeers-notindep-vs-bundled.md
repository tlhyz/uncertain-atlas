# 例：看见能按名字拿到另一个反应堆 is not already independent interchangeable / not already recommended interchangeable / not already current interchangeable

**层次**：网络 / 按名字拿到反应堆 not already independent / not already recommended / not already current 正式三事（308 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / NumPeers vs all。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「按名字拿到反应堆 not already independent / not already recommended / not already current 正式三事（308 余量）/ not 1008 numpeers-notindep interchangeable / not 308 numpeers-vs-all bundled interchangeable」，不是反应堆查询 bundled（308），也不是 InitPeer 已经能交互（305/1001），也不是跑着就已经能再登记（305/1003）。不要另写怎样数邻居或怎样切共识。

## 官方三件事

1. **看见能按名字拿到另一个反应堆 / 看见 Block Sync 能切到 Consensus 这份查询 is not already 已经独立 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1008 numpeers-notindep interchangeable / 1007 numpeers-notall interchangeable / 308 numpeers item 1 NumPeers interchangeable，也不是已经按名字拿到反应堆 not already independent / not already recommended / not already current 正式三事 bundled（308 item 2 余量） interchangeable / 308 numpeers item 2 interchangeable。**  
   官方写：Switch.Reactor(name) 能按登记名拿到另一个反应堆。这种反应堆互相拿的做法不鼓励，应该避免，因为它违反「反应堆彼此独立」这条假设。看见能拿到，不是已经独立 interchangeable——本页从 308 item 2 侧钉 not already independent 单句。308 numpeers vs all bundled unbundling 在本页 item 2 续。

2. **看见能切过去 / 看见能拿到 / 这份查询 is not already 已经该当推荐路径 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1008 numpeers-notindep interchangeable / 308 numpeers item 3 PeerState interchangeable / 1009 numpeers-notheight interchangeable，也不是已经 InitPeer 已经能交互 interchangeable / 305/1001 initpeer-nottalk interchangeable。**  
   官方把能切过去和已经该当推荐路径分开。看见能切过去，不是已经该当推荐路径 interchangeable。本页钉 not already recommended 单句。

3. **看见方法还在 / 看见能拿到 / 这份查询 is not already 已经该当现行用法 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1008 numpeers-notindep interchangeable / 1007 numpeers-notall interchangeable，也不是已经跑着就已经能再登记 interchangeable / 305/1003 initpeer-nothot interchangeable。**  
   官方把方法还在和已经该当现行用法分开。看见方法还在，不是已经该当现行用法 interchangeable。308 numpeers vs all bundled unbundling 在本页 item 2 续。

好邻居票数、发送超时、通道号是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **按名字拿到反应堆 not already independent ≠ 已经独立 interchangeable：** 官方把能拿到和违反独立分开。
- **看见能切过去 not already recommended ≠ 已经该当推荐路径 interchangeable：** 官方把能切过去和已经该当推荐路径分开。
- **看见方法还在 not already current ≠ 已经该当现行用法 interchangeable：** 官方把方法还在和已经该当现行用法分开；308 numpeers vs all bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 按名字拿到反应堆 | 不是已经独立，也不是已经推荐 | 不是 InitPeer 已经能交互（305/1001） |
| 看见能切过去 | 不是已经该当推荐路径 | 不是跑着就已经能再登记（305/1003） |
| 看见方法还在 | 不是已经该当现行用法 | 不是 PeerState 就已经验过高度（1009） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看按名字拿到反应堆 not already independent / not already recommended / not already current 正式三事（308 余量），必须分开是不是已经独立、是不是已经该当推荐路径、是不是已经该当现行用法。可以跳过「看见能问就已经数完」。不要另写怎样数邻居或怎样切共识。308 numpeers vs all bundled unbundling 在本页 item 2 续；续 [`worked-example-numpeers-notheight-vs-bundled.md`](worked-example-numpeers-notheight-vs-bundled.md)（不变量 1009 item 3）。

## 本页不抄

- 好邻居票数、发送超时、通道号。
- 反应堆查询 bundled。那是不变量 308。
- InitPeer 已经能交互。那是不变量 305/1001。
- 跑着就已经能再登记。那是不变量 305/1003。
