# 例：看见 Peer 上有 KV is not already verified interchangeable / not already evidence-ready interchangeable / not already spec-height interchangeable

**层次**：网络 / PeerState not already verified / not already evidence-ready / not already spec-height 正式三事（308 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / NumPeers vs all。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「PeerState not already verified / not already evidence-ready / not already spec-height 正式三事（308 余量）/ not 1009 numpeers-notheight interchangeable / not 308 numpeers-vs-all bundled interchangeable」，不是反应堆查询 bundled（308），也不是入站配额已经认领 ID（67），也不是 HasChannel 就已经入队（309）。不要另写怎样数邻居或怎样切共识。

## 官方三件事

1. **看见 Peer 上有 KV / 看见 Consensus 写了 PeerState 这份查询 is not already 已经验过高度 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1009 numpeers-notheight interchangeable / 1007 numpeers-notall interchangeable / 308 numpeers item 1 NumPeers interchangeable，也不是已经 PeerState not already verified / not already evidence-ready / not already spec-height 正式三事 bundled（308 item 3 余量） interchangeable / 308 numpeers item 3 interchangeable。**  
   官方写：每个 Peer 带一份同步键值店。现行用法是 Consensus 给每个已连接的人放一份 PeerState。Evidence 和 Mempool 会定期去拿，尤其是这个人报的最后高度。看见能 Get 到高度，不是已经验过 interchangeable——本页从 308 item 3 侧钉 not already verified 单句。308 numpeers vs all bundled unbundling 在本页 item 3 完成。

2. **看见 Consensus 写过 / 看见 KV / 这份查询 is not already 证据已经齐 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1009 numpeers-notheight interchangeable / 308 numpeers item 2 按名拿到 interchangeable / 1008 numpeers-notindep interchangeable，也不是已经入站配额已经认领 ID interchangeable / 67 inbound quota interchangeable。**  
   官方把 Consensus 写过和证据已经齐分开。看见 Consensus 写过，不是证据已经齐 interchangeable。本页钉 not already evidence-ready 单句。

3. **看见 Mempool 读到了 / 看见 KV / 这份查询 is not already 已经是规范高度 interchangeable，也不是已经反应堆查询 bundled（308） interchangeable / 1009 numpeers-notheight interchangeable / 1007 numpeers-notall interchangeable，也不是已经 HasChannel 就已经入队 interchangeable / 309 send-vs-enqueued interchangeable。**  
   官方把 Mempool 读到了和已经是规范高度分开。看见 Mempool 读到了，不是已经是规范高度 interchangeable。308 numpeers vs all bundled unbundling 在本页 item 3 完成。

好邻居票数、发送超时、通道号是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **PeerState not already verified ≠ 已经验过高度 interchangeable：** 官方把共识反应堆写下的高度和已经验过分开。
- **看见 Consensus 写过 not already evidence-ready ≠ 证据已经齐 interchangeable：** 官方把 Consensus 写过和证据已经齐分开。
- **看见 Mempool 读到了 not already spec-height ≠ 已经是规范高度 interchangeable：** 官方把 Mempool 读到了和已经是规范高度分开；308 numpeers vs all bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Peer 上的 KV / PeerState | 不是已经验过高度 | 不是入站配额已经认领 ID（67） |
| 看见 Consensus 写过 | 不是证据已经齐 | 不是 HasChannel 就已经入队（309） |
| 看见 Mempool 读到了 | 不是已经是规范高度 | 不是 NumPeers 就已经数完（1007） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PeerState not already verified / not already evidence-ready / not already spec-height 正式三事（308 余量），必须分开是不是已经验过高度、是不是证据已经齐、是不是已经是规范高度。可以跳过「看见能问就已经数完」。不要另写怎样数邻居或怎样切共识。308 numpeers vs all bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 好邻居票数、发送超时、通道号。
- 反应堆查询 bundled。那是不变量 308。
- 入站配额已经认领 ID。那是不变量 67。
- HasChannel 就已经入队。那是不变量 309。
