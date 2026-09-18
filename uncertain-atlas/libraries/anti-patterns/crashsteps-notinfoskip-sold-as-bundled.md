# 反模式：把 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事（320 余量）说成已经能从半截高度接着走 / 已经能跳步 / 已经不用再叫 InitChain

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[startup Info not already mid-height resume ≠ bundled（320）](../../tracks/implementation/worked-example-crashsteps-notinfoskip-vs-bundled.md)。

## 卖法

把启动 Info / Info 绿了 / 应用回了与上次成功 Commit 一致的信息 写成已经能从半截高度接着走 interchangeable / 已经是任意高度 interchangeable / 314 querystate interchangeable / 370 info-vs-handshake interchangeable / 320 crashsteps bundled interchangeable；把对上了 / Info 对齐 写成已经能跳过重放 interchangeable / 已经能跳步 interchangeable / 685 finpersist-notrememberheight interchangeable / 38 genesis-replay interchangeable / 323 full-history interchangeable；把 InitChain 叫过 / 第一块 Commit 之前 InitChain 之后崩了 写成已经不用再叫 InitChain interchangeable / 已经创世已经齐 interchangeable / 411 initonce interchangeable / 495 initchainusage bundled interchangeable，或已经和 320 crashsteps bundled / crashsteps-sold-as-committed interchangeable / 688 crashsteps-notinfoskip interchangeable。

## 为什么错

官方把 Crash Recovery 启动 Info 单句、already mid-height resume、already can skip replay、InitChain already done 写成三件独立的实现事。把它们卖成 already mid-height resume interchangeable / already can skip replay interchangeable / InitChain already done interchangeable，会把 not already mid-height resume、not already can skip replay、not InitChain already done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事（320 余量），必须分开 not already mid-height resume、not already can skip replay、not InitChain already done 三件事，不要和 320 / 314 / 370 / 685 / 38 / 411 / 495 / 686 / 687 糊成一句。

## 和相邻反模式

- [crashsteps-notblockstore-sold-as-bundled](crashsteps-notblockstore-sold-as-bundled.md) 是 blockstore vs already settled（320 item 2 余量 / 687），不是本页 startup Info item 3 单句边界。
- [crashsteps-notapptaller-sold-as-bundled](crashsteps-notapptaller-sold-as-bundled.md) 是 app taller than engine vs already allowed（320 item 1 余量 / 686），不是本页 Info 对上边界。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是 Crash Recovery 三步 bundled 全段，不是本页 startup Info item 3 单句边界。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 握手对齐 bundled（370），不是本页 Crash Recovery 重放 / InitChain 再叫边界。
