# 反模式：把 FinalizeBlock When locks mempool not already settled / not four gates settled / not finlock bundled 正式三事（588 余量）说成已经交差 / 已经四门已经结算 / 已经 finlock bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When locks mempool not already settled ≠ bundled（588）](../../tracks/implementation/worked-example-finlock-notsettled-vs-bundled.md)。

## 错在哪里

把 CometBFT locks the mempool / 引擎锁内存池 写成已经交差 interchangeable，或已经 Finalize + Commit 交差 interchangeable；把 locks the mempool 写成已经四门已经结算 interchangeable，或已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable；把 locks the mempool 写成已经是 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable，或已经 finlock bundled interchangeable，或已经和 no calls to CheckTx on new transactions / locks mempool after persist / 403 / 310 / 312 / 373 / 33 / 587 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When locks mempool not already settled / not four gates settled / not finlock bundled 正式三事（588 余量），必须分开 not already settled、not four gates settled、not finlock bundled 三件事，不要和 588 / 403 / 310 / 312 / 373 / 33 / 587 / 630 / 631 糊成一句。

## 和相邻反模式

- [finlock-sold-as-settled](finlock-sold-as-settled.md) 是 588 finlock bundled 三事专用，不是本页 588 item 1 单句边界。
- [finalizeafter-sold-as-commit](finalizeafter-sold-as-commit.md) 是 Finalize 之后 bundled（403），不是本页 locks mempool not settled 单句边界。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 前上锁（310），不是本页 588 item 1 单句边界。
- [finreturn-notpersist-sold-as-bundled](finreturn-notpersist-sold-as-bundled.md) 是 616（587 item 3 余量）专用，不是本页 locks mempool 单句边界。
