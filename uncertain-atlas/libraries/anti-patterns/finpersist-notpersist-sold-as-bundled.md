# 反模式：把 FinalizeBlock When persist decision not executes block v / 已经交差 正式三事（478 余量）说成已经 executes block v / 已经交差 / 已经 finpersist bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When persist decision not executes block v ≠ bundled（478）](../../tracks/implementation/worked-example-finpersist-notpersist-vs-bundled.md)。

## 错在哪里

把 _p_ persists _v_ as the decision for height _h_ 写成已经 Application executes block _v_ interchangeable，或已经 When 第 3 步 executes block v interchangeable；把 persist decision 写成已经 Finalize + Commit 交差 interchangeable，或已经 persist tx outputs / AppHash / ResultsHash interchangeable；把 persist decision 写成已经是 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable，或已经 finpersist bundled interchangeable，或已经和 466 executes block v / 572 not execbv / 33 four gates / 587 finreturn / 362 +2/3 precommit / 602 notgates interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When persist decision not executes block v / 已经交差 正式三事（478 余量），必须分开 not executes block v、not 交差 / persist outputs、not finpersist bundled 三件事，不要和 478 / 466 / 572 / 33 / 587 / 362 / 602 糊成一句。

## 和相邻反模式

- [finpersist-sold-as-commit](finpersist-sold-as-commit.md) 是 478 finpersist bundled 三事专用，不是本页 478 item 1 单句边界。
- [finexec-sold-as-decided](finexec-sold-as-decided.md) 是 executes 就已经决定，不是本页 persist decision not executes block v 单句边界。
- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页 persist decision 不是 decides trigger 单句边界。
