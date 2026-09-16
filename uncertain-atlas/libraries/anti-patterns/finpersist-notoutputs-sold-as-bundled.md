# 反模式：把 FinalizeBlock When calls FinalizeBlock not persist outputs / 362 decides trigger 正式三事（478 余量）说成已经 persist outputs / 已经 decides trigger / 已经 finpersist bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When calls FinalizeBlock not persist outputs ≠ bundled（478）](../../tracks/implementation/worked-example-finpersist-notoutputs-vs-bundled.md)。

## 错在哪里

把 _p_'s CometBFT calls `FinalizeBlock` with _v_'s data 写成已经 persist the transaction outputs, AppHash, and ResultsHash interchangeable，或已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable；把 calls FinalizeBlock 写成已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize interchangeable，或已经 decides block 触发条件 interchangeable；把 calls FinalizeBlock 写成已经是 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable，或已经 finpersist bundled interchangeable，或已经和 587 finreturn / 362 finwhen / 605 notpersist / 479 fintrigger / 335 finpersist interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calls FinalizeBlock not persist outputs / 362 decides trigger 正式三事（478 余量），必须分开 not persist outputs、not decides trigger、not finpersist bundled 三件事，不要和 478 / 587 / 467 / 362 / 605 / 479 / 335 糊成一句。

## 和相邻反模式

- [finpersist-sold-as-commit](finpersist-sold-as-commit.md) 是 478 finpersist bundled 三事专用，不是本页 478 item 2 单句边界。
- [finpersist-notpersist-sold-as-bundled](finpersist-notpersist-sold-as-bundled.md) 是 605（478 item 1 余量）专用，不是本页 persist outputs 单句边界。
- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页 calls FinalizeBlock not persist outputs 单句边界。
