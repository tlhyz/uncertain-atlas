# 反模式：把 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事（321 余量）说成已经装完 / 已经有了全部块 / 已经验过 AppHash

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Offer 收下 not already restored ≠ bundled（321）](../../tracks/implementation/worked-example-snapshotrestore-notrestored-vs-bundled.md)。

## 卖法

把 Offer 收下 / OfferSnapshot 收下了 / Accept 了这份快照 写成已经装完 interchangeable / 已经 restored interchangeable / 已经装回交差 interchangeable / 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable；把选了这份 / 选了这份快照 / 开始拉 chunk 写成已经有了全部块 interchangeable / 已经 all-chunks interchangeable；把元数据对上 / 元数据字段完全一样 / 邻居元数据对上 写成已经验过 AppHash interchangeable / 已经 AppHash-verified interchangeable，或已经和 321 snapshotrestore bundled / snapshotrestore-sold-as-offered interchangeable / 719 snapshotrestore-notrestored interchangeable。

## 为什么错

官方把 Offer 收下单句、already restored、already all-chunks、already AppHash-verified 写成三件独立的实现事。把它们卖成 already restored interchangeable / already all-chunks interchangeable / already AppHash-verified interchangeable，会把 not already restored、not already all-chunks、not already AppHash-verified 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事（321 余量），必须分开 not already restored、not already all-chunks、not already AppHash-verified 三件事，不要和 321 / 33 / 648 / 720 / 721 / 38 / 483 / 314 / 320 糊成一句。

## 和相邻反模式

- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Snapshot Restoration bundled 全段，不是本页 Offer 收下 item 1 单句边界。
- [offersnapusage-notrestored-sold-as-bundled](offersnapusage-notrestored-sold-as-bundled.md) 是 OfferSnapshot Usage upon accepting（499 / 648），不是本页 Snapshot Restoration Requirements 侧。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是崩溃三步（320），不是本页 Offer 收下边界。
