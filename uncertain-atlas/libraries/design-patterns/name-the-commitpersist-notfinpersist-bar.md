# 模式：把 Signal persist application state not Finalize already persisted / not engine persist tx outputs AppHash ResultsHash / not expected persist at end of this call 正式三事（481 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Signal persist application state not Finalize already persisted ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-notfinpersist-vs-bundled.md)。

## 三个名字

1. **Signal persist application state 不是 Finalize already persisted：** 看见 Methods Usage 侧 persist signal，不是已经 Finalize 改了就已经落盘 interchangeable，不是 335 finpersist bundled interchangeable / 335 item 1 MUST NOT persist in Finalize interchangeable / 680 commitpersist-notfinpersist interchangeable。

2. **persist signal 不是 engine persist tx outputs AppHash ResultsHash：** 看见 Signal the Application to persist application state，不是已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable / 已经 When 第 4–6 步 interchangeable，不是 587 finreturn bundled interchangeable / 616 finreturn-notpersist interchangeable / 645 fincommit-notpersist interchangeable。

3. **叫 Commit 让应用落盘 不是 expected persist at end of this call：** 看见 persist signal，不是已经 Application is expected to persist at end of this call interchangeable / 已经 Commit 不带参数 interchangeable / 已经 signal 就已经交差 interchangeable，不是 681 commitpersist-notendofcall interchangeable / 399 commit-empty-echo bundled interchangeable / 399 commitnoparam interchangeable。

官方把 Commit Usage persist signal 单句、Finalize 落盘禁令（335）、引擎 persist 这三份（587）、expected persist at end（481 item 2）写成三个名字。把它们叫成一个「看见 Signal persist application state 就已经 Finalize 落了 interchangeable / 就已经引擎 persist 这三份 interchangeable / 就已经 expected persist at end interchangeable」，会把 not Finalize already persisted、not engine persist tx outputs AppHash ResultsHash、not expected persist at end of this call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Signal persist application state not Finalize already persisted / not engine persist tx outputs AppHash ResultsHash / not expected persist at end of this call 正式三事（481 余量），先数清问的是 Signal persist 是不是 Finalize already persisted / 335 / 403，是不是 persist signal 是不是 engine persist 这三份 / 587 / 645，还是叫 Commit 让应用落盘 是不是 expected persist at end / 681 / 399，再决定要不要同一次发布。481 commitpersist vs finalize bundled unbundling 在本页 item 1 完成。
