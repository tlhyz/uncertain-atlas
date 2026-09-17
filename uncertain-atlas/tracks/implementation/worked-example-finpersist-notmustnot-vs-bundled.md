# 例：看见 FinalizeBlock changed state MUST NOT persist is not already already persisted interchangeable / already settled interchangeable / crash recovery block in store already Commit interchangeable

**层次**：实现 / FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事（335 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事（335 余量）/ not 683 finpersist-notmustnot interchangeable / not 335 finpersist-vs-commit bundled interchangeable」，不是 FinalizeBlock 落盘禁令 bundled（335），也不是 Signal persist application state not Finalize already persisted（481 item 1 余量 / 680）或 Finalize 之后引擎才落盘 bundled（403）。不要另写怎样落盘、怎样写 Commit、怎样做 WAL 旋转。

## 官方三件事

规范把 Requirements 里 FinalizeBlock 转移状态但 **MUST NOT** 持久化 和「已经是已经落盘 interchangeable / 已经是已经交差 interchangeable / 已经是崩溃恢复三步已经 Commit interchangeable / 已经半写已经原子 interchangeable」分开写成三件独立的实现事，不是「看见 Finalize 改了状态 就已经落盘 interchangeable / 就已经交差 interchangeable / 就已经能从半截高度接着走 interchangeable」一件事：

1. **看见 `FinalizeBlock` 改了状态 / 看见决定块已经交给应用 / 看见转移状态 but MUST NOT persist is not already 已经落盘 interchangeable / 已经写盘 interchangeable / 已经 Commit interchangeable / 335 finpersist bundled interchangeable / 335 finpersist item 2 MUST persist in Commit interchangeable / 335 finpersist item 3 remember last Commit height interchangeable / 481 commitpersist item 1 persist signal interchangeable / 680 commitpersist-notfinpersist interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 683 finpersist-notmustnot interchangeable / 335 finpersist-vs-commit bundled interchangeable / 335 finpersist item 1 interchangeable，也不是已经 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事 bundled（335 item 1 余量） interchangeable / 335 finpersist item 1 interchangeable，也不是已经 Signal the Application to persist application state（481） interchangeable / 645 fincommit-notpersist interchangeable / 497 infousage-persist interchangeable / 467 finpersist interchangeable，也不是已经 Application is expected to persist at end of this call（681） interchangeable / 399 commit-empty-echo bundled interchangeable。**  
   官方 Requirements 写：应用用它转移状态，但 **MUST NOT** 持久化。看见改了状态，不是已经写盘 interchangeable——335 钉 MUST NOT persist in Finalize 单句，本页从 335 item 1 侧钉 not already persisted 单句。看见决定块来了，不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable——335 钉 bundled 三事，本页钉 MUST NOT persist 单句。看见能转移，不是已经 When instruct Application to persist its state（590 / 645） interchangeable——645 另钉 When 第 8 步，本页钉 item 1 第一件事。335 finpersist vs commit bundled unbundling 在本页 item 1 启动。

2. **看见 FinalizeBlock changed state / 看见 MUST NOT persist / 看见转移状态 is not already 已经交差 interchangeable / 已经 Finalize + Commit interchangeable / 33 four gates interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 587 finreturn interchangeable / 616 finreturn-notpersist interchangeable / 601 notsettled interchangeable / 467 finpersist interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 683 finpersist-notmustnot interchangeable / 335 finpersist item 2 MUST persist in Commit interchangeable / 335 finpersist item 3 remember last Commit height interchangeable，也不是已经 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事 bundled（335 item 1 余量） interchangeable / 335 finpersist item 1 interchangeable，也不是已经 Finalize 之后引擎才落盘 bundled（403 item 1 余量 / 632） interchangeable / 632 notsettled interchangeable / 633 notlock interchangeable / 634 notrecheck interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash（587） interchangeable / 606 notoutputs interchangeable / 478 finpersist interchangeable / 605 notpersist interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 466 executes block v interchangeable / 572 not execbv interchangeable。**  
   官方把 MUST NOT persist in Finalize 单句和已经交差 / Finalize + Commit / 引擎 persist 这三份 路径分开——335 bundled 第一件事常与 33 / 403 / 587 混成「看见 Finalize 改了状态 就已经交差 interchangeable / 就已经 Finalize + Commit interchangeable / 就已经四门已经结算 interchangeable」，本页钉 not already settled 单句。看见 MUST NOT persist，不是已经 Finalize 之后引擎才落盘（403 / 632） interchangeable——403 钉 When 第 6 步引擎 persist，本页钉 Requirements MUST NOT 单句。看见转移状态，不是已经 persist decision not executes block v（605） interchangeable——605 另钉 When persist decision，本页钉 item 1 第二件事。335 finpersist vs commit bundled unbundling 在本页 item 1 启动。

3. **看见 FinalizeBlock changed state / 看见 MUST NOT persist / 看见转移状态 is not already 已经崩溃恢复三步已经 Commit interchangeable / 块进 store 已经 Commit interchangeable / 启动 Info 对上已经能跳步 interchangeable / 320 crash recovery interchangeable / 38 genesis-replay interchangeable / 323 full-history interchangeable / 5 half-write atomic interchangeable / 310 commit-lock-vs-rpc interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 683 finpersist-notmustnot interchangeable / 335 finpersist item 2 MUST persist in Commit interchangeable / 335 finpersist item 3 remember last Commit height interchangeable，也不是已经 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事 bundled（335 item 1 余量） interchangeable / 335 finpersist item 1 interchangeable，也不是已经记住上次成功 Commit 高度 bundled（335 item 3 余量 / 684 余量） interchangeable / 684 finpersist-notmustincommit interchangeable / 335 finpersist item 3 interchangeable，也不是已经必须在 Commit 落盘 bundled（335 item 2 余量 / 684） interchangeable / 481 commitpersist interchangeable / 681 commitpersist-notendofcall interchangeable，也不是已经默认锁已经 RPC 安全 interchangeable / 310 commitlock interchangeable / 588 finlock interchangeable。**  
   官方把 MUST NOT persist in Finalize 单句和崩溃恢复三步 / 块进 store 已经 Commit / 半写已经原子 路径分开——335 bundled 第一件事常与 320 混成「看见 Finalize 改了状态 就已经崩溃恢复已经 Commit interchangeable / 就已经块进 store interchangeable / 就已经能从半截高度接着走 interchangeable」，本页钉 not crash recovery block in store already Commit 单句。看见 MUST NOT persist，不是已经崩溃恢复三步已经交差 interchangeable——320 钉 crash recovery 全段，本页钉 item 1 单句。看见转移状态，不是已经半写已经原子（5） interchangeable——5 另钉原子性，本页钉 item 1 第三件事。335 finpersist vs commit bundled unbundling 在本页 item 1 启动。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的做法，本页不抄。FinalizeBlock 落盘禁令 bundled（335）、必须在 Commit 落盘 not already persisted in Finalize（335 item 2 余量 / 684）、记住上次成功 Commit 高度 not already can skip steps（335 item 3 余量）、Signal persist application state not Finalize already persisted（481 item 1 余量 / 680）、Finalize 之后引擎才落盘 bundled（403）、崩溃恢复三步已经交差（320）、默认锁已经 RPC 安全（310）、半写已经原子（5）是另外那套，本页不抄。

## 官方为什么这样拆

- **MUST NOT persist not already persisted ≠ 684 finpersist-notmustincommit interchangeable：** 官方把 Requirements MUST NOT persist in Finalize 单句和 MUST persist in Commit 路径分开。
- **MUST NOT persist not already settled ≠ 680 commitpersist-notfinpersist interchangeable：** 官方把 MUST NOT persist 单句和已经交差 / 引擎 persist 这三份 / Signal persist 路径分开。
- **MUST NOT persist not crash recovery block in store already Commit ≠ 320 crash recovery interchangeable：** 官方把 MUST NOT persist 单句和崩溃恢复三步 / 块进 store 已经 Commit 路径分开；335 finpersist vs commit bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlock changed state MUST NOT persist | 不是 already persisted | 不是 MUST persist in Commit alone（684/335 item 2） |
| MUST NOT persist | 不是 already settled | 不是 Finalize 之后引擎 persist（403/632） |
| 转移状态 | 不是 crash recovery already Commit | 不是 remember last Commit height（684 item 3/335 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事（335 余量），必须分开 MUST NOT persist 是不是 already persisted interchangeable / 335 finpersist bundled interchangeable / 684 finpersist-notmustincommit interchangeable / 481 commitpersist interchangeable、Finalize 改了状态 是不是 already settled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 587 finreturn interchangeable、MUST NOT persist 是不是 crash recovery block in store already Commit interchangeable / 320 crash recovery interchangeable / 5 half-write atomic interchangeable / 310 commitlock interchangeable。可以跳过「看见 Finalize 改了状态 就已经落盘 interchangeable / 就已经交差 interchangeable / 就已经崩溃恢复已经 Commit interchangeable」。不要另写怎样落盘。335 finpersist vs commit bundled unbundling 在本页 item 1 完成；续 [`worked-example-finpersist-notmustincommit-vs-bundled.md`](worked-example-finpersist-notmustincommit-vs-bundled.md)（不变量 684 item 2）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- FinalizeBlock 落盘禁令 bundled。那是不变量 335。
- 必须在 Commit 落盘 not already persisted in Finalize。那是不变量 335 item 2 余量 / 684。
- 记住上次成功 Commit 高度 not already can skip steps。那是不变量 335 item 3 余量。
- Signal persist application state not Finalize already persisted。那是不变量 481 item 1 余量 / 680。
- Finalize 之后引擎才落盘 bundled。那是不变量 403。
- 崩溃恢复三步已经交差。那是不变量 320。
- 默认锁已经 RPC 安全。那是不变量 310。
- 半写已经原子。那是不变量 5。
