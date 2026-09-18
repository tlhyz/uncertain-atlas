# 模式：把 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事（320 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**例**：[app taller than engine not already allowed ≠ bundled（320）](../../tracks/implementation/worked-example-crashsteps-notapptaller-vs-bundled.md)。

## 三个名字

1. **应用比引擎高 不是 already allowed：** 看见应用已经持久化的高度高于 CometBFT、应用先落了盘，不是已经允许 interchangeable / 已经合法 interchangeable，不是 320 crashsteps bundled interchangeable / 685 finpersist-notrememberheight interchangeable / 335 finpersist item 3 interchangeable。

2. **两边高度不一样 不是 already can wake separately：** 看见应用高度比引擎高，不是已经能各醒各的 interchangeable / 已经能单独恢复 interchangeable，不是 314 querystate interchangeable / 370 info-vs-handshake interchangeable / 687 crashsteps-notblockstore interchangeable。

3. **能单独重启应用 不是 half-write atomic：** 看见应用先落了盘 / 能单独重启应用，不是已经半写已经原子 interchangeable / 已经和半写已经原子同一句 interchangeable，不是 5 half-write atomic interchangeable / 298 wal-fsync interchangeable。

官方把 Crash Recovery 不许应用领先单句、already allowed、already can wake separately、half-write atomic（5）写成三个名字。把它们叫成一个「看见应用比引擎高 就已经允许 interchangeable / 就已经能各醒各的 interchangeable / 就已经半写原子 interchangeable」，会把 not already allowed、not already can wake separately、not half-write atomic 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事（320 余量），先数清问的是应用比引擎高 是不是 already allowed / 320 / 685，是不是两边高度不一样 是不是 already can wake separately / 314 / 370，还是能单独重启应用 是不是 half-write atomic / 5 / 298，再决定要不要同一次发布。320 crash recovery bundled unbundling 在本页 item 1 完成。
