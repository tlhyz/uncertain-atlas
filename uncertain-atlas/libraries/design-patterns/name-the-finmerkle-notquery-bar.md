# 模式：把 FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash / not ProofOp key lookup / not finmerkle bundled 正式三事（475 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash ≠ bundled（475）](../../tracks/implementation/worked-example-finmerkle-notquery-vs-bundled.md)。

## 三个名字

1. **Query proofs anchored 不是已经对上 AppHash：** 看见 Query 可以拿这份根当锚，不是已经对上 AppHash interchangeable，不是 404 finapphash interchangeable / 147 apphash vs this block interchangeable / 371 queryheight interchangeable。
2. **Query proofs anchored 不是 ProofOp 按键查：** 看见 anchored in this Merkle root，不是已经是按键查 interchangeable，不是 325 proofop interchangeable / 371 queryheight interchangeable / 487 queryusage interchangeable。
3. **Query proofs anchored 不是 finmerkle bundled：** 看见 Query proofs anchored，不是已经 finmerkle bundled interchangeable，不是 623 notthisheader interchangeable / 624 notnextheader interchangeable / 475 finmerkle item 1 optional Merkle root interchangeable / 475 finmerkle item 2 next block Header interchangeable。

## 为什么要分开叫

官方把 Usage 里 optional Merkle root、included as Header.AppHash in the next block、Query proofs anchored 写成三个名字。把它们叫成一个「看见 Query 可以拿这份根当锚 就已经对上 AppHash interchangeable、就已经是按键查 interchangeable、就已经 finmerkle bundled interchangeable」，会把 not matched AppHash、not ProofOp key lookup、not finmerkle bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash / not ProofOp key lookup / not finmerkle bundled 正式三事（475 余量），先数清问的是 Query proofs anchored 是不是 already 对上 AppHash / 404 / 147，是不是 already ProofOp 按键查 / 325 / 371，还是 Query proofs anchored 是不是 already finmerkle bundled / 623 / 624，再决定要不要同一次发布。
