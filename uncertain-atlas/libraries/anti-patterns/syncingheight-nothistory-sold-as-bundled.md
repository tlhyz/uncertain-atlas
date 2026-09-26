# 反模式：把 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 余量）说成已经有完整历史 / 已经是快照重放 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了目标 not already history ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-nothistory-vs-bundled.md)。

## 卖法

把填了目标 / syncing_to_height 同步或重放时是目标高、否则等于本高 / 填了 syncing_to_height 写成已经有完整历史 interchangeable / 已经 history interchangeable / 已经有从创世的完整历史交差 interchangeable / 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable；把在同步 / 在同步或重放 / 正在追目标高 写成已经是快照重放 interchangeable / 已经 restored interchangeable / 已经是快照重放交差 interchangeable；把等于本高 / syncing_to_height 等于本高 / 目标就是本高 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 382 syncingheight bundled / syncingheight-sold-as-history interchangeable / 893 syncingheight-nothistory interchangeable。

## 为什么错

官方把填了目标、不是已经是快照重放、不是已经交差写成三件独立的实现事。把它们卖成 already history interchangeable / already restored interchangeable / already settled interchangeable，会把 not already history、not already restored、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 余量），必须分开 not already history、not already restored、not already settled 三件事，不要和 382 / 323 / 321 / 316 糊成一句。

## 和相邻反模式

- [syncingheight-sold-as-history](syncingheight-sold-as-history.md) 是 syncingheight bundled 全段，不是本页填了目标 item 1 单句边界。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是切进共识就已经有从创世的完整历史（323），不是本页 not already history 边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完（321），不是本页 not already restored 单句。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表就已经同一顺序（316），不是本页 not already settled 边界。
