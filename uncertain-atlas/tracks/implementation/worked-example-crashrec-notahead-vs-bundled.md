# 例：看见应用高度比引擎高 is not already allowed interchangeable / not already recover-alone interchangeable / not already same-as-atomic interchangeable

**层次**：实现 / 应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事（320 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事（320 余量）/ not 1019 crashrec-notahead interchangeable / not 320 crash-steps-vs-commit bundled interchangeable」，不是 Crash Recovery bundled（320），也不是半写已经原子（5），也不是 WAL 已经 fsync（298）。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

1. **看见应用高度比引擎高 / 看见应用先落了盘 这份恢复 is not already 已经允许 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1019 crashrec-notahead interchangeable / 1020 crashrec-notcommit interchangeable / 320 crash item 2 块进 store interchangeable，也不是已经应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事 bundled（320 item 1 余量） interchangeable / 320 crash item 1 interchangeable。**  
   官方写：CometBFT 和应用被指望一起崩。不该出现应用已经持久化的高度，高于 CometBFT 已经持久化的最新高度。看见应用先写完，不是已经合法 interchangeable——本页从 320 item 1 侧钉 not already allowed 单句。320 crash-steps vs commit bundled unbundling 在本页 item 1 启动。

2. **看见两边高度不一样 / 看见应用先落了盘 / 这份恢复 is not already 已经能各醒各的 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1019 crashrec-notahead interchangeable / 320 crash item 3 Info interchangeable / 1021 crashrec-notskip interchangeable，也不是已经半写已经原子 interchangeable / 5 atomic interchangeable。**  
   官方把两边高度不一样和已经能各醒各的分开。看见两边高度不一样，不是已经能各醒各的 interchangeable。本页钉 not already recover-alone 单句。

3. **看见能单独重启应用 / 看见应用先落了盘 / 这份恢复 is not already 已经和半写已经原子同一句 interchangeable，也不是已经 Crash Recovery bundled（320） interchangeable / 1019 crashrec-notahead interchangeable / 1020 crashrec-notcommit interchangeable，也不是已经 WAL 已经 fsync interchangeable / 298 wal interchangeable。**  
   官方把能单独重启应用和已经和半写已经原子同一句分开。看见能单独重启应用，不是已经和半写已经原子同一句 interchangeable。320 crash-steps vs commit bundled unbundling 在本页 item 1 启动。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **应用比引擎高 not already allowed ≠ 已经允许 interchangeable：** 官方把一起崩和不许应用领先分开。
- **看见两边高度不一样 not already recover-alone ≠ 已经能各醒各的 interchangeable：** 官方把两边高度不一样和已经能各醒各的分开。
- **看见能单独重启应用 not already same-as-atomic ≠ 已经和半写已经原子同一句 interchangeable：** 官方把能单独重启应用和已经和半写已经原子同一句分开；320 crash-steps vs commit bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用高度比引擎高 | 不是已经允许 | 不是半写已经原子（5） |
| 看见两边高度不一样 | 不是已经能各醒各的 | 不是 WAL 已经 fsync（298） |
| 看见能单独重启应用 | 不是已经和半写已经原子同一句 | 不是块进 store 就已经 Commit（1020） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事（320 余量），必须分开是不是已经允许、是不是已经能各醒各的、是不是已经和半写已经原子同一句。可以跳过「看见块已经进 store 就已经交差」。不要另写怎样落盘或怎样写 Commit。320 crash-steps vs commit bundled unbundling 在本页 item 1 启动；续 [`worked-example-crashrec-notcommit-vs-bundled.md`](worked-example-crashrec-notcommit-vs-bundled.md)（不变量 1020 item 2）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- Crash Recovery bundled。那是不变量 320。
- 半写已经原子。那是不变量 5。
- WAL 已经 fsync。那是不变量 298。
