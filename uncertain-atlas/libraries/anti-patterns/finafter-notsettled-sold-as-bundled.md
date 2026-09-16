# 反模式：把 FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state / not finafter bundled 正式三事（403 余量）说成已经交差 / 已经落盘应用状态 / 已经 finafter bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled ≠ bundled（403）](../../tracks/implementation/worked-example-finafter-notsettled-vs-bundled.md)。

## 错在哪里

把 Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash / CometBFT persists 这三份 写成已经交差 interchangeable，或已经 Finalize + Commit 交差 interchangeable；把 persists 这三份 写成已经落盘应用状态 interchangeable，或已经应用在 Commit 里落盘 interchangeable；把 Finalize 之后引擎才落盘 写成已经是 Finalize 之后 bundled（403） interchangeable，或已经 finafter bundled interchangeable，或已经和落完再锁内存池 / optional recheck unlock h+1 / 588 / 616 / 335 / 481 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state / not finafter bundled 正式三事（403 余量），必须分开 not already settled、not Commit persist application state、not finafter bundled 三件事，不要和 403 / 335 / 481 / 616 / 633 / 634 糊成一句。

## 和相邻反模式

- [finreturn-notpersist-sold-as-bundled](finreturn-notpersist-sold-as-bundled.md) 是 587 item 3 余量 / 616 专用，不是本页 403 item 1 单句边界。
- [finalizeafter-sold-as-commit](finalizeafter-sold-as-commit.md) 是 403 finafter bundled 三事专用，不是本页 403 item 1 单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 Finalize 落盘禁令（335），不是本页 When 第 6 步引擎 persist 这三份 单句边界。
- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 Commit persist signal（481），不是本页 403 item 1 单句边界。
