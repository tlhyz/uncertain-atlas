# 反模式：把 InitChain Usage Called once upon genesis not crash then InitChain / not InitChain Usage remainder bundled / not process up is past genesis_time 正式三事（495 余量）说成已经崩溃后再调 / 已经 412 bundled / 已经过了 genesis_time

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[once upon genesis not crash ≠ bundled（495）](../../tracks/implementation/worked-example-initchainusage-notcrash-vs-bundled.md)。

## 卖法

把 Called once upon genesis / InitChain 创世时只调一次 写成已经崩溃后第一块 Commit 之前再调 InitChain interchangeable / 320 crash interchangeable / 已经交差 interchangeable；把看见创世时只调一次写成已经 InitChain Usage 余量 bundled 第一件事 interchangeable / 412 initonce interchangeable；把看见 Usage 这句写成已经进程起来就已经过了 genesis_time interchangeable / 303 genesis interchangeable，或已经和 495 initchainusage-vs-bundled / initchainusage-notcrash-sold-as-bundled interchangeable / 695 initchainusage-notcrash interchangeable。

## 为什么错

官方把 InitChain Usage once、崩溃恢复再调、412 余量 bundled、进程起来就已经过了 genesis_time 写成三件独立的实现事。把它们卖成 crash interchangeable / remainder bundled interchangeable / genesis_time interchangeable，会把 not crash、not remainder bundled、not process up is past genesis_time 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage once 正式三事（495 余量），必须分开 not crash、not remainder bundled、not process up is past genesis_time 三件事，不要和 495 / 320 / 412 / 303 / 696 / 697 糊成一句。

## 和相邻反模式

- [initchainusage-sold-as-bundled](initchainusage-sold-as-bundled.md) 是 InitChain Usage 正式三事 bundled（495），不是本页 item 1 单句边界。
- [initchainusage-notempty-sold-as-bundled](initchainusage-notempty-sold-as-bundled.md) 是 empty → Request 单句边界（696 item 2），不是本页 once 边界。
