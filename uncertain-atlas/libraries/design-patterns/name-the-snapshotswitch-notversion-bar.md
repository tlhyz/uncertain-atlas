# 模式：把 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事（323 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**例**：[AppHash 对上 not already version-matched ≠ bundled（323）](../../tracks/implementation/worked-example-snapshotswitch-notversion-vs-bundled.md)。

## 三个名字

1. **AppHash 对上 不是 already version-matched：** 看见 Info 的 AppHash 对上了 / 快照 AppHash 对上下一高度，不是已经是版本也对上 interchangeable / 已经版本交差 interchangeable，不是 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable。

2. **对了下一高度 不是 already current-header：** 看见对上下一高度 / 下一高度块里 AppHash 对上，不是已经对了当前头 interchangeable / 已经当前高度头交差 interchangeable，不是 323 snapshotswitch item 3 interchangeable / 727 snapshotswitch-nothistory interchangeable。

3. **Info 绿了 不是 already this-header-settled：** 看见再叫 Info 绿了 / InfoResponse 对上，不是已经是本头已经交差 interchangeable / 已经本头 AppHash 交差 interchangeable，不是 323 snapshotswitch item 1 interchangeable / 725 snapshotswitch-notchainid interchangeable。

官方把 AppHash 对上单句、already version-matched、already current-header、already this-header-settled 写成三个名字。把它们叫成一个「看见 Info 的 AppHash 对上了就已经版本也对上 interchangeable / 就已经对了当前头 interchangeable / 就已经本头交差 interchangeable」，会把 not already version-matched、not already current-header、not already this-header-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事（323 余量），先数清问的是 AppHash 对上 是不是 already version-matched / 323 / snapshotswitch-sold-as-full-history，是不是对了下一高度 是不是 already current-header，还是 Info 绿了 是不是 already this-header-settled，再决定要不要同一次发布。323 snapshotswitch vs history bundled unbundling 在本页 item 2 续。
