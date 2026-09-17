# 例：看见启动 Info 对上了 is not already any-height interchangeable / not already skip-replay interchangeable / not already no-reinit interchangeable

**层次**：实现 / 启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事（320 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事（320 余量）/ not 1021 crashrec-notskip interchangeable / not 320 crash-steps-vs-commit bundled interchangeable」，不是 Crash Recovery bundled（320），也不是启动对齐已经是快照重放（314），也不是 Commit 锁（310）。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

1. **看见启动 Info / 看见对上了 这份恢复 is not already 已经是任意高度 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1021 crashrec-notskip interchangeable / 1019 crashrec-notahead interchangeable / 320 crash item 1 应用比引擎高 interchangeable，也不是已经启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事 bundled（320 item 3 余量） interchangeable / 320 crash item 3 interchangeable。**  
   官方写：醒来时 CometBFT 在 Info 连接上叫 Info，应用必须回与上次成功完成 Commit 的那一块一致的信息。看见 Info 绿了，不是已经能从半截高度接着走 interchangeable——本页从 320 item 3 侧钉 not already any-height 单句。320 crash-steps vs commit bundled unbundling 在本页 item 3 完成。

2. **看见对上了 / 看见启动 Info / 这份恢复 is not already 已经跳过重放 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1021 crashrec-notskip interchangeable / 320 crash item 2 块进 store interchangeable / 1020 crashrec-notcommit interchangeable，也不是已经启动对齐已经是快照重放 interchangeable / 314 querystate interchangeable。**  
   官方把对上了和已经跳过重放分开。看见对上了，不是已经跳过重放 interchangeable。本页钉 not already skip-replay 单句。

3. **看见 InitChain 叫过 / 看见启动 Info / 这份恢复 is not already 已经不用再叫 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1021 crashrec-notskip interchangeable / 1019 crashrec-notahead interchangeable，也不是已经 Commit 锁 interchangeable / 310 commit-lock interchangeable。**  
   官方把 InitChain 叫过和已经不用再叫分开。看见 InitChain 叫过，不是已经不用再叫 interchangeable。320 crash-steps vs commit bundled unbundling 在本页 item 3 完成。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **启动 Info 对上 not already any-height ≠ 已经是任意高度 interchangeable：** 官方把必须对上上次 Commit、重放、乱序 panic、InitChain 再叫分开。
- **看见对上了 not already skip-replay ≠ 已经跳过重放 interchangeable：** 官方把对上了和已经跳过重放分开。
- **看见 InitChain 叫过 not already no-reinit ≠ 已经不用再叫 interchangeable：** 官方把 InitChain 叫过和已经不用再叫分开；320 crash-steps vs commit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 启动 Info 对上 | 不是已经能跳步 | 不是启动对齐已经是快照重放（314） |
| 看见对上了 | 不是已经跳过重放 | 不是 Commit 锁（310） |
| 看见 InitChain 叫过 | 不是已经不用再叫 | 不是应用比引擎高就已经允许（1019） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事（320 余量），必须分开是不是已经是任意高度、是不是已经跳过重放、是不是已经不用再叫 InitChain。可以跳过「看见块已经进 store 就已经交差」。不要另写怎样落盘或怎样写 Commit。320 crash-steps vs commit bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- Crash Recovery bundled。那是不变量 320。
- 启动对齐已经是快照重放。那是不变量 314。
- Commit 锁。那是不变量 310。
