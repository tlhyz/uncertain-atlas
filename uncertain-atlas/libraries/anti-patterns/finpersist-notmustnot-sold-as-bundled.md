# 反模式：把 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事（335 余量）说成已经落盘 / 已经交差 / 已经崩溃恢复已经 Commit

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock changed state MUST NOT persist not already persisted ≠ bundled（335）](../../tracks/implementation/worked-example-finpersist-notmustnot-vs-bundled.md)。

## 卖法

把 `FinalizeBlock` 改了状态 / 决定块已经交给应用 / 转移状态 but MUST NOT persist 写成已经落盘 interchangeable / 已经写盘 interchangeable / 已经 Commit interchangeable / 335 finpersist bundled interchangeable / 481 commitpersist interchangeable / 680 commitpersist-notfinpersist interchangeable；把 MUST NOT persist in Finalize 写成已经交差 interchangeable / 已经 Finalize + Commit interchangeable / 33 four gates interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 587 finreturn interchangeable / 616 finreturn-notpersist interchangeable；把 Finalize 改了状态 写成已经崩溃恢复三步已经 Commit interchangeable / 已经块进 store interchangeable / 已经能从半截高度接着走 interchangeable / 320 crash recovery interchangeable / 5 half-write atomic interchangeable，或已经和 335 finpersist-vs-commit bundled / finalizepersist-sold-as-committed interchangeable / 683 finpersist-notmustnot interchangeable。

## 为什么错

官方把 Requirements MUST NOT persist in Finalize 单句、already persisted、already settled、crash recovery block in store already Commit 写成三件独立的实现事。把它们卖成 already persisted interchangeable / already settled interchangeable / crash recovery already Commit interchangeable，会把 not already persisted、not already settled、not crash recovery block in store already Commit 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事（335 余量），必须分开 not already persisted、not already settled、not crash recovery block in store already Commit 三件事，不要和 335 / 684 / 680 / 481 / 403 / 587 / 320 / 310 / 5 / 33 / 632 糊成一句。

## 和相邻反模式

- [commitpersist-notfinpersist-sold-as-bundled](commitpersist-notfinpersist-sold-as-bundled.md) 是 Signal persist vs Finalize already persisted（481 item 1 余量），不是本页 Requirements MUST NOT persist in Finalize 单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 FinalizeBlock 落盘禁令 bundled 全段，不是本页 MUST NOT persist item 1 单句边界。
- [finafter-notsettled-sold-as-bundled](finafter-notsettled-sold-as-bundled.md) 是 Finalize 之后引擎 persist vs already settled（403 item 1），不是本页 MUST NOT persist in Finalize 边界。
