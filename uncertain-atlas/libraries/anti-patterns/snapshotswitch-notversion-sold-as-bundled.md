# 反模式：把 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事（323 余量）说成已经版本也对上 / 已经对了当前头 / 已经本头交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[AppHash 对上 not already version-matched ≠ bundled（323）](../../tracks/implementation/worked-example-snapshotswitch-notversion-vs-bundled.md)。

## 卖法

把 AppHash 对上 / Info 的 AppHash 对上了 / 快照 AppHash 对上下一高度 写成已经是版本也对上 interchangeable / 已经 version-matched interchangeable / 已经版本交差 interchangeable / 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable；把对了下一高度 / 对上下一高度 / 下一高度块里 AppHash 对上 写成已经对了当前头 interchangeable / 已经 current-header interchangeable；把 Info 绿了 / 再叫 Info 绿了 / InfoResponse 对上 写成已经是本头已经交差 interchangeable / 已经 this-header-settled interchangeable，或已经和 323 snapshotswitch bundled / snapshotswitch-sold-as-full-history interchangeable / 726 snapshotswitch-notversion interchangeable。

## 为什么错

官方把 AppHash 对上单句、already version-matched、already current-header、already this-header-settled 写成三件独立的实现事。把它们卖成 already version-matched interchangeable / already current-header interchangeable / already this-header-settled interchangeable，会把 not already version-matched、not already current-header、not already this-header-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事（323 余量），必须分开 not already version-matched、not already current-header、not already this-header-settled 三件事，不要和 323 / 33 / 725 / 727 / 321 / 38 / 314 糊成一句。

## 和相邻反模式

- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是 Transition to Consensus bundled 全段，不是本页 AppHash 对上 item 2 单句边界。
- [snapshotswitch-notchainid-sold-as-bundled](snapshotswitch-notchainid-sold-as-bundled.md) 是装完 item 1，不是本页 Info 核对边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 语义，不是本页切共识两次核对边界。
