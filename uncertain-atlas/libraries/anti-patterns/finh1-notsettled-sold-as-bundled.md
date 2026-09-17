# 反模式：把 FinalizeBlock When starts consensus for height h+1 not already settled / not persist decision / not finh1 bundled 正式三事（593 余量）说成已经交差 / 已经 persist decision / 已经 finh1 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When starts consensus for height h+1 not already settled ≠ bundled（593）](../../tracks/implementation/worked-example-finh1-notsettled-vs-bundled.md)。

## 错在哪里

把 starts consensus for height h+1 / When 第 11 步开下一高 写成已经 Finalize + Commit 交差 interchangeable，或已经四门已经结算 interchangeable；把 starts consensus for height _h+1_ 写成已经 _p_ persists _v_ as the decision for height _h_ interchangeable，或已经 persist decision interchangeable；把 When 第 11 步开下一高 写成已经是 FinalizeBlock When starts consensus for h+1 round 0 正式三事 bundled（593） interchangeable，或已经 finh1 bundled interchangeable，或已经和 round 0 / after unlock / 403 / 478 / 592 / 640 / 642 / 643 / 634 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When starts consensus for height h+1 not already settled / not persist decision / not finh1 bundled 正式三事（593 余量），必须分开 not already settled、not persist decision、not finh1 bundled 三件事，不要和 593 / 403 / 478 / 592 / 640 / 642 / 643 / 634 / 589 / 480 / 479 糊成一句。

## 和相邻反模式

- [finh1-sold-as-nextheight](finh1-sold-as-nextheight.md) 是 starts consensus h+1 round 0（593）专用 bundled，不是本页 593 item 1 单句边界。
- [finunlock-notcommitlock-sold-as-bundled](finunlock-notcommitlock-sold-as-bundled.md) 是 592 item 3 余量 / 640 专用，不是本页 When 第 11 步 starts consensus not settled 单句边界。
- [finafter-notrecheck-sold-as-bundled](finafter-notrecheck-sold-as-bundled.md) 是 403 item 3 余量 / 634 专用，不是本页 593 item 1 单句边界。
- [finpersist-sold-as-commit](finpersist-sold-as-commit.md) 是 persist decision（478）专用，不是本页 not persist decision 单句边界。
