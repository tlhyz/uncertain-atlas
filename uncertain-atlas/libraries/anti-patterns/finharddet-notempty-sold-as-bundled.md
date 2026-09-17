# 反模式：把 FinalizeBlockResponse app_hash may be empty not no state root / not settled / not finharddet bundled 正式三事（476 余量）说成已经没有状态 / 已经交差 / 已经 finharddet bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse app_hash may be empty not no state root ≠ bundled（476）](../../tracks/implementation/worked-example-finharddet-notempty-vs-bundled.md)。

## 错在哪里

把 `FinalizeBlockResponse.app_hash` may also be empty 写成已经没有状态根 interchangeable，或没有应用状态 interchangeable；把 may be empty 写成已经交差 interchangeable，或已经印进本头 interchangeable；把 may be empty 写成已经是 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476） interchangeable，或已经 finharddet bundled interchangeable，或已经和 may be hard-coded / MUST be deterministic / 404 / 475 / 470 / 621 / 622 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse app_hash may be empty not no state root / not settled / not finharddet bundled 正式三事（476 余量），必须分开 not no state root、not settled、not finharddet bundled 三件事，不要和 476 / 404 / 475 / 147 / 621 / 622 糊成一句。

## 和相邻反模式

- [finharddet-sold-as-noroot](finharddet-sold-as-noroot.md) 是 476 finharddet bundled 三事专用，不是本页 476 item 1 may be empty 单句边界。
- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Finalize 回包余量 bundled（404），不是本页 may be empty 单句边界。
- [finmerkle-sold-as-header](finmerkle-sold-as-header.md) 是 optional Merkle root bundled（475），不是本页 may be empty 单句边界。
