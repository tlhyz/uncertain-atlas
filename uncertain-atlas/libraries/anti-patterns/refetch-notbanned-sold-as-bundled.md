# 反模式：把应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 余量）说成已经封了 / 已经齐 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[能再拉 not already banned ≠ bundled（378）](../../tracks/implementation/worked-example-refetch-notbanned-vs-bundled.md)。

## 卖法

把能再拉 / 应用可以再拉块或封邻居、引擎不自己做 / 能再拉块 写成已经封了 interchangeable / 已经 banned interchangeable / 已经封了交差 interchangeable / 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable；把能封 / 能封邻居 / 能封 P2P 写成已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable；把有指令 / 应用下了指令 / 有下指令 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 378 refetch bundled / refetch-sold-as-restored interchangeable / 881 refetch-notbanned interchangeable。

## 为什么错

官方把能再拉、不是已经齐、不是已经交差写成三件独立的实现事。把它们卖成 already banned interchangeable / already complete interchangeable / already settled interchangeable，会把 not already banned、not already complete、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 余量），必须分开 not already banned、not already complete、not already settled 三件事，不要和 378 / 321 / 332 / 375 糊成一句。

## 和相邻反模式

- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch bundled 全段，不是本页能再拉 item 1 单句边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完（321），不是本页 not already banned 单句。
- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是封禁邻居就已经没有快照 DoS（332），不是本页 not already complete 边界。
- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375），不是本页 not already settled 边界。
