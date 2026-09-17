# 反模式：把 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事（335 余量）说成已经能比引擎高 / 已经能跳步 / 已经 Info 对上

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[remember last Commit height not already app taller than engine ≠ bundled（335）](../../tracks/implementation/worked-example-finpersist-notrememberheight-vs-bundled.md)。

## 卖法

把应用必须记住最近一次成功跑完 `Commit` 的高度 / 好告诉 CometBFT 崩溃之后从哪接 写成已经允许应用比引擎高 interchangeable / 已经应用比引擎高已经允许 interchangeable / 320 crash recovery interchangeable / 5 half-write atomic interchangeable / 684 finpersist-notmustincommit interchangeable；把能告诉引擎从哪接 / 记住了高度 写成已经能跳过重放 interchangeable / 已经能跳步 interchangeable / 已经 can skip steps interchangeable / 320 crash recovery interchangeable / 38 genesis-replay interchangeable / 323 full-history interchangeable；把有这个高度 / 记住上次成功 Commit 高度 写成已经和启动 Info 对上 interchangeable / 已经 Info 握手对齐 interchangeable / 370 info-vs-handshake interchangeable / 497 infousage-persist interchangeable / 665 infousage-notcommitpersist interchangeable，或已经和 335 finpersist-vs-commit bundled / finalizepersist-sold-as-committed interchangeable / 685 finpersist-notrememberheight interchangeable。

## 为什么错

官方把 Requirements remember last Commit height 单句、already app taller than engine（320）、already can skip replay（320/5）、Info handshake aligned（370）写成三件独立的实现事。把它们卖成 already app taller than engine interchangeable / already can skip replay interchangeable / Info handshake aligned interchangeable，会把 not already app taller than engine、not already can skip replay、not Info handshake aligned 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 remember last Commit height not already app taller than engine / not already can skip replay / not Info handshake aligned 正式三事（335 余量），必须分开 not already app taller than engine、not already can skip replay、not Info handshake aligned 三件事，不要和 335 / 320 / 5 / 370 / 497 / 684 / 683 / 38 糊成一句。

## 和相邻反模式

- [finpersist-notmustincommit-sold-as-bundled](finpersist-notmustincommit-sold-as-bundled.md) 是 MUST persist in Commit vs already persisted in Finalize（335 item 2 余量 / 684），不是本页 remember last Commit height 单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 FinalizeBlock 落盘禁令 bundled 全段，不是本页 remember height item 3 单句边界。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是崩溃恢复三步已经交差（320），不是本页 Requirements remember last Commit height 单句边界。
