# 反模式：把 FinalizeBlock When locks mempool after persist not Commit lock / not unlock / not Recheck / not finlock bundled 正式三事（588 余量）说成已经是 Commit 锁 / 已经解锁 / 已经是 Recheck / 已经 finlock bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When locks mempool after persist not Commit lock ≠ bundled（588）](../../tracks/implementation/worked-example-finlock-notcommitlock-vs-bundled.md)。

## 错在哪里

把 locks mempool after persist / persist 之后才锁 写成已经是 Commit 锁 interchangeable，或已经 Commit 前上锁 interchangeable；把 locks mempool after persist 写成已经解锁 interchangeable，或已经是 Recheck interchangeable；把 locks mempool after persist 写成已经是 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable，或已经 finlock bundled interchangeable，或已经和 locks the mempool / no calls to CheckTx on new transactions / 310 / 592 / 591 / 629 / 630 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When locks mempool after persist not Commit lock / not unlock / not Recheck / not finlock bundled 正式三事（588 余量），必须分开 not Commit lock、not unlock / not Recheck、not finlock bundled 三件事，不要和 588 / 310 / 592 / 591 / 403 / 629 / 630 糊成一句。

## 和相邻反模式

- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 前上锁（310），不是本页 When 第 7 步 persist 之后才锁 单句边界。
- [finunlock-sold-as-checked](finunlock-sold-as-checked.md) 是 unlocks mempool（592），不是本页 588 item 3 单句边界。
- [finrecheck-sold-as-recheck](finrecheck-sold-as-recheck.md) 是 optional recheck（591），不是本页 locks mempool after persist 单句边界。
- [finlock-notoptional-sold-as-bundled](finlock-notoptional-sold-as-bundled.md) 是 588 item 2 余量 / 630 专用，不是本页 588 item 3 单句边界。
- [finalizeafter-sold-as-commit](finalizeafter-sold-as-commit.md) 是 Finalize 之后 bundled（403），不是本页 persist 之后才锁 单句边界。
