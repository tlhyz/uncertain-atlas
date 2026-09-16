# 反模式：把 FinalizeBlockResponse app_hash optional Merkle root not this header AppHash / not settled / not finmerkle bundled 正式三事（475 余量）说成已经是本头 AppHash / 已经交差 / 已经 finmerkle bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse app_hash optional Merkle root not this header AppHash ≠ bundled（475）](../../tracks/implementation/worked-example-finmerkle-notthisheader-vs-bundled.md)。

## 错在哪里

把 `FinalizeBlockResponse.app_hash` contains optional Merkle root 写成已经是本头 AppHash interchangeable，或已经印进本头 interchangeable；把 optional Merkle root 写成已经交差 interchangeable，或已经本头 AppHash 就代表本高度交差 interchangeable；把 optional Merkle root 写成已经是 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475） interchangeable，或已经 finmerkle bundled interchangeable，或已经和 included in next block / Query anchored / 404 / 476 / 147 / 624 / 625 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse app_hash optional Merkle root not this header AppHash / not settled / not finmerkle bundled 正式三事（475 余量），必须分开 not this header AppHash、not settled、not finmerkle bundled 三件事，不要和 475 / 404 / 476 / 147 / 624 / 625 糊成一句。

## 和相邻反模式

- [finmerkle-sold-as-header](finmerkle-sold-as-header.md) 是 475 finmerkle bundled 三事专用，不是本页 475 item 1 optional Merkle root 单句边界。
- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Finalize 回包余量 bundled（404），不是本页 optional Merkle root 单句边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页 optional Merkle root 单句边界。
- [finharddet-notempty-sold-as-bundled](finharddet-notempty-sold-as-bundled.md) 是 may be empty not no state root（476 item 1 余量 / 620），不是本页 optional Merkle root 单句边界。
