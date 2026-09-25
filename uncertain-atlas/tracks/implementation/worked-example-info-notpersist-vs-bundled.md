# 例：看见回了这两列 / 看见要在 Commit 里落 / 看见有高度 is not already already settled interchangeable / already crash-commit interchangeable / already pruning interchangeable

**层次**：实现 / last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事（370 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事（370 余量）/ not 859 info-notpersist interchangeable / not 370 info bundled interchangeable」，不是 info bundled（370），也不是 Info 用来握手对齐不是已经是快照重放（857 item 1 余量）或 app_version 进每块头不是已经印进本头 AppHash（858 item 2 余量）。不要另写怎样写 Info 握手。

## 官方三件事

规范把 Methods 里引擎指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘 和「已经是回了这两列就已经交差 interchangeable / 已经是要在 Commit 里落就已经是崩溃三步已经 Commit interchangeable / 已经是有高度就已经在剪 interchangeable / 已经是 info bundled interchangeable」分开写成三件独立的实现事，不是「看见回了这两列就已经交差 interchangeable / 就已经是崩溃三步已经 Commit interchangeable / 就已经在剪 interchangeable」一件事：

1. **看见回了这两列 / 看见引擎指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘 / 看见回了 last_block 两列 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 370 info bundled interchangeable / 320 crashsteps interchangeable / info-sold-as-handshake interchangeable，也不是已经 info bundled（370） interchangeable / 859 info-notpersist interchangeable / 370 info item 3 interchangeable，也不是已经 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事 bundled（370 item 3 余量） interchangeable / 370 info item 3 interchangeable，也不是已经握手对齐就已经是快照重放（857） interchangeable / 858 info-notapphash interchangeable / 147 apphash interchangeable，也不是已经崩溃三步就已经 Commit（320） interchangeable。**  
   官方写：CometBFT 指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘。看见回了这两列，不是已经交差。看见回了这两列，不是已经 settled interchangeable——370 钉 bundled 三事，本页从 item 3 侧钉 not already settled 单句。看见引擎指望这两列在 Commit 里更新并落盘，不是已经 info bundled（370） interchangeable——370 钉 bundled，本页钉 item 3 第一件事。看见回了这两列，不是已经握手对齐就已经是快照重放（857） interchangeable——857 另钉 item 1。看见回了这两列，不是已经 app_version 进头就已经印进本头 AppHash（858） interchangeable——858 另钉 item 2。370 info-vs-handshake bundled unbundling 在本页 item 3 完成。

2. **看见要在 Commit 里落 / 看见要在 Commit 里更新并落盘 / 看见指望落盘 is not already 已经是崩溃三步已经 Commit interchangeable / 已经 crash-commit interchangeable / 已经是崩溃三步已经 Commit 交差 interchangeable / 370 info bundled interchangeable / 320 crashsteps interchangeable，也不是已经 info bundled（370） interchangeable / 859 info-notpersist interchangeable / 370 info item 1 握手 interchangeable / 370 info item 2 进头 interchangeable，也不是已经 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事 bundled（370 item 3 余量） interchangeable / 370 info item 3 interchangeable，也不是已经交差（本页第一件事） interchangeable。**  
   官方写：看见要在 Commit 里落，不是已经是崩溃三步已经 Commit。看见要在 Commit 里更新并落盘，不是已经 crash-commit interchangeable——本页钉 not already crash-commit 单句。看见指望落盘，不是已经交差（本页第一件事） interchangeable——三件事分开钉。370 info-vs-handshake bundled unbundling 在本页 item 3 完成。

3. **看见有高度 / 看见有 `last_block_height` / 看见高度列在 is not already 已经在剪 interchangeable / 已经 pruning interchangeable / 已经在剪交差 interchangeable / 370 info bundled interchangeable / 366 retain interchangeable，也不是已经 info bundled（370） interchangeable / 859 info-notpersist interchangeable / 370 info item 1 / 370 info item 2，也不是已经 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事 bundled（370 item 3 余量） interchangeable / 370 info item 3 interchangeable，也不是已经交差（本页第一件事） interchangeable / 已经是崩溃三步已经 Commit（本页第二件事） interchangeable。**  
   官方写：看见有高度，不是已经在剪。看见有 `last_block_height`，不是已经 pruning interchangeable——本页钉 not already pruning 单句。看见高度列在，不是已经是崩溃三步已经 Commit（本页第二件事） interchangeable——三件事分开钉。370 info-vs-handshake bundled unbundling 在本页 item 3 完成。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。info bundled（370）、Info 用来握手对齐不是已经是快照重放（370 item 1 余量 / 857）、app_version 进每块头不是已经印进本头 AppHash（370 item 2 余量 / 858）、崩溃三步就已经 Commit（320）、本头 AppHash 就已经是本高度交差（147）、QueryState 就已经是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了这两列 not already settled ≠ 370 / 320 interchangeable：** 官方把要落盘和已经交差分开。
- **要在 Commit 里落 not already crash-commit ≠ 已经是崩溃三步已经 Commit interchangeable：** 官方把要落盘和已经崩溃三步 Commit 分开。
- **有高度 not already pruning ≠ 已经在剪 interchangeable：** 官方把有高度和已经在剪分开；370 info-vs-handshake bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了这两列 | 不是 already settled | 不是崩溃三步就已经 Commit alone（320） |
| 要在 Commit 里落 | 不是 already crash-commit | 不是握手对齐 already statesync alone（857） |
| 有高度 | 不是 already pruning | 不是 app_version 进头 already apphash alone（858） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事（370 余量），必须分开回了这两列 是不是 already settled interchangeable / 370 info bundled interchangeable / info-sold-as-handshake interchangeable、要在 Commit 里落 是不是 already crash-commit interchangeable、有高度 是不是 already pruning interchangeable。可以跳过「看见回了这两列就已经交差 interchangeable / 就已经是崩溃三步已经 Commit interchangeable / 就已经在剪 interchangeable」。不要另写怎样写 Info 握手。370 info-vs-handshake bundled unbundling 在本页 item 3 完成（857 + 858 + 859）。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- info bundled。那是不变量 370。
- Info 用来握手对齐不是已经是快照重放。那是不变量 370 item 1 余量 / 857。
- app_version 进每块头不是已经印进本头 AppHash。那是不变量 370 item 2 余量 / 858。
- 崩溃三步就已经 Commit。那是不变量 320。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
