# 模式：把 FinalizeBlock 落盘禁令三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**例**：[Finalize 改了状态 ≠ 已经落盘](../../tracks/implementation/worked-example-finalize-persist-vs-commit.md)。

## 三个名字

1. **Finalize 改了状态不是已经落盘：** 看见决定块已经交给应用不是已经交差。
2. **必须在 Commit 落盘不是已经在 Finalize 落了：** 看见返回前写完不是内存池锁已经放下。
3. **记住上次成功 Commit 高度不是已经能跳步：** 看见能告诉引擎从哪接不是已经允许应用比引擎高。

## 为什么要分开叫

官方把 Finalize 只许转移状态、Commit 才许落盘、记住上次成功 Commit 高度写成三件事。把它们叫成一个「看见 Finalize 改了就已经交差」，会把崩溃恢复三步、默认锁和半写一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Finalize 改了状态就已经交差」，先数清问的是 Finalize 改了不是已经落盘、必须在 Commit 落盘不是已经在 Finalize 落了，还是记住上次成功 Commit 高度不是已经能跳步，再决定要不要同一次发布。
