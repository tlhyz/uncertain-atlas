# 反模式：把 FinalizeBlock When newly received transactions can now be checked not optional recheck outstanding txs / not CheckTx optional / not finunlock bundled 正式三事（592 余量）说成已经 optional recheck outstanding txs / 已经 CheckTx 技术上可选 / 已经 finunlock bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When newly received transactions can now be checked not optional recheck outstanding txs ≠ bundled（592）](../../tracks/implementation/worked-example-finunlock-notnewly-vs-bundled.md)。

## 错在哪里

把 newly received transactions can now be checked / 新收到的交易现在可以 CheckTx 写成已经 optionally re-checks all outstanding transactions in the mempool interchangeable，或已经 optional recheck outstanding txs interchangeable；把 can now be checked 写成已经 CheckTx technically optional — not involved in processing blocks interchangeable，或已经 CheckTx 技术上可选 interchangeable；把 When 第 10 步 newly received can now be checked 写成已经是 FinalizeBlock When unlocks mempool 正式三事 bundled（592） interchangeable，或已经 finunlock bundled interchangeable，或已经和 unlocks the mempool / unlock after optional recheck / 591 / 373 / 588 / 630 / 638 / 640 / 634 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When newly received transactions can now be checked not optional recheck outstanding txs / not CheckTx optional / not finunlock bundled 正式三事（592 余量），必须分开 not optional recheck outstanding txs、not CheckTx optional、not finunlock bundled 三件事，不要和 592 / 591 / 373 / 588 / 630 / 636 / 638 / 640 / 634 糊成一句。

## 和相邻反模式

- [finunlock-notsettled-sold-as-bundled](finunlock-notsettled-sold-as-bundled.md) 是 592 item 1 余量 / 638 专用，不是本页 592 item 2 单句边界。
- [finrecheck-notoutstanding-sold-as-bundled](finrecheck-notoutstanding-sold-as-bundled.md) 是 591 item 2 余量 / 636 专用，不是本页 592 item 2 单句边界。
- [finunlock-sold-as-checked](finunlock-sold-as-checked.md) 是 unlocks mempool（592）专用，不是本页 592 item 2 单句边界。
