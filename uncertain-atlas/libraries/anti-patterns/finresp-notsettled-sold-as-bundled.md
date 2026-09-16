# 反模式：把 Finalize 回包义务 must provide 四列 not already changed set / settled 正式三事（363 余量）说成已经改了集合 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Finalize must provide 四列 not changed set / settled ≠ bundled（363）](../../tracks/implementation/worked-example-finresp-notsettled-vs-bundled.md)。

## 错在哪里

把 must provide 四列 / 必须回 app_hash / tx_results / validator_updates / consensus_param_updates 写成已经改了集合，或已经 validator_updates 非空 / H+1 换人 interchangeable；把 must provide 四列写成已经 Finalize + Commit 交差，或已经 persist decision / 四门已经结算 interchangeable；把 must provide 四列写成已经是 Finalize 回包义务 bundled（363） interchangeable，或已经 finresp bundled interchangeable，或已经和 594 not settled / 477 finasresult / 463 finreward / 458 finempty / 471 / 478 / 600 notgates interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包义务 must provide 四列 not already changed set / settled 正式三事（363 余量），必须分开 must provide 四列 not changed set、not settled、not finresp bundled 三件事，不要和 363 / 594 / 477 / 463 / 458 / 471 / 478 / 600 糊成一句。

## 和相邻反模式

- [finasresult-notsettled-sold-as-bundled](finasresult-notsettled-sold-as-bundled.md) 是 594（477 item 1 余量）专用，不是本页 363 item 3 单句边界。
- [finresp-notgates-sold-as-bundled](finresp-notgates-sold-as-bundled.md) 是 600（363 item 1 余量）专用，不是本页 must provide 四列 单句边界。
- [finreward-notslashed-sold-as-bundled](finreward-notslashed-sold-as-bundled.md) 是 463（363 item 2 余量）专用，不是本页 not changed set 单句边界。
