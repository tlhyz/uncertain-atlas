# 例：看见 LastSignBytes 对上 is not already new-height interchangeable / not already new-commit interchangeable / not already settled interchangeable

**层次**：实现 / LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事（298 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事（298 余量）/ not 982 wal-notheight interchangeable / not 298 wal-vs-signed bundled interchangeable」，不是预写日志 bundled（298），也不是四门已经结算（33），也不是默认锁就已经 RPC 安全（310/974）。不要另写怎样按旋转体积切文件或怎样从损坏里恢复。

## 官方三件事

1. **看见 LastSignBytes 对上 / 看见回放走到 precommit 这份对上 is not already 已经换了高度 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 982 wal-notheight interchangeable / 980 wal-notfsync interchangeable / 981 wal-notresign interchangeable / 298 wal item 1 写下 interchangeable，也不是已经 LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事 bundled（298 item 3 余量） interchangeable / 298 wal item 3 interchangeable。**  
   官方写：回放到 precommit 时，签名器里有 LastSignBytes，这一次会成功，然后会再回放 WAL 里那张 precommit。看见 LastSignBytes 对上，不是已经换了高度 interchangeable——本页从 298 item 3 侧钉 not already new-height 单句。298 wal vs signed bundled unbundling 在本页 item 3 完成。

2. **看见回放走到 precommit / 看见对上 / 这份对上 is not already 已经发出另一张承诺 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 982 wal-notheight interchangeable / 298 wal item 2 回放再签 interchangeable / 981 wal-notresign interchangeable，也不是已经四门已经结算 interchangeable / 33 four-gates interchangeable。**  
   官方把回放走到 precommit 和已经发出另一张承诺分开。看见回放走到 precommit，不是已经发出另一张承诺 interchangeable。本页钉 not already new-commit 单句。

3. **看见签名器这次肯签 / 看见对上 / 这份对上 is not already 已经交差 interchangeable，也不是已经预写日志 bundled（298） interchangeable / 982 wal-notheight interchangeable / 980 wal-notfsync interchangeable，也不是已经默认锁就已经 RPC 安全 interchangeable / 310/974 commit-lock-notrpc interchangeable。**  
   官方把签名器这次肯签和已经是崩溃之后的新一轮分开。看见签名器这次肯签，不是已经交差 interchangeable。298 wal vs signed bundled unbundling 在本页 item 3 完成。

旋转体积、总上限、损坏恢复步骤是规范或运维里的取值或做法，本页不抄。

## 官方为什么这样拆

- **LastSignBytes 对上 not already new-height ≠ 已经换了高度 interchangeable：** 官方把对上旧字节写成能继续回放，不是新高度的新承诺。
- **看见回放走到 precommit not already new-commit ≠ 已经发出另一张承诺 interchangeable：** 官方把回放走到 precommit 和已经发出另一张承诺分开。
- **看见签名器这次肯签 not already settled ≠ 已经交差 interchangeable：** 官方把这次肯签和已经是崩溃之后的新一轮分开；298 wal vs signed bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| LastSignBytes 对上 | 不是已经换了高度 | 不是四门已经结算（33） |
| 看见回放走到 precommit | 不是已经发出另一张承诺 | 不是默认锁就已经 RPC 安全（310/974） |
| 看见签名器这次肯签 | 不是已经交差 | 不是写下就已经刷盘（980） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事（298 余量），必须分开是不是已经换了高度、是不是已经发出另一张承诺、是不是已经交差。可以跳过「看见写下就已经防了双签」。不要另写怎样按旋转体积切文件或怎样从损坏里恢复。298 wal vs signed bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 旋转体积、总上限、autofile 做法。
- 预写日志 bundled。那是不变量 298。
- 四门已经结算。那是不变量 33。
- 默认锁就已经 RPC 安全。那是不变量 310/974。
