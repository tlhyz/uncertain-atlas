# 例：看见记住上次成功 Commit 高度 is not already app ahead interchangeable / not already can skip interchangeable / not already settled interchangeable

**层次**：实现 / 记住上次成功 Commit 高度 not already app ahead / not already can skip / not already settled 正式三事（335 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「记住上次成功 Commit 高度 not already app ahead / not already can skip / not already settled 正式三事（335 余量）/ not 904 finalize-persist-notskip interchangeable / not 335 finalize-persist-vs-commit bundled interchangeable」，不是 Finalize 落盘禁令 bundled（335），也不是崩溃恢复三步已经交差（320），也不是半写已经原子（5）。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

1. **看见记住上次成功 `Commit` 的高度 / 看见能告诉引擎从哪接 这份高度 is not already 已经能单独比引擎高 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 904 finalize-persist-notskip interchangeable / 902 finalize-persist-notdisk interchangeable / 335 finalize-persist item 1 改了状态 interchangeable，也不是已经记住上次成功 Commit 高度 not already app ahead / not already can skip / not already settled 正式三事 bundled（335 item 3 余量） interchangeable / 335 finalize-persist item 3 interchangeable。**  
   官方写：应用必须记住最近一次成功跑完 `Commit` 的高度，好告诉 CometBFT 崩溃之后从哪接。看见记住了高度，不是已经允许应用比引擎高 interchangeable——本页从 335 item 3 侧钉 not already app ahead 单句。335 finalize-persist vs commit bundled unbundling 在本页 item 3 完成。

2. **看见能告诉从哪接 / 看见记住了高度 / 这份高度 is not already 已经能跳步 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 904 finalize-persist-notskip interchangeable / 335 finalize-persist item 2 Commit 落盘 interchangeable / 903 finalize-persist-notfin interchangeable，也不是已经崩溃恢复三步已经交差 interchangeable / 320 crash-recover interchangeable。**  
   官方把能告诉从哪接和已经跳过重放分开——335 bundled 第三件事常与 320 混成「看见记住了高度就已经能跳步或已经和启动 Info 对上 interchangeable」，本页钉 not already can skip 单句。

3. **看见有这个高度 / 看见能告诉从哪接 / 这份高度 is not already 已经交差 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 904 finalize-persist-notskip interchangeable / 902 finalize-persist-notdisk interchangeable，也不是已经和启动 Info 对上同一句 interchangeable / 320 info interchangeable。**  
   官方把有这个高度和已经交差 / 已经和启动 Info 对上同一句分开。看见有这个高度，不是已经交差 interchangeable。335 finalize-persist vs commit bundled unbundling 在本页 item 3 完成。

怎样落盘、怎样写 `Commit`、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **记住上次成功 Commit 高度 not already app ahead ≠ 已经能单独比引擎高 interchangeable：** 官方把记住高度和不许领先分开。
- **看见能告诉从哪接 not already can skip ≠ 已经能跳步 interchangeable：** 官方把告诉引擎从哪接和已经跳过重放分开。
- **看见有这个高度 not already settled ≠ 已经交差 interchangeable：** 官方把有这个高度和已经交差分开；335 finalize-persist vs commit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 记住上次成功 Commit 高度 | 不是已经能单独比引擎高 | 不是崩溃恢复三步已经交差（320） |
| 看见能告诉从哪接 | 不是已经能跳步 | 不是半写已经原子（5） |
| 看见有这个高度 | 不是已经交差 | 不是 Finalize 改了就已经落盘（902） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看记住上次成功 Commit 高度 not already app ahead / not already can skip / not already settled 正式三事（335 余量），必须分开是不是已经能单独比引擎高、是不是已经能跳步、是不是已经交差。可以跳过「看见记住了高度就已经能跳步」。不要另写怎样落盘或怎样写 Commit。335 finalize-persist vs commit bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样落盘、怎样写 `Commit`、怎样做 WAL 旋转。
- Finalize 落盘禁令 bundled。那是不变量 335。
- Finalize 改了就已经落盘。那是不变量 335 item 1 余量 / 902。
- 崩溃恢复三步已经交差。那是不变量 320。
- 半写已经原子。那是不变量 5。
