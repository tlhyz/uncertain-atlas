# 模式：把空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事（368 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**例**：[写成 1 not already complete ≠ bundled（368）](../../tracks/implementation/worked-example-snapident-notcomplete-vs-bundled.md)。

## 三个名字

1. **写成 1 不是 already complete：** 看见写成 1 / `chunks` 至少是 1、哪怕是空快照 / 有块数，不是已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，不是 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable。

2. **有上限 不是 already consensus-const：** 看见有上限 / 网上一份快照报文最多 4 MB / 有 4 MB 上限，不是已经是共识常数 interchangeable / 已经 consensus-const interchangeable / 已经是共识常数交差 interchangeable，不是 299 maxbytes interchangeable / 851 snapident-notrestored interchangeable。

3. **能发 不是 already restored：** 看见能发 / 能发这份快照报文 / 报文能上网上，不是已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable，不是 852 snapident-notapphash interchangeable / 321 offer interchangeable。

官方把写成 1、不是已经是共识常数、不是已经装完写成三个名字。把它们叫成一个「看见写成 1 就已经齐 interchangeable / 就已经是共识常数 interchangeable / 就已经装完 interchangeable」，会把 not already complete、not already consensus-const、not already restored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事（368 余量），先数清问的是写成 1 是不是 already complete / 368 / snapshot-sold-as-identical，是不是有上限 是不是 already consensus-const，还是能发 是不是 already restored，再决定要不要同一次发布。368 snapshot-vs-identical bundled unbundling 在本页 item 3 完成。
