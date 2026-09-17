# 例：看见记住上次成功 Commit 高度 / 能告诉引擎从哪接 is not already app taller than engine interchangeable / already can skip replay interchangeable / Info handshake aligned interchangeable

**层次**：实现 / remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事（335 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事（335 余量）/ not 685 finpersist-notrememberheight interchangeable / not 335 finpersist-vs-commit bundled interchangeable」，不是 FinalizeBlock 落盘禁令 bundled（335），也不是 MUST persist in Commit（684 item 2 余量）或崩溃恢复三步已经交差 bundled（320）。不要另写怎样落盘、怎样写 Commit、怎样做 WAL 旋转。

## 官方三件事

规范把 Requirements 里应用必须记住最近一次成功跑完 `Commit` 的高度、好告诉 CometBFT 崩溃之后从哪接 和「已经是已经允许应用比引擎高 interchangeable / 已经是已经能跳过重放 interchangeable / 已经是启动 Info 对上 interchangeable / 已经是崩溃恢复三步已经交差 interchangeable」分开写成三件独立的实现事，不是「看见记住了高度 就已经能比引擎高 interchangeable / 就已经能跳步 interchangeable / 就已经 Info 对上 interchangeable」一件事：

1. **看见记住上次成功 `Commit` 的高度 / 看见应用必须记住最近一次成功跑完 Commit 的高度 / 看见能告诉引擎从哪接 is not already 已经允许应用比引擎高 interchangeable / 已经应用比引擎高已经允许 interchangeable / 320 crash recovery interchangeable / 320 crashsteps interchangeable / 5 half-write atomic interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 685 finpersist-notrememberheight interchangeable / 335 finpersist-vs-commit bundled interchangeable / 335 finpersist item 3 interchangeable，也不是已经 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事 bundled（335 item 3 余量） interchangeable / 335 finpersist item 3 interchangeable，也不是已经 MUST persist in Commit（684） interchangeable / 683 finpersist-notmustnot interchangeable / 680 commitpersist-notfinpersist interchangeable，也不是已经崩溃恢复块进 store 已经 Commit（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方 Requirements 写：应用必须记住最近一次成功跑完 `Commit` 的高度，好告诉 CometBFT 崩溃之后从哪接。看见记住了高度，不是已经允许应用比引擎高 interchangeable——320 钉崩溃恢复三步里应用不得比引擎高，本页从 335 item 3 侧钉 not already app taller than engine 单句。看见能告诉从哪接，不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable——335 钉 bundled 三事，本页钉 remember last Commit height 单句。看见记住上次成功 Commit 高度，不是已经 MUST persist in Commit（684） interchangeable——684 另钉 item 2，本页钉 item 3 第一件事。335 finpersist vs commit bundled unbundling 在本页 item 3 启动。

2. **看见记住上次成功 Commit 高度 / 看见能告诉引擎从哪接 / 看见好告诉 CometBFT 崩溃之后从哪接 is not already 已经能跳过重放 interchangeable / 已经能跳步 interchangeable / 已经 can skip steps interchangeable / 320 crash recovery interchangeable / 38 genesis-replay interchangeable / 323 full-history interchangeable / 314 querystate interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 685 finpersist-notrememberheight interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable / 335 finpersist item 2 MUST persist in Commit interchangeable，也不是已经 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事 bundled（335 item 3 余量） interchangeable / 335 finpersist item 3 interchangeable，也不是已经半写已经原子（5） interchangeable / 5 half-write atomic interchangeable / 310 commitlock interchangeable，也不是已经块进 store 已经 Commit（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方把记住高度单句和已经能跳过重放 / 已经能跳步 路径分开——335 bundled 第三件事常与 320 混成「看见记住了高度 就已经能跳步 interchangeable / 就已经能跳过重放 interchangeable / 就已经崩溃恢复已经交差 interchangeable」，本页钉 not already can skip replay 单句。看见能告诉从哪接，不是已经崩溃恢复三步已经交差（320） interchangeable——320 钉崩溃恢复三步，本页钉 Requirements remember height 单句。看见好告诉引擎从哪接，不是已经半写已经原子（5） interchangeable——5 另钉半写原子，本页钉 item 3 第二件事。335 finpersist vs commit bundled unbundling 在本页 item 3 启动。

3. **看见记住上次成功 Commit 高度 / 看见有这个高度 / 看见能告诉引擎从哪接 is not already 已经和启动 Info 对上 interchangeable / 已经 Info 握手对齐 interchangeable / 370 info-vs-handshake interchangeable / 668 infousage-notquerystate interchangeable / 669 infousage-nothandshake interchangeable / 497 infousage-persist interchangeable / 665 infousage-notcommitpersist interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 685 finpersist-notrememberheight interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable / 335 finpersist item 2 MUST persist in Commit interchangeable，也不是已经 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事 bundled（335 item 3 余量） interchangeable / 335 finpersist item 3 interchangeable，也不是已经 last_block persisted during Commit（497） interchangeable / 665 infousage-notcommitpersist interchangeable / 680 commitpersist-notfinpersist interchangeable，也不是已经崩溃恢复启动 Info 对上已经能跳步（320） interchangeable / 320 crash recovery interchangeable。**  
   官方把记住高度单句和启动 Info 对上 / Info 握手对齐路径分开——335 bundled 第三件事常与 370 / 320 混成「看见有这个高度 就已经 Info 对上 interchangeable / 就已经握手对齐 interchangeable / 就已经能跳步 interchangeable」，本页钉 not Info handshake aligned 单句。看见有这个高度，不是已经 Info 用来握手对齐（370） interchangeable——370 钉 Info vs handshake，本页钉 remember last Commit height 单句。看见能告诉从哪接，不是已经 last_block persisted during Commit（497） interchangeable——497 另钉 Info Usage persist，本页钉 item 3 第三件事。335 finpersist vs commit bundled unbundling 在本页 item 3 完成。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的做法，本页不抄。FinalizeBlock 落盘禁令 bundled（335）、FinalizeBlock changed state MUST NOT persist（335 item 1 余量 / 683）、MUST persist in Commit not already persisted in Finalize（335 item 2 余量 / 684）、崩溃恢复三步已经交差（320）、半写已经原子（5）、Info 握手对齐（370）、默认锁已经 RPC 安全 bundled（310）是另外那套，本页不抄。

## 官方为什么这样拆

- **remember last Commit height not already app taller than engine ≠ 320 crash recovery interchangeable：** 官方把 Requirements 记住高度单句和应用比引擎高已经允许路径分开。
- **remember last Commit height not already can skip replay ≠ 320 crash recovery / 5 half-write interchangeable：** 官方把记住高度单句和已经能跳过重放 / 已经能跳步路径分开。
- **remember last Commit height not Info handshake aligned ≠ 370 info-vs-handshake interchangeable：** 官方把记住高度单句和启动 Info 对上 / Info 握手对齐路径分开；335 finpersist vs commit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 记住上次成功 Commit 高度 | 不是 already app taller than engine（320） | 不是 MUST persist in Commit alone（684） |
| 能告诉引擎从哪接 | 不是 already can skip replay（320/5） | 不是 crash recovery steps alone（320） |
| 有这个高度 | 不是 Info handshake aligned（370） | 不是 last_block persisted alone（497） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事（335 余量），必须分开记住高度 是不是 already app taller than engine interchangeable / 320 crash recovery interchangeable / 5 half-write atomic interchangeable、能告诉从哪接 是不是 already can skip replay interchangeable / 320 crash recovery interchangeable / 38 genesis-replay interchangeable、有这个高度 是不是 Info handshake aligned interchangeable / 370 info-vs-handshake interchangeable / 497 infousage-persist interchangeable。可以跳过「看见记住了高度 就已经能比引擎高 interchangeable / 就已经能跳步 interchangeable / 就已经 Info 对上 interchangeable」。不要另写怎样落盘。335 finpersist vs commit bundled unbundling 在本页 item 3 完成（683 + 684 + 685）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- FinalizeBlock 落盘禁令 bundled。那是不变量 335。
- FinalizeBlock changed state MUST NOT persist。那是不变量 335 item 1 余量 / 683。
- MUST persist in Commit not already persisted in Finalize。那是不变量 335 item 2 余量 / 684。
- 崩溃恢复三步已经交差。那是不变量 320。
- 半写已经原子。那是不变量 5。
- Info 握手对齐。那是不变量 370。
- 默认锁已经 RPC 安全 bundled。那是不变量 310。
