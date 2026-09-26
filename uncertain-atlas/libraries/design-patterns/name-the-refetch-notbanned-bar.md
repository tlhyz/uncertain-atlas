# 模式：把应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[能再拉 not already banned ≠ bundled（378）](../../tracks/implementation/worked-example-refetch-notbanned-vs-bundled.md)。

## 三个名字

1. **能再拉 不是 already banned：** 看见能再拉 / 应用可以再拉块或封邻居、引擎不自己做 / 能再拉块，不是已经封了 interchangeable / 已经 banned interchangeable / 已经封了交差 interchangeable，不是 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable。

2. **能封 不是 already complete：** 看见能封 / 能封邻居 / 能封 P2P，不是已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，不是 332 snapshotverify interchangeable / 378 refetch item 2 interchangeable。

3. **有指令 不是 already settled：** 看见有指令 / 应用下了指令 / 有下指令，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 375 loadchunk interchangeable / 378 refetch item 3 interchangeable。

官方把能再拉、不是已经齐、不是已经交差写成三个名字。把它们叫成一个「看见能再拉就已经封了 interchangeable / 就已经齐 interchangeable / 就已经交差 interchangeable」，会把 not already banned、not already complete、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 余量），先数清问的是能再拉 是不是 already banned / 378 / refetch-sold-as-restored，是不是能封 是不是 already complete，还是有指令 是不是 already settled，再决定要不要同一次发布。378 refetch-vs-restored bundled unbundling 在本页 item 1 启动。
