# 反模式：把 Signal persist application state not Finalize already persisted / not engine persist tx outputs AppHash ResultsHash / not expected persist at end of this call 正式三事（481 余量）说成已经 Finalize 落了 / 已经引擎 persist 这三份 / 已经 expected persist at end

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Signal persist application state not Finalize already persisted ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-notfinpersist-vs-bundled.md)。

## 卖法

把 Signal the Application to persist application state / persist signal / 叫 Commit 让应用落盘 写成已经 Finalize 改了就已经落盘 interchangeable / 335 finpersist bundled interchangeable / 335 item 1 MUST NOT persist in Finalize interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 已经 Finalize 落了 interchangeable；把 persist signal 写成已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable / 587 finreturn bundled interchangeable / 616 finreturn-notpersist interchangeable / 645 fincommit-notpersist interchangeable / 已经 When 第 4–6 步 interchangeable / 已经引擎 persist 这三份 interchangeable；把 Signal persist 写成已经 Application is expected to persist at end of this call interchangeable / 681 commitpersist-notendofcall interchangeable / 399 commit-empty-echo bundled interchangeable / 399 commitnoparam interchangeable / 已经 Commit 不带参数 interchangeable / 已经 signal 就已经交差 interchangeable，或已经和 481 commitpersist-vs-finalize bundled / commitpersist-sold-as-finalize interchangeable / 680 commitpersist-notfinpersist interchangeable。

## 为什么错

官方把 Commit Usage persist signal 单句、Finalize 落盘禁令（335）、引擎 persist 这三份（587）、expected persist at end（481 item 2）写成三件独立的实现事。把它们卖成 Finalize already persisted interchangeable / engine persist tx outputs AppHash ResultsHash interchangeable / expected persist at end interchangeable，会把 not Finalize already persisted、not engine persist tx outputs AppHash ResultsHash、not expected persist at end of this call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Signal persist application state not Finalize already persisted / not engine persist tx outputs AppHash ResultsHash / not expected persist at end of this call 正式三事（481 余量），必须分开 not Finalize already persisted、not engine persist tx outputs AppHash ResultsHash、not expected persist at end of this call 三件事，不要和 481 / 335 / 587 / 399 / 681 / 682 / 645 / 665 / 497 糊成一句。

## 和相邻反模式

- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 Commit Usage persist signal 正式三事 bundled 全段，不是本页 item 1 persist signal 单句边界。
- [finpersist-sold-as-commit](finpersist-sold-as-commit.md) 是 Finalize 落盘禁令 bundled 全段，不是本页 signal vs Finalize already persisted 边界。
- [infousage-notcommitpersist-sold-as-bundled](infousage-notcommitpersist-sold-as-bundled.md) 是 Info last_block during Commit 单句边界，不是本页 Signal persist 单句边界。
