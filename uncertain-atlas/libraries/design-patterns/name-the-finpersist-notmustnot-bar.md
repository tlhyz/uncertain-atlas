# 模式：把 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事（335 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**例**：[FinalizeBlock changed state MUST NOT persist not already persisted ≠ bundled（335）](../../tracks/implementation/worked-example-finpersist-notmustnot-vs-bundled.md)。

## 三个名字

1. **MUST NOT persist 不是 already persisted：** 看见 FinalizeBlock 转移状态 but MUST NOT persist，不是已经落盘 interchangeable / 已经写盘 interchangeable / 已经 Commit interchangeable，不是 335 finpersist bundled interchangeable / 684 finpersist-notmustincommit interchangeable / 680 commitpersist-notfinpersist interchangeable / 481 commitpersist item 1 interchangeable。

2. **Finalize 改了状态 不是 already settled：** 看见 MUST NOT persist in Finalize，不是已经交差 interchangeable / 已经 Finalize + Commit interchangeable / 已经四门已经结算 interchangeable，不是 33 four gates interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 587 finreturn interchangeable / 616 finreturn-notpersist interchangeable。

3. **转移状态 不是 crash recovery block in store already Commit：** 看见 MUST NOT persist，不是已经崩溃恢复三步已经 Commit interchangeable / 已经块进 store interchangeable / 已经能从半截高度接着走 interchangeable，不是 320 crash recovery interchangeable / 5 half-write atomic interchangeable / 310 commitlock interchangeable / 684 finpersist-notmustincommit item 3 interchangeable。

官方把 Requirements MUST NOT persist in Finalize 单句、already persisted、already settled、crash recovery block in store already Commit 写成三个名字。把它们叫成一个「看见 Finalize 改了状态 就已经落盘 interchangeable / 就已经交差 interchangeable / 就已经崩溃恢复已经 Commit interchangeable」，会把 not already persisted、not already settled、not crash recovery block in store already Commit 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock changed state MUST NOT persist not already persisted / not already settled / not crash recovery block in store already Commit 正式三事（335 余量），先数清问的是 MUST NOT persist 是不是 already persisted / 335 / 684 / 680 / 481，是不是 Finalize 改了状态 是不是 already settled / 33 / 403 / 632 / 587，还是转移状态 是不是 crash recovery already Commit / 320 / 5 / 310，再决定要不要同一次发布。335 finpersist vs commit bundled unbundling 在本页 item 1 完成。
