# 反模式：把 FinalizeBlock equiv ABCI 1.0 not no Prepare/Process 正式三事（586 余量）说成已经没有 Prepare/Process / 已经 finequiv bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock equiv not no Prepare/Process ≠ bundled（586）](../../tracks/implementation/worked-example-finequiv-notnoprep-vs-bundled.md)。

## 错在哪里

把 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 写成已经没有 Prepare/Process interchangeable，或已经 ABCI++ 只剩 Finalize 一门 interchangeable；把收成一门 写成已经 CheckTx 过了就可以跳过 Prepare/Process interchangeable，或已经 Process 回了 Accept 就不需要 Prepare interchangeable；把 equiv 写成已经是 FinalizeBlock 等价于 ABCI 1.0 正式三事 bundled（586） interchangeable，或已经 finequiv bundled interchangeable，或已经和 602 notgates / 600 notgates item 3 / 586 item 3 / 351 / 373 / 356 / 460 fincand interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not no Prepare/Process 正式三事（586 余量），必须分开 not no Prepare/Process、not CheckTx skip Prepare/Process、not finequiv bundled / not Contains newly decided 三件事，不要和 586 / 602 / 600 / 351 / 373 / 356 / 460 / 461 糊成一句。

## 和相邻反模式

- [finequiv-sold-as-gates](finequiv-sold-as-gates.md) 是 586 finequiv bundled 三事专用，不是本页 586 item 2 单句边界。
- [finequiv-notgates-sold-as-bundled](finequiv-notgates-sold-as-bundled.md) 是 602（586 item 1 余量）专用，不是本页 no Prepare/Process 单句边界。
- [finresp-notgates-sold-as-bundled](finresp-notgates-sold-as-bundled.md) 是 600 item 3（363 item 1 余量）专用，不是本页 586 item 2 单句边界。
