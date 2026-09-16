# 反模式：把 FinalizeBlock equiv ABCI 1.0 not four gates settled 正式三事（586 余量）说成已经四门已经结算 / 已经 finequiv bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock equiv not four gates settled ≠ bundled（586）](../../tracks/implementation/worked-example-finequiv-notgates-vs-bundled.md)。

## 错在哪里

把 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 写成已经四门已经结算 interchangeable，或已经交差 / persist decision interchangeable；把 equiv 收成一门 写成已经是 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable，或已经 finequiv bundled interchangeable，或已经和 600 notgates / 363 finresp / 601 notsettled / 594 not settled interchangeable；把 equiv 写成已经和 586 item 2 no Prepare/Process / 586 item 3 Contains newly decided / 460 fincand interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not four gates settled 正式三事（586 余量），必须分开 equiv not four gates settled、not settled、not finequiv bundled 三件事，不要和 586 / 600 / 363 / 601 / 33 / 478 糊成一句。

## 和相邻反模式

- [finequiv-sold-as-gates](finequiv-sold-as-gates.md) 是 586 finequiv bundled 三事专用，不是本页 586 item 1 单句边界。
- [finresp-notgates-sold-as-bundled](finresp-notgates-sold-as-bundled.md) 是 600（363 item 1 余量）专用，不是本页 finequiv bundled 单句边界。
- [finresp-notsettled-sold-as-bundled](finresp-notsettled-sold-as-bundled.md) 是 601（363 item 3 余量）专用，不是本页 not settled 单句边界。
