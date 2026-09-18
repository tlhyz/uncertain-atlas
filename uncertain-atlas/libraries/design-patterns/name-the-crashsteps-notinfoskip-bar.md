# 模式：把 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事（320 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**例**：[startup Info not already mid-height resume ≠ bundled（320）](../../tracks/implementation/worked-example-crashsteps-notinfoskip-vs-bundled.md)。

## 三个名字

1. **启动 Info 绿了 不是 already mid-height resume：** 看见 Info 绿了 / 应用回了与上次成功 Commit 一致的信息，不是已经能从半截高度接着走 interchangeable / 已经是任意高度 interchangeable，不是 314 querystate interchangeable / 370 info-vs-handshake interchangeable / 320 crashsteps bundled interchangeable。

2. **Info 对上了 不是 already can skip replay：** 看见对上了 / Info 对齐，不是已经能跳过重放 interchangeable / 已经能跳步 interchangeable，不是 685 finpersist-notrememberheight interchangeable / 38 genesis-replay interchangeable / 323 full-history interchangeable。

3. **InitChain 叫过 不是 InitChain already done：** 看见第一块 Commit 之前 InitChain 之后崩了 / InitChain 叫过，不是已经不用再叫 InitChain interchangeable / 已经创世已经齐 interchangeable，不是 411 initonce interchangeable / 495 initchainusage bundled interchangeable。

官方把 Crash Recovery 启动 Info 单句、already mid-height resume、already can skip replay、InitChain already done 写成三个名字。把它们叫成一个「看见 Info 对上了 就已经能从任意高度接着走 interchangeable / 就已经能跳步 interchangeable / 就已经不用再叫 InitChain interchangeable」，会把 not already mid-height resume、not already can skip replay、not InitChain already done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事（320 余量），先数清问的是 Info 绿了 是不是 already mid-height resume / 314 / 370，是不是对上了 是不是 already can skip replay / 685 / 38，还是 InitChain 叫过 是不是 InitChain already done / 411 / 495，再决定要不要同一次发布。320 crash recovery bundled unbundling 在本页 item 3 完成。
