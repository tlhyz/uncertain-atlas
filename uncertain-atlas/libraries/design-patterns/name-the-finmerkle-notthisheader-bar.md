# 模式：把 FinalizeBlockResponse app_hash optional Merkle root not this header AppHash / not settled / not finmerkle bundled 正式三事（475 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlockResponse app_hash optional Merkle root not this header AppHash ≠ bundled（475）](../../tracks/implementation/worked-example-finmerkle-notthisheader-vs-bundled.md)。

## 三个名字

1. **optional Merkle root 不是本头 AppHash：** 看见 optional Merkle root，不是已经本头 `Header.AppHash` interchangeable，不是 404 finapphash interchangeable / 476 finharddet interchangeable / 392 initchain apphash interchangeable。
2. **optional Merkle root 不是已经交差：** 看见 optional Merkle root，不是已经交差 interchangeable，不是 147 apphash vs this block interchangeable / 614 notheader interchangeable / 33 four gates interchangeable。
3. **optional Merkle root 不是 finmerkle bundled：** 看见 optional Merkle root，不是已经 finmerkle bundled interchangeable，不是 624 notnextheader interchangeable / 625 notquery interchangeable / 475 finmerkle item 2 next block Header interchangeable / 475 finmerkle item 3 Query anchored interchangeable。

## 为什么要分开叫

官方把 Usage 里 optional Merkle root、included as Header.AppHash in the next block、Query proofs anchored 写成三个名字。把它们叫成一个「看见 optional Merkle root 就已经是本头 AppHash interchangeable、就已经印进本头 interchangeable、就已经 finmerkle bundled interchangeable」，会把 not this header AppHash、not settled、not finmerkle bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse app_hash optional Merkle root not this header AppHash / not settled / not finmerkle bundled 正式三事（475 余量），先数清问的是 optional Merkle root 是不是 already 本头 AppHash / 404 / 476，是不是 already 已经交差 / 147 / 614，还是 optional Merkle root 是不是 already finmerkle bundled / 624 / 625，再决定要不要同一次发布。
