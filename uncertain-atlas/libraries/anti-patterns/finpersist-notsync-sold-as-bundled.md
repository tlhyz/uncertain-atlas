# 反模式：把 FinalizeBlock When synchronous call not decides trigger / Process sync 正式三事（478 余量）说成已经 Process 同步 / 已经 decides trigger / 已经 finpersist bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When synchronous call not decides trigger ≠ bundled（478）](../../tracks/implementation/worked-example-finpersist-notsync-vs-bundled.md)。

## 错在哪里

把 The call is synchronous 写成已经 ProcessProposal 调用是同步的、返回后不得再改裁决 interchangeable，或已经 异步 / 已经可以在返回后再改裁决 interchangeable；把 synchronous call 写成已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize interchangeable，或已经 decides block 触发条件 interchangeable；把 synchronous call 写成已经是 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable，或已经 finpersist bundled interchangeable，或已经和 354 processwhen synchronous / 362 finwhen / 605 notpersist / 606 notoutputs / 479 fintrigger interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When synchronous call not decides trigger / Process sync 正式三事（478 余量），必须分开 not Process sync / 异步、not decides trigger、not finpersist bundled 三件事，不要和 478 / 354 / 362 / 605 / 606 / 479 糊成一句。

## 和相邻反模式

- [finpersist-sold-as-commit](finpersist-sold-as-commit.md) 是 478 finpersist bundled 三事专用，不是本页 478 item 3 单句边界。
- [finpersist-notpersist-sold-as-bundled](finpersist-notpersist-sold-as-bundled.md) 是 605（478 item 1 余量）专用，不是本页 synchronous call 单句边界。
- [finpersist-notoutputs-sold-as-bundled](finpersist-notoutputs-sold-as-bundled.md) 是 606（478 item 2 余量）专用，不是本页 decides trigger 单句边界。
- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页 synchronous call not Process sync 单句边界。
