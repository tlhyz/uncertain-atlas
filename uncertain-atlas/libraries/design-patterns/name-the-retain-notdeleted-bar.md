# 模式：把低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[能删 not already deleted ≠ bundled（366）](../../tracks/implementation/worked-example-retain-notdeleted-vs-bundled.md)。

## 三个名字

1. **能删 不是 already deleted：** 看见能删 / 低于这个高度的块可以被删 / 回了高度可删，不是已经删完 interchangeable / 已经 deleted interchangeable / 已经删完交差 interchangeable，不是 366 retain bundled interchangeable / retain-sold-as-kept interchangeable。

2. **回了高度 不是 already snapshot-trunc：** 看见回了高度 / 回了高度可删 / 能删，不是已经是这个节点快照截断 interchangeable / 已经 snapshot-trunc interchangeable / 已经快照截断交差 interchangeable，不是 323 full-history interchangeable / 845 retain-notpruning interchangeable。

3. **能剪 不是 already no-history：** 看见能剪 / 能删就等于能剪 / 低于这个高度可剪，不是已经没有历史 interchangeable / 已经 no-history interchangeable / 已经没有历史交差 interchangeable，不是 847 retain-notgenesis interchangeable / 38 genesis-replay interchangeable。

官方把能删、不是已经是快照截断、不是已经没有历史写成三个名字。把它们叫成一个「看见能删就已经删完 interchangeable / 就已经是快照截断 interchangeable / 就已经没有历史 interchangeable」，会把 not already deleted、not already snapshot-trunc、not already no-history 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 余量），先数清问的是能删 是不是 already deleted / 366 / retain-sold-as-kept，是不是回了高度 是不是 already snapshot-trunc，还是能剪 是不是 already no-history，再决定要不要同一次发布。366 retain-vs-kept bundled unbundling 在本页 item 2 续。
