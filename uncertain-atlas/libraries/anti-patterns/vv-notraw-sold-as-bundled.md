# 反模式：把没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事（356 余量）说成已经又收了一遍池子 / 已经是一份新的 raw 提案 / 已经从提案拿掉 tx

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[没调 Prepare not already reap-again ≠ bundled（356）](../../tracks/implementation/worked-example-vv-notraw-vs-bundled.md)。

## 卖法

把没调 Prepare / validValue 非 nil 时不会再从池子收 / 不会再从池子按优先级收 写成已经又收了一遍池子 interchangeable / 已经 reap-again interchangeable / 已经又收池子交差 interchangeable / 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable；把用了 validValue / 不会再造头 写成已经是一份新的 raw 提案 interchangeable / 已经 new-raw interchangeable / 已经新 raw 交差 interchangeable；把跳过了 / 跳过 Prepare / 没走 Prepare 那条路 写成已经从提案拿掉 tx interchangeable / 已经 preparedrop interchangeable / 已经从提案拿掉交差 interchangeable，或已经和 356 validvalue bundled / validvalue-sold-as-prepared interchangeable / 823 vv-notraw interchangeable。

## 为什么错

官方把没调 Prepare、不是已经是一份新的 raw 提案、不是已经从提案拿掉 tx 写成三件独立的实现事。把它们卖成 already reap-again interchangeable / already new-raw interchangeable / already preparedrop interchangeable，会把 not already reap-again、not already new-raw、not already preparedrop 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事（356 余量），必须分开 not already reap-again、not already new-raw、not already preparedrop 三件事，不要和 356 / 311 / 338 / 821 / 822 糊成一句。

## 和相邻反模式

- [validvalue-sold-as-prepared](validvalue-sold-as-prepared.md) 是 validValue 跳过 Prepare bundled 全段，不是本页没调 Prepare item 3 单句边界。
- [vv-noteveryround-sold-as-bundled](vv-noteveryround-sold-as-bundled.md) 是自己是提议者 not already will-call（356 item 2），不是本页 not already reap-again 边界。
- [vv-notstillprepare-sold-as-bundled](vv-notstillprepare-sold-as-bundled.md) 是 validValue 非 nil not already still-prepare（356 item 1），不是本页 not already preparedrop 边界。
