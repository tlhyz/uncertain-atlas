# 反模式：把 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事（370 余量）说成已经交差 / 已经是崩溃三步已经 Commit / 已经在剪

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了这两列 not already settled ≠ bundled（370）](../../tracks/implementation/worked-example-info-notpersist-vs-bundled.md)。

## 卖法

把回了这两列 / 引擎指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘 / 回了 last_block 两列 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 370 info bundled interchangeable / info-sold-as-handshake interchangeable；把要在 Commit 里落 / 要在 Commit 里更新并落盘 / 指望落盘 写成已经是崩溃三步已经 Commit interchangeable / 已经 crash-commit interchangeable / 已经是崩溃三步已经 Commit 交差 interchangeable；把有高度 / 有 `last_block_height` / 高度列在 写成已经在剪 interchangeable / 已经 pruning interchangeable / 已经在剪交差 interchangeable，或已经和 370 info bundled / info-sold-as-handshake interchangeable / 859 info-notpersist interchangeable。

## 为什么错

官方把回了这两列、不是已经是崩溃三步已经 Commit、不是已经在剪写成三件独立的实现事。把它们卖成 already settled interchangeable / already crash-commit interchangeable / already pruning interchangeable，会把 not already settled、not already crash-commit、not already pruning 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事（370 余量），必须分开 not already settled、not already crash-commit、not already pruning 三件事，不要和 370 / 320 / 857 / 858 糊成一句。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 info bundled 全段，不是本页回了这两列 item 3 单句边界。
- [info-notstatesync-sold-as-bundled](info-notstatesync-sold-as-bundled.md) 是握手对齐 not already statesync（370 item 1），不是本页 not already settled 边界。
- [info-notapphash-sold-as-bundled](info-notapphash-sold-as-bundled.md) 是 app_version 进头 not already apphash（370 item 2），不是本页 not already crash-commit 边界。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是崩溃三步就已经 Commit（320），不是本页 not already crash-commit 单句。
