# 反模式：把 FinalizeBlock When round 0 not same round / not next_block_delay / not timeout_commit / not finh1 bundled 正式三事（593 余量）说成已经继续同一 round / 已经 next_block_delay / 已经 timeout_commit

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When round 0 not same round ≠ bundled（593）](../../tracks/implementation/worked-example-finh1-notround-vs-bundled.md)。

## 错在哪里

把 round 0 / starts consensus for height h+1, round 0 写成已经继续同一 round _r_ interchangeable，或已经同高换轮 interchangeable；把 round 0 写成已经 `FinalizeBlockResponse.next_block_delay` 槽位 interchangeable，或已经 Deterministic = No interchangeable；把 round 0 写成已经 processing time / more precommits / `timeout_commit` interchangeable，或已经是 FinalizeBlock When starts consensus for h+1 round 0 正式三事 bundled（593） interchangeable，或已经和 641 finh1-notsettled / 643 finh1-notafterunlock / 302 / 589 / 480 / 640 / 634 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When round 0 not same round / not next_block_delay / not timeout_commit / not finh1 bundled 正式三事（593 余量），必须分开 not same round、not next_block_delay、not timeout_commit / not finh1 bundled 三件事，不要和 593 / 302 / 589 / 480 / 641 / 643 / 640 / 617 / 611 / 612 糊成一句。

## 和相邻反模式

- [finh1-sold-as-nextheight](finh1-sold-as-nextheight.md) 是 starts consensus h+1 round 0（593）专用 bundled，不是本页 593 item 2 单句边界。
- [finh1-notsettled-sold-as-bundled](finh1-notsettled-sold-as-bundled.md) 是 593 item 1 余量 / 641 专用，不是本页 round 0 单句边界。
- [fndelay-notslot-sold-as-bundled](fndelay-notslot-sold-as-bundled.md) 是 589 item 1 余量 / 617 专用，不是本页 593 item 2 单句边界。
- [finmorepre-notproctime-sold-as-bundled](finmorepre-notproctime-sold-as-bundled.md) 是 480 item 1 余量 / 611 专用，不是本页 timeout_commit 单句边界。
- [finunlock-notcommitlock-sold-as-bundled](finunlock-notcommitlock-sold-as-bundled.md) 是 592 item 3 余量 / 640 专用，不是本页 When 第 11 步 round 0 单句边界。
