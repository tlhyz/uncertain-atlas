# 反模式：把 Finalize 回包义务 not four gates settled 正式三事（363 余量）说成已经四门已经结算 / 已经 finresp bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Finalize equiv not four gates settled ≠ bundled（363）](../../tracks/implementation/worked-example-finresp-notgates-vs-bundled.md)。

## 错在哪里

把 Finalize 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 写成已经四门已经结算 interchangeable，或已经交差 / persist decision interchangeable；把 equiv 收成一门 写成已经是 Finalize 回包义务 bundled（363） interchangeable，或已经 must provide 四列 interchangeable，或已经和 463 finreward / 594 not settled interchangeable；把 equiv 写成已经没有 Prepare/Process interchangeable，或已经和 586 finequiv / 373 CheckTx optional / 460 fincand interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包义务 not four gates settled 正式三事（363 余量），必须分开 equiv not four gates settled、not finresp bundled、not no Prepare/Process 三件事，不要和 363 / 33 / 463 / 586 / 594 糊成一句。

## 和相邻反模式

- [finalizeequiv-sold-as-gates](finalizeequiv-sold-as-gates.md) 是 586 finequiv 专用，不是本页 363 item 1 单句边界。
- [finreward-notslashed-sold-as-bundled](finreward-notslashed-sold-as-bundled.md) 是 463（363 item 2 余量）专用，不是本页 four gates 单句边界。
- [finasresult-notsettled-sold-as-bundled](finasresult-notsettled-sold-as-bundled.md) 是 594（477 item 1 余量）专用，不是本页 finresp bundled 单句边界。
