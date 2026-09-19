# 反模式：把一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事（321 余量）说成已经齐 / 已经封禁 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[收下一块 not already complete ≠ bundled（321）](../../tracks/implementation/worked-example-snapshotrestore-notchunkcomplete-vs-bundled.md)。

## 卖法

把收下一块 / ApplySnapshotChunk 收下了一块 / 回了收下这块等下一块 写成已经齐 interchangeable / 已经 complete interchangeable / 已经 chunk 齐交差 interchangeable / 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable；把回了再拉 / 要再拉当前这块 / 再拉前面若干块 写成已经封禁 interchangeable / 已经 banned interchangeable；把能回指令 / 能回封禁邻居 / 能回拒掉或重试这份快照 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 321 snapshotrestore bundled / snapshotrestore-sold-as-offered interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable。

## 为什么错

官方把收下一块单句、already complete、already banned、already settled 写成三件独立的实现事。把它们卖成 already complete interchangeable / already banned interchangeable / already settled interchangeable，会把 not already complete、not already banned、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事（321 余量），必须分开 not already complete、not already banned、not already settled 三件事，不要和 321 / 33 / 719 / 721 / 378 / 38 / 483 / 314 / 320 糊成一句。

## 和相邻反模式

- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Snapshot Restoration bundled 全段，不是本页 chunk 齐 item 2 单句边界。
- [snapshotrestore-notrestored-sold-as-bundled](snapshotrestore-notrestored-sold-as-bundled.md) 是 Offer 收下 item 1，不是本页 chunk 齐边界。
- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是再拉当装完，不是本页 not already banned / settled 三事边界。
