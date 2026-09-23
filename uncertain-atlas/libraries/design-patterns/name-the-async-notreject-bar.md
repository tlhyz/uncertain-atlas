# 模式：把只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事（354 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[只做基本检查再异步 Process not already still-revise ≠ bundled（354）](../../tracks/implementation/worked-example-async-notreject-vs-bundled.md)。

## 三个名字

1. **异步了 不是 already still-revise：** 看见只做基本检查再异步 Process / 异步了 / 已经回了 `ACCEPT`，不是已经还能改票 interchangeable / 已经 still-revise interchangeable / 已经还能改票交差 interchangeable，不是 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable。

2. **先回了 不是 already still-reject：** 看见先回了 / 已经回了 `ACCEPT` / 先回了 ACCEPT，不是已经还能再 Reject interchangeable / 已经 still-reject interchangeable / 已经还能 Reject 交差 interchangeable，不是 33 fourgates interchangeable / 815 sync-notlater interchangeable。

3. **还在跑 不是 already force-nil：** 看见还在跑 / 异步还在跑 / 还在处理，不是已经能强迫 `nil` interchangeable / 已经 force-nil interchangeable / 已经强迫 nil 交差 interchangeable，不是 817 nonval-notverified interchangeable / 351 processalso interchangeable。

官方把异步了、不是已经还能 Reject、不是已经能强迫 nil 写成三个名字。把它们叫成一个「看见异步了就已经还能改票 interchangeable / 就已经还能 Reject interchangeable / 就已经能强迫 nil interchangeable」，会把 not already still-revise、not already still-reject、not already force-nil 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事（354 余量），先数清问的是异步了 是不是 already still-revise / 354 / processwhen-sold-as-later，是不是先回了 是不是 already still-reject，还是还在跑 是不是 already force-nil，再决定要不要同一次发布。354 processwhen vs later bundled unbundling 在本页 item 2 续。
