# 例：看见 NumPeers is not already all-neighbors interchangeable / not already unconditional interchangeable / not already dialing-ok interchangeable

**层次**：网络 / NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事（308 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / NumPeers vs all。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事（308 余量）/ not 1007 numpeers-notall interchangeable / not 308 numpeers-vs-all bundled interchangeable」，不是反应堆查询 bundled（308），也不是句柄已经是那个人（306/1004），也不是 InitPeer 已经能交互（305/1001）。不要另写怎样数邻居或怎样切共识。

## 官方三件事

1. **看见 NumPeers / 看见 outbound+inbound 这份查询 is not already 已经数完所有邻居 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1007 numpeers-notall interchangeable / 1008 numpeers-notindep interchangeable / 308 numpeers item 2 按名拿到 interchangeable，也不是已经 NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事 bundled（308 item 1 余量） interchangeable / 308 numpeers item 1 interchangeable。**  
   官方写：NumPeers() 回已连接的出站和入站个数。无条件邻居不在这里面。第三个数 dialing 是正在试着连、还没连上的人。看见回了三个数，不是已经数完 interchangeable——本页从 308 item 1 侧钉 not already all-neighbors 单句。308 numpeers vs all bundled unbundling 在本页 item 1 启动。

2. **看见出站加进站 / 看见三个数 / 这份查询 is not already 无条件名单已经算进去 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1007 numpeers-notall interchangeable / 308 numpeers item 3 PeerState interchangeable / 1009 numpeers-notheight interchangeable，也不是已经句柄已经是那个人 interchangeable / 306/1004 peerhand-notsame interchangeable。**  
   官方把出站加进站和无条件名单已经算进去分开。看见出站加进站，不是无条件名单已经算进去 interchangeable。本页钉 not already unconditional 单句。

3. **看见正在拨 / 看见三个数 / 这份查询 is not already 已经连上 interchangeable，也不是协议层该当现行用法 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1007 numpeers-notall interchangeable / 1008 numpeers-notindep interchangeable，也不是已经 InitPeer 已经能交互 interchangeable / 305/1001 initpeer-nottalk interchangeable。**  
   官方写：dialing 不该给协议层看；除了可算 p2p 层一部分的 PEX，标准反应堆都不用这个数。看见正在拨，不是已经连上，也不是协议层该当现行用法 interchangeable。308 numpeers vs all bundled unbundling 在本页 item 1 启动。

好邻居票数、发送超时、通道号是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **NumPeers not already all-neighbors ≠ 已经数完所有邻居 interchangeable：** 官方把已连接、无条件邻居、正在拨分开。
- **看见出站加进站 not already unconditional ≠ 无条件名单已经算进去 interchangeable：** 官方把出站加进站和无条件名单已经算进去分开。
- **看见正在拨 not already dialing-ok ≠ 已经连上 / 协议层该当现行用法 interchangeable：** 官方把 dialing 不该给协议层看写明；308 numpeers vs all bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| NumPeers 三个数 | 不是已经数完，也不是协议层该看 dialing | 不是句柄已经是那个人（306/1004） |
| 看见出站加进站 | 不是无条件名单已经算进去 | 不是 InitPeer 已经能交互（305/1001） |
| 看见正在拨 | 不是已经连上 | 不是按名字拿到就已经独立（1008） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事（308 余量），必须分开是不是已经数完、是不是无条件名单已经算进去、是不是正在拨就已经连上。可以跳过「看见能问就已经数完」。不要另写怎样数邻居或怎样切共识。308 numpeers vs all bundled unbundling 在本页 item 1 启动；续 [`worked-example-numpeers-notindep-vs-bundled.md`](worked-example-numpeers-notindep-vs-bundled.md)（不变量 1008 item 2）。

## 本页不抄

- 好邻居票数、发送超时、通道号。
- 反应堆查询 bundled。那是不变量 308。
- 句柄已经是那个人。那是不变量 306/1004。
- InitPeer 已经能交互。那是不变量 305/1001。
