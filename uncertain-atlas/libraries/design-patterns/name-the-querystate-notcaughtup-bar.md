# 模式：把上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事（314 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**例**：[上次 Commit not already caught up ≠ bundled（314）](../../tracks/implementation/worked-example-querystate-notcaughtup-vs-bundled.md)。

## 三个名字

1. **上次 Commit 不是 already caught up：** 看见 QueryState / 提交到盘之后的副本，不是已经跟上正在跑的块 interchangeable / 已经含本轮还没交差的执行 interchangeable，不是 314 querystate bundled interchangeable / 312 checktxstate bundled interchangeable / querystate-sold-as-execute interchangeable。

2. **能读 不是 already CheckTxState：** 看见可以查 / 只读副本能答，不是已经是内存池那份 CheckTxState interchangeable / 已经是 CheckTx 那份 interchangeable，不是 314 querystate item 1 interchangeable / 701 querystate-notexecute interchangeable。

3. **只读 不是 already synced：** 看见只读副本 / QueryState 只读，不是已经和正在改的 ExecuteTxState 同步 interchangeable / 已经跟上执行那份 interchangeable，不是 314 querystate item 3 interchangeable / 703 querystate-notsnapshot interchangeable。

官方把上次 Commit 单句、already caught up、already CheckTxState、already synced 写成三个名字。把它们叫成一个「看见上次 Commit 就已经跟上 interchangeable / 就已经是 CheckTxState interchangeable / 就已经同步 interchangeable」，会把 not already caught up、not already CheckTxState、not already synced 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事（314 余量），先数清问的是上次 Commit 是不是 already caught up / 314 / querystate-sold-as-execute，是不是能读 是不是 already CheckTxState，还是只读 是不是 already synced，再决定要不要同一次发布。314 querystate vs execute bundled unbundling 在本页 item 2 完成。
