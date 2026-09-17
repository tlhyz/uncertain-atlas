# 模式：把 Commit 保留高度三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[retain_height 默认 0 ≠ 已经在剪](../../tracks/implementation/worked-example-retain-vs-kept.md)。

## 三个名字

1. **retain_height 默认 0 不是已经在剪：** 看见没填不是已经交差。
2. **低于这个高度的块可以被删不是已经没有历史：** 看见回了高度不是已经是这个节点快照截断。
3. **全网都删了会永久丢不是已经能从创世再装：** 看见能剪不是已经能给轻客户端验。

## 为什么要分开叫

官方把 `retain_height` 默认全留、低于这个高度的块可以被删、全网都删会永久丢写成三件事。把它们叫成一个「看见 Commit 回了高度就已经在剪」，会把崩溃三步、快照截断和从创世重放一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Commit 回了高度就已经在剪」，先数清问的是 retain_height 默认 0 不是已经在剪、低于这个高度的块可以被删不是已经没有历史，还是全网都删了会永久丢不是已经能从创世再装，再决定要不要同一次发布。
