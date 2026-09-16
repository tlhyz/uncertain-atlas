# 模式：把 FinalizeBlockResponse app_hash included as Header.AppHash in the next block not already written / not this header AppHash / not finmerkle bundled 正式三事（475 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlockResponse app_hash included as Header.AppHash in the next block not already written ≠ bundled（475）](../../tracks/implementation/worked-example-finmerkle-notnextheader-vs-bundled.md)。

## 三个名字

1. **included in next block 不是已经写进下一块头：** 看见会写进下一块头，不是已经写进下一块头 interchangeable，不是 432 finrespend interchangeable / 467 finreturn interchangeable / 587 finreturn interchangeable。
2. **included in next block 不是本头 AppHash：** 看见 next block Header.AppHash，不是已经本头 AppHash interchangeable，不是 147 apphash vs this block interchangeable / 614 notheader interchangeable / 33 four gates interchangeable。
3. **included in next block 不是 finmerkle bundled：** 看见 included in next block，不是已经 finmerkle bundled interchangeable，不是 623 notthisheader interchangeable / 625 notquery interchangeable / 475 finmerkle item 1 optional Merkle root interchangeable / 475 finmerkle item 3 Query anchored interchangeable。

## 为什么要分开叫

官方把 Usage 里 optional Merkle root、included as Header.AppHash in the next block、Query proofs anchored 写成三个名字。把它们叫成一个「看见 included in next block 就已经写进下一块头 interchangeable、就已经是本头 AppHash interchangeable、就已经 finmerkle bundled interchangeable」，会把 not already written、not this header AppHash、not finmerkle bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse app_hash included as Header.AppHash in the next block not already written / not this header AppHash / not finmerkle bundled 正式三事（475 余量），先数清问的是 included in next block 是不是 already 写进下一块头 / 432 / 467，是不是 already 本头 AppHash / 147 / 614，还是 included in next block 是不是 already finmerkle bundled / 623 / 625，再决定要不要同一次发布。
