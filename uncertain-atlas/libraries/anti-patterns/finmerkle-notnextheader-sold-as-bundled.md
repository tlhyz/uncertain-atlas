# 反模式：把 FinalizeBlockResponse app_hash included as Header.AppHash in the next block not already written / not this header AppHash / not finmerkle bundled 正式三事（475 余量）说成已经写进下一块头 / 已经是本头 AppHash / 已经 finmerkle bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse app_hash included as Header.AppHash in the next block not already written ≠ bundled（475）](../../tracks/implementation/worked-example-finmerkle-notnextheader-vs-bundled.md)。

## 错在哪里

把 `FinalizeBlockResponse.app_hash` is included as Header.AppHash in the next block 写成已经写进下一块头 interchangeable，或下一块头 AppHash interchangeable；把 included in next block 写成已经是本头 AppHash interchangeable，或已经本头 AppHash 就代表本高度交差 interchangeable；把 included in next block 写成已经是 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475） interchangeable，或已经 finmerkle bundled interchangeable，或已经和 optional Merkle root / Query anchored / 432 / 147 / 623 / 625 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse app_hash included as Header.AppHash in the next block not already written / not this header AppHash / not finmerkle bundled 正式三事（475 余量），必须分开 not already written、not this header AppHash、not finmerkle bundled 三件事，不要和 475 / 432 / 467 / 147 / 623 / 625 糊成一句。

## 和相邻反模式

- [finmerkle-sold-as-header](finmerkle-sold-as-header.md) 是 475 finmerkle bundled 三事专用，不是本页 475 item 2 included in next block 单句边界。
- [finmerkle-notthisheader-sold-as-bundled](finmerkle-notthisheader-sold-as-bundled.md) 是 optional Merkle root not this header AppHash（475 item 1 余量 / 623），不是本页 included in next block 单句边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页 included in next block 单句边界。
- [finrespend-sold-as-params](finrespend-sold-as-params.md) 是 Finalize 回包末栏 bundled（432），不是本页 included in next block 单句边界。
