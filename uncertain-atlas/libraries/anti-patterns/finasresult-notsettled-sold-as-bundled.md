# 反模式：把 FinalizeBlock must provide values not already changed set / settled 正式三事（477 余量）说成已经改了集合 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[must provide 四列 not already changed set / settled ≠ bundled（477）](../../tracks/implementation/worked-example-finasresult-notsettled-vs-bundled.md)。

## 错在哪里

把 must provide values for app_hash / tx_results / validator_updates / consensus_param_updates 写成已经改了集合，或已经 validator_updates 非空 / H+1 换人 interchangeable；把 must provide 四列写成已经 Finalize + Commit 交差，或已经 persist decision / 四门已经结算 interchangeable；把 must provide 写成已经是 FinalizeBlock must provide values bundled（477） interchangeable，或已经 finresp bundled（363） interchangeable，或已经 empty keep current（458） interchangeable，或已经和 471 / 459 / 478 / 33 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values not already changed set / settled 正式三事（477 余量），必须分开 must provide 四列、must provide not settled、must provide not finasresult bundled 三件事，不要和 477 / 363 / 458 / 471 / 459 / 478 / 33 糊成一句。

## 和相邻反模式

- [finasresult-sold-as-candidate](finasresult-sold-as-candidate.md) 是 477 bundled 三事专用，不是本页 not changed set / settled 单句边界。
- [finempty-sold-as-noset](finempty-sold-as-noset.md) 是 458 空更新专用，不是本页 not changed set 单句边界。
