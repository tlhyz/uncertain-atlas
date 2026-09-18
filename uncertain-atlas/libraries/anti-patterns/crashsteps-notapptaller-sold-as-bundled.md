# 反模式：把 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事（320 余量）说成已经允许 / 已经能各醒各的 / 已经半写原子

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[app taller than engine not already allowed ≠ bundled（320）](../../tracks/implementation/worked-example-crashsteps-notapptaller-vs-bundled.md)。

## 卖法

把应用高度比引擎高 / 应用先落了盘 / 应用已经持久化的高度高于 CometBFT 已经持久化的最新高度 写成已经允许 interchangeable / 已经合法 interchangeable / 320 crashsteps bundled interchangeable / 685 finpersist-notrememberheight interchangeable / 335 finpersist item 3 interchangeable；把两边高度不一样 / 应用先落了盘 写成已经能各醒各的 interchangeable / 已经能单独恢复 interchangeable / 314 querystate interchangeable / 370 info-vs-handshake interchangeable；把能单独重启应用 / 应用先落了盘 写成已经半写已经原子 interchangeable / 5 half-write atomic interchangeable / 298 wal-fsync interchangeable，或已经和 320 crashsteps bundled / crashsteps-sold-as-committed interchangeable / 686 crashsteps-notapptaller interchangeable。

## 为什么错

官方把 Crash Recovery 不许应用领先单句、already allowed、already can wake separately、half-write atomic（5）写成三件独立的实现事。把它们卖成 already allowed interchangeable / already can wake separately interchangeable / half-write atomic interchangeable，会把 not already allowed、not already can wake separately、not half-write atomic 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事（320 余量），必须分开 not already allowed、not already can wake separately、not half-write atomic 三件事，不要和 320 / 685 / 5 / 298 / 314 / 370 / 335 糊成一句。

## 和相邻反模式

- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是 Crash Recovery 三步 bundled 全段，不是本页 app taller than engine item 1 单句边界。
- [finpersist-notrememberheight-sold-as-bundled](finpersist-notrememberheight-sold-as-bundled.md) 是 remember last Commit height vs app taller（335 item 3 余量 / 685），不是本页 Crash Recovery 不许领先单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 FinalizeBlock 落盘禁令 bundled，不是本页 Crash Recovery item 1 边界。
