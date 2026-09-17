# 反模式：把 FinalizeBlockResponse MUST be deterministic not next_block_delay nondet / not 印进本头 / not finharddet bundled 正式三事（476 余量）说成 next_block_delay 非确定 / 已经 settled / 已经 finharddet bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse MUST be deterministic not next_block_delay nondet ≠ bundled（476）](../../tracks/implementation/worked-example-finharddet-notnondet-vs-bundled.md)。

## 错在哪里

把 `FinalizeBlockResponse` MUST be deterministic 写成 next_block_delay 非确定 interchangeable，或整包 Response 非确定 interchangeable；把 MUST be deterministic 写成已经 settled interchangeable，或已经印进本头 interchangeable；把 MUST be deterministic 写成已经是 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476） interchangeable，或已经 finharddet bundled interchangeable，或已经和 may be empty / may be hard-coded / 589 / 470 / 620 / 621 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse MUST be deterministic not next_block_delay nondet / not 印进本头 / not finharddet bundled 正式三事（476 余量），必须分开 not next_block_delay nondet、not 印进本头、not finharddet bundled 三件事，不要和 476 / 589 / 470 / 147 / 620 / 621 糊成一句。

## 和相邻反模式

- [finharddet-sold-as-noroot](finharddet-sold-as-noroot.md) 是 476 finharddet bundled 三事专用，不是本页 476 item 3 MUST be deterministic 单句边界。
- [fndelay-sold-as-slot](fndelay-sold-as-slot.md) 是 next_block_delay Deterministic = No not slot（589 item 1 余量 / 617），不是本页 MUST be deterministic 单句边界。
- [findet-notapphash-sold-as-bundled](findet-notapphash-sold-as-bundled.md) 是 app_hash MUST be deterministic not 印进本头（470 item 2 余量 / 580），不是本页 476 item 3 单句边界。
- [finharddet-notempty-sold-as-bundled](finharddet-notempty-sold-as-bundled.md) 是 may be empty not no state root（476 item 1 余量 / 620），不是本页 MUST be deterministic 单句边界。
- [finharddet-nothardcoded-sold-as-bundled](finharddet-nothardcoded-sold-as-bundled.md) 是 may be hard-coded not Merkle root（476 item 2 余量 / 621），不是本页 MUST be deterministic 单句边界。
