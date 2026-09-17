# 模式：把 Commit Usage Signal persist application state not Finalize already persisted / not engine persist outputs / not When step 8 calls Commit 正式三事（481 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Signal ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-notfinalize-vs-bundled.md)。

## 三个名字

1. **Signal persist 不是 Finalize 改了就已经落盘：** 看见 Methods Usage persist signal，不是已经 335 interchangeable / 701 commitpersist-notfinalize interchangeable。
2. **看见叫 Commit 让应用落盘 不是引擎 persist 这三份：** 看见 signal，不是已经 587 interchangeable。
3. **看见 Usage 这句 不是 When step 8 calls Commit：** 看见 persist signal 单句，不是已经 590 interchangeable。

官方把 Commit Usage persist signal 三条核心句拆成三个名字。把它们叫成一个「看见叫了 Commit 就已经落盘」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage persist signal 正式三事（481 余量），先数清问的是 signal 是不是 Finalize 改了就已经落盘 / 335、是不是引擎 persist 这三份 / 587、还是看见 Usage 是不是 When step 8 / 590，再决定要不要同一次发布。481 commitpersist vs finalize bundled unbundling 在本页 item 1 启动。
