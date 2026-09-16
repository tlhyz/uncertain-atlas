# 反模式：把 FinalizeBlock equiv ABCI 1.0 not Contains newly decided / apply candidate 正式三事（586 余量）说成已经 Contains newly decided / 已经 Process 跑过就不用在 Finalize 再执行 / 已经 finequiv bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock equiv not Contains newly decided / apply candidate ≠ bundled（586）](../../tracks/implementation/worked-example-finequiv-notnewdec-vs-bundled.md)。

## 错在哪里

把 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 写成已经 Contains the fields of the newly decided block interchangeable，或已经 newly decided block fields interchangeable；把收成一门 写成已经 Process 跑过 / 已经有 candidate 就不用在 Finalize 再执行 interchangeable，或已经 executes txs deterministically interchangeable / 已经 apply candidate state interchangeable；把 equiv 写成已经是 FinalizeBlock 等价于 ABCI 1.0 正式三事 bundled（586） interchangeable，或已经 finequiv bundled interchangeable，或已经和 602 notgates / 603 notnoprep / 460 fincand / 461 finnewfields / 474 finnewdec / 466 executes block v interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not Contains newly decided / apply candidate 正式三事（586 余量），必须分开 not Contains newly decided block fields、not apply candidate / previously executed、not finequiv bundled 三件事，不要和 586 / 602 / 603 / 460 / 461 / 474 / 466 / 577 糊成一句。

## 和相邻反模式

- [finequiv-sold-as-gates](finequiv-sold-as-gates.md) 是 586 finequiv bundled 三事专用，不是本页 586 item 3 单句边界。
- [finequiv-notgates-sold-as-bundled](finequiv-notgates-sold-as-bundled.md) 是 602（586 item 1 余量）专用，不是本页 Contains newly decided 单句边界。
- [finequiv-notnoprep-sold-as-bundled](finequiv-notnoprep-sold-as-bundled.md) 是 603（586 item 2 余量）专用，不是本页 apply candidate 单句边界。
- [fincand-sold-as-commit](fincand-sold-as-commit.md) 是 460 fincand bundled 专用，不是本页 586 item 3 单句边界。
