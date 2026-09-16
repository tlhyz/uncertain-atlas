# 模式：把 FinalizeBlock height/time match header not already verified 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / When。  
**例**：[FinalizeBlock height/time match header not already verified ≠ bundled](../../tracks/implementation/worked-example-finht-notverified-vs-bundled.md)。

## 三个名字

1. **Finalize height/time match header not already verified 不是 FinalizeBlock height/time 对上拟议块头 bundled：** 看见对上了不是已经验过块头，不是 462 bundled interchangeable / 416 When verify interchangeable / 354 async can Reject interchangeable。
2. **Finalize height/time match header not already ran Process 不是 Finalize Process guarantee：** 看见 Usage match 不是已经跑过 Process，不是 462 bundled interchangeable / 360 Process guarantee interchangeable / 351 Process follows Prepare interchangeable。
3. **Finalize height/time match header not header fields bundled 不是 417 know hash：** 看见对上了不是已经知道本头哈希，不是 462 bundled interchangeable / 417 header fields bundled interchangeable / 428 Finalize hash interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock height/time match header not already verified 写成三个名字。把它们叫成一个「看见 Finalize 对上了就已经验过块头」，会把 When verify header、already ran Process、header fields bundled know hash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock height/time match header not already verified 正式三事，先数清问的是 Finalize height/time match header 是不是 already verified block header、Finalize height/time match header 是不是 already ran Process、Finalize height/time match header 是不是 header fields bundled know hash，再决定要不要同一次发布。
