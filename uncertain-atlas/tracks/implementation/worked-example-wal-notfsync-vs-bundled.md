# 例：看见写下每条消息 is not already fsynced interchangeable / not already double-sign-safe interchangeable / not already settled interchangeable

**层次**：实现 / 写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事（298 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事（298 余量）/ not 980 wal-notfsync interchangeable / not 298 wal-vs-signed bundled interchangeable」，不是预写日志 bundled（298），也不是锁谓词（4），也不是同进程就已经隔离（307/977）。不要另写怎样按旋转体积切文件或怎样从损坏里恢复。

## 官方三件事

1. **看见共识模块写下每条消息 / 看见 WAL 里有消息 这份日志 is not already 已经对本节点签过的消息做了 fsync interchangeable，也不是已经预写日志 bundled（298） interchangeable / 980 wal-notfsync interchangeable / 981 wal-notresign interchangeable / 298 wal item 2 回放再签 interchangeable，也不是已经写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事 bundled（298 item 1 余量） interchangeable / 298 wal item 1 interchangeable。**  
   官方写：共识模块把每条消息写入 WAL。对本节点签过的消息，还会走 fsync，为的是防双签。看见写下了，不是已经刷盘 interchangeable——本页从 298 item 1 侧钉 not already fsynced 单句。298 wal vs signed bundled unbundling 在本页 item 1 启动。

2. **看见别人的消息也在日志里 / 看见写下了 / 这份日志 is not already 已经防了双签 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 980 wal-notfsync interchangeable / 298 wal item 3 LastSignBytes interchangeable / 982 wal-notheight interchangeable，也不是已经锁谓词 interchangeable / 4 lock interchangeable。**  
   官方把别人的消息也在日志里和已经按本节点签名那条路刷过分开。看见别人的消息也在日志里，不是已经防了双签 interchangeable。本页钉 not already double-sign-safe 单句。

3. **看见有预写日志 / 看见写下了 / 这份日志 is not already 已经交差 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 980 wal-notfsync interchangeable / 981 wal-notresign interchangeable，也不是已经同进程就已经隔离 interchangeable / 307/977 abci-conn-notsock interchangeable。**  
   官方把有预写日志和已经守住同一高度不得再签矛盾票分开。看见有预写日志，不是已经交差 interchangeable。298 wal vs signed bundled unbundling 在本页 item 1 启动。

旋转体积、总上限、损坏恢复步骤是规范或运维里的取值或做法，本页不抄。

## 官方为什么这样拆

- **写下每条消息 not already fsynced ≠ 已经对本节点签名做了 fsync interchangeable：** 官方把每条都写和本节点签名才刷盘写成两件事。
- **看见别人的消息也在日志里 not already double-sign-safe ≠ 已经防了双签 interchangeable：** 官方把别人的消息也在日志里和已经按本节点签名那条路刷过分开。
- **看见有预写日志 not already settled ≠ 已经交差 interchangeable：** 官方把有预写日志和已经守住不得再签矛盾票分开；298 wal vs signed bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写下每条消息 | 不是已经对本节点签名做了 fsync | 不是锁谓词（4） |
| 看见别人的消息也在日志里 | 不是已经防了双签 | 不是同进程就已经隔离（307/977） |
| 看见有预写日志 | 不是已经交差 | 不是回放再签就已经双签（981） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事（298 余量），必须分开是不是已经刷盘、是不是已经防了双签、是不是已经交差。可以跳过「看见写下就已经防了双签」。不要另写怎样按旋转体积切文件或怎样从损坏里恢复。298 wal vs signed bundled unbundling 在本页 item 1 启动；续 [`worked-example-wal-notresign-vs-bundled.md`](worked-example-wal-notresign-vs-bundled.md)（不变量 981 item 2）。

## 本页不抄

- 旋转体积、总上限、autofile 做法。
- 预写日志 bundled。那是不变量 298。
- 锁谓词。那是不变量 4。
- 同进程就已经隔离。那是不变量 307/977。
