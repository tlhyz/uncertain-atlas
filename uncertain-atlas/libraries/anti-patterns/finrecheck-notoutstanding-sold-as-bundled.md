# 反模式：把 FinalizeBlock When all outstanding transactions in the mempool not new transactions / not CheckTx passed forever valid / not finrecheck bundled 正式三事（591 余量）说成已经 new transactions / 已经 CheckTx 过了就永远有效 / 已经 finrecheck bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When all outstanding transactions in the mempool not new transactions ≠ bundled（591）](../../tracks/implementation/worked-example-finrecheck-notoutstanding-vs-bundled.md)。

## 错在哪里

把 all outstanding transactions in the mempool / 池里剩下的 outstanding txs 写成已经 new transactions interchangeable，或已经 no calls to CheckTx on new transactions interchangeable；把 re-checks outstanding 写成已经 CheckTx 过了就永远有效 interchangeable，或已经 CheckTx 过了 interchangeable；把 outstanding in mempool 写成已经是 FinalizeBlock When optional recheck 正式三事 bundled（591） interchangeable，或已经 finrecheck bundled interchangeable，或已经和 optionally re-checks / against newly persisted / 588 / 301 / 635 / 637 / 634 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When all outstanding transactions in the mempool not new transactions / not CheckTx passed forever valid / not finrecheck bundled 正式三事（591 余量），必须分开 not new transactions、not CheckTx passed forever valid、not finrecheck bundled 三件事，不要和 591 / 588 / 630 / 301 / 635 / 637 / 312 / 634 糊成一句。

## 和相邻反模式

- [finrecheck-notmust-sold-as-bundled](finrecheck-notmust-sold-as-bundled.md) 是 591 item 1 余量 / 635 专用，不是本页 591 item 2 单句边界。
- [finrecheck-sold-as-recheck](finrecheck-sold-as-recheck.md) 是 optional recheck（591）专用，不是本页 591 item 2 单句边界。
- [finlock-notoptional-sold-as-bundled](finlock-notoptional-sold-as-bundled.md) 是 no calls on new transactions（588 item 2 余量 / 630）专用，不是本页 591 item 2 单句边界。
