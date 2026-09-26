# 模式：把 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事（378 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[拒了人 not already proceed ≠ bundled（378）](../../tracks/implementation/worked-example-refetch-notproceed-vs-bundled.md)。

## 三个名字

1. **拒了人 不是 already proceed：** 看见拒了人 / reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名 / 拒了发送者，不是已经能接着装 interchangeable / 已经 proceed interchangeable / 已经能接着装交差 interchangeable，不是 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable。

2. **丢掉排队 不是 already stopped：** 看见丢掉排队 / 这些人排队的块会丢掉 / 丢掉排队块，不是已经停 interchangeable / 已经 stopped interchangeable / 已经停交差 interchangeable，不是 332 snapshotverify interchangeable / 321 Offer restored interchangeable。

3. **已装的还在 不是 already complete：** 看见已装的还在 / 已经装上的块不会重拉除非点名 / 已装的还在字段，不是已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，不是 882 refetch-notcomplete interchangeable / 378 refetch item 2 interchangeable。

官方把拒了人、不是已经停、不是已经齐写成三个名字。把它们叫成一个「看见拒了人就能接着装 interchangeable / 就已经停 interchangeable / 就已经齐 interchangeable」，会把 not already proceed、not already stopped、not already complete 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事（378 余量），先数清问的是拒了人 是不是 already proceed / 378 / refetch-sold-as-restored，是不是丢掉排队 是不是 already stopped，还是已装的还在 是不是 already complete，再决定要不要同一次发布。378 refetch-vs-restored bundled unbundling 在本页 item 3 完成。
