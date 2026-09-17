# 反模式：把 ApplySnapshotChunk Result RETRY_SNAPSHOT not switched / not restored / not Offer accepted 正式三事（398 余量） 说成已经换一份就能接着装 / 已经装完 / 已经 Offer 收下交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[RETRY_SNAPSHOT ≠ bundled（398）](../../tracks/implementation/worked-example-applyretry-notswitch-vs-bundled.md)。

## 卖法

把 ApplySnapshotChunk Result 这句写成已经已经换一份就能接着装 / 已经装完 / 已经 Offer 收下交差 interchangeable，或已经和 398 applyretry-vs-refetch bundled / applyretry-notswitch-sold-as-bundled interchangeable。

## 为什么错

官方把 ApplySnapshotChunk Result 三条核心句写成三件独立的实现事。把它们卖成已经换一份就能接着装 / 已经装完 / 已经 Offer 收下交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result RETRY_SNAPSHOT 正式三事（398 余量），必须分开 not switched、not restored、not Offer accepted 三件事，不要和 398 / 321 / 401 / 719 / 721 糊成一句。

## 和相邻反模式

- [applyretry 父页 bundled](../../tracks/implementation/worked-example-applyretry-vs-refetch.md) 是 ApplySnapshotChunk 结果枚举 bundled（398），不是本页 item 2 单句边界。
- [applyretry-notrefetch-sold-as-bundled](applyretry-notrefetch-sold-as-bundled.md) 是 RETRY 单句边界（719 item 1），不是本页 RETRY_SNAPSHOT 边界。
