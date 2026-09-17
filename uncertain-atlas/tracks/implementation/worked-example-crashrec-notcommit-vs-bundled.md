# 例：看见块进了 blockstore is not already settled interchangeable / not already committed interchangeable / not already atomic interchangeable

**层次**：实现 / 块进 store not already settled / not already committed / not already atomic 正式三事（320 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「块进 store not already settled / not already committed / not already atomic 正式三事（320 余量）/ not 1020 crashrec-notcommit interchangeable / not 320 crash-steps-vs-commit bundled interchangeable」，不是 Crash Recovery bundled（320），也不是 WAL 已经 fsync（298），也不是 Finalize 禁令 persist（335）。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

1. **看见块已经进 blockstore / 看见 Finalize 结果已经落盘 这份恢复 is not already 已经交差 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1020 crashrec-notcommit interchangeable / 1019 crashrec-notahead interchangeable / 320 crash item 1 应用比引擎高 interchangeable，也不是已经块进 store not already settled / not already committed / not already atomic 正式三事 bundled（320 item 2 余量） interchangeable / 320 crash item 2 interchangeable。**  
   官方写：一个高度算持久化，要走三步，最后一步才是应用的 Commit，也是应用唯一被指望持久化/提交自己状态的地方。看见块存了，不是已经交差 interchangeable——本页从 320 item 2 侧钉 not already settled 单句。320 crash-steps vs commit bundled unbundling 在本页 item 2 续。

2. **看见结果存了 / 看见块进了 store / 这份恢复 is not already 应用已经提交 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1020 crashrec-notcommit interchangeable / 320 crash item 3 Info interchangeable / 1021 crashrec-notskip interchangeable，也不是已经 WAL 已经 fsync interchangeable / 298 wal interchangeable。**  
   官方把结果存了和应用已经提交分开。看见结果存了，不是应用已经提交 interchangeable。本页钉 not already committed 单句。

3. **看见三步 / 看见块进了 store / 这份恢复 is not already 已经原子 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1020 crashrec-notcommit interchangeable / 1019 crashrec-notahead interchangeable，也不是已经 Finalize 禁令 persist interchangeable / 335 finalize-persist interchangeable。**  
   官方把三步和已经原子分开。看见三步，不是已经原子 interchangeable。320 crash-steps vs commit bundled unbundling 在本页 item 2 续。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **块进 store not already settled ≠ 已经交差 interchangeable：** 官方把三步和只有 Commit 才让应用落盘分开。
- **看见结果存了 not already committed ≠ 应用已经提交 interchangeable：** 官方把结果存了和应用已经提交分开。
- **看见三步 not already atomic ≠ 已经原子 interchangeable：** 官方把三步和已经原子分开；320 crash-steps vs commit bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 块进 store / 结果落盘 | 不是已经 Commit | 不是 WAL 已经 fsync（298） |
| 看见结果存了 | 不是应用已经提交 | 不是 Finalize 禁令 persist（335） |
| 看见三步 | 不是已经原子 | 不是启动 Info 对上就已经能跳步（1021） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看块进 store not already settled / not already committed / not already atomic 正式三事（320 余量），必须分开是不是已经交差、是不是应用已经提交、是不是已经原子。可以跳过「看见块已经进 store 就已经交差」。不要另写怎样落盘或怎样写 Commit。320 crash-steps vs commit bundled unbundling 在本页 item 2 续；续 [`worked-example-crashrec-notskip-vs-bundled.md`](worked-example-crashrec-notskip-vs-bundled.md)（不变量 1021 item 3）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- Crash Recovery bundled。那是不变量 320。
- WAL 已经 fsync。那是不变量 298。
- Finalize 禁令 persist。那是不变量 335。
