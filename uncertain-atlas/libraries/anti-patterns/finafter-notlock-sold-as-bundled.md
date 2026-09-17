# 反模式：把 FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock / not already settled / not finafter bundled 正式三事（403 余量）说成已经是 Commit 锁 / 已经交差 / 已经 finafter bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock ≠ bundled（403）](../../tracks/implementation/worked-example-finafter-notlock-vs-bundled.md)。

## 错在哪里

把落完再锁内存池、新交易不进 CheckTx / locks the mempool / no calls to CheckTx on new transactions 写成已经是 Commit 锁 interchangeable，或已经 Commit 前上锁 interchangeable；把落完再锁内存池 写成已经交差 interchangeable，或已经 Finalize + Commit 交差 interchangeable；把 When 第 7 步 落完再锁 写成已经是 Finalize 之后 bundled（403） interchangeable，或已经 finafter bundled interchangeable，或已经和 Finalize 之后引擎才落盘 / optional recheck unlock h+1 / 588 / 631 / 632 / 634 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock / not already settled / not finafter bundled 正式三事（403 余量），必须分开 not Commit lock、not already settled、not finafter bundled 三件事，不要和 403 / 310 / 631 / 632 / 634 / 629 / 630 糊成一句。

## 和相邻反模式

- [finlock-notcommitlock-sold-as-bundled](finlock-notcommitlock-sold-as-bundled.md) 是 588 item 3 余量 / 631 专用，不是本页 403 item 2 单句边界。
- [finafter-notsettled-sold-as-bundled](finafter-notsettled-sold-as-bundled.md) 是 403 item 1 余量 / 632 专用，不是本页 403 item 2 单句边界。
- [finalizeafter-sold-as-commit](finalizeafter-sold-as-commit.md) 是 403 finafter bundled 三事专用，不是本页 403 item 2 单句边界。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 前上锁（310），不是本页 When 第 7 步 落完再锁 单句边界。
