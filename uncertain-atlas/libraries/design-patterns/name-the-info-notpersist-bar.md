# 模式：把 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事（370 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[回了这两列 not already settled ≠ bundled（370）](../../tracks/implementation/worked-example-info-notpersist-vs-bundled.md)。

## 三个名字

1. **回了这两列 不是 already settled：** 看见回了这两列 / 引擎指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘 / 回了 last_block 两列，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 370 info bundled interchangeable / info-sold-as-handshake interchangeable。

2. **要在 Commit 里落 不是 already crash-commit：** 看见要在 Commit 里落 / 要在 Commit 里更新并落盘 / 指望落盘，不是已经是崩溃三步已经 Commit interchangeable / 已经 crash-commit interchangeable / 已经是崩溃三步已经 Commit 交差 interchangeable，不是 320 crashsteps interchangeable / 857 info-notstatesync interchangeable。

3. **有高度 不是 already pruning：** 看见有高度 / 有 `last_block_height` / 高度列在，不是已经在剪 interchangeable / 已经 pruning interchangeable / 已经在剪交差 interchangeable，不是 858 info-notapphash interchangeable / 366 retain interchangeable。

官方把回了这两列、不是已经是崩溃三步已经 Commit、不是已经在剪写成三个名字。把它们叫成一个「看见回了这两列就已经交差 interchangeable / 就已经是崩溃三步已经 Commit interchangeable / 就已经在剪 interchangeable」，会把 not already settled、not already crash-commit、not already pruning 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差 not already settled / not already crash-commit / not already pruning 正式三事（370 余量），先数清问的是回了这两列 是不是 already settled / 370 / info-sold-as-handshake，是不是要在 Commit 里落 是不是 already crash-commit，还是有高度 是不是 already pruning，再决定要不要同一次发布。370 info-vs-handshake bundled unbundling 在本页 item 3 完成。
