# 模式：把头字段对上余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**例**：[自己是提议者会先走完 Prepare 那五步 ≠ 已经不用再 Process](../../tracks/implementation/worked-example-htmatch-vs-header.md)。

## 三个名字

1. **自己是提议者会先走完 Prepare 那五步不是已经不用再 Process：** 看见走完了不是已经保证是这一次。
2. **Process 的 height / time 对上拟议块头不是已经验过块头：** 看见对上了不是已经跑过 Process。
3. **Finalize 的 height / time 对上拟议块头不是已经是刚决定那块的字段：** 看见对上了不是已经知道本头哈希。

## 为什么要分开叫

官方把自己是提议者会先走完 Prepare 那五步、Process 的 `height` / `time` 对上拟议块头、Finalize 的 `height` / `time` 对上拟议块头写成三件事。把它们叫成一个「看见填了头字段就已经不用再 Process」，会把已经不用再 Process、已经验过块头和已经是刚决定那块的字段一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了头字段就已经不用再 Process」，先数清问的是自己是提议者会先走完 Prepare 那五步不是已经不用再 Process、Process 的 height / time 对上拟议块头不是已经验过块头，还是 Finalize 的 height / time 对上拟议块头不是已经是刚决定那块的字段，再决定要不要同一次发布。
