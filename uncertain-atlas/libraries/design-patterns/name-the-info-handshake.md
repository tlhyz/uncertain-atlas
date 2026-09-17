# 模式：把 Info 握手三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info 用来握手对齐 ≠ 已经是快照重放](../../tracks/implementation/worked-example-info-vs-handshake.md)。

## 三个名字

1. **Info 用来握手对齐不是已经是快照重放：** 看见能回不是已经是 QueryState。
2. **app_version 进每块头不是已经印进本头 AppHash：** 看见有版本不是已经交差。
3. **last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差：** 看见回了这两列不是已经在剪。

## 为什么要分开叫

官方把 Info 用来握手对齐、`app_version` 进每块头、`last_block_app_hash` / `last_block_height` 要在 Commit 里落盘写成三件事。把它们叫成一个「看见能回 Info 就已经是快照重放」，会把 QueryState、本头 AppHash 和崩溃三步一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能回 Info 就已经是快照重放」，先数清问的是 Info 用来握手对齐不是已经是快照重放、app_version 进每块头不是已经印进本头 AppHash，还是 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差，再决定要不要同一次发布。
