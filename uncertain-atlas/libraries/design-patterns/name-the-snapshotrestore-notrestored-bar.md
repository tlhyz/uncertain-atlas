# 模式：把 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事（321 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**例**：[Offer 收下 not already restored ≠ bundled（321）](../../tracks/implementation/worked-example-snapshotrestore-notrestored-vs-bundled.md)。

## 三个名字

1. **Offer 收下 不是 already restored：** 看见 OfferSnapshot 收下了 / Accept 了这份快照，不是已经装完 interchangeable / 已经装回交差 interchangeable，不是 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable。

2. **选了这份 不是 already all-chunks：** 看见选了这份快照 / 开始拉 chunk，不是已经有了全部块 interchangeable / 已经有块交差 interchangeable，不是 321 snapshotrestore item 2 interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable。

3. **元数据对上 不是 already AppHash-verified：** 看见元数据字段完全一样 / 邻居元数据对上，不是已经验过 AppHash interchangeable / 已经和 Only AppHash trusted 同一句 interchangeable，不是 38 apphash interchangeable / 483 offersnaptrust interchangeable。

官方把 Offer 收下单句、already restored、already all-chunks、already AppHash-verified 写成三个名字。把它们叫成一个「看见 OfferSnapshot 收下就已经装完 interchangeable / 就已经有了全部块 interchangeable / 就已经验过 AppHash interchangeable」，会把 not already restored、not already all-chunks、not already AppHash-verified 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事（321 余量），先数清问的是 Offer 收下 是不是 already restored / 321 / snapshotrestore-sold-as-offered，是不是选了这份 是不是 already all-chunks，还是元数据对上 是不是 already AppHash-verified，再决定要不要同一次发布。321 snapshotrestore vs offer bundled unbundling 在本页 item 1 启动。
