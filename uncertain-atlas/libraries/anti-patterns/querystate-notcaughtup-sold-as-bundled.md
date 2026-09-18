# 反模式：把上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事（314 余量）说成已经跟上 / 已经是 CheckTxState / 已经同步

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[上次 Commit not already caught up ≠ bundled（314）](../../tracks/implementation/worked-example-querystate-notcaughtup-vs-bundled.md)。

## 卖法

把上次 Commit / QueryState / 提交到盘之后的副本 写成已经跟上正在跑的块 interchangeable / 已经 caught up interchangeable / 已经含本轮还没交差的执行 interchangeable / 314 querystate bundled interchangeable / 312 checktxstate bundled interchangeable / querystate-sold-as-execute interchangeable；把能读 / 可以查 / 只读副本能答 写成已经是内存池那份 CheckTxState interchangeable / 已经 CheckTxState interchangeable；把只读 / 只读副本 / QueryState 只读 写成已经和正在改的 ExecuteTxState 同步 interchangeable / 已经 synced interchangeable，或已经和 314 querystate bundled / querystate-sold-as-execute interchangeable / 702 querystate-notcaughtup interchangeable。

## 为什么错

官方把上次 Commit 单句、already caught up、already CheckTxState、already synced 写成三件独立的实现事。把它们卖成 already caught up interchangeable / already CheckTxState interchangeable / already synced interchangeable，会把 not already caught up、not already CheckTxState、not already synced 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事（314 余量），必须分开 not already caught up、not already CheckTxState、not already synced 三件事，不要和 314 / 312 / 701 / 703 / 310 / 33 糊成一句。

## 和相邻反模式

- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState vs ExecuteTxState bundled 全段，不是本页上次 Commit item 2 单句边界。
- [querystate-notexecute-sold-as-bundled](querystate-notexecute-sold-as-bundled.md) 是能查 item 1，不是本页跟上正在跑的块边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState vs ExecuteTxState（312），不是本页能读是否已经是 CheckTxState 边界。
