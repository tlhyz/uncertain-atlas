# 模式：把 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事（335 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**例**：[remember last Commit height not already app taller than engine ≠ bundled（335）](../../tracks/implementation/worked-example-finpersist-notrememberheight-vs-bundled.md)。

## 三个名字

1. **记住高度 不是 already app taller than engine：** 看见应用必须记住最近一次成功跑完 Commit 的高度，不是已经允许应用比引擎高 interchangeable / 已经应用比引擎高已经允许 interchangeable，不是 320 crash recovery interchangeable / 5 half-write atomic interchangeable / 684 finpersist-notmustincommit interchangeable。

2. **能告诉从哪接 不是 already can skip replay：** 看见好告诉 CometBFT 崩溃之后从哪接，不是已经能跳过重放 interchangeable / 已经能跳步 interchangeable / 已经 can skip steps interchangeable，不是 320 crash recovery interchangeable / 38 genesis-replay interchangeable / 323 full-history interchangeable。

3. **有这个高度 不是 Info handshake aligned：** 看见记住了上次成功 Commit 高度，不是已经和启动 Info 对上 interchangeable / 已经 Info 握手对齐 interchangeable，不是 370 info-vs-handshake interchangeable / 497 infousage-persist interchangeable / 665 infousage-notcommitpersist interchangeable。

官方把 Requirements remember last Commit height 单句、already app taller than engine（320）、already can skip replay（320/5）、Info handshake aligned（370）写成三个名字。把它们叫成一个「看见记住了高度 就已经能比引擎高 interchangeable / 就已经能跳步 interchangeable / 就已经 Info 对上 interchangeable」，会把 not already app taller than engine、not already can skip replay、not Info handshake aligned 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事（335 余量），先数清问的是记住高度 是不是 already app taller than engine / 320 / 5，是不是能告诉从哪接 是不是 already can skip replay / 320 / 38，还是有这个高度 是不是 Info handshake aligned / 370 / 497，再决定要不要同一次发布。335 finpersist vs commit bundled unbundling 在本页 item 3 完成。
