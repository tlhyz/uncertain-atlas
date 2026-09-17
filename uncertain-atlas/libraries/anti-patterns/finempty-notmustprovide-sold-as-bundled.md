# 反模式：把 FinalizeBlock empty keep current not no must provide obligation 正式三事（458 余量）说成已经空着就没有义务 / 已经 finempty bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[empty keep current not no must provide ≠ bundled（458）](../../tracks/implementation/worked-example-finempty-notmustprovide-vs-bundled.md)。

## 错在哪里

把 validator_updates / consensus_param_updates may be empty / CometBFT will keep the current values 写成已经空着就没有 must provide 义务，或已经 keep current values 就不需要回四列 interchangeable；把 empty keep current 写成已经是 FinalizeBlock 空更新 keep current bundled（458） interchangeable，或已经 finempty bundled interchangeable，或已经和 596 notempty / 477 item 3 interchangeable；把 may be empty 写成已经 nil 就什么也不做，或已经 Finalize 没回 ConsensusParams（319） interchangeable，或已经和 471 / 459 / 432 / 335 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty keep current not no must provide obligation 正式三事（458 余量），必须分开 empty keep current not no must provide、not finempty bundled、not nil means do nothing 三件事，不要和 477 / 596 / 363 / 471 / 459 / 319 / 458 bundled 糊成一句。

## 和相邻反模式

- [finasresult-notempty-sold-as-bundled](finasresult-notempty-sold-as-bundled.md) 是 596（477 item 3 余量）专用，不是本页 458 item 1 单句边界。
- [finasresult-sold-as-candidate](finasresult-sold-as-candidate.md) 是 477 bundled 三事专用，不是本页 empty keep current 单句边界。
- [finempty-sold-as-noset](finempty-sold-as-noset.md) 是 458 item 2 余量专用，不是本页 not no must provide 单句边界。
