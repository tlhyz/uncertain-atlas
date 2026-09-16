# 反模式：把 FinalizeBlock When trigger decides block v not at height h will Finalize / not persist outputs 正式三事（479 余量）说成已经 at height h will Finalize / 已经 persist outputs / 已经 fintrigger bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When trigger decides block v not at height h will Finalize ≠ bundled（479）](../../tracks/implementation/worked-example-fintrigger-notdecides-vs-bundled.md)。

## 错在哪里

把 then _p_ decides block _v_ and finalizes consensus for height _h_ 写成已经处在高度 _h_ 就会调 Finalize interchangeable，或已经 +2/3 precommit 就会调 Finalize interchangeable；把 decides block v 写成已经 persist outputs / AppHash / ResultsHash interchangeable，或已经 persist decision interchangeable，或已经 Finalize + Commit 交差 interchangeable；把 then decides block _v_ 写成已经是 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable，或已经 fintrigger bundled interchangeable，或已经和 Proposal + all block parts / 2f+1 precommit / 362 finwhen / 478 finpersist / 605 notpersist / 608 notparts / 609 notprecommit interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger decides block v not at height h will Finalize / not persist outputs 正式三事（479 余量），必须分开 not at height h will Finalize、not persist outputs / 交差、not fintrigger bundled 三件事，不要和 479 / 362 / 478 / 608 / 609 糊成一句。

## 和相邻反模式

- [finwhenparts-sold-as-partial](finwhenparts-sold-as-partial.md) 是 479 fintrigger bundled 三事专用，不是本页 479 item 3 单句边界。
- [fintrigger-notparts-sold-as-bundled](fintrigger-notparts-sold-as-bundled.md) 是 608（479 item 1 余量）专用，不是本页 decides block v not at height h will Finalize 单句边界。
- [fintrigger-notprecommit-sold-as-bundled](fintrigger-notprecommit-sold-as-bundled.md) 是 609（479 item 2 余量）专用，不是本页 not persist outputs 单句边界。
- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页 decides block v not persist outputs 单句边界。
