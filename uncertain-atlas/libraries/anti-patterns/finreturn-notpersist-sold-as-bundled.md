# 反模式：把 FinalizeBlock When CometBFT persists tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state 正式三事（587 余量）说成已经交差 / 已经 Commit 落盘 / 已经 finreturn bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When CometBFT persists tx outputs / AppHash / ResultsHash not Commit 落盘 ≠ bundled（587）](../../tracks/implementation/worked-example-finreturn-notpersist-vs-bundled.md)。

## 错在哪里

把 CometBFT persists the transaction outputs, AppHash, and ResultsHash 写成已经交差 interchangeable，或已经 Finalize + Commit 交差 interchangeable；把 persists 这三份 写成已经 Commit 落盘应用状态 interchangeable，或已经 Signal persist application state interchangeable；把 persists 这三份 写成已经是 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587） interchangeable，或已经 finreturn bundled interchangeable，或已经和 Application returns AppHash + tx outputs / CometBFT hashes into ResultHash / 335 / 481 / 403 / 614 / 615 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When CometBFT persists tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state 正式三事（587 余量），必须分开 not already settled、not Commit persist application state、not finreturn bundled 三件事，不要和 587 / 335 / 481 / 614 / 615 糊成一句。587 finreturn unbundling 在本页 item 3 完成。

## 和相邻反模式

- [finreturn-notheader-sold-as-bundled](finreturn-notheader-sold-as-bundled.md) 是 587 finreturn item 1 Application returns，不是本页 When 第 6 步 persists 单句边界。
- [finreturn-notresulthash-sold-as-bundled](finreturn-notresulthash-sold-as-bundled.md) 是 587 finreturn item 2 hashes into ResultHash，不是本页 persists 单句边界。
- [finreturn-sold-as-header](finreturn-sold-as-header.md) 是 587 finreturn bundled 三事专用，不是本页 587 item 3 单句边界。
- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 Commit Usage persist signal，不是本页 When 第 6 步引擎 persist 这三份 单句边界。
