# 模式：把 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[列了块号 not already complete ≠ bundled（378）](../../tracks/implementation/worked-example-refetch-notcomplete-vs-bundled.md)。

## 三个名字

1. **列了块号 不是 already complete：** 看见列了块号 / refetch_chunks 不论 result 都再拉再装、按顺序 / 列了块号字段，不是已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，不是 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable。

2. **再装 不是 already settled：** 看见再装 / 再按顺序装回去 / 再装块，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 881 refetch-notbanned interchangeable / 321 Offer restored interchangeable。

3. **按顺序 不是 already identical：** 看见按顺序 / 按顺序装回去 / 顺序列，不是已经是同一份 interchangeable / 已经 identical interchangeable / 已经是同一份交差 interchangeable，不是 368 Snapshot identical interchangeable / 378 refetch item 3 interchangeable。

官方把列了块号、不是已经交差、不是已经是同一份写成三个名字。把它们叫成一个「看见列了块号就已经齐 interchangeable / 就已经交差 interchangeable / 就已经是同一份 interchangeable」，会把 not already complete、not already settled、not already identical 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 余量），先数清问的是列了块号 是不是 already complete / 378 / refetch-sold-as-restored，是不是再装 是不是 already settled，还是按顺序 是不是 already identical，再决定要不要同一次发布。378 refetch-vs-restored bundled unbundling 在本页 item 2 续。
