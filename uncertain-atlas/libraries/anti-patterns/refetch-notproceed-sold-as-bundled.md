# 反模式：把 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事（378 余量）说成已经能接着装 / 已经停 / 已经齐

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[拒了人 not already proceed ≠ bundled（378）](../../tracks/implementation/worked-example-refetch-notproceed-vs-bundled.md)。

## 卖法

把拒了人 / reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名 / 拒了发送者 写成已经能接着装 interchangeable / 已经 proceed interchangeable / 已经能接着装交差 interchangeable / 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable；把丢掉排队 / 这些人排队的块会丢掉 / 丢掉排队块 写成已经停 interchangeable / 已经 stopped interchangeable / 已经停交差 interchangeable；把已装的还在 / 已经装上的块不会重拉除非点名 / 已装的还在字段 写成已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，或已经和 378 refetch bundled / refetch-sold-as-restored interchangeable / 883 refetch-notproceed interchangeable。

## 为什么错

官方把拒了人、不是已经停、不是已经齐写成三件独立的实现事。把它们卖成 already proceed interchangeable / already stopped interchangeable / already complete interchangeable，会把 not already proceed、not already stopped、not already complete 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事（378 余量），必须分开 not already proceed、not already stopped、not already complete 三件事，不要和 378 / 375 / 332 / 882 糊成一句。

## 和相邻反模式

- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch bundled 全段，不是本页拒了人 item 3 单句边界。
- [refetch-notbanned-sold-as-bundled](refetch-notbanned-sold-as-bundled.md) 是能再拉 not already banned（378 item 1），不是本页 not already proceed 边界。
- [refetch-notcomplete-sold-as-bundled](refetch-notcomplete-sold-as-bundled.md) 是列了块号 not already complete（378 item 2），不是本页 not already complete 单句（已装的还在）。
- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375），不是本页 not already proceed 边界。
