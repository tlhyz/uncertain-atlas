# 反模式：把 FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck / not unlock / not finafter bundled 正式三事（403 余量）说成已经是 Recheck / 已经解锁 / 已经 finafter bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck ≠ bundled（403）](../../tracks/implementation/worked-example-finafter-notrecheck-vs-bundled.md)。

## 错在哪里

把 optional recheck / 可选再验池里剩下的 / against newly persisted Application state 写成已经是 Recheck interchangeable，或已经 CheckTx Type RECHECK interchangeable；把 unlocks the mempool / newly received can now be checked 写成已经解锁 interchangeable，或已经能往下走 interchangeable；把 When 第 9–11 步 recheck+unlock+h+1 写成已经是 Finalize 之后 bundled（403） interchangeable，或已经 finafter bundled interchangeable，或已经和 Finalize 之后引擎才落盘 / 落完再锁内存池 / 591 / 592 / 593 / 632 / 633 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck / not unlock / not finafter bundled 正式三事（403 余量），必须分开 not Recheck、not unlock、not finafter bundled 三件事，不要和 403 / 591 / 592 / 593 / 312 / 632 / 633 / 631 糊成一句。

## 和相邻反模式

- [finrecheck-sold-as-recheck](finrecheck-sold-as-recheck.md) 是 optional recheck（591）专用，不是本页 403 item 3 单句边界。
- [finunlock-sold-as-checked](finunlock-sold-as-checked.md) 是 unlocks mempool（592）专用，不是本页 403 item 3 单句边界。
- [finh1-sold-as-nextheight](finh1-sold-as-nextheight.md) 是 starts consensus h+1 round 0（593）专用，不是本页 403 item 3 单句边界。
- [finafter-notlock-sold-as-bundled](finafter-notlock-sold-as-bundled.md) 是 403 item 2 余量 / 633 专用，不是本页 403 item 3 单句边界。
- [finalizeafter-sold-as-commit](finalizeafter-sold-as-commit.md) 是 403 finafter bundled 三事专用，不是本页 403 item 3 单句边界。
