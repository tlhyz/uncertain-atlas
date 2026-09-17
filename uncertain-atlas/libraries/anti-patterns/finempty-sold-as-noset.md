# 反模式：把 FinalizeBlock empty keep current not changed set / H+1 effective 正式三事（458 余量）说成 validator_updates 空则没有集合 / 已经改了集合

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[empty keep current not changed set ≠ bundled（458）](../../tracks/implementation/worked-example-finempty-notnoset-vs-bundled.md)。

## 错在哪里

把 validator_updates may be empty … CometBFT will keep the current values 写成 validator_updates 空则保持当前集合就已经没有集合 interchangeable，或已经 empty means no validator set interchangeable；把 empty keep current 写成已经 changed validator set / H+1 换人 interchangeable，或已经 validator_updates 非空 interchangeable，或已经和 459 validator_updates H+1/H+2/H+3 / 471 fincparam / 594 not settled interchangeable；把 empty keep current 写成已经是 FinalizeBlock 空更新 keep current bundled（458） interchangeable，或已经 finempty bundled interchangeable，或已经和 597 notmustprovide / 596 notempty / 477 finasresult interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty keep current not changed set / H+1 effective 正式三事（458 余量），必须分开 empty keep current set not no set、not changed set / H+1 effective、not finempty bundled 三件事，不要和 458 / 597 / 459 / 471 / 594 / 477 糊成一句。

## 和相邻反模式

- [finempty-notmustprovide-sold-as-bundled](finempty-notmustprovide-sold-as-bundled.md) 是 597（458 item 1 余量）专用，不是本页 not changed set 单句边界。
- [finasresult-notsettled-sold-as-bundled](finasresult-notsettled-sold-as-bundled.md) 是 594（477 item 1 余量）专用，不是本页 empty keep current 单句边界。
