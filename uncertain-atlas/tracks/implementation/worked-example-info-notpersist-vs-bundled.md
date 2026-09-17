# 例：看见 last_block_app_hash / last_block_height 要在 Commit 里落盘 is not already settled interchangeable / not already crash-three-step Commit interchangeable / not already pruning interchangeable

**层次**：实现 / last_block 落盘 not already settled / not already crash-three-step Commit / not already pruning 正式三事（370 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「last_block 落盘 not already settled / not already crash-three-step Commit / not already pruning 正式三事（370 余量）/ not 817 info-notpersist interchangeable / not 370 info-vs-handshake bundled interchangeable」，不是 Info 握手 bundled（370），也不是崩溃三步就已经 Commit（320），也不是 Commit persist signal 就已经落盘（481），也不是 Info Usage last_block 就已经是 370 bundled（497/665）。不要另写怎样写 Info 握手。

## 官方三件事

1. **看见引擎指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘 / 看见回了这两列 / 这份落盘 is not already 已经交差 interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 817 info-notpersist interchangeable / 815 info-notreplay interchangeable / 370 info item 1 握手 interchangeable，也不是已经 last_block 落盘 not already settled / not already crash-three-step Commit / not already pruning 正式三事 bundled（370 item 3 余量） interchangeable / 370 info item 3 interchangeable。**  
   官方写：CometBFT 指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘。看见回了这两列，不是已经交差 interchangeable——本页从 370 item 3 侧钉 not already settled 单句。370 info vs handshake bundled unbundling 在本页 item 3 完成。

2. **看见回了这两列 / 看见要在 Commit 里落 / 这份落盘 is not already 已经是崩溃三步已经 Commit interchangeable / 320 crash interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 817 info-notpersist interchangeable / 370 info item 2 app_version interchangeable / 816 info-notapphash interchangeable，也不是已经 Commit persist signal 就已经落盘 interchangeable / 481 persist / 701 persist-notsignal interchangeable，也不是已经 Info Usage last_block 就已经是 370 bundled interchangeable / 497 infousage / 665 infousage-notcommitpersist interchangeable。**  
   官方把要在 Commit 里落和已经是崩溃三步已经 Commit 分开——370 bundled 第三件事常与 320 / 481 / 497 混成「看见回了这两列就已经交差或已经 Commit interchangeable」，本页钉 not already crash-three-step Commit 单句。

3. **看见回了这两列 / 看见有高度 / 这份落盘 is not already 已经在剪 interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 817 info-notpersist interchangeable / 815 info-notreplay interchangeable，也不是已经 retain_height 就已经在剪 interchangeable / 491 retain / 692 retain-notcaution interchangeable。**  
   官方把有高度和已经在剪分开。看见有高度，不是已经在剪 interchangeable。370 info vs handshake bundled unbundling 在本页 item 3 完成。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。

## 官方为什么这样拆

- **last_block 落盘 not already settled ≠ 已经交差 interchangeable：** 官方把要落盘和已经交差分开。
- **看见要在 Commit 里落 not already crash-three-step ≠ 320 interchangeable：** 官方把要落盘和崩溃三步已经 Commit 分开。
- **看见有高度 not already pruning ≠ 已经在剪 interchangeable：** 官方把有高度和已经在剪分开；370 info vs handshake bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| last_block_app_hash / last_block_height 要在 Commit 里落盘 | 不是已经交差 | 不是握手对齐（815/370 item 1） |
| 看见要在 Commit 里落 | 不是已经是崩溃三步已经 Commit（320） | 不是 persist signal（481/701） |
| 看见有高度 | 不是已经在剪 | 不是 Info Usage last_block（497/665） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 last_block 落盘 not already settled / not already crash-three-step Commit / not already pruning 正式三事（370 余量），必须分开是不是已经交差、是不是已经是崩溃三步已经 Commit interchangeable / 320、是不是已经在剪。可以跳过「看见回了这两列就已经交差」。不要另写怎样写 Info 握手。370 info vs handshake bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Info 握手 bundled。那是不变量 370。
- 握手对齐。那是不变量 370 item 1 余量 / 815。
- 崩溃三步就已经 Commit。那是不变量 320。
- Commit persist signal 就已经落盘。那是不变量 481 / 701。
