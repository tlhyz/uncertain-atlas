# 反模式：把 FinalizeBlock When after unlock not unlock mempool / not finafter bundled / not When trigger 正式三事（593 余量）说成已经 unlocks the mempool / 已经 Finalize 之后 bundled / 已经 When trigger

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When after unlock not unlock mempool ≠ bundled（593）](../../tracks/implementation/worked-example-finh1-notafterunlock-vs-bundled.md)。

## 错在哪里

把 When 第 11 步 after unlock / unlock 之后才开下一高 写成已经 unlocks the mempool interchangeable，或已经 When 第 10 步 unlock interchangeable；把 When 第 11 步 after unlock 写成已经 Finalize 之后 bundled interchangeable，或已经 recheck+unlock+h+1 interchangeable；把 unlock 之后才开下一高 写成已经 When trigger 2f+1 precommit decides _v_ interchangeable，或已经是 FinalizeBlock When starts consensus for h+1 round 0 正式三事 bundled（593） interchangeable，或已经和 641 finh1-notsettled / 642 finh1-notround / 592 / 403 / 479 / 634 / 640 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When after unlock not unlock mempool / not finafter bundled / not When trigger 正式三事（593 余量），必须分开 not unlock mempool、not finafter bundled、not When trigger 三件事，不要和 593 / 592 / 403 / 479 / 641 / 642 / 634 / 640 / 632 / 633 糊成一句。

## 和相邻反模式

- [finh1-sold-as-nextheight](finh1-sold-as-nextheight.md) 是 starts consensus h+1 round 0（593）专用 bundled，不是本页 593 item 3 单句边界。
- [finh1-notsettled-sold-as-bundled](finh1-notsettled-sold-as-bundled.md) 是 593 item 1 余量 / 641 专用，不是本页 after unlock 单句边界。
- [finh1-notround-sold-as-bundled](finh1-notround-sold-as-bundled.md) 是 593 item 2 余量 / 642 专用，不是本页 after unlock 单句边界。
- [finafter-notrecheck-sold-as-bundled](finafter-notrecheck-sold-as-bundled.md) 是 403 item 3 余量 / 634 专用，不是本页 593 item 3 单句边界。
- [finunlock-notcommitlock-sold-as-bundled](finunlock-notcommitlock-sold-as-bundled.md) 是 592 item 3 余量 / 640 专用，不是本页 When 第 11 步 after unlock 单句边界。
- [finwhenparts-sold-as-partial](finwhenparts-sold-as-partial.md) 是 When trigger 2f+1 precommit（479）bundled 专用，不是本页 593 item 3 单句边界。
