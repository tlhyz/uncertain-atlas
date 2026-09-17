# 反模式：把 FinalizeBlock When optionally re-checks not must recheck / not already settled / not finrecheck bundled 正式三事（591 余量）说成已经必须再验 / 已经交差 / 已经 finrecheck bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When optionally re-checks not must recheck ≠ bundled（591）](../../tracks/implementation/worked-example-finrecheck-notmust-vs-bundled.md)。

## 错在哪里

把 optionally re-checks / When 第 9 步 optional recheck 写成已经必须再验才能开下一高 interchangeable，或已经 CheckTx Type RECHECK interchangeable；把 When 第 9 步 optional recheck 写成已经 Finalize + Commit 交差 interchangeable，或已经四门已经结算 interchangeable；把 When 第 9 步 optional recheck 写成已经是 FinalizeBlock When optional recheck 正式三事 bundled（591） interchangeable，或已经 finrecheck bundled interchangeable，或已经和 outstanding vs new / against newly persisted / 403 / 634 / 312 / 588 / 301 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When optionally re-checks not must recheck / not already settled / not finrecheck bundled 正式三事（591 余量），必须分开 not must recheck、not already settled、not finrecheck bundled 三件事，不要和 591 / 403 / 634 / 312 / 484 / 636 / 637 / 33 / 588 / 301 糊成一句。

## 和相邻反模式

- [finrecheck-sold-as-recheck](finrecheck-sold-as-recheck.md) 是 optional recheck（591）专用，不是本页 591 item 1 单句边界。
- [finafter-notrecheck-sold-as-bundled](finafter-notrecheck-sold-as-bundled.md) 是 403 item 3 余量 / 634 专用，不是本页 591 item 1 单句边界。
- [finlock-notsettled-sold-as-bundled](finlock-notsettled-sold-as-bundled.md) 是 locks mempool not settled（588 item 1 余量 / 629）专用，不是本页 591 item 1 单句边界。
