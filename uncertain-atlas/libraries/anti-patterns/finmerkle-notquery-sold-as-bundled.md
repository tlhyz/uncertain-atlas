# 反模式：把 FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash / not ProofOp key lookup / not finmerkle bundled 正式三事（475 余量）说成已经对上 AppHash / 已经是按键查 / 已经 finmerkle bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash ≠ bundled（475）](../../tracks/implementation/worked-example-finmerkle-notquery-vs-bundled.md)。

## 错在哪里

把 Later calls to `Query` can return proofs anchored in this Merkle root 写成已经对上 AppHash interchangeable，或这一高 AppHash interchangeable；把 Query proofs anchored 写成已经是 ProofOp 按键查 interchangeable，或已经是按键查 interchangeable；把 Query proofs anchored 写成已经是 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475） interchangeable，或已经 finmerkle bundled interchangeable，或已经和 optional Merkle root / included in next block / 404 / 325 / 371 / 623 / 624 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash / not ProofOp key lookup / not finmerkle bundled 正式三事（475 余量），必须分开 not matched AppHash、not ProofOp key lookup、not finmerkle bundled 三件事，不要和 475 / 404 / 325 / 371 / 147 / 623 / 624 糊成一句。

## 和相邻反模式

- [finmerkle-sold-as-header](finmerkle-sold-as-header.md) 是 475 finmerkle bundled 三事专用，不是本页 475 item 3 Query proofs anchored 单句边界。
- [finmerkle-notthisheader-sold-as-bundled](finmerkle-notthisheader-sold-as-bundled.md) 是 optional Merkle root not this header AppHash（475 item 1 余量 / 623），不是本页 Query proofs anchored 单句边界。
- [finmerkle-notnextheader-sold-as-bundled](finmerkle-notnextheader-sold-as-bundled.md) 是 included in next block not already written（475 item 2 余量 / 624），不是本页 Query proofs anchored 单句边界。
- [proofop-sold-as-key](proofop-sold-as-key.md) 是 ProofOp.type 就已经是按键查（325），不是本页 Query proofs anchored 单句边界。
- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Finalize 回包余量 bundled（404），不是本页 Query proofs anchored 单句边界。
