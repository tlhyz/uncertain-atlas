# 反模式：把 FinalizeBlock When unlock after optional recheck not Commit lock / not h+1 round 0 / not finunlock bundled 正式三事（592 余量）说成已经是 Commit 锁 / 已经开下一高 round 0 / 已经 finunlock bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When unlock after optional recheck not Commit lock ≠ bundled（592）](../../tracks/implementation/worked-example-finunlock-notcommitlock-vs-bundled.md)。

## 错在哪里

把 When 第 10 步 unlock after optional recheck / unlock 之后才开下一高 写成已经是 Commit 锁 interchangeable，或已经 Commit 前上锁 interchangeable；把 unlocks the mempool after optional recheck 写成已经 starts consensus for h+1 round 0 interchangeable，或已经开下一高 round 0 interchangeable；把 When 第 10 步 unlock 写成已经是 FinalizeBlock When unlocks mempool 正式三事 bundled（592） interchangeable，或已经 finunlock bundled interchangeable，或已经和 unlocks the mempool / newly received can now be checked / 310 / 593 / 403 / 638 / 639 / 634 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When unlock after optional recheck not Commit lock / not h+1 round 0 / not finunlock bundled 正式三事（592 余量），必须分开 not Commit lock、not h+1 round 0、not finunlock bundled 三件事，不要和 592 / 310 / 593 / 403 / 631 / 638 / 639 / 634 / 591 糊成一句。

## 和相邻反模式

- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 前上锁（310），不是本页 When 第 10 步 unlock not Commit lock 单句边界。
- [finh1-sold-as-nextheight](finh1-sold-as-nextheight.md) 是 starts consensus h+1 round 0（593），不是本页 592 item 3 单句边界。
- [finunlock-notnewly-sold-as-bundled](finunlock-notnewly-sold-as-bundled.md) 是 592 item 2 余量 / 639 专用，不是本页 592 item 3 单句边界。
- [finunlock-notsettled-sold-as-bundled](finunlock-notsettled-sold-as-bundled.md) 是 592 item 1 余量 / 638 专用，不是本页 592 item 3 单句边界。
- [finafter-notrecheck-sold-as-bundled](finafter-notrecheck-sold-as-bundled.md) 是 403 item 3 余量 / 634 专用，不是本页 When 第 10 步 unlock 单句边界。
