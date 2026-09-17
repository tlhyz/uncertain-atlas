# 反模式：把 FinalizeBlock When calls Commit after lock mempool not Commit lock / not optional recheck / unlock / not fincommit bundled 正式三事（590 余量）说成已经 Commit 锁 / 已经 optional recheck / unlock / 已经 fincommit bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When calls Commit after lock mempool not Commit lock ≠ bundled（590）](../../tracks/implementation/worked-example-fincommit-notcommitlock-vs-bundled.md)。

## 错在哪里

把 When 第 8 步 calls Commit after lock mempool / lock 之后才 Commit 写成已经是 Commit 锁 interchangeable，或已经 Commit 前上锁 interchangeable；把 calls Commit after lock 写成已经 optional recheck interchangeable，或已经 unlocks the mempool interchangeable，或已经是 Recheck interchangeable；把 When 第 8 步 lock 之后才 Commit 写成已经是 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590） interchangeable，或已经 fincommit bundled interchangeable，或已经和 calls Commit / instruct persist / 310 / 591 / 592 / 403 / 631 / 644 / 645 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calls Commit after lock mempool not Commit lock / not optional recheck / unlock / not fincommit bundled 正式三事（590 余量），必须分开 not Commit lock、not optional recheck / unlock、not fincommit bundled 三件事，不要和 590 / 310 / 588 / 591 / 592 / 403 / 631 / 634 / 644 / 645 / 481 糊成一句。

## 和相邻反模式

- [fincommit-sold-as-settled](fincommit-sold-as-settled.md) 是 calls Commit instruct persist（590）专用 bundled，不是本页 590 item 3 单句边界。
- [fincommit-notsettled-sold-as-bundled](fincommit-notsettled-sold-as-bundled.md) 是 590 item 1 余量 / 644 专用，不是本页 calls Commit after lock not Commit lock 单句边界。
- [fincommit-notpersist-sold-as-bundled](fincommit-notpersist-sold-as-bundled.md) 是 590 item 2 余量 / 645 专用，不是本页 not optional recheck / unlock 单句边界。
- [finlock-notcommitlock-sold-as-bundled](finlock-notcommitlock-sold-as-bundled.md) 是 588 item 3 余量 / 631 专用，不是本页 When 第 8 步 calls Commit after lock 单句边界。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 前上锁（310）专用，不是本页 not Commit lock 单句边界。
