# 模式：把快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事（368 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**例**：[对上了 not already restored ≠ bundled（368）](../../tracks/implementation/worked-example-snapident-notrestored-vs-bundled.md)。

## 三个名字

1. **对上了 不是 already restored：** 看见对上了 / 快照全字段（含 `Metadata`）对上才算同一份 / 同一份，不是已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable，不是 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable。

2. **能拉 不是 already settled：** 看见能拉 / 同一份才能从各节点拉 chunk / 对上了就能拉，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 321 offer interchangeable / 852 snapident-notapphash interchangeable。

3. **Metadata 在 不是 already complete：** 看见 `Metadata` 在 / 全字段含 Metadata / Metadata 字段在，不是已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，不是 853 snapident-notcomplete interchangeable / 322 listsnap interchangeable。

官方把对上了、不是已经交差、不是已经齐写成三个名字。把它们叫成一个「看见对上了就已经装完 interchangeable / 就已经交差 interchangeable / 就已经齐 interchangeable」，会把 not already restored、not already settled、not already complete 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事（368 余量），先数清问的是对上了 是不是 already restored / 368 / snapshot-sold-as-identical，是不是能拉 是不是 already settled，还是 Metadata 在 是不是 already complete，再决定要不要同一次发布。368 snapshot-vs-identical bundled unbundling 在本页 item 1 启动。
