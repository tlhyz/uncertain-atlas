# 例：看见回放时又要签 is not already double-signed interchangeable / not already new-vote interchangeable / not already settled interchangeable

**层次**：实现 / 回放时再签 not already double-signed / not already new-vote / not already settled 正式三事（298 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「回放时再签 not already double-signed / not already new-vote / not already settled 正式三事（298 余量）/ not 981 wal-notresign interchangeable / not 298 wal-vs-signed bundled interchangeable」，不是预写日志 bundled（298），也不是半写已经原子（5），也不是一条连接就已经是四门（307/979）。不要另写怎样按旋转体积切文件或怎样从损坏里恢复。

## 官方三件事

1. **看见崩溃后回放上一高度 / 看见私钥签名器在回放时又要签 这份回放 is not already 已经双签 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 981 wal-notresign interchangeable / 980 wal-notfsync interchangeable / 298 wal item 1 写下 interchangeable，也不是已经回放时再签 not already double-signed / not already new-vote / not already settled 正式三事 bundled（298 item 2 余量） interchangeable / 298 wal item 2 interchangeable。**  
   官方写：崩溃后，共识模块会回放 WAL 里上一高度写下的全部消息。私钥签名器有点各走各的，并不知道正在回放，回放时可能再想签。看见签名器又要签，不是已经双签 interchangeable——本页从 298 item 2 侧钉 not already double-signed 单句。298 wal vs signed bundled unbundling 在本页 item 2 续。

2. **看见回放 / 看见这次失败 / 这份回放 is not already 已经对外发出新票 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 981 wal-notresign interchangeable / 298 wal item 3 LastSignBytes interchangeable / 982 wal-notheight interchangeable，也不是已经半写已经原子 interchangeable / 5 atomic interchangeable。**  
   官方把回放和已经对外发出新票分开。看见回放，不是已经发出新票 interchangeable。本页钉 not already new-vote 单句。

3. **看见这次失败 / 看见又要签 / 这份回放 is not already 已经交差 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 981 wal-notresign interchangeable / 980 wal-notfsync interchangeable，也不是已经一条连接就已经是四门 interchangeable / 307/979 abci-conn-notgates interchangeable。**  
   官方把这次失败和回放已经坏了分开。看见这次失败，不是已经交差 interchangeable。298 wal vs signed bundled unbundling 在本页 item 2 续。

旋转体积、总上限、损坏恢复步骤是规范或运维里的取值或做法，本页不抄。

## 官方为什么这样拆

- **回放时再签 not already double-signed ≠ 已经双签 interchangeable：** 官方把签名器不知道正在回放、先失败再看见 WAL 里旧票，写成正常回放。
- **看见回放 not already new-vote ≠ 已经对外发出新票 interchangeable：** 官方把回放和已经对外发出新票分开。
- **看见这次失败 not already settled ≠ 已经交差 interchangeable：** 官方把这次失败和回放已经坏了分开；298 wal vs signed bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回放时又要签 | 不是已经双签 | 不是半写已经原子（5） |
| 看见回放 | 不是已经对外发出新票 | 不是一条连接就已经是四门（307/979） |
| 看见这次失败 | 不是已经交差 | 不是 LastSignBytes 对上就已经换了高度（982） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回放时再签 not already double-signed / not already new-vote / not already settled 正式三事（298 余量），必须分开是不是已经双签、是不是已经发出新票、是不是已经交差。可以跳过「看见写下就已经防了双签」。不要另写怎样按旋转体积切文件或怎样从损坏里恢复。298 wal vs signed bundled unbundling 在本页 item 2 续；续 [`worked-example-wal-notheight-vs-bundled.md`](worked-example-wal-notheight-vs-bundled.md)（不变量 982 item 3）。

## 本页不抄

- 旋转体积、总上限、autofile 做法。
- 预写日志 bundled。那是不变量 298。
- 半写已经原子。那是不变量 5。
- 一条连接就已经是四门。那是不变量 307/979。
