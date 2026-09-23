# 模式：把没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事（356 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**例**：[没调 Prepare not already reap-again ≠ bundled（356）](../../tracks/implementation/worked-example-vv-notraw-vs-bundled.md)。

## 三个名字

1. **没调 Prepare 不是 already reap-again：** 看见没调 Prepare / validValue 非 nil 时不会再从池子收 / 不会再从池子按优先级收，不是已经又收了一遍池子 interchangeable / 已经 reap-again interchangeable / 已经又收池子交差 interchangeable，不是 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable。

2. **用了 validValue 不是 already new-raw：** 看见用了 validValue / 不会再造头 / 用 validValue 当提案，不是已经是一份新的 raw 提案 interchangeable / 已经 new-raw interchangeable / 已经新 raw 交差 interchangeable，不是 311 candidate interchangeable / 821 vv-notstillprepare interchangeable。

3. **跳过了 不是 already preparedrop：** 看见跳过了 / 跳过 Prepare / 没走 Prepare 那条路，不是已经从提案拿掉 tx interchangeable / 已经 preparedrop interchangeable / 已经从提案拿掉交差 interchangeable，不是 822 vv-noteveryround interchangeable / 355 preparedrop interchangeable。

官方把没调 Prepare、不是已经是一份新的 raw 提案、不是已经从提案拿掉 tx 写成三个名字。把它们叫成一个「看见没调 Prepare 就已经又收了一遍池子 interchangeable / 就已经是一份新的 raw 提案 interchangeable / 就已经从提案拿掉 tx interchangeable」，会把 not already reap-again、not already new-raw、not already preparedrop 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事（356 余量），先数清问的是没调 Prepare 是不是 already reap-again / 356 / validvalue-sold-as-prepared，是不是用了 validValue 是不是 already new-raw，还是跳过了 是不是 already preparedrop，再决定要不要同一次发布。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。
