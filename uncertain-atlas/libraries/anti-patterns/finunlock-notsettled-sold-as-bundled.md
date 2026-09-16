# 反模式：把 FinalizeBlock When unlocks the mempool not already settled / not four gates settled / not finunlock bundled 正式三事（592 余量）说成已经交差 / 已经四门已经结算 / 已经 finunlock bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When unlocks the mempool not already settled ≠ bundled（592）](../../tracks/implementation/worked-example-finunlock-notsettled-vs-bundled.md)。

## 错在哪里

把 unlocks the mempool / When 第 10 步解锁内存池 写成已经 Finalize + Commit 交差 interchangeable，或已经四门已经结算 interchangeable；把 When 第 10 步 unlock 写成已经是 FinalizeBlock When unlocks mempool 正式三事 bundled（592） interchangeable，或已经 finunlock bundled interchangeable，或已经和 newly received can now be checked / unlock after optional recheck / 403 / 591 / 588 / 310 / 373 / 639 / 640 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When unlocks the mempool not already settled / not four gates settled / not finunlock bundled 正式三事（592 余量），必须分开 not already settled、not four gates settled、not finunlock bundled 三件事，不要和 592 / 403 / 33 / 591 / 588 / 639 / 640 / 634 糊成一句。

## 和相邻反模式

- [finunlock-sold-as-checked](finunlock-sold-as-checked.md) 是 unlocks mempool（592）专用，不是本页 592 item 1 单句边界。
- [finlock-notsettled-sold-as-bundled](finlock-notsettled-sold-as-bundled.md) 是 locks mempool not settled（588 item 1 余量 / 629）专用，不是本页 592 item 1 单句边界。
- [finafter-notrecheck-sold-as-bundled](finafter-notrecheck-sold-as-bundled.md) 是 403 item 3 余量 / 634 专用，不是本页 592 item 1 单句边界。
